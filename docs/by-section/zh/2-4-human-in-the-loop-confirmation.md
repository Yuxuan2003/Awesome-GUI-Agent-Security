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

#### VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents (VerificAgent) (2025-06)

把持久化记忆当作一个**显式的对齐面**来处理，理由是：持续的记忆增强让 CUA 能从过往交互中学习， 但未经审核的记忆会编码领域不适当或不安全的启发式规则——这些伪规则会悄然偏离用户意图与安全 约束。VerificAgent 结合三部分：专家策划的领域知识种子、训练期基于轨迹的迭代记忆增长、以及 部署前的人工事实核查环节。真正的贡献在其框定方式：让人类**一次性**纠正高影响错误，就把 经核验的记忆变成一份「冻结的安全契约」，后续所有动作都必须满足它，且无需微调模型。

`环境: Desktop` ｜ [arXiv:2506.02539](https://arxiv.org/abs/2506.02539)
