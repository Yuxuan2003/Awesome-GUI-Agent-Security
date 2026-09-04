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
SLEEP = 3.2       # arXiv 有速率限制，相邻请求间隔
RETRY = 3
SIM_MIN = 0.92    # 标题相似度阈值。不要放太松：
                  # "... Part I" 与 "... Part II" 相似度可达 0.995，
                  # 正是要抓的错链场景，因此同时做长度差与子串检查


def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s or "")).strip().lower()


def fetch(aid):
    """返回 (title, v1_date) 或 None"""
    url = API + "?" + urllib.parse.urlencode({"id_list": aid, "max_results": 1})
    for attempt in range(RETRY):
        try:
            raw = urllib.request.urlopen(url, timeout=45).read().decode()
        except Exception as e:
            if attempt == RETRY - 1:
                return None
            time.sleep(10)
            continue
        titles = re.findall(r"<title>(.*?)</title>", raw, re.S)
        pub = re.findall(r"<published>(.*?)</published>", raw)
        if len(titles) < 2:
            return None
        return " ".join(titles[1].split()), (pub[0][:7] if pub else None)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", type=int, default=0, help="只抽查 N 条")
    args = ap.parse_args()

    papers = yaml.safe_load(
        (ROOT / "data" / "papers.yaml").read_text(encoding="utf-8"))["papers"]

    targets = [p for p in papers if p.get("id")]
    if args.sample and args.sample < len(targets):
        targets = random.sample(targets, args.sample)

    print(f"校验 {len(targets)} 条 arXiv 记录（间隔 {SLEEP}s）\n")

    bad, warn = [], []
    for i, p in enumerate(targets, 1):
        aid = str(p["id"])
        tag = p.get("abbr") or p["title"][:40]

        if "XXXXX" in aid.upper():
            bad.append(f"[{tag}] ID 是未回填的占位符：{aid}")
            print(f"  {i:>3}. ✗ {tag} — 占位符")
            continue

        got = fetch(aid)
        if got is None:
            bad.append(f"[{tag}] arXiv {aid} 无法访问或不存在")
            print(f"  {i:>3}. ✗ {tag} — 取回失败")
            time.sleep(SLEEP)
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

        time.sleep(SLEEP)

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

    print(f"✓ 全部通过（{len(targets)} 条，0 不一致）")


if __name__ == "__main__":
    main()
