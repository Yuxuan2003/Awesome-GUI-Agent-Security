# 贡献指南

## 一句话流程

**只改 `data/papers.yaml`**，提 PR。`README.md` 与 `papers_by_*/` 下所有文件由
GitHub Actions 自动生成 —— 请勿手工编辑它们，你的改动会被覆盖。

---

## 收录边界（硬规则）

### ✅ 收录

论文的**主要研究对象**是 GUI agent / computer-use agent / browser agent / mobile agent，
且研究内容属于安全范畴：攻击、防御、越狱、注入、隐私、后门、风险评测。

### ❌ 不收录

| 类型 | 说明 | 该去哪 |
|---|---|---|
| 通用 LLM / Agent 安全 | 仅把 GUI agent 当作若干实验环境之一，主要贡献不针对 GUI/CUA 形态 | `LLMSecurity/awesome-agent-skills-security` |
| 用 agent 做安全工作 | 渗透测试、漏洞挖掘、CTF、威胁狩猎 | `kagnlp/Awesome-Agentic-Security` |
| agent 审计与溯源 | provenance、audit trail、可观测性 | `yzhao062/awesome-auditable-ai` |
| 纯能力向工作 | grounding 精度、任务成功率、推理效率 | `OSU-NLP-Group/GUI-Agents-Paper-List` |
| 具身智能 / 机器人安全 | 物理世界交互为主 | `x-zheng16/Awesome-Embodied-AI-Safety` |

**为什么把边界写这么死**：同类仓库普遍出现过范围失守 —— 某个 GUI agent 安全清单收了 42 篇，
其中「Misc（通用领域）」类占 18 篇成为最大分组，收进了通用 LLM 安全的护栏模型、多模态安全
基准等工作。结果是一个 CUA 安全仓库里最大的分组不是 CUA。本仓库不重复这个错误。

**判据**：如果把论文标题里的 "GUI agent" / "computer-use agent" 换成 "LLM"，论文的贡献依然
成立，那它大概率不属于本仓库。

### 时间范围

只收 **2025.01 起**的工作。日期以 **arXiv v1 首次提交**为准，不是 v2/v3 更新月 ——
CI 会自动比对并拦截。

---

## 条目格式

在 `data/papers.yaml` 的 `papers:` 下追加：

```yaml
  - id: "2608.06477"
    title: "StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection"
    abbr: "StepJack"
    date: "2026-08"
    venue: "arXiv"
    section: "1.1"
    env: [desktop, cross]
    summary: >-
      针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI
      基准 StepJack，构造 480 个测试用例……实验显示多步注入相比单步把攻击成功率最高抬升
      31.2 个百分点。
    code: https://github.com/...    # 可选
```

### 字段要求

| 字段 | 必填 | 说明 |
|---|---|---|
| `id` | △ | arXiv ID，**不带版本号**。非 arXiv 来源用 `url` 代替 |
| `title` | ✅ | 官方完整标题，**必须与 arXiv 精确一致**（CI 会比对） |
| `abbr` | | 方法/基准缩写 |
| `date` | ✅ | `YYYY-MM`，arXiv **v1** 提交月 |
| `venue` | | 会议/期刊，未发表填 `arXiv` |
| `section` | ✅ | 小节 ID，见 `data/sections.yaml` |
| `env` | ✅ | `web` / `mobile` / `desktop` / `cross`，可多选 |
| `summary` | ✅ | **中文** 2–4 句、150–300 字 |
| `code` | | 代码仓库 URL |

△ = `id` 与 `url` 至少有一个

### 简介怎么写

三段式：**动机 → 机制 → 关键数字**。

- ✅ `实测 Claude Code 搭配 Qwen3-Coder 的攻击成功率达 73.63%`
- ❌ `实验表明该方法效果显著`

数字要具体到指标名与数值。术语保留英文原文（`prompt injection`、`grounding`、
`accessibility tree` 等），行文用中文。

### 归类原则

- **一篇论文只放一个小节。** 跨领域时选最贴近的主贡献，在 PR 描述里说明理由。
- 按**攻击载体**归类，不按运行环境 —— 环境走 `env` 字段。
  例：移动端的无障碍树注入 → `1.3 环境注入` + `env: [mobile]`，而不是放进某个「Mobile」章节。
- 拿不准时**先收录 + 在 PR 里列明理由**，让维护者定夺，不要自行删掉。

---

## 本地验证

```bash
pip install pyyaml

python3 scripts/build.py              # 生成 README 与分组文件
python3 scripts/build.py --check      # 只校验结构，不写文件
python3 scripts/check_links.py --sample 8   # 抽查 arXiv 元数据
```

`check_links.py` 会校验三件事，任一不过 CI 就会失败：

1. arXiv ID 可访问（拦 404 与 `XXXXX` 占位符）
2. **返回标题与 yaml 精确匹配**（拦 ID 写错、条目凭空编造）
3. **v1 日期与 `date` 字段一致**（拦把 v2 更新月当首发月）

第 2 条不能省。只查 HTTP 200 拦不住「ID 指向另一篇真实论文」的错误。
