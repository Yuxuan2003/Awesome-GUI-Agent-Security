# Awesome-GUI-Agent-Security

[English](README.md) ｜ **简体中文**

> GUI / Computer-Use / 浏览器 Agent 安全论文清单 —— 按攻防轴组织，而非按运行环境。

![Last Update](https://img.shields.io/badge/last%20update-2026.09-brightgreen) ![Papers](https://img.shields.io/badge/papers-30%2B-blue) ![Time Range](https://img.shields.io/badge/time-2025.01--2026.09-orange) [![Link Check](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml/badge.svg)](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml) ![Awesome](https://img.shields.io/badge/-awesome-ff69b4)

## 收录范围

只收录**主要研究对象**是 GUI / computer-use / browser / mobile agent，且贡献属于安全范畴的论文。

**不收录：**

- 通用 LLM / Agent 安全工作（仅把 GUI agent 当作若干实验环境之一）
- 用 agent 做安全工作（渗透测试、漏洞挖掘、CTF）
- 纯能力向工作（grounding 精度、任务成功率提升）

## 为什么按攻防轴而不按环境组织

现有的 GUI agent 清单大多按运行环境（Web / Mobile / Desktop）切分，结果是同一类攻击被打散：多步间接注入落在 Desktop、效率后门落在 Mobile、弹窗攻击横跨 Web 与 Desktop 两处。想回答「视觉层攻击有哪些」就得翻遍所有分组。

本仓库以**攻击载体与防御介入时点**为一级维度，运行环境降为交叉标签，仅在评测基准一章内作为一级维度使用。

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
  - [3.4 Desktop 与 OS 环境基准](#34-desktop-与-os-环境基准)
- [4 商用 AI 浏览器与产品安全](#4-商用-ai-浏览器与产品安全)

按环境浏览： [Web](docs/by-env/web.zh-CN.md) ｜ [Mobile](docs/by-env/mobile.zh-CN.md) ｜ [Desktop](docs/by-env/desktop.zh-CN.md) ｜ [跨环境](docs/by-env/cross.zh-CN.md)

---

## 0 综述与威胁模型

*领域综述、SoK、以及 OWASP ASI / MITRE ATLAS 等威胁分类框架的对照*

#### A Systematization of Security Vulnerabilities in Computer Use Agents (CUA Vuln SoK) (2025-07)

对真实 CUA 做系统化威胁分析与对抗测试，归纳出七类该范式独有的风险，并深入剖析三个具体 利用链：用视觉覆盖层误导界面级推理的 clickjacking、经工具链串联实现远程代码执行的间接提示 注入、以及通过操纵隐式界面语境劫持多步推理的 CoT 暴露攻击。三个案例共同指向当前实现的 三处架构性缺陷：缺少输入来源追踪、界面与动作绑定薄弱、控制流完整性不足。

`环境: Desktop, Web` ｜ [arXiv:2507.05445](https://arxiv.org/abs/2507.05445)

#### Towards Trustworthy GUI Agents: A Survey (Trustworthy GUI Survey) (2025-03)

把「执行落差」（execution gap）确立为可信 GUI agent 的核心障碍——即在动态、部分可观测界面下 感知、推理与交互三者之间的错配。与对话系统不同，GUI agent 执行的是提交表单、授予权限、删除 数据这类不可逆操作。综述提出与工作流对齐的分类法，把信任拆为感知信任、推理信任、交互信任 三层，梳理失败如何在动作/观察循环中传播并累积，并主张仅用任务完成率评估可信度是不充分的。

`环境: 跨环境` ｜ [arXiv:2503.23434](https://arxiv.org/abs/2503.23434)

## 1 攻击面

*按攻击载体与入口组织，而非按运行环境*

### 1.1 间接提示注入

*经网页、文档、邮件等外部内容承载的注入*

#### SIR: Self-improving Red-teaming for Compute Use Agents (SIR) (2026-08)

指出现有 CUA 安全基准用的都是人工手写的固定注入载荷，会低估自适应攻击者的真实威胁。提出 黑盒 IPI 攻击 SIR：从一个用自然语言描述的可复用「隐蔽性原则」小库中组合注入内容，再套一层 迭代反馈循环——诊断受害 agent 失败的攻击轨迹，把成功绕过的模式蒸馏回原则库。这把红队从 静态测试变成自我改进的过程，说明固定载荷的评测结论会随攻击者迭代迅速失效。

`环境: Desktop, Web` ｜ [arXiv:2608.30207](https://arxiv.org/abs/2608.30207)

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)

针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI 基准 StepJack，构造 480 个测试用例，把注入载荷分散在多步任务的中间环节，模拟攻击者只能污染 流程某一环的现实约束。实验显示多步注入相比单步把攻击成功率最高抬升 31.2 个百分点， 说明单步评测显著低估了 CUA 的真实暴露面，且现有防御在流程中段几乎不再触发。

`环境: Desktop, 跨环境` ｜ [arXiv:2608.06477](https://arxiv.org/abs/2608.06477)

#### Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents (Invisible Ink) (2026-08)

研究攻击者如何把恶意目标伪装在看似合法的任务描述中，使 CUA 在执行用户确认过的正常任务时 顺带完成攻击者目标。核心发现是这类攻击能绕过 human-in-the-loop 确认机制——因为人工审核 看到的动作序列本身每一步都合理，只有组合起来才产生危害。这揭示了「逐步确认」这一主流 防御范式的结构性盲区。

`环境: Desktop` ｜ [arXiv:2608.02018](https://arxiv.org/abs/2608.02018)

### 1.2 视觉层攻击

*对抗补丁、弹窗诱导、排版攻击、截图污染*

#### MIRAGE: Stealthy Visual Prompt Injection for Vulnerability Detection in Web Agents (MIRAGE) (2026-06)

批评现有针对多模态 web agent 的对抗评测普遍采用过于宽松的威胁模型、依赖视觉上显眼的 伪影。本文转向受约束的现实设定：评测者只是不具特权的第三方（如商家或广告主），仅能控制 广告位、赞助卡片这类语义合法且空间受限的区域。在此约束下提出视觉间接注入框架 MIRAGE， 实现对下一步动作的定向劫持，说明即便攻击者只掌握页面上一小块合法区域，也足以操纵 基于视觉的 agent。

`环境: Web` ｜ [arXiv:2606.20717](https://arxiv.org/abs/2606.20717)

#### Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection (Semantic UI Injection) (2026-04)

指出现有 GUI agent 红队研究的两个局限：对抗扰动需要商业部署中拿不到的白盒访问，而提示 注入正被日益增强的安全对齐所化解。提出黑盒范式「语义级 UI 元素注入」——把本身安全对齐、 内容无害的 UI 元素叠加到截图上以误导视觉 grounding，用模块化的 Editor-Overlapper-Victim 流水线配合迭代搜索。在 8 个模型家族共 19 个受害模型上，策略化优化相比随机注入在最鲁棒的 模型上高出 3.5–6.9 倍，且跨架构迁移性近乎完美。

`环境: 跨环境` ｜ [arXiv:2604.07831](https://arxiv.org/abs/2604.07831)

### 1.3 环境注入

*UI 元素注入、无障碍树、伪造通知、覆盖层*

#### Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments (AnTrap) (2026-08)

指出现有基准缺乏对 GUI agent 运行时异常鲁棒性的系统评估，而 Android 实机部署中意外弹窗、 动作误用等动态扰动十分常见。提出基准 AnTrap，把真实异常归纳为 State / Thinking / Action / Round 四层共十个细分类别，并设计了在注入对抗扰动的同时保持任务仍可完成的构造流程。评测 16 个主流 GUI 模型显示对动态异常存在普遍脆弱性，最强模型也出现显著性能下降；作者还在 原始与对抗环境下各做一轮 GRPO 训练，以区分环境难度与模型能力两个混杂因素。

`环境: Mobile` ｜ [arXiv:2608.24099](https://arxiv.org/abs/2608.24099)

#### Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection (Not an A11y) (2026-08)

指出 Android 无障碍树（accessibility tree）是移动 agent 的一条被忽视的注入通道：任何 应用都能往无障碍节点写入文本，而 agent 会把这些内容当作可信的界面语义读取。攻击者无需 任何特殊权限即可通过普通应用注入指令。这条路径完全绕开了针对视觉截图或网页内容的 防御，暴露出移动 agent 输入通道治理的缺失。

`环境: Mobile` ｜ [arXiv:2608.08939](https://arxiv.org/abs/2608.08939)

#### Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents (eTAMP) (2026-04)

记忆让 web agent 变得个性化，也使其可被利用：存储历史交互创造出跨站点、跨会话持续存在的 攻击面。已有研究假设攻击者能直接写入记忆或利用跨用户共享，而 eTAMP 仅靠环境观察就实现 跨会话跨站点污染——单次被污染的观察（如浏览一个被操纵的商品页）即可静默投毒记忆，并在 日后其他网站的任务中激活，绕开基于权限的防御。攻击成功率在 GPT-5-mini 上达 32.5%、 GPT-5.2 上 23.4%、GPT-OSS-120B 上 19.5%，另发现「挫败感利用」现象。

`环境: Web` ｜ [arXiv:2604.02623](https://arxiv.org/abs/2604.02623)

#### AdInject: Real-World Black-Box Attacks on Web Agents via Advertising Delivery (AdInject) (2025-05)

批评已有环境注入研究依赖不现实的假设——直接改 HTML、已知用户意图、或能访问模型参数。 AdInject 改用互联网广告投放这一真实渠道注入恶意内容，威胁模型严格得多：agent 为黑盒、 恶意内容静态不可变、且不掌握用户意图。方法上结合诱导 agent 点击的广告内容设计，以及 基于 VLM 从目标站点反推用户潜在意图的内容优化，是该方向最贴近真实部署的威胁模型之一。

`环境: Web` ｜ [arXiv:2505.21499](https://arxiv.org/abs/2505.21499)

### 1.4 越权与权限滥用

*OS 级越权、跨应用提权、权限弹窗诱导、TOCTOU*

#### "Allow" to Achieve, Over-Privileged Inadvertently: The Unintended Cost of Task-Completion-Driven Pop-up Decisions in Mobile GUI Agents (Allow to Achieve) (2026-08)

发现移动 GUI agent 在遇到权限弹窗时存在系统性的过度授权倾向，识别出两种偏差：App-Trust Bias（对已安装应用默认信任而一律点允许）与 Task-Prior Override（为达成任务目标而牺牲 权限最小化）。结果是 agent 在用户不知情的情况下累积远超任务所需的权限，把权限弹窗这一 最后防线变成了形式。

`环境: Mobile` ｜ [arXiv:2608.04755](https://arxiv.org/abs/2608.04755)

#### (A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents (AI Sees) (2026-07)

系统分析第三方移动 agent 引入的新攻击面，核心是「感知鸿沟」——agent 能读取到屏幕上用户 实际看不到或不会注意的内容（隐藏视图、后台通知、无障碍节点），攻击者可利用这一差异实施 用户完全无法察觉的诱导。指出第三方 agent 生态缺乏对 agent 可见性范围的约束机制。

`环境: Mobile` ｜ [arXiv:2607.00333](https://arxiv.org/abs/2607.00333)

#### Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents (PUSV) (2026-04)

把「截图—点击」循环中的观察到动作间隔（真实 OSWorld 负载下平均 6.51 秒）形式化为「视觉 原子性破坏」，指出这构成一个 TOCTOU 窗口，无特权攻击者可在其中篡改 UI 状态。刻画三种攻击 原语：通知覆盖劫持、窗口焦点操纵、网页 DOM 注入——其中第二种是 Android Action Rebinding 的桌面对应物，动作重定向成功率 100% 且在观察时刻不留任何视觉痕迹。提出 PUSV 防御，在每次 动作派发前立即复验 UI 状态（点击目标处的掩码像素 SSIM、全局截图差分、X Window 快照差分）， 在 180 次对抗试验中拦截率 100%、零误报、开销低于 0.1 秒。

`环境: Desktop` ｜ [arXiv:2604.18860](https://arxiv.org/abs/2604.18860)

#### Mind the Gap: Action Rebinding Attacks against Android GUI Agents (Action Rebinding) (2026-01)

指出把 GUI agent 当作高权限操作者（跨应用边界感知屏幕、注入输入）与 Android 严格的应用 沙箱机制存在根本冲突。跨应用 Action Rebinding 攻击让一个不申请任何危险权限的恶意应用即可 劫持 agent 执行：先渲染一个无害的「上下文载体」诱导 agent 规划出某个动作，再在其推理延迟 窗口内把前台切换到敏感目标应用，agent 察觉不到切换、于是在特权上下文中执行了该动作。 作者进一步利用 agent 自身的任务恢复逻辑，把攻击武器化为可编程的多步利用循环。

`环境: Mobile` ｜ [arXiv:2601.12349](https://arxiv.org/abs/2601.12349)

### 1.5 数据泄露与隐私

*凭据窃取、PII 外泄、上下文完整性破坏、过度分享*

#### LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents (LoginTrap) (2026-08)

登录对 web agent 而言是涉及凭据的敏感认证边界，但已有工作尚未考察恶意页面内容能否诱导 agent 登录并造成端到端的私密数据泄漏。LoginTrap 是一种与任务无关的诱导登录攻击，假设 黑盒攻击者只控制页面上下文与被诱导的登录流程，并不知道用户任务或 agent 内部实现：通过 类 fuzzing 的流程生成页面专属的间接注入内容，使「先登录」看起来是继续完成任务的合理 前置条件，从而把 agent 引导至攻击者控制的登录页。

`环境: Web` ｜ [arXiv:2608.04741](https://arxiv.org/abs/2608.04741)

#### Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? (Capable but Careless) (2026-06)

用「上下文完整性」（contextual integrity）框架考察 CUA 在跨应用操作时是否会不当传播敏感 信息。结论是能力越强的 agent 反而越容易越界：它们为完成任务会主动把 A 应用中的私密数据 带入 B 应用的输入框，而这类行为不触发任何现有的隐私告警，因为每一次读写都在授权范围内。 提出了以信息流而非权限边界为判据的评估方法。

`环境: Desktop` ｜ [arXiv:2606.23189](https://arxiv.org/abs/2606.23189)

#### Do Phone-Use Agents Respect Your Privacy? (MyPhoneBench) (2026-04)

追问手机操作类 agent 在完成正常任务时是否尊重隐私。这一问题此前难以回答，因为隐私合规 行为从未被形式化定义，且普通应用不会暴露 agent 究竟把哪些数据填进了哪个表单项。 MyPhoneBench 用一份最小隐私契约把「尊重隐私」操作化为三条：授权访问、最小披露、用户可控 记忆，并配以插桩的模拟应用与规则化审计。在 5 个前沿模型、10 个应用、300 个任务上发现， 任务成功率、隐私合规完成度、后续会话中对已存偏好的使用是三种彼此独立的能力，无一模型全占优。

`环境: Mobile` ｜ [arXiv:2604.00986](https://arxiv.org/abs/2604.00986)

#### WebPII: Benchmarking Visual PII Detection for Computer-Use Agents (WebPII) (2026-03)

CUA 从两个方向带来新的隐私风险：从真实网站采集的训练数据不可避免含敏感信息，而云端推理 会暴露用户截图。此前没有公开基准用于检测网页截图中的个人身份信息。WebPII 提供 44865 张 标注的电商 UI 图像，特点包括扩展的 PII 分类（含可用于重识别的交易级标识符）、针对用户 正在填写的半完成表单的前瞻式检测、以及基于 VLM 的可扩展 UI 复现。配套 WebRedact 把 文本抽取基线准确率翻倍以上（0.753 vs 0.357 mAP@50），CPU 延迟仅 20ms。

`环境: Web, Desktop` ｜ [arXiv:2603.17357](https://arxiv.org/abs/2603.17357)

#### SPILLage: Agentic Oversharing on the Web (SPILLage) (2026-02)

与在受控环境中回答问题的聊天机器人不同，web agent 是「在野」运行的：它能访问用户的邮件、 日历等资源，与第三方交互，并留下动作轨迹。本文把「自然的 agent 过度分享」形式化为—— 通过这条动作轨迹无意披露与任务无关的用户信息，并沿「通道」（内容 vs. 行为）与「直接性」 （显式 vs. 隐式）两个维度刻画。这揭示了一处盲区：已有工作聚焦文本泄漏，但 agent 还会通过 点击、滚动、导航模式等行为层面过度暴露，而这些可被第三方监测。在真实电商站点的 180 个 任务上做了基准评测。

`环境: Web` ｜ [arXiv:2602.13516](https://arxiv.org/abs/2602.13516)

### 1.6 后门与投毒

*grounding 后门、效率后门、记忆投毒*

#### AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents (AgentRAE) (2026-03)

已有针对 web GUI agent 的后门依赖环境注入或欺骗性弹窗，但在基于截图的移动 agent 上失效—— 触发器设计空间受限、操作系统后台干扰、以及多个触发器与动作映射之间相互冲突。AgentRAE 用 视觉上自然的触发器（如通知栏里的正常应用图标）诱发远程动作执行，采用两阶段流程：先用 对比学习强化 agent 对细微图标差异的敏感度，再通过后门后训练把每个触发器绑定到特定动作。

`环境: Mobile` ｜ [arXiv:2603.23007](https://arxiv.org/abs/2603.23007)

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)

提出针对 VLM-based GUI agent 的效率后门：触发器不改变任务最终结果，只让 agent 的响应 延迟大幅增加或步数显著膨胀。这类后门极难被察觉——正确性检测全部通过，只有观察资源消耗 才能发现，因此可长期潜伏并造成持续的算力成本损失。拓展了 GUI agent 后门的威胁定义， 从「结果篡改」扩展到「可用性与经济性攻击」。

`环境: Mobile, 跨环境` ｜ [arXiv:2603.08316](https://arxiv.org/abs/2603.08316)

### 1.7 良性指令下的意外危害

*无恶意攻击者，agent 自身在正常指令下造成危害*

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)

提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。

`环境: Mobile, 跨环境` ｜ [arXiv:2607.29199](https://arxiv.org/abs/2607.29199)

## 2 防御层

*按防御在执行链上的介入时点组织*

### 2.1 输入侧过滤与净化

#### Untrusted Content Masking for Web Agents with Security Guarantees (UCM) (2026-07)

指出可证明的注入防御依赖可信指令与不可信数据之间的严格隔离，这在纯文本的 tool-use 场景 中天然成立（agent 可只依据接口定义推理，无需接触不可信内容），但 web agent 必须先观察 渲染后的页面才能感知环境，而页面把可信与不可信内容结构性地混在一起，导致安全保证赖以 成立的信任边界消失。提出 Untrusted Content Masking，利用页面的结构特性在 web 环境中 重建这一边界，使既有的可证明防御能够迁移过来。

`环境: Web` ｜ [arXiv:2607.05277](https://arxiv.org/abs/2607.05277)

#### The Cognitive Firewall: Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense (Cognitive Firewall) (2026-03)

针对「云端防御语义分析能力强但引入延迟与隐私暴露」这一矛盾，提出三阶段拆分计算架构 Cognitive Firewall，把安全检查分布在客户端与云端：本地视觉 Sentinel、云端 Deep Planner、 以及在执行期强制策略的确定性 Guard。在 1000 个对抗样本上，纯边端防御漏检 86.9% 的语义 攻击，而完整混合架构把攻击成功率压到 1% 以下（静态评测 0.88%、自适应评测 0.67%），同时 对有副作用的动作保持确定性约束；由于表现层攻击在本地即被过滤，相比纯云端基线取得约 17000 倍的延迟优势。

`环境: Web` ｜ [arXiv:2603.23791](https://arxiv.org/abs/2603.23791)

### 2.2 执行前风险评估

*世界模型预测、动作风险打分*

#### WebGuard: Building a Generalizable Guardrail for Web Agents (WebGuard) (2025-07)

主张 web agent 需要类似人类用户的访问控制机制，并发布首个支持 agent 动作风险评估的数据集： 来自 22 个领域、193 个网站（含常被忽视的长尾站点）的 4939 条人工标注状态改变动作，按 SAFE / LOW / HIGH 三级风险标注，并划分好训练测试集以支持泛化研究。核心结论相当刺眼—— 即便前沿 LLM 预测动作后果的准确率也不足 60%。

`环境: Web` ｜ [arXiv:2507.14293](https://arxiv.org/abs/2507.14293)

### 2.3 执行中拦截与权限控制

*信息流追踪、OS 级策略强制、沙箱*

#### CURA: Certified Runtime Alarms for Computer-Use Agents (CURA) (2026-08)

揭示 self-report 这一最廉价的监督通道恰恰在最需要它的地方失效：在 361 个 OSWorld 任务上， 流水线平均分 82.9（超过人类基线 72.4），但 71 次失败里有 64 次（90%）以「成功」收尾， 61 次声称没有遇到任何阻碍，约 9100 次调用中显式的失败上报机制从未被使用。提出外部监控器 CURA，只读 harness 可见的遥测数据，不需模型内部状态、额外 LLM 调用或改 prompt，把运行 轨迹转成带误报率保证的序贯检验：α=0.10 时 CUSUM 告警能在终止前中位 31 步检出 42.3% 的 失败，实测误报率 0.066。

`环境: Desktop` ｜ [arXiv:2608.27808](https://arxiv.org/abs/2608.27808)

#### Prismata: Confining Cross-Site Prompt Injection in Web Agents (Prismata) (2026-07)

把 web agent 面临的注入风险类比为 XSS 的重现：XSS 已经证明混合可信与不可信内容是危险的， 而 agent 把自然语言当指令解释，使第三方与用户生成内容能够劫持 agent。核心难点在于推导 任务专属的安全策略需要理解页面结构，而页面结构本身已与攻击者内容纠缠。提出 Prismata， 借鉴经典完整性模型的思路做动态信任推导，为页面内容打上权限标签并提供结构性隔离保证， 同时约束 agent「能看到什么」与「能做什么」，实现上下文最小权限。

`环境: Web` ｜ [arXiv:2607.08147](https://arxiv.org/abs/2607.08147)

#### Secure and Efficient Access Control for Computer-Use Agents via Context Space (CSAgent) (2025-09)

主张把计算机控制权交给 agent 之所以危险，根源在 LLM 固有的不确定性——一旦动作偏离用户 意图，后果可能不可逆；而用户确认与基于 LLM 的动态校验分别在可用性、安全性或性能上有短板。 CSAgent 是系统级、基于静态策略的访问控制框架，通过「意图感知 + 上下文感知」策略弥合静态 策略与动态上下文之间的落差，并提供自动化工具链协助开发者构造与精炼策略，最终由优化过的 操作系统服务强制执行，确保动作只在特定用户意图与上下文下才被允许。

`环境: Desktop` ｜ [arXiv:2509.22256](https://arxiv.org/abs/2509.22256)

### 2.4 人在环与确认机制

*本节暂无收录条目*

### 2.5 事后恢复与回滚

#### CUADebug: Diagnosing and Repairing Computer-Use Agent Failures (CUADebug) (2026-07)

面向 CUA 执行失败后的诊断与修复，提出定位失败步骤并生成修复方案的框架。虽以可靠性为 出发点，但其失败归因与状态回滚能力可直接用于安全事件的事后恢复——在 agent 被注入劫持后 判断从哪一步开始偏离、并回退到最后一个可信状态。是「事后恢复」这一防御层中较少见的 系统性工作。

`环境: Desktop` ｜ [arXiv:2608.02643](https://arxiv.org/abs/2608.02643)

### 2.6 形式化保证与验证

#### CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation (CORA) (2026-04)

现有 GUI agent 防护依赖 prompt 工程、脆弱的启发式规则与 VLM-as-critic，既无形式化验证也 不提供用户可调的保证。CORA 是一个「策略之后、动作之前」的防护框架，对已执行的有害动作 给出统计保证：把安全性重构为选择性动作执行，训练 Guardian 模型估计动作条件风险，再用 Conformal Risk Control 校准满足用户指定风险预算的执行/弃权边界，被拒动作交由 Diagnostician 做多模态推理并建议确认、反思或中止。另设 Goal-Lock 机制抵御视觉注入。

`环境: Mobile` ｜ [arXiv:2604.09155](https://arxiv.org/abs/2604.09155)

## 3 评测基准与数据集

*本章二级按运行环境切分（这是环境标签唯一作为一级组织维度的地方）*

### 3.1 综合与跨环境基准

#### ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agents Across Devices (ADeptS-Bench) (2026-08)

针对「没有基准能同时考察 CUA 在视觉界面下的安全性与对模糊指令的处理」这一空缺，提出双流 可信度基准 ADeptS-Bench：Safety 流提供威胁嵌在视觉界面中的良性/恶意配对任务，Disambiguation 流考察 agent 在意图模糊时是否会主动澄清。评测 7 个模型的结论相当刺眼——没有模型能在任务 成功率超 80% 的同时把攻击成功率压到 30% 以下；所有模型都会毫不犹豫点下 2.5 万美元订单的 「结账」，也没有一个能识别出被标为「优化」的按钮实际是「恢复出厂设置」。

`环境: Desktop, Mobile` ｜ [arXiv:2608.26204](https://arxiv.org/abs/2608.26204)

#### AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents (AgentHazard) (2026-04)

针对 CUA 具备跨工具、跨文件持久化操作能力后产生的新型安全风险，构建覆盖多风险类别与 攻击策略的基准 AgentHazard，含 2653 个实例。关键结论是有害行为往往由一串「单看都合理、 合起来不安全」的动作累积产生。实测 Claude Code 搭配 Qwen3-Coder 的攻击成功率达 73.63%， 表明仅靠底座模型的对齐无法保障 agent 层面的安全。

`环境: Desktop` ｜ [arXiv:2604.02947](https://arxiv.org/abs/2604.02947)

### 3.2 Web 环境基准

#### Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents (Who Pays the Price) (2026-06)

指出现有安全基准都采用「攻击视角」，只关注注入在技术上是否可行，忽略了危害在不同受害方 之间的分布差异。本文主张注入风险是**受害者依赖**的：同一个漏洞对不同利益相关方（用户、 平台、商家）造成的后果高度不对称，同一攻击模式的有效性也随目标不同而显著变化。据此构建 以利益相关方为中心的基准，聚焦电商这类动作直接带来财务后果的真实场景。

`环境: Web` ｜ [arXiv:2606.13385](https://arxiv.org/abs/2606.13385)

### 3.3 Mobile 环境基准

#### MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps (MobileWorldSafety) (2026-08)

指出现有基准脱离日常使用场景，缺乏对移动 GUI agent 在环境注入下的系统评估——而这类 agent 已从研究原型走向真实部署，且日常操作中会不断处理不可信的环境内容。提出基于真实 Android 应用构建的基准 MobileWorldSafety，含 142 个风险任务，覆盖间接提示注入与对抗 指令等多种日常渠道，每个任务都定义了可程序化验证的判定条件，使攻击是否成功可被客观测量。

`环境: Mobile` ｜ [arXiv:2608.17659](https://arxiv.org/abs/2608.17659)

#### GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments? (GhostEI-Bench) (2025-10)

把环境注入确立为区别于提示类攻击的、研究不足的威胁向量：它不改文本指令，而是把欺骗性 覆盖层、伪造通知这类对抗 UI 元素直接插入 GUI 以污染 agent 的视觉感知，从而绕开文本层 防护，可导致隐私泄漏、财务损失甚至不可逆的设备失陷。GhostEI-Bench 跳出静态图像评测， 在完整可运行的 Android 模拟器中把对抗事件注入真实应用工作流。

`环境: Mobile` ｜ [arXiv:2510.20333](https://arxiv.org/abs/2510.20333)

### 3.4 Desktop 与 OS 环境基准

#### OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents (OS-Harm) (2025-06)

指出 CUA 已在快速部署但安全性长期被忽视，基于 OSWorld 环境构建 OS-Harm，考察三类危害： 用户故意滥用、提示注入攻击、模型自身失当行为。含 150 个任务，覆盖骚扰、侵犯版权、虚假 信息、数据外泄等违规类型，要求 agent 操作邮件客户端、代码编辑器、浏览器等多种应用。 配套自动评判器同时评估准确性与安全性，与人工标注一致性达 0.76 / 0.79 F1。

`环境: Desktop` ｜ [arXiv:2506.14866](https://arxiv.org/abs/2506.14866)

## 4 商用 AI 浏览器与产品安全

*本章以非 arXiv 来源为主（厂商安全公告、CVE、安全博客、漏洞披露）。 原因：arXiv 上 browser agent / browser-use 三周召回 0 篇，但 Atlas / Comet / Edge Copilot Mode 类产品安全是当期热点，相关工作不走论文渠道。 周更时本章需单独走非 arXiv 检索流程，不要因 arXiv 无结果就跳过。*

*本节暂无收录条目*

---

## 贡献

只需修改 **`data/papers.yaml`** —— `README.md`、`README.zh-CN.md` 与 `docs/` 下所有文件均由 GitHub Actions 自动生成。收录标准与条目格式见 [CONTRIBUTING.md](CONTRIBUTING.md)，维护流程见 [MAINTENANCE.md](MAINTENANCE.md)。

## 相关仓库

本仓库聚焦 GUI/CUA agent 自身安全，以下方向请见：

- 通用 agent 安全（OWASP ASI 全谱系）：`LLMSecurity/awesome-agent-skills-security`
- 用 agent 做安全工作（红队 / 渗透测试）：`kagnlp/Awesome-Agentic-Security`
- agent 审计与溯源：`yzhao062/awesome-auditable-ai`
- GUI agent 能力向研究：`OSU-NLP-Group/GUI-Agents-Paper-List`

