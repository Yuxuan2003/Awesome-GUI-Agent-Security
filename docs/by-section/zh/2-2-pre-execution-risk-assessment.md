# 2.2 执行前风险评估

*Pre-execution Risk Assessment*

[← 返回索引](../../../README.zh-CN.md#22-执行前风险评估) ｜ [English](../en/2-2-pre-execution-risk-assessment.md)

*世界模型预测、动作风险打分*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction (SeerGuard) (2026-07)

指出移动 GUI agent 现有安全机制本质上都是被动响应，无法在动作触发前评估风险，而这类 agent 的单个错误动作往往不可逆。SeerGuard 是「后果感知」框架，将指令级筛查与动作级 风险评估结合：在当前 GUI 状态下分析 agent 拟执行的动作，预判可能结果再决定是否放行。 支撑能力来自一个多任务学习训练的安全增强世界模型（SAWM），把语义化的下一状态预测与 安全风险评估融进同一个模型，且该框架可跨不同底层 GUI agent 迁移。

`环境: Mobile` ｜ [arXiv:2607.15550](https://arxiv.org/abs/2607.15550)

#### Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces (DUDE) (2026-05)

指出以往工作的割裂之处：一类方法能检测欺骗但不与任务回路结合，另一类记录了攻击却不提出 防御。论文形式化了「欺骗感知的 web agent 防御」，提出两阶段框架 DUDE，把带非对称惩罚的 混合奖励学习与经验总结结合起来，将失败模式蒸馏为可迁移的指导。配套发布基准 RUC（Real UI Clickboxes），含跨四个领域与欺骗类别的 1407 个场景。DUDE 在保持任务性能的同时把易受骗 程度降低 53.8%——这一点很关键，因为多数安全干预都是以牺牲效用为代价。

`环境: Web` ｜ [arXiv:2605.09497](https://arxiv.org/abs/2605.09497)

#### When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents (DeAction) (2026-02)

把通常被分开研究的两类失效来源统一起来：源自外部攻击（如间接提示注入）的偏离动作，与源自 内部局限（如推理错误）的偏离动作——两者都背离用户意图、都损害安全性与任务可靠性，因此只针对 攻击设计的检测器会漏掉一半问题。工作定义了 CUA 的「偏离动作检测」任务，归纳出真实部署中的 三类常见情形，并基于真实轨迹构建带人工标注的动作级对齐标签基准 MisActBench。DeAction 是 通用护栏，在执行前检出偏离动作，并通过结构化反馈迭代纠正。

`环境: Desktop` ｜ [arXiv:2602.08995](https://arxiv.org/abs/2602.08995)

#### SafePred: A Predictive Guardrail for Computer-Using Agents via World Models (SafePred) (2026-02)

指出现有 CUA 护栏的共同盲区：它们都是被动式的，只在当前观测空间内约束行为，因此能拦下 「点击钓鱼链接」这类即时危害，却看不见长周期风险。文中的例子很到位——清理日志在局部看 完全合理，但会导致未来审计无从追溯，而这个后果在当前观测里根本不可见。SafePred 转而把 预测出的未来风险与当前决策对齐，建立「风险到决策」的闭环，使延迟发生、不可逆的后果能被 计入每一步的判断。

`环境: Desktop` ｜ [arXiv:2602.01725](https://arxiv.org/abs/2602.01725)

#### WebGuard: Building a Generalizable Guardrail for Web Agents (WebGuard) (2025-07)

主张 web agent 需要类似人类用户的访问控制机制，并发布首个支持 agent 动作风险评估的数据集： 来自 22 个领域、193 个网站（含常被忽视的长尾站点）的 4939 条人工标注状态改变动作，按 SAFE / LOW / HIGH 三级风险标注，并划分好训练测试集以支持泛化研究。核心结论相当刺眼—— 即便前沿 LLM 预测动作后果的准确率也不足 60%。

`环境: Web` ｜ [arXiv:2507.14293](https://arxiv.org/abs/2507.14293)
