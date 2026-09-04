# 维护手册

本仓库的日常维护流程。设计目标：**只改一个 YAML，其余全自动**。

---

## 双周更新流程

### 为什么是双周而非周更

实测该方向 arXiv 增量约 **4.3 篇/周**，波动很大（某周只召回 1 篇）。周更会频繁空窗，
双周窗口约 9 篇召回、4–6 篇收录，节奏更稳。

实测记录：

| 窗口 | 召回 | 收录 | 剔除 |
|---|---|---|---|
| 2026.08.20–09.02 | 9 | 4 | 5（纯能力向 2 / 可靠性视角 3） |

### 步骤

**1. 确认上次实际覆盖到哪天**

不是上次「请求」到哪天。查库里最大的 arXiv ID：

```bash
grep 'id: "' data/papers.yaml | sort -t'"' -k2 -r | head -3
```

**当天投稿几乎必然未索引** —— 窗口终点写到今天没关系，但必须在 commit 里标明实际覆盖区间，
把缺的天留给下一轮起点。

**2. 检索候选**

```bash
python3 scripts/fetch.py 2026-09-03 2026-09-16
```

脚本会自动剔除库中已有 ID，输出 v1 日期、主分类、命中的形态词。

若某小节想单独补历史存量：

```bash
python3 scripts/fetch.py 2025-01-01 2026-09-04 --section 1.2
```

**3. 人工判断范围（不能省的一步）**

对每篇候选问三个问题：

1. **主要研究对象**是 GUI/CUA/browser/mobile agent 吗？还是只把它当实验环境之一？
2. 主要贡献在**安全**吗？还是能力/可靠性/效率？
3. 把标题里的 "GUI agent" 换成 "LLM"，贡献是否依然成立？成立 → 不收。

实测常见的剔除类型：

| 类型 | 例子 | 判断 |
|---|---|---|
| 纯能力向技术报告 | UI-Venus-2 Technical Report | 剔 |
| 系统优化综述 | Efficient GUI Agents: A Systems Survey | 剔 |
| 可靠性/检测视角 | Monitoring Web Agents、Automated Trajectory Evaluation | 边界，倾向剔并在 commit 说明 |
| 反检测（攻方但非 agent 安全） | ActReal（对抗自动化检测） | 边界 |

**拿不准时收录 + 在 commit / PR 里列明理由**，不要自行删掉。但对「纯能力向」要果断剔除。

**4. 撰写条目**

读原文摘要（不要只看标题）：

```bash
curl -s "https://export.arxiv.org/api/query?id_list=2608.27808" | \
  python3 -c "import sys,re;raw=sys.stdin.read();print(' '.join(re.findall(r'<summary>(.*?)</summary>',raw,re.S)[0].split()))"
```

简介三段式：**动机 → 机制 → 关键数字**。数字要具体到指标名与数值。

**5. 校验并提交**

```bash
python3 scripts/build.py          # 生成产物 + 校验结构与锚点
python3 scripts/check_links.py    # 全量校验 arXiv 元数据
git diff --stat                   # 确认只动了预期文件
```

Commit message 模板：

```
Add N papers from YYYY.MM.DD to YYYY.MM.DD

新增（召回 X 篇，收录 N 篇）：
  §1.1 间接提示注入  方法名（一句话）
  §2.3 执行中拦截    方法名（一句话）

按范围剔除 M 篇：
  论文名 —— 理由

N 篇全部通过 arXiv 元数据校验。
```

---

## 第 4 章需要单独跟进

`4 商用 AI 浏览器与产品安全` **不能靠 arXiv 检索**。实测 `browser agent` / `browser-use`
在 arXiv 三周召回 **0 篇**，但 Atlas / Comet / Edge Copilot Mode 类产品的安全问题是当期热点 ——
相关工作走的是厂商安全公告、CVE、安全博客、漏洞披露。

建议跟进渠道：

- 厂商安全公告与 changelog
- CVE / NVD 检索 AI browser 相关条目
- Simon Willison 的 prompt injection 追踪系列
- Embrace The Red 等 agent 安全研究博客

这类条目在 `papers.yaml` 里用 `url` 字段代替 `id`。

---

## 存量建库

首发只铺了 14 篇，各节存量（2026-09-04 实测，见 `data/sections.yaml` 的 `stock` 字段）：

| 节 | 存量 | 已收 |
|---|---|---|
| 1.3 环境注入 | 65 | 2 |
| 1.5 数据泄露与隐私 | 63 | 1 |
| 1.1 间接提示注入 | 56 | 3 |
| 1.4 越权与权限滥用 | 28 | 2 |
| 1.2 视觉层攻击 | 18 | 0 |
| 1.7 良性指令意外危害 | 18 | 1 |
| 0 综述与威胁模型 | 15 | 0 |
| 1.6 后门与投毒 | 10 | 1 |
| 2 防御层 | 104 | 2 |
| 3 评测基准 | 143 | 2 |

**总存量约 252 篇**（2025-01 至 2026-09，含跨类重叠）。建议按 `1.1 → 1.3 → 1.5 → 3.x → 2.x`
顺序分批补齐，每批 15–25 篇，一批一个 PR，便于回溯。

---

## 检索 query 的三个坑（实测）

**1. 三层交集不能省。** 形态词 × 安全词 × 分类键。少任何一层都会出问题：
只用形态词混入能力向论文；只用安全词混入通用 LLM 安全；分类键不叠加前两层则存量虚高数倍 ——
实测 `benchmark` 一项召回 726 篇，收紧后仅 143 篇（因为 benchmark 在能力向论文里是标配词）。

**2. 不能强制 `AND security`。** 这类论文惯用 attack / injection / safety / hijack。
实测强制 security 使召回从 5.3 篇/周 压到 0.7 篇/周。

**3. 单个形态词都撑不起来。** computer-use agent 1.3/周、GUI agent 1.7/周、mobile 1.0/周、
web agent 0.3/周。必须用并集。

---

## 常见问题

**Q: 改了 papers.yaml 但 README 没变？**
跑 `python3 scripts/build.py`。或者推到 main 后由 Actions 自动重建。

**Q: CI 报「标题不匹配」？**
以 arXiv 返回的标题为准修改 yaml。这个检查专门拦 ID 写错和条目凭空编造 ——
实测同类仓库存在 arXiv ID 是 LLM 幻觉或 `26xx.XXXXX` 未回填占位符的情况。

**Q: CI 报「date 与 v1 不一致」？**
以 v1 为准。收录日期是**首次提交月**，不是 v2/v3 更新月。

**Q: 某节长期没有条目怎么办？**
保留骨架，不要为凑数降低收录标准。ASI/威胁模型分类本身就是有价值的信号 ——
某节为空说明该攻击面研究稀缺，这是领域现状而非仓库缺陷。
