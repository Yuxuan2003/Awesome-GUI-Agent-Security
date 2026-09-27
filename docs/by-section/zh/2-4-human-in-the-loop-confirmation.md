# 2.4 人在环与确认机制

*Human-in-the-Loop & Confirmation*

[← 返回索引](../../../README.zh-CN.md#24-人在环与确认机制) ｜ [English](../en/2-4-human-in-the-loop-confirmation.md)

*关键动作前的人工确认、审批门、可打断性*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Mobile GUI Agent Privacy Personalization with Trajectory Induced Preference Optimization (TIPO) (2026-04)

把隐私重新框定为**个性化**问题而非一套固定策略：多数系统只优化任务成功率或效率，忽略了不同 用户想要的隐私姿态本就不同。技术上的关键观察是个性化会引起轨迹的系统性结构异质——隐私优先的 用户偏好拒绝权限、登出、最小化暴露这类保护性动作，产生与效用优先用户在逻辑上不同、长度也 不等的轨迹，从而使标准偏好优化变得不稳定且信息量下降。TIPO 用偏好强度加权突出关键隐私步骤， 并以 padding gating 抑制对齐噪声。

`环境: Mobile` ｜ [arXiv:2604.11259](https://arxiv.org/abs/2604.11259)

#### PrivWeb: Unobtrusive and Content-aware Privacy Protection For Web Agents (PrivWeb) (2025-09)

把设计建立在用户的真实认知上：一项形成性研究（N=15）发现人们普遍误解 agent 的数据使用方式， 并希望数据管理既透明又不打扰——而这两个目标通常是互相牺牲的。PrivWeb 是运行在 web agent 上 的可信附加组件，用本地化 LLM 按用户偏好对界面内容做匿名化，其核心机制是**分级打断**： 自适应通知仅在高敏感信息上暂停任务、交由用户明确控制，而较低敏感度的情形走非打断式处理。 正是这种分级让「人在环」的成本可承受，并通过第二项用户研究（N=14，覆盖旅行、信息检索、 购物与娱乐任务）得到验证。

`环境: Web` ｜ [arXiv:2509.11939](https://arxiv.org/abs/2509.11939)

#### VeriOS: Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents (VeriOS) (2025-09)

多数 OS agent 是为理想化环境设计的，而真实环境常常并不可信——因此要防的失败模式是 「过度执行」。VeriOS 没有外挂一层过滤器，而是把「何时该问人」变成一种可学习的能力： 提出查询驱动的人-agent-GUI 交互框架，让 agent 在正常条件下自主执行、在不可信场景中 主动向用户发问。VeriOS-Agent 采用三阶段训练（监督微调 + 组相对策略优化），目的是把 关于「可信性」的元知识与任务知识解耦，使两者可以独立调用。这个设定对 §2.4 很有意义： 确认机制不再是硬加在上层的固定策略，而是 agent 自己必须学会有选择地做出的决策。

`环境: Mobile, Desktop` ｜ [arXiv:2509.07553](https://arxiv.org/abs/2509.07553)

#### InquireMobile: Teaching VLM-based Mobile Agent to Request Human Assistance via Reinforcement Fine-Tuning (InquireMobile) (2025-08)

当移动 agent 的模型理解或推理能力不足时，当前这种完全自主的范式会带来潜在安全风险。作者 先提出 InquireBench —— 专门评估移动 agent 安全交互与主动向用户询问能力的基准，含 5 个 大类、22 个子类别，而现有多数基于 VLM 的 agent 在上面接近零分。随后提出 InquireMobile： 一个在关键决策点主动向用户寻求确认的交互式系统，采用两阶段训练策略与「动作前交互式推理」 机制。该模型把询问成功率提升 46.8%，并在 InquireBench 上取得基线中的最佳综合成功率。

`环境: Mobile` ｜ [arXiv:2508.19679](https://arxiv.org/abs/2508.19679)

#### VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents (VerificAgent) (2025-06)

把持久化记忆当作一个**显式的对齐面**来处理，理由是：持续的记忆增强让 CUA 能从过往交互中学习， 但未经审核的记忆会编码领域不适当或不安全的启发式规则——这些伪规则会悄然偏离用户意图与安全 约束。VerificAgent 结合三部分：专家策划的领域知识种子、训练期基于轨迹的迭代记忆增长、以及 部署前的人工事实核查环节。真正的贡献在其框定方式：让人类**一次性**纠正高影响错误，就把 经核验的记忆变成一份「冻结的安全契约」，后续所有动作都必须满足它，且无需微调模型。

`环境: Desktop` ｜ [arXiv:2506.02539](https://arxiv.org/abs/2506.02539)

#### Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents (2025-04)

LLM 驱动的 GUI agent 会在有限人工监督下处理敏感数据，由此带来的隐私与安全风险既不同于 传统 GUI 自动化，也不同于一般的自主 agent。这篇立场论文识别出三类关键风险，同时指出：现有 评测几乎只关注性能，隐私与安全评估基本处于空白。文章梳理了 GUI agent 与通用 LLM agent 的 现有评测指标，并指出把人工评估者引入 GUI agent 评测时的五个关键挑战。作者主张建立以人为 中心的评测框架 —— 把风险评估纳入其中，通过上下文内的 consent 提升用户知情度，并把隐私与 安全考量嵌入 GUI agent 的设计与评测全过程。

`环境: Web` ｜ [arXiv:2504.17934](https://arxiv.org/abs/2504.17934)
