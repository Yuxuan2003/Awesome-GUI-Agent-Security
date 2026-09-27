#!/usr/bin/env python3
"""
幂等地把一批新条目合并进 data/papers.yaml。

为什么需要这个脚本：直接 `cat batch.yaml >> data/papers.yaml` 在重试或
命令被中断重跑时会把同一批追加两次。虽然 build.py 的重复校验能拦住，
但事后截断修正很容易多切或少切。此脚本在写入前先比对 arXiv ID，
已存在的条目直接跳过，因此可以安全地反复执行。

用法：
    python3 scripts/merge.py /tmp/batch.yaml
    python3 scripts/merge.py /tmp/batch.yaml --dry-run

输入文件格式：与 data/papers.yaml 的 papers 列表项相同的 YAML 片段
（顶层可以有或没有 `papers:` 键，两种都接受）。
"""
import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 PyYAML：pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
TARGET = ROOT / "data" / "papers.yaml"


def load_batch(path):
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if raw is None:
        return []
    if isinstance(raw, dict):
        return raw.get("papers") or []
    if isinstance(raw, list):
        return raw
    sys.exit(f"无法解析 {path}：顶层应为列表或含 papers 键的字典")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batch", help="待合并的 YAML 片段路径")
    ap.add_argument("--dry-run", action="store_true", help="只报告，不写入")
    args = ap.parse_args()

    existing = yaml.safe_load(TARGET.read_text(encoding="utf-8"))["papers"]
    have_ids = {str(p.get("id")) for p in existing if p.get("id")}
    have_urls = {str(p.get("url")) for p in existing if p.get("url")}

    batch = load_batch(args.batch)
    if not batch:
        sys.exit("待合并文件为空")

    fresh, dup = [], []
    seen_in_batch = set()
    for p in batch:
        key = str(p.get("id") or p.get("url") or "")
        tag = p.get("abbr") or p.get("title", "")[:40]
        if not key:
            sys.exit(f"[{tag}] 缺少 id 与 url，无法判重")
        if key in have_ids or key in have_urls or key in seen_in_batch:
            dup.append((tag, key))
            continue
        seen_in_batch.add(key)
        fresh.append(p)

    for tag, key in dup:
        print(f"  跳过（已存在）{key}  {tag}")
    print(f"\n待合并 {len(batch)} 条：新增 {len(fresh)}，跳过 {len(dup)}")

    if args.dry_run or not fresh:
        return

    # 以文本方式追加，保留原文件里手写的 >- 折行与注释风格
    text = Path(args.batch).read_text(encoding="utf-8")
    # 关键：剥掉批文件顶层的 `papers:` 键。
    # 历史 bug（2026-09-25）：整段追加时把 `papers:` 也写进去了，文件里出现两个
    # 顶层 `papers:` 键，PyYAML 取最后一个 —— 原来的 139 条全部被解析丢弃，
    # 只剩新批次的 10 条。build.py --check 会如实打印「10 篇」，但如果没看这行
    # 就直接提交，等于静默删库。因此这里剥离键，并在写入后做数量自检。
    lines = text.split("\n")
    if lines and lines[0].strip() == "papers:":
        lines = lines[1:]
    text = "\n".join(lines).strip("\n")
    if dup:
        # 有跳过项时不能整段追加，改为逐条 dump
        chunk = yaml.dump(fresh, allow_unicode=True, sort_keys=False,
                          default_flow_style=False, width=100)
        chunk = "\n".join("  " + ln if ln.strip() else ln
                          for ln in chunk.split("\n"))
        chunk = chunk.replace("  - id:", "- id:", 1)
        chunk = "\n  " + chunk.lstrip()
    else:
        chunk = text if text.startswith("\n") else "\n" + text

    # 先拼出完整文本并校验，确认无误再落盘 —— 绝不让损坏的中间状态留在源文件上
    merged = TARGET.read_text(encoding="utf-8").rstrip() + chunk.rstrip() + "\n"
    check = yaml.safe_load(merged)
    if not isinstance(check, dict) or list(check.keys()) != ["papers"]:
        sys.exit(f"✗ 合并结果顶层键异常：{list(check.keys()) if isinstance(check, dict) else type(check)}，"
                 f"已放弃写入（源文件未改动）")
    if len(check["papers"]) != len(existing) + len(fresh):
        sys.exit(f"✗ 合并后条目数 {len(check['papers'])} ≠ 原有 {len(existing)} + 新增 {len(fresh)}，"
                 f"已放弃写入（源文件未改动）—— 多半是批文件混入了第二个 papers: 键")
    TARGET.write_text(merged, encoding="utf-8")
    print(f"✓ 已写入 {TARGET.relative_to(ROOT)}（{len(existing)} → {len(check['papers'])} 篇）")
    print("  接着跑：python3 scripts/build.py")


if __name__ == "__main__":
    main()
