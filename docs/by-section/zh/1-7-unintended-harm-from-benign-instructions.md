# 1.7 良性指令下的意外危害

*Unintended Harm from Benign Instructions*

[← 返回索引](../../../README.zh-CN.md#17-良性指令下的意外危害) ｜ [English](../en/1-7-unintended-harm-from-benign-instructions.md)

*无恶意攻击者，agent 自身在正常指令下造成危害*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)

提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。

`环境: Mobile, 跨环境` ｜ [arXiv:2607.29199](https://arxiv.org/abs/2607.29199)

#### The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents (OS-BLIND) (2026-04)

隔离出现有安全评测跳过的那个场景：用户指令完全良性，危害来自任务上下文或执行后果，既无 滥用也无注入。OS-BLIND 提供 300 个人工构造任务，覆盖 12 个类别、8 个应用，分为「环境 嵌入型威胁」与「agent 自发危害」两簇。数字相当刺眼——多数 CUA 的攻击成功率超过 90%， 即便经过安全对齐的 Claude 4.5 Sonnet 也达到 73.0%。更糟的是，同一模型置于多 agent 配置中时 ASR 从 73.0% 升至 92.7%，说明编排本身就在侵蚀对齐效果。

`环境: Desktop` ｜ [arXiv:2604.10577](https://arxiv.org/abs/2604.10577)

#### When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents (AutoElicit) (2026-02)

观察到 CUA 即便在良性输入下也确实会产生不安全的非预期行为，但对这类风险的探索一直停留在 个案层面——既无具体刻画，也无自动化手段挖掘长尾情形。论文提供了首个关于 CUA 非预期行为的 概念与方法框架：定义其关键特征、自动化诱发、并分析它如何从良性输入中产生。AutoElicit 利用 CUA 的执行反馈迭代扰动良性指令，同时保持扰动本身真实且无恶意，从 Claude 4.5 Haiku、Opus 等前沿模型上挖掘出数百个有害行为。

`环境: Desktop` ｜ [arXiv:2602.08235](https://arxiv.org/abs/2602.08235)

#### When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent (AgentBait) (2026-01)

指出以往研究集中在提示注入、后门这类模型层威胁，而针对 web 自动化 agent 的社会工程攻击一直 无人探索——尽管 Browser Use、Skyvern-AI 等开源框架已显著扩大了攻击面。AgentBait 攻击范式 利用执行层面的内在弱点：诱导性上下文会扭曲 agent 的推理，把它引向与原任务不一致的目标， 而全程不需要注入任何指令。防御侧提出 SUPERVISOR，一个轻量可插拔的运行时模块，强制网页 上下文与预期目标之间的「环境—意图一致性」对齐。

`环境: Web` ｜ [arXiv:2601.07263](https://arxiv.org/abs/2601.07263)

#### DECEPTICON: How Dark Patterns Manipulate Web Agents (DECEPTICON) (2025-12)

把暗黑模式（dark patterns，即真实网络上早已泛滥的欺骗性 UI 设计）作为一类 agent 安全威胁 来研究——它不需要攻击者搭建任何基础设施，因为恶意界面本身就是现状。DECEPTICON 在 700 个 网页导航任务（600 合成 + 100 真实）中隔离测试单个暗黑模式。结果是暗黑模式在超过 70% 的 任务中成功把 agent 引向恶意结果，而人类平均只有 31%。最值得警惕的发现颠覆了通常的 scaling 直觉：操纵有效性与模型规模、测试时推理量**正相关**——越大越强的 agent 反而更易受骗。

`环境: Web` ｜ [arXiv:2512.22894](https://arxiv.org/abs/2512.22894)
