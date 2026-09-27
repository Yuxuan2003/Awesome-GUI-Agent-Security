#!/usr/bin/env python3
"""
按日期窗口从 arXiv 检索本仓库范围内的候选论文。

检索策略是「形态词 × 安全词 × 分类键」三层交集 —— 这三层都不能省：
  - 只用形态词 → 混入大量能力向论文
  - 只用安全词 → 混入通用 LLM 安全论文
  - 分类键不叠加前两层 → 存量虚高数倍（实测 benchmark 一项召回 726 篇，
    收紧后仅 143 篇，因为 benchmark 在能力向论文里是标配词）

用法：
    python3 scripts/fetch.py 2026-09-05 2026-09-18          # 双周窗口
    python3 scripts/fetch.py 2026-09-05 2026-09-18 --section 1.1   # 只查某节

输出候选清单（含 v1 日期、主分类、命中的形态词），已自动剔除库中已有 ID。
人工判断范围后再写进 data/papers.yaml。
"""
import argparse
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 PyYAML：pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
API = "https://export.arxiv.org/api/query"
# 翻页间隔。arXiv 的 WAF 会间歇性返回 406/429 —— 与客户端无关（同一条 URL 用
# curl 与 urllib 都可能 200 也可能被拒），只与**短时间内的请求频率**相关：连续
# 十几次请求后会进入几分钟的拒绝期。3.5s 在单窗口（1–2 个请求）够用，但补存量
# 要连续翻 3–4 页，实测会撞墙。默认放宽到 15s，可用 AGAS_SLEEP 覆盖。
SLEEP = float(os.environ.get("AGAS_SLEEP", "15"))
# 请求必须带 User-Agent：arXiv 会拒绝无 UA 的请求（HTTP 406）。
UA = "Awesome-GUI-Agent-Security/1.0 (weekly maintenance; +https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security)"

# 分类过滤放在本地做（parse 后按主分类筛），不再拼进 search_query。
# 2026-09-25 实测：9 个 cat + 15 个形态词 + 13 个安全词拼成的一条 URL 稳定被
# arXiv WAF 拒（406/400），而短查询全部 200 —— 限制的是**查询串规模**，不是内容。
CATS = ("cs.CR", "cs.AI", "cs.CL", "cs.LG", "cs.MA", "cs.SE", "cs.HC", "cs.CV", "cs.MM")
# 形态词按这个数量分块，每块单独发一次请求。实测 4 词一组长度安全。
FORM_CHUNK = 4

# 形态词 —— 单个词召回都极低（computer-use agent 1.3/周、GUI agent 1.7/周），
# 必须用并集。browser agent/browser-use 实测三周 0 篇，商用 AI 浏览器安全
# 走的是厂商公告与 CVE，需另行人工跟进（见 sections.yaml 第 4 章说明）。
FORMS = [
    "computer-use agent", "computer use agent", "GUI agent", "web agent",
    "browser agent", "browser-use", "mobile agent", "phone agent",
    "smartphone agent", "app agent", "Android agent", "screen agent",
    "desktop agent", "OS agent", "device-control agent",
]

# 安全词 —— 不能只用 security。这类论文惯用 attack / injection / safety，
# 强制 AND security 会把召回从 5.3/周 压到 0.7/周。
SECS = [
    "attack", "security", "injection", "safety", "hijack", "jailbreak",
    "malicious", "vulnerability", "defense", "backdoor", "privacy",
    "risk", "harmful",
]


def http_get(url):
    """取回响应文本。优先用 curl，失败再回退 urllib。

    为什么不用纯 urllib：2026-09-25 实测，同一条 URL 同一时刻 curl 得 200、
    urllib 得 406，且连续 5 次重试都是 406 —— 换 curl 立刻成功。arXiv 前置的
    WAF 对 Python urllib 的 TLS/HTTP 指纹不友好。判断依据用 curl 重放同一 URL。
    """
    try:
        p = subprocess.run(
            ["curl", "-sS", "--compressed", "--max-time", "90", "-A", UA, url],
            capture_output=True, text=True)
        if p.returncode == 0 and "<feed" in p.stdout:
            return p.stdout
        last = f"curl rc={p.returncode}: {p.stderr.strip()[:120]}"
    except FileNotFoundError:
        last = "curl 不可用"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=90).read().decode()


def q_or(field, terms):
    return "(" + " OR ".join(
        f'{field}:"{t}"' if " " in t or "-" in t else f"{field}:{t}"
        for t in terms) + ")"


def _one_page(forms, extra, s, e, start, page_size):
    parts = [q_or("abs", forms), q_or("abs", SECS),
             f"submittedDate:[{s} TO {e}]"]
    if extra:
        parts.append(f"({extra})")
    params = urllib.parse.urlencode({
        "search_query": " AND ".join(parts),
        "start": start, "max_results": page_size,
        "sortBy": "submittedDate", "sortOrder": "descending",
    })
    last = None
    # 退避必须指数级。arXiv 的限流有两种形状：429（明确限流）与 406
    # （WAF 拒绝，也能由短时间高频请求触发）。两者都是**瞬时**的 —— 同一条查询
    # 隔几十秒重试即返回 200。固定 12s 重试在连续请求场景下会一路撞到墙上，
    # 表现为「整个窗口 0 篇」，与「存量已清完」无法区分。
    for attempt in range(5):
        try:
            return http_get(API + "?" + params)
        except Exception as ex:
            last = ex
            if attempt < 4:
                wait = 20 * (2 ** attempt)      # 20 / 40 / 80 / 160
                print(f"  请求失败（第 {attempt + 1} 次），{wait}s 后重试：{ex}", file=sys.stderr)
                time.sleep(wait)
    # 关键：网络故障绝不能伪装成「无结果」。
    # 历史 bug：原实现返回 "" 让 search() 静默 break，全区间 174 篇候选被报成 0 篇，
    # 日志里连「arXiv 报告命中」都不打印 —— 极易被误读为「存量已清完」。
    raise RuntimeError(f"arXiv 请求连续 4 次失败（start={start}）：{last}")


def _search_chunk(forms, extra, s, e, page_size, max_pages):
    """arXiv 单次最多返回 100 条，**必须翻页**，否则长窗口会被静默截断。

    历史 bug：原实现硬编码 start=0 单次请求，全区间实际 252 篇只召回 100 篇，
    漏掉 60%。翻页直到某页不足 page_size 为止。
    """
    pages, total, got_all = [], None, 0
    for i in range(max_pages):
        xml = _one_page(forms, extra, s, e, i * page_size, page_size)
        if total is None:
            m = re.search(r"opensearch:totalResults[^>]*>(\d+)<", xml)
            total = int(m.group(1)) if m else None
            print(f"  arXiv 报告命中 {total if total is not None else '?'} 篇，开始翻页…",
                  file=sys.stderr)
        pages.append(xml)
        got = len(re.findall(r"<entry>", xml))
        got_all += got
        if got < page_size:
            break
        time.sleep(SLEEP)
    # 自检：翻页拿到的条数应与 arXiv 报告的总数一致，否则说明被截断
    if total is not None and got_all < total:
        print(f"  ⚠ 警告：arXiv 报告 {total} 篇，实际只取到 {got_all} 篇 —— 疑似翻页被截断，"
              f"请检查 max_pages（当前 {max_pages}）", file=sys.stderr)
    return "".join(pages)


def search(extra, start_ymd, end_ymd, page_size=100, max_pages=20):
    """把形态词分块后逐块检索再合并。

    为什么不发一条大查询：15 个形态词 + 13 个安全词 + 9 个 cat 拼成的 URL
    会被 arXiv WAF 判为不可接受（406/400），而拆成 4 词一组后稳定 200。
    """
    s = start_ymd.replace("-", "") + "0000"
    e = end_ymd.replace("-", "") + "2359"
    chunks = [FORMS[i:i + FORM_CHUNK] for i in range(0, len(FORMS), FORM_CHUNK)]
    out = []
    for n, forms in enumerate(chunks, 1):
        print(f"  形态词分组 {n}/{len(chunks)}: {', '.join(forms)}", file=sys.stderr)
        out.append(_search_chunk(forms, extra, s, e, page_size, max_pages))
        time.sleep(SLEEP)
    return "".join(out)


def parse(xml):
    out = []
    for blk in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        aid = re.search(r"<id>http://arxiv\.org/abs/([^<]+)</id>", blk)
        ti = re.search(r"<title>(.*?)</title>", blk, re.S)
        pub = re.search(r"<published>(.*?)</published>", blk)
        summ = re.search(r"<summary>(.*?)</summary>", blk, re.S)
        cats = re.findall(r'<category term="([^"]+)"', blk)
        if not (aid and ti):
            continue
        # 分类过滤本地做：主分类或任一交叉分类命中即保留
        if cats and not any(c in CATS for c in cats):
            continue
        ab = " ".join((summ.group(1) if summ else "").split()).lower()
        out.append({
            "id": aid.group(1).split("v")[0],
            "title": " ".join(ti.group(1).split()),
            "v1": pub.group(1)[:10] if pub else "?",
            "cat": cats[0] if cats else "?",
            "forms": [f for f in FORMS if f.lower() in ab],
        })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("start", help="窗口起始 YYYY-MM-DD")
    ap.add_argument("end", help="窗口结束 YYYY-MM-DD")
    ap.add_argument("--section", help="只查该小节（用 sections.yaml 里的 queries）")
    args = ap.parse_args()

    secs = yaml.safe_load((ROOT / "data" / "sections.yaml").read_text(encoding="utf-8"))
    have = {str(p["id"]) for p in yaml.safe_load(
        (ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))["papers"] if p.get("id")}

    jobs = [(None, "全部")]
    if args.section:
        flat = []
        for s in secs["sections"]:
            flat.append(s)
            flat += s.get("children") or []
        hit = next((s for s in flat if str(s["id"]) == args.section), None)
        if not hit:
            sys.exit(f"未找到小节 {args.section}")
        qs = hit.get("queries") or []
        if not qs:
            sys.exit(f"小节 {args.section} 未配置 queries（第 4 章需人工跟进非 arXiv 来源）")
        jobs = [(" OR ".join(qs), f"{hit['id']} {hit['title']}")]

    seen, rows = set(), []
    for extra, label in jobs:
        print(f"检索 {label} … {args.start} → {args.end}", file=sys.stderr)
        for p in parse(search(extra, args.start, args.end)):
            if p["id"] in seen:
                continue
            seen.add(p["id"])
            rows.append(p)
        time.sleep(SLEEP)

    new = [r for r in rows if r["id"] not in have]
    dup = len(rows) - len(new)

    print(f"\n召回 {len(rows)} 篇，去重后新增 {len(new)} 篇（库中已有 {dup} 篇）\n")
    if not new:
        print("本窗口无新增。若窗口末端是今天，注意 arXiv 当天投稿通常尚未索引，")
        print("需在 commit / PR 中标明实际覆盖区间，并把缺的天留给下一轮起点。")
        return

    for r in sorted(new, key=lambda x: x["v1"], reverse=True):
        print(f"{r['v1']}  {r['id']}  [{r['cat']}]")
        print(f"          {r['title'][:96]}")
        print(f"          命中形态词: {', '.join(r['forms']) or '⚠ 无（需人工确认是否属本仓库范围）'}")
        print()

    from collections import Counter
    print("v1 日期分布:", dict(sorted(Counter(r["v1"] for r in new).items())))
    print("\n下一步：人工判断范围（剔除仅把 GUI agent 当实验环境之一的通用安全工作），")
    print("      归类到小节后写入 data/papers.yaml，再跑 build.py 与 check_links.py。")


if __name__ == "__main__":
    main()
