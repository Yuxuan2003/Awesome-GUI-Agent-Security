# 2.6 形式化保证与验证

*Formal Guarantees & Verification*

[← 返回索引](../../../README.zh-CN.md#26-形式化保证与验证) ｜ [English](../en/2-6-formal-guarantees-verification.md)

*带可证明保证的防御：形式化验证、控制流完整性、共形风险控制*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction (AOHP) (2026-06)

面向终端用户的操作系统是为「以应用为中心」的工作流设计的，对 AI agent 几乎没有原生支持； 因此在传统系统上跑 agent 会带来执行开销与安全风险。agent 原生操作系统的概念正在出现， 但社区缺少一个开放测试平台，来探索 agent 中介的交互究竟需要哪些架构原语。AOHP （Android Open Harness Project）是基于 AOSP 构建的 OS 级 agent harness，核心设计原则是 把 agent 当作一等的 OS 参与者，从而支持自适应用户界面与 agent 友好的运行时环境。收录 于此是因为它把安全问题从行为层面推到了结构层面：它提供了一个基底，可以在其上原型化并 对比面向 GUI agent 的 OS 级隔离与权限原语，而不是给「屏幕抓取」范式事后加装护栏。

`环境: Mobile` ｜ [arXiv:2606.23449](https://arxiv.org/abs/2606.23449)

#### SkillHarness: Harnessing Safe Skills for Computer-Use Agents (SkillHarness) (2026-06)

针对 skill 学习类方法中一个被默认接受的假设：它们从成功轨迹中蒸馏可复用 skill，却隐含假定 环境是静态且安全的，既忽略提示注入这类对抗交互，也忽略弹窗这类环境动态。在动态环境下，这个 假设会产出有风险的 skill 与脆弱的执行——也就是说漏洞被**固化进**了 agent 的可复用库里。 SkillHarness 把 skill 的学习与使用建模为受安全约束的交互过程，引入「skill 边界」以取代 静态的 skill 抽象。

`环境: Desktop` ｜ [arXiv:2606.20636](https://arxiv.org/abs/2606.20636)

#### CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation (CORA) (2026-04)

现有 GUI agent 防护依赖 prompt 工程、脆弱的启发式规则与 VLM-as-critic，既无形式化验证也 不提供用户可调的保证。CORA 是一个「策略之后、动作之前」的防护框架，对已执行的有害动作 给出统计保证：把安全性重构为选择性动作执行，训练 Guardian 模型估计动作条件风险，再用 Conformal Risk Control 校准满足用户指定风险预算的执行/弃权边界，被拒动作交由 Diagnostician 做多模态推理并建议确认、反思或中止。另设 Goal-Lock 机制抵御视觉注入。

`环境: Mobile` ｜ [arXiv:2604.09155](https://arxiv.org/abs/2604.09155)

#### Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks (DMAST) (2026-03)

定位到一处由架构本身造就的攻击面：多模态 web agent 同时消费截图与无障碍树，因此攻击者只需 注入 DOM 就能**同时**污染两个观测通道，并且两边叙述互相一致，使任何跨通道一致性检查都失效。 MiniWob++ 上的漏洞分析显示，带视觉成分的攻击远强于纯文本注入，暴露出以文本为中心的 VLM 安全训练所留下的缺口。DMAST 把 agent 与攻击者的交互形式化为二人零和马尔可夫博弈，通过模仿 学习、带「零确认」策略的 oracle 引导 SFT、以及最后的对抗阶段共训双方。

`环境: Web` ｜ [arXiv:2603.04364](https://arxiv.org/abs/2603.04364)

#### Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System (Aura) (2026-02)

本文主张当前主流的「屏幕即接口」范式本身就是病根而非细节：让 agent 依赖非结构化的视觉 数据，既继承了屏幕固有的结构性脆弱性，也与移动生态的经济基础相冲突。作者以一款已上线的 商用助手为案例做系统性安全分析，把威胁面拆为 Agent 身份、外部接口、内部推理、动作执行 四个维度，暴露出伪造应用身份、视觉欺骗、间接提示注入、越权提权等缺陷，并且都可追溯到 同一个根源——对非结构化像素的依赖。给出的答案是推倒重来：提出 Aura（Agent 通用运行时 架构），用以意图为中心的接口取代脆弱的 GUI 抓取，使安全性来自架构本身，而不是靠给感知层 打补丁。

`环境: Mobile` ｜ [arXiv:2602.10915](https://arxiv.org/abs/2602.10915)

#### CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents (NOVA) (2026-01)

正面处理一个真实的架构僵局：架构隔离通过严格分离「可信规划」与「不可信观测」提供了最强的 注入防护保证，但 CUA 必须持续观测 UI 才能决定每一步动作——这两项要求直接冲突。论文用一个 经检验成立的经验判断来破局：UI 工作流虽然是动态的，但在**结构上是可预测的**。因此 NOVA 采用单次规划：由可信规划器预先给出一份覆盖所有可预期运行时状态的完整分支计划，从而对任意 指令注入提供控制流完整性**保证**，而不是尽力而为的检测。

`环境: Desktop` ｜ [arXiv:2601.09923](https://arxiv.org/abs/2601.09923)

#### LaSM: Layer-wise Scaling Mechanism for Defending Pop-up Attack on GUI Agents (LaSM) (2025-07)

指出针对弹窗式环境注入的现有防御要么需要昂贵重训、要么在归纳性干扰下失效，转而走机制 可解释性路线。论文系统研究这类攻击如何改变 GUI agent 的注意力分布，发现正确输出与错误输出 之间存在**逐层的注意力发散模式**。LaSM 直接利用这一发现，选择性放大关键层的注意力与 MLP 模块，无需任何额外训练即把模型显著性重新对齐到任务相关的屏幕区域——这是把可解释性结论 转化为可部署 GUI agent 防御的少见案例。

`环境: Desktop, Web` ｜ [arXiv:2507.10610](https://arxiv.org/abs/2507.10610)
