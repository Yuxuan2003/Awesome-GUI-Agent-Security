# 2.4 人在环与确认机制

*Human-in-the-Loop & Confirmation*

[← 返回索引](../../../README.zh-CN.md#24-人在环与确认机制) ｜ [English](../en/2-4-human-in-the-loop-confirmation.md)

*关键动作前的人工确认、审批门、可打断性*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Mobile GUI Agent Privacy Personalization with Trajectory Induced Preference Optimization (TIPO) (2026-04)

把隐私重新框定为**个性化**问题而非一套固定策略：多数系统只优化任务成功率或效率，忽略了不同 用户想要的隐私姿态本就不同。技术上的关键观察是个性化会引起轨迹的系统性结构异质——隐私优先的 用户偏好拒绝权限、登出、最小化暴露这类保护性动作，产生与效用优先用户在逻辑上不同、长度也 不等的轨迹，从而使标准偏好优化变得不稳定且信息量下降。TIPO 用偏好强度加权突出关键隐私步骤， 并以 padding gating 抑制对齐噪声。

`环境: Mobile` ｜ [arXiv:2604.11259](https://arxiv.org/abs/2604.11259)

#### VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents (VerificAgent) (2025-06)

把持久化记忆当作一个**显式的对齐面**来处理，理由是：持续的记忆增强让 CUA 能从过往交互中学习， 但未经审核的记忆会编码领域不适当或不安全的启发式规则——这些伪规则会悄然偏离用户意图与安全 约束。VerificAgent 结合三部分：专家策划的领域知识种子、训练期基于轨迹的迭代记忆增长、以及 部署前的人工事实核查环节。真正的贡献在其框定方式：让人类**一次性**纠正高影响错误，就把 经核验的记忆变成一份「冻结的安全契约」，后续所有动作都必须满足它，且无需微调模型。

`环境: Desktop` ｜ [arXiv:2506.02539](https://arxiv.org/abs/2506.02539)
