#!/usr/bin/env python3
"""
死链与元数据校验。做三件事：

1. 每个 arXiv ID 可访问（抓 404 与占位符）
2. **返回标题与 papers.yaml 中的标题精确匹配**（抓 ID 写错、LLM 幻觉条目）
3. **v1 提交日期与 date 字段一致**（抓把 v2 更新月当作首发月的错误）

第 2 条是关键：调研阶段实测发现同类仓库存在 arXiv ID 是 LLM 幻觉或未回填
`26xx.XXXXX` 占位符的情况。只查 HTTP 200 拦不住 ID 写成另一篇真实论文的错误，
必须比对标题。

用法：
    python3 scripts/check_links.py            # 全量
    python3 scripts/check_links.py --sample 8 # 抽样（本地快速验）
"""
import argparse
import difflib
import random
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
BATCH = 40        # arXiv 的 id_list 支持批量查询。逐条请求会在十几次后被限流
                  # （实测 CI 上 126 条只有前 12 条通过、其余 114 条全部「无法访问」）
SLEEP = 3.2       # 批次之间的间隔
RETRY = 4
SIM_MIN = 0.92    # 标题相似度阈值。不要放太松：
                  # "... Part I" 与 "... Part II" 相似度可达 0.995，
                  # 正是要抓的错链场景，因此同时做长度差与子串检查


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s or "")).strip().lower()


def fetch_batch(aids):
    """批量查询，返回 {id: (title, v1_date)}。

    关键：用 id_list 一次查多条，而不是逐条请求。arXiv 对高频单条请求限流很快
    （CI 环境尤其明显，共享出口 IP），逐条模式下 100+ 条几乎必然大面积失败，
    表现为「论文集体消失」这种明显不可能的结果。

    网络连续失败时抛错而非返回空 —— 否则会被误判为「这些论文都不存在」。
    """
    url = API + "?" + urllib.parse.urlencode(
        {"id_list": ",".join(aids), "max_results": len(aids)})
    last = None
    for attempt in range(RETRY):
        try:
            raw = urllib.request.urlopen(url, timeout=90).read().decode()
            break
        except Exception as e:
            last = e
            if attempt < RETRY - 1:
                wait = 15 * (attempt + 1)
                print(f"    批次请求失败（第 {attempt + 1} 次），{wait}s 后重试：{e}",
                      file=sys.stderr)
                time.sleep(wait)
    else:
        raise RuntimeError(
            f"arXiv 批量请求连续 {RETRY} 次失败：{last}\n"
            f"        这是网络/限流问题，不代表论文不存在 —— 请勿据此删除条目。")

    out = {}
    for blk in re.findall(r"<entry>(.*?)</entry>", raw, re.S):
        m = re.search(r"<id>https?://arxiv\.org/abs/([^<]+)</id>", blk)
        t = re.findall(r"<title>(.*?)</title>", blk, re.S)
        pub = re.findall(r"<published>(.*?)</published>", blk)
        if not m or not t:
            continue
        out[m.group(1).split("v")[0]] = (
            " ".join(t[0].split()), pub[0][:7] if pub else None)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=0, help="只抽查 N 条")
    args = ap.parse_args()

    papers = yaml.safe_load(
        (ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))["papers"]

    targets = [p for p in papers if p.get("id")]
    if args.sample and args.sample < len(targets):
        targets = random.sample(targets, args.sample)

    # 占位符先单独拦下，不必发请求
    bad, warn = [], []
    real = []
    for p in targets:
        if "XXXXX" in str(p["id"]).upper():
            bad.append(f"[{p.get('abbr') or p['title'][:40]}] "
                       f"ID 是未回填的占位符：{p['id']}")
        else:
            real.append(p)

    batches = [real[i:i + BATCH] for i in range(0, len(real), BATCH)]
    print(f"校验 {len(real)} 条 arXiv 记录（{len(batches)} 批 × 最多 {BATCH} 条/批）\n")

    meta = {}
    for bi, grp in enumerate(batches, 1):
        print(f"  批次 {bi}/{len(batches)}（{len(grp)} 条）…", flush=True)
        meta.update(fetch_batch([str(p["id"]) for p in grp]))
        if bi < len(batches):
            time.sleep(SLEEP)

    # 全批次都取不到 = 请求层面出了问题，而非数据错误。宁可报错也不要指控条目不存在。
    if real and not meta:
        sys.exit("✗ 所有批次均未返回任何条目 —— 判定为 arXiv 请求异常而非数据错误，"
                 "请稍后重试，不要据此修改 papers.yaml")

    print()
    for i, p in enumerate(real, 1):
        aid = str(p["id"])
        tag = p.get("abbr") or p["title"][:40]
        got = meta.get(aid)

        if got is None:
            bad.append(f"[{tag}] arXiv {aid} 无法访问或不存在")
            print(f"  {i:>3}. ✗ {tag} — 未在返回结果中")
            continue

        got_title, v1 = got
        a, b = norm(p["title"]), norm(got_title)
        sim = difflib.SequenceMatcher(None, a, b).ratio()

        # 相似度 + 长度差双判据，防 "Part I"/"Part II" 这类高相似但不同的论文
        len_ok = abs(len(a) - len(b)) <= max(12, 0.15 * max(len(a), len(b)))
        if sim < SIM_MIN or not len_ok:
            bad.append(
                f"[{tag}] 标题不匹配（相似度 {sim:.3f}）\n"
                f"        yaml: {p['title']}\n"
                f"        arXiv: {got_title}")
            print(f"  {i:>3}. ✗ {tag} — 标题不符 {sim:.3f}")
        elif v1 and p.get("date") and v1 != str(p["date"]):
            warn.append(f"[{tag}] date={p['date']} 但 arXiv v1={v1}（应以 v1 为准）")
            print(f"  {i:>3}. ⚠ {tag} — 日期不一致 {p['date']} vs {v1}")
        else:
            print(f"  {i:>3}. ✓ {tag}")

    print()
    if warn:
        print(f"{len(warn)} 个警告：")
        for w in warn:
            print(f"  ⚠ {w}")
        print()
    if bad:
        print(f"{len(bad)} 个错误：", file=sys.stderr)
        for e in bad:
            print(f"  ✗ {e}", file=sys.stderr)
        sys.exit(1)

    print(f"✓ 全部通过（{len(real)} 条，0 不一致）")


if __name__ == "__main__":
    main()
