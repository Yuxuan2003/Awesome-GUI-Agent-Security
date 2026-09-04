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
import re
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
SLEEP = 3.5

CATS = ("cat:cs.CR OR cat:cs.AI OR cat:cs.CL OR cat:cs.LG OR "
        "cat:cs.MA OR cat:cs.SE OR cat:cs.HC OR cat:cs.CV OR cat:cs.MM")

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


def q_or(field, terms):
    return "(" + " OR ".join(
        f'{field}:"{t}"' if " " in t or "-" in t else f"{field}:{t}"
        for t in terms) + ")"


def search(extra, start_ymd, end_ymd, max_results=100):
    s = start_ymd.replace("-", "") + "0000"
    e = end_ymd.replace("-", "") + "2359"
    parts = [f"({CATS})", q_or("abs", FORMS), q_or("abs", SECS),
             f"submittedDate:[{s} TO {e}]"]
    if extra:
        parts.append(f"({extra})")
    params = urllib.parse.urlencode({
        "search_query": " AND ".join(parts),
        "start": 0, "max_results": max_results,
        "sortBy": "submittedDate", "sortOrder": "descending",
    })
    for attempt in range(3):
        try:
            return urllib.request.urlopen(API + "?" + params, timeout=60).read().decode()
        except Exception:
            if attempt == 2:
                return ""
            time.sleep(12)
    return ""


def parse(xml):
    out = []
    for blk in re.findall(r"<entry>(.*?)</entry>", xml, re.S):
        aid = re.search(r"<id>http://arxiv\.org/abs/([^<]+)</id>", blk)
        ti = re.search(r"<title>(.*?)</title>", blk, re.S)
        pub = re.search(r"<published>(.*?)</published>", blk)
        summ = re.search(r"<summary>(.*?)</summary>", blk, re.S)
        cat = re.search(r'<category term="([^"]+)"', blk)
        if not (aid and ti):
            continue
        ab = " ".join((summ.group(1) if summ else "").split()).lower()
        out.append({
            "id": aid.group(1).split("v")[0],
            "title": " ".join(ti.group(1).split()),
            "v1": pub.group(1)[:10] if pub else "?",
            "cat": cat.group(1) if cat else "?",
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
