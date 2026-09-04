#!/usr/bin/env python3
"""
从 data/papers.yaml + data/sections.yaml 生成：
  - README.md
  - papers_by_section/<id>.md
  - papers_by_env/<env>.md

用法：
    python3 scripts/build.py           # 生成
    python3 scripts/build.py --check   # 只校验，不写文件（CI 用）

设计约定：README 与分组文件都是产物，绝不手工编辑。
"""
import argparse
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("需要 PyYAML：pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

REPO = "Yuxuan2003/Awesome-GUI-Agent-Security"
ENV_LABEL = {"web": "Web", "mobile": "Mobile", "desktop": "Desktop", "cross": "跨环境"}


def load():
    papers = yaml.safe_load((DATA / "papers.yaml").read_text(encoding="utf-8"))["papers"]
    secs = yaml.safe_load((DATA / "sections.yaml").read_text(encoding="utf-8"))
    return papers, secs


def flatten(sections):
    """展平章节树，返回 [(id, title, desc, stock, is_leaf, depth)]"""
    out = []
    for s in sections:
        kids = s.get("children") or []
        out.append((s["id"], s["title"], s.get("desc"), s.get("stock"), not kids, 0))
        for c in kids:
            out.append((c["id"], c["title"], c.get("desc"), c.get("stock"), True, 1))
    return out


def validate(papers, secs):
    """返回错误列表。CI 靠这个拦住脏数据。"""
    errs = []
    valid_secs = {i for i, *_ in flatten(secs["sections"])}
    valid_envs = {e["id"] for e in secs["envs"]}
    seen_ids, seen_titles = {}, {}

    for idx, p in enumerate(papers):
        tag = p.get("abbr") or p.get("title", "")[:40] or f"#{idx}"

        for f in ("title", "date", "section", "env", "summary"):
            if not p.get(f):
                errs.append(f"[{tag}] 缺少必填字段 {f}")

        if not p.get("id") and not p.get("url"):
            errs.append(f"[{tag}] 必须有 id（arXiv）或 url（非 arXiv 来源）之一")

        aid = p.get("id")
        if aid:
            if not re.fullmatch(r"\d{4}\.\d{4,5}", str(aid)):
                errs.append(f"[{tag}] arXiv ID 格式非法：{aid}（不应带版本号）")
            if "XXXXX" in str(aid).upper():
                errs.append(f"[{tag}] arXiv ID 是占位符未回填：{aid}")
            if aid in seen_ids:
                errs.append(f"[{tag}] arXiv ID 与 [{seen_ids[aid]}] 重复：{aid}")
            seen_ids[aid] = tag

        t = re.sub(r"\W+", "", p.get("title", "")).lower()
        if t and t in seen_titles:
            errs.append(f"[{tag}] 标题与 [{seen_titles[t]}] 近似重复")
        seen_titles[t] = tag

        if p.get("date") and not re.fullmatch(r"\d{4}-\d{2}", str(p["date"])):
            errs.append(f"[{tag}] date 应为 YYYY-MM：{p['date']}")

        if p.get("section") and str(p["section"]) not in valid_secs:
            errs.append(f"[{tag}] section 未定义：{p['section']}")

        for e in p.get("env") or []:
            if e not in valid_envs:
                errs.append(f"[{tag}] env 未定义：{e}")

        s = (p.get("summary") or "").strip()
        if s and len(s) < 60:
            errs.append(f"[{tag}] 简介过短（{len(s)} 字），惯例 150–300 字含动机/机制/关键数字")
    return errs


def entry(p):
    """渲染单条目。格式与 awesome-agentic 的中文简介惯例一致。"""
    head = p["title"]
    if p.get("abbr"):
        head += f" ({p['abbr']})"
    head += f" ({p['date']})"

    lines = [f"#### {head}", f"- **简介**：{' '.join((p['summary'] or '').split())}"]

    envs = "、".join(ENV_LABEL.get(e, e) for e in (p.get("env") or []))
    meta = f"- **环境**：{envs}"
    if p.get("venue") and p["venue"] != "arXiv":
        meta += f" ｜ **发表**：{p['venue']}"
    lines.append(meta)

    if p.get("id"):
        lines.append(f"- **arXiv**：[{p['id']}](https://arxiv.org/abs/{p['id']})")
    elif p.get("url"):
        lines.append(f"- **链接**：{p['url']}")
    if p.get("code"):
        lines.append(f"- **代码**：{p['code']}")
    return "\n".join(lines)


def sort_key(p):
    """同节内按 v1 日期倒序（新的在前）。"""
    return (p.get("date", ""), p.get("id", ""))


def anchor_of(sid, title):
    """GitHub 风格锚点：小写、去标点、空格转连字符。
    注意标题里的 '/' 必须去掉，否则锚点失效（如 'Desktop / OS 环境基准'）。"""
    s = f"{sid} {title}".lower()
    s = re.sub(r"[^\w\s\u4e00-\u9fff-]", "", s)   # 去标点，保留中日韩字符与连字符
    return re.sub(r"\s+", "-", s.strip())


def build_readme(papers, secs):
    by_sec = defaultdict(list)
    for p in papers:
        by_sec[str(p["section"])].append(p)

    total = len(papers)
    rounded = total // 10 * 10
    badge_papers = f"{rounded}%2B" if rounded >= 10 else str(total)
    ym = date.today().strftime("%Y.%m")

    L = []
    L.append("# Awesome-GUI-Agent-Security")
    L.append("")
    L.append("> GUI / Computer-Use / 浏览器 Agent 安全论文清单 —— 按攻防轴组织，每篇附中文简介")
    L.append("")
    L.append(
        f"![Last Update](https://img.shields.io/badge/last%20update-{ym}-brightgreen) "
        f"![Papers](https://img.shields.io/badge/papers-{badge_papers}-blue) "
        f"![Time Range](https://img.shields.io/badge/time-2025.01--{ym}-orange) "
        f"[![Link Check](https://github.com/{REPO}/actions/workflows/check.yml/badge.svg)]"
        f"(https://github.com/{REPO}/actions/workflows/check.yml) "
        "![Awesome](https://img.shields.io/badge/-awesome-ff69b4)"
    )
    L.append("")
    L.append("## 这个仓库收录什么")
    L.append("")
    L.append(
        "只收录**以 GUI / computer-use / browser / mobile agent 为主要研究对象**的安全工作，"
        "按「威胁模型 → 攻击面 → 防御层 → 评测」组织。"
    )
    L.append("")
    L.append("**不收录**：")
    L.append("")
    L.append("- 通用 LLM / Agent 安全工作（仅把 GUI agent 当作若干实验环境之一）")
    L.append("- 用 agent 做安全工作（渗透测试、漏洞挖掘、CTF）")
    L.append("- 纯能力向工作（grounding 精度、任务成功率提升）")
    L.append("")
    L.append("## 为什么按攻防轴而不按环境组织")
    L.append("")
    L.append(
        "现有的 GUI agent 清单大多按运行环境（Web / Mobile / Desktop）切分，"
        "结果是同一类攻击被打散：多步间接注入落在 Desktop、效率后门落在 Mobile、"
        "弹窗攻击横跨 Web 与 Desktop 两处。想回答「视觉层攻击有哪些」就得翻遍所有分组。"
    )
    L.append("")
    L.append(
        "本仓库以**攻击载体与防御介入时点**为一级维度，运行环境降为交叉标签"
        "（仅在第 3 章评测基准内做二级切分）。"
    )
    L.append("")
    L.append("## 目录")
    L.append("")
    for sid, title, _desc, _stock, is_leaf, depth in flatten(secs["sections"]):
        L.append(f"{'  ' * depth}- [{sid} {title}](#{anchor_of(sid, title)})")
    L.append("")
    L.append("按环境浏览：" + " ｜ ".join(
        f"[{ENV_LABEL[e['id']]}](papers_by_env/{e['id']}.md)" for e in secs["envs"]))
    L.append("")
    L.append("---")
    L.append("")

    for sid, title, desc, stock, is_leaf, depth in flatten(secs["sections"]):
        L.append(f"{'#' * (2 + depth)} {sid} {title}")
        L.append("")
        if desc:
            L.append(f"*{' '.join(str(desc).split())}*")
            L.append("")

        if not is_leaf:
            continue

        items = sorted(by_sec.get(sid, []), key=sort_key, reverse=True)
        if items:
            for p in items:
                L.append(entry(p))
                L.append("")
        else:
            note = "*本节暂无收录条目*"
            if stock:
                note += f"（arXiv 存量约 {stock} 篇待整理，欢迎 PR）"
            L.append(note)
            L.append("")

    L.append("---")
    L.append("")
    L.append("## 贡献")
    L.append("")
    L.append(
        "只需修改 `data/papers.yaml`，`README.md` 与 `papers_by_*/` 下所有文件"
        "由 GitHub Actions 自动生成。收录标准与条目格式见 [CONTRIBUTING.md](CONTRIBUTING.md)，"
        "维护流程见 [MAINTENANCE.md](MAINTENANCE.md)。"
    )
    L.append("")
    L.append("## 相关仓库")
    L.append("")
    L.append("本仓库聚焦 GUI/CUA agent 自身安全，以下方向请见：")
    L.append("")
    L.append("- 通用 agent 安全（OWASP ASI 全谱系）：`LLMSecurity/awesome-agent-skills-security`")
    L.append("- 用 agent 做安全工作（红队 / 渗透测试）：`kagnlp/Awesome-Agentic-Security`")
    L.append("- agent 审计与溯源：`yzhao062/awesome-auditable-ai`")
    L.append("- GUI agent 能力向研究：`OSU-NLP-Group/GUI-Agents-Paper-List`")
    L.append("")
    return "\n".join(L) + "\n"


def build_group(papers, heading, note=None):
    L = [f"# {heading}", ""]
    if note:
        L += [note, ""]
    L.append("> 本文件由 `scripts/build.py` 生成，请勿手工编辑。")
    L.append("")
    if not papers:
        L += ["*暂无条目*", ""]
    for p in sorted(papers, key=sort_key, reverse=True):
        L.append(entry(p))
        L.append("")
    return "\n".join(L)


def check_anchors(readme):
    """校验目录锚点都能对上标题。中文标题与含 '/' 的标题最容易出问题。"""
    links = re.findall(r"\]\(#([^)]+)\)", readme)
    heads = [
        re.sub(r"\s+", "-", re.sub(r"[^\w\s\u4e00-\u9fff-]", "", h.strip().lower()))
        for h in re.findall(r"^#{2,4} (.+)$", readme, re.M)
    ]
    return [l for l in links if l not in heads]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="只校验，不写文件")
    args = ap.parse_args()

    papers, secs = load()

    errs = validate(papers, secs)
    if errs:
        print(f"校验失败，{len(errs)} 个问题：\n", file=sys.stderr)
        for e in errs:
            print(f"  ✗ {e}", file=sys.stderr)
        sys.exit(1)
    print(f"✓ 校验通过：{len(papers)} 篇")

    readme = build_readme(papers, secs)

    bad = check_anchors(readme)
    if bad:
        print(f"目录锚点失效 {len(bad)} 个：{bad}", file=sys.stderr)
        sys.exit(1)
    print("✓ 目录锚点全部有效")

    if args.check:
        return

    (ROOT / "README.md").write_text(readme, encoding="utf-8")
    print("✓ README.md")

    titles = {i: t for i, t, *_ in flatten(secs["sections"])}
    by_sec = defaultdict(list)
    for p in papers:
        by_sec[str(p["section"])].append(p)
    for sid, items in sorted(by_sec.items()):
        f = ROOT / "papers_by_section" / f"{sid}.md"
        f.write_text(build_group(items, f"{sid} {titles.get(sid, '')}"), encoding="utf-8")
    print(f"✓ papers_by_section/（{len(by_sec)} 个）")

    for e in secs["envs"]:
        items = [p for p in papers if e["id"] in (p.get("env") or [])]
        f = ROOT / "papers_by_env" / f"{e['id']}.md"
        f.write_text(
            build_group(items, f"{ENV_LABEL[e['id']]} 环境",
                        "*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*"),
            encoding="utf-8")
    print(f"✓ papers_by_env/（{len(secs['envs'])} 个）")


if __name__ == "__main__":
    main()
