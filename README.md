# Awesome-GUI-Agent-Security

> GUI / Computer-Use / 浏览器 Agent 安全论文清单 —— 按攻防轴组织，每篇附中文简介

![Last Update](https://img.shields.io/badge/last%20update-2026.09-brightgreen) ![Papers](https://img.shields.io/badge/papers-10%2B-blue) ![Time Range](https://img.shields.io/badge/time-2025.01--2026.09-orange) [![Link Check](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml/badge.svg)](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml) ![Awesome](https://img.shields.io/badge/-awesome-ff69b4)

## 这个仓库收录什么

只收录**以 GUI / computer-use / browser / mobile agent 为主要研究对象**的安全工作，按「威胁模型 → 攻击面 → 防御层 → 评测」组织。

**不收录**：

- 通用 LLM / Agent 安全工作（仅把 GUI agent 当作若干实验环境之一）
- 用 agent 做安全工作（渗透测试、漏洞挖掘、CTF）
- 纯能力向工作（grounding 精度、任务成功率提升）

## 为什么按攻防轴而不按环境组织

现有的 GUI agent 清单大多按运行环境（Web / Mobile / Desktop）切分，结果是同一类攻击被打散：多步间接注入落在 Desktop、效率后门落在 Mobile、弹窗攻击横跨 Web 与 Desktop 两处。想回答「视觉层攻击有哪些」就得翻遍所有分组。

本仓库以**攻击载体与防御介入时点**为一级维度，运行环境降为交叉标签（仅在第 3 章评测基准内做二级切分）。

## 目录

- [0 综述与威胁模型](#0-综述与威胁模型)
- [1 攻击面](#1-攻击面)
  - [1.1 间接提示注入](#11-间接提示注入)
  - [1.2 视觉层攻击](#12-视觉层攻击)
  - [1.3 环境注入](#13-环境注入)
  - [1.4 越权与权限滥用](#14-越权与权限滥用)
  - [1.5 数据泄露与隐私](#15-数据泄露与隐私)
  - [1.6 后门与投毒](#16-后门与投毒)
  - [1.7 良性指令下的意外危害](#17-良性指令下的意外危害)
- [2 防御层](#2-防御层)
  - [2.1 输入侧过滤与净化](#21-输入侧过滤与净化)
  - [2.2 执行前风险评估](#22-执行前风险评估)
  - [2.3 执行中拦截与权限控制](#23-执行中拦截与权限控制)
  - [2.4 人在环与确认机制](#24-人在环与确认机制)
  - [2.5 事后恢复与回滚](#25-事后恢复与回滚)
  - [2.6 形式化保证与验证](#26-形式化保证与验证)
- [3 评测基准与数据集](#3-评测基准与数据集)
  - [3.1 综合与跨环境基准](#31-综合与跨环境基准)
  - [3.2 Web 环境基准](#32-web-环境基准)
  - [3.3 Mobile 环境基准](#33-mobile-环境基准)
  - [3.4 Desktop / OS 环境基准](#34-desktop-os-环境基准)
- [4 商用 AI 浏览器与产品安全](#4-商用-ai-浏览器与产品安全)

按环境浏览：[Web](papers_by_env/web.md) ｜ [Mobile](papers_by_env/mobile.md) ｜ [Desktop](papers_by_env/desktop.md) ｜ [跨环境](papers_by_env/cross.md)

---

## 0 综述与威胁模型

*领域综述、SoK、以及 OWASP ASI / MITRE ATLAS 等威胁分类框架的对照*

*本节暂无收录条目*（arXiv 存量约 15 篇待整理，欢迎 PR）

## 1 攻击面

*按攻击载体与入口组织，而非按运行环境*

### 1.1 间接提示注入

*经网页、文档、邮件等外部内容承载的注入*

#### SIR: Self-improving Red-teaming for Compute Use Agents (SIR) (2026-08)
- **简介**：指出现有 CUA 安全基准用的都是人工手写的固定注入载荷，会低估自适应攻击者的真实威胁。提出 黑盒 IPI 攻击 SIR：从一个用自然语言描述的可复用「隐蔽性原则」小库中组合注入内容，再套一层 迭代反馈循环——诊断受害 agent 失败的攻击轨迹，把成功绕过的模式蒸馏回原则库。这把红队从 静态测试变成自我改进的过程，说明固定载荷的评测结论会随攻击者迭代迅速失效。
- **环境**：Desktop、Web
- **arXiv**：[2608.30207](https://arxiv.org/abs/2608.30207)

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)
- **简介**：针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI 基准 StepJack，构造 480 个测试用例，把注入载荷分散在多步任务的中间环节，模拟攻击者只能污染 流程某一环的现实约束。实验显示多步注入相比单步把攻击成功率最高抬升 31.2 个百分点， 说明单步评测显著低估了 CUA 的真实暴露面，且现有防御在流程中段几乎不再触发。
- **环境**：Desktop、跨环境
- **arXiv**：[2608.06477](https://arxiv.org/abs/2608.06477)

#### Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents (Invisible Ink) (2026-08)
- **简介**：研究攻击者如何把恶意目标伪装在看似合法的任务描述中，使 CUA 在执行用户确认过的正常任务时 顺带完成攻击者目标。核心发现是这类攻击能绕过 human-in-the-loop 确认机制——因为人工审核 看到的动作序列本身每一步都合理，只有组合起来才产生危害。这揭示了「逐步确认」这一主流 防御范式的结构性盲区。
- **环境**：Desktop
- **arXiv**：[2608.02018](https://arxiv.org/abs/2608.02018)

### 1.2 视觉层攻击

*对抗补丁、弹窗诱导、排版攻击、截图污染*

*本节暂无收录条目*（arXiv 存量约 18 篇待整理，欢迎 PR）

### 1.3 环境注入

*UI 元素注入、无障碍树、伪造通知、覆盖层*

#### Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments (AnTrap) (2026-08)
- **简介**：指出现有基准缺乏对 GUI agent 运行时异常鲁棒性的系统评估，而 Android 实机部署中意外弹窗、 动作误用等动态扰动十分常见。提出基准 AnTrap，把真实异常归纳为 State / Thinking / Action / Round 四层共十个细分类别，并设计了在注入对抗扰动的同时保持任务仍可完成的构造流程。评测 16 个主流 GUI 模型显示对动态异常存在普遍脆弱性，最强模型也出现显著性能下降；作者还在 原始与对抗环境下各做一轮 GRPO 训练，以区分环境难度与模型能力两个混杂因素。
- **环境**：Mobile
- **arXiv**：[2608.24099](https://arxiv.org/abs/2608.24099)

#### Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection (Not an A11y) (2026-08)
- **简介**：指出 Android 无障碍树（accessibility tree）是移动 agent 的一条被忽视的注入通道：任何 应用都能往无障碍节点写入文本，而 agent 会把这些内容当作可信的界面语义读取。攻击者无需 任何特殊权限即可通过普通应用注入指令。这条路径完全绕开了针对视觉截图或网页内容的 防御，暴露出移动 agent 输入通道治理的缺失。
- **环境**：Mobile
- **arXiv**：[2608.08939](https://arxiv.org/abs/2608.08939)

### 1.4 越权与权限滥用

*OS 级越权、跨应用提权、权限弹窗诱导*

#### "Allow" to Achieve, Over-Privileged Inadvertently: The Unintended Cost of Task-Completion-Driven Pop-up Decisions in Mobile GUI Agents (Allow to Achieve) (2026-08)
- **简介**：发现移动 GUI agent 在遇到权限弹窗时存在系统性的过度授权倾向，识别出两种偏差：App-Trust Bias（对已安装应用默认信任而一律点允许）与 Task-Prior Override（为达成任务目标而牺牲 权限最小化）。结果是 agent 在用户不知情的情况下累积远超任务所需的权限，把权限弹窗这一 最后防线变成了形式。
- **环境**：Mobile
- **arXiv**：[2608.04755](https://arxiv.org/abs/2608.04755)

#### (A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents (AI Sees) (2026-07)
- **简介**：系统分析第三方移动 agent 引入的新攻击面，核心是「感知鸿沟」——agent 能读取到屏幕上用户 实际看不到或不会注意的内容（隐藏视图、后台通知、无障碍节点），攻击者可利用这一差异实施 用户完全无法察觉的诱导。指出第三方 agent 生态缺乏对 agent 可见性范围的约束机制。
- **环境**：Mobile
- **arXiv**：[2607.00333](https://arxiv.org/abs/2607.00333)

### 1.5 数据泄露与隐私

*凭据窃取、PII 外泄、上下文完整性破坏*

#### Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? (Capable but Careless) (2026-06)
- **简介**：用「上下文完整性」（contextual integrity）框架考察 CUA 在跨应用操作时是否会不当传播敏感 信息。结论是能力越强的 agent 反而越容易越界：它们为完成任务会主动把 A 应用中的私密数据 带入 B 应用的输入框，而这类行为不触发任何现有的隐私告警，因为每一次读写都在授权范围内。 提出了以信息流而非权限边界为判据的评估方法。
- **环境**：Desktop
- **arXiv**：[2606.23189](https://arxiv.org/abs/2606.23189)

### 1.6 后门与投毒

*grounding 后门、效率后门、训练数据投毒*

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)
- **简介**：提出针对 VLM-based GUI agent 的效率后门：触发器不改变任务最终结果，只让 agent 的响应 延迟大幅增加或步数显著膨胀。这类后门极难被察觉——正确性检测全部通过，只有观察资源消耗 才能发现，因此可长期潜伏并造成持续的算力成本损失。拓展了 GUI agent 后门的威胁定义， 从「结果篡改」扩展到「可用性与经济性攻击」。
- **环境**：Mobile、跨环境
- **arXiv**：[2603.08316](https://arxiv.org/abs/2603.08316)

### 1.7 良性指令下的意外危害

*无恶意攻击者，agent 自身在正常指令下造成危害*

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)
- **简介**：提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。
- **环境**：Mobile、跨环境
- **arXiv**：[2607.29199](https://arxiv.org/abs/2607.29199)

## 2 防御层

*按防御在执行链上的介入时点组织*

### 2.1 输入侧过滤与净化

*本节暂无收录条目*

### 2.2 执行前风险评估

*世界模型预测、动作风险打分*

*本节暂无收录条目*

### 2.3 执行中拦截与权限控制

*信息流追踪、OS 级策略强制、沙箱*

#### CURA: Certified Runtime Alarms for Computer-Use Agents (CURA) (2026-08)
- **简介**：揭示 self-report 这一最廉价的监督通道恰恰在最需要它的地方失效：在 361 个 OSWorld 任务上， 流水线平均分 82.9（超过人类基线 72.4），但 71 次失败里有 64 次（90%）以「成功」收尾， 61 次声称没有遇到任何阻碍，约 9100 次调用中显式的失败上报机制从未被使用。提出外部监控器 CURA，只读 harness 可见的遥测数据，不需模型内部状态、额外 LLM 调用或改 prompt，把运行 轨迹转成带误报率保证的序贯检验：α=0.10 时 CUSUM 告警能在终止前中位 31 步检出 42.3% 的 失败，实测误报率 0.066。
- **环境**：Desktop
- **arXiv**：[2608.27808](https://arxiv.org/abs/2608.27808)

### 2.4 人在环与确认机制

*本节暂无收录条目*

### 2.5 事后恢复与回滚

#### CUADebug: Diagnosing and Repairing Computer-Use Agent Failures (CUADebug) (2026-07)
- **简介**：面向 CUA 执行失败后的诊断与修复，提出定位失败步骤并生成修复方案的框架。虽以可靠性为 出发点，但其失败归因与状态回滚能力可直接用于安全事件的事后恢复——在 agent 被注入劫持后 判断从哪一步开始偏离、并回退到最后一个可信状态。是「事后恢复」这一防御层中较少见的 系统性工作。
- **环境**：Desktop
- **arXiv**：[2608.02643](https://arxiv.org/abs/2608.02643)

### 2.6 形式化保证与验证

*本节暂无收录条目*

## 3 评测基准与数据集

*本章二级按运行环境切分（这是环境标签唯一作为一级组织维度的地方）*

### 3.1 综合与跨环境基准

#### ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agents Across Devices (ADeptS-Bench) (2026-08)
- **简介**：针对「没有基准能同时考察 CUA 在视觉界面下的安全性与对模糊指令的处理」这一空缺，提出双流 可信度基准 ADeptS-Bench：Safety 流提供威胁嵌在视觉界面中的良性/恶意配对任务，Disambiguation 流考察 agent 在意图模糊时是否会主动澄清。评测 7 个模型的结论相当刺眼——没有模型能在任务 成功率超 80% 的同时把攻击成功率压到 30% 以下；所有模型都会毫不犹豫点下 2.5 万美元订单的 「结账」，也没有一个能识别出被标为「优化」的按钮实际是「恢复出厂设置」。
- **环境**：Desktop、Mobile
- **arXiv**：[2608.26204](https://arxiv.org/abs/2608.26204)

#### AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents (AgentHazard) (2026-04)
- **简介**：针对 CUA 具备跨工具、跨文件持久化操作能力后产生的新型安全风险，构建覆盖多风险类别与 攻击策略的基准 AgentHazard，含 2653 个实例。关键结论是有害行为往往由一串「单看都合理、 合起来不安全」的动作累积产生。实测 Claude Code 搭配 Qwen3-Coder 的攻击成功率达 73.63%， 表明仅靠底座模型的对齐无法保障 agent 层面的安全。
- **环境**：Desktop
- **arXiv**：[2604.02947](https://arxiv.org/abs/2604.02947)

### 3.2 Web 环境基准

*本节暂无收录条目*

### 3.3 Mobile 环境基准

*本节暂无收录条目*

### 3.4 Desktop / OS 环境基准

*本节暂无收录条目*

## 4 商用 AI 浏览器与产品安全

*本章以非 arXiv 来源为主（厂商安全公告、CVE、安全博客、漏洞披露）。 原因：arXiv 上 browser agent / browser-use 三周召回 0 篇，但 Atlas / Comet / Edge Copilot Mode 类产品安全是当期热点，相关工作不走论文渠道。 周更时本章需单独走非 arXiv 检索流程，不要因 arXiv 无结果就跳过。*

*本节暂无收录条目*

---

## 贡献

只需修改 `data/papers.yaml`，`README.md` 与 `papers_by_*/` 下所有文件由 GitHub Actions 自动生成。收录标准与条目格式见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 相关仓库

本仓库聚焦 GUI/CUA agent 自身安全，以下方向请见：

- 通用 agent 安全（OWASP ASI 全谱系）：`LLMSecurity/awesome-agent-skills-security`
- 用 agent 做安全工作（红队 / 渗透测试）：`kagnlp/Awesome-Agentic-Security`
- agent 审计与溯源：`yzhao062/awesome-auditable-ai`
- GUI agent 能力向研究：`OSU-NLP-Group/GUI-Agents-Paper-List`

