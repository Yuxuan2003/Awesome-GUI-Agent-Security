# 1.1 间接提示注入

*Indirect Prompt Injection*

[← 返回索引](../../../README.zh-CN.md#11-间接提示注入) ｜ [English](../en/1-1-indirect-prompt-injection.md)

*经网页、文档、邮件等外部内容承载的注入*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### SIR: Self-improving Red-teaming for Compute Use Agents (SIR) (2026-08)

指出现有 CUA 安全基准用的都是人工手写的固定注入载荷，会低估自适应攻击者的真实威胁。提出 黑盒 IPI 攻击 SIR：从一个用自然语言描述的可复用「隐蔽性原则」小库中组合注入内容，再套一层 迭代反馈循环——诊断受害 agent 失败的攻击轨迹，把成功绕过的模式蒸馏回原则库。这把红队从 静态测试变成自我改进的过程，说明固定载荷的评测结论会随攻击者迭代迅速失效。

`环境: Desktop, Web` ｜ [arXiv:2608.30207](https://arxiv.org/abs/2608.30207)

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)

针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI 基准 StepJack，构造 480 个测试用例，把注入载荷分散在多步任务的中间环节，模拟攻击者只能污染 流程某一环的现实约束。实验显示多步注入相比单步把攻击成功率最高抬升 31.2 个百分点， 说明单步评测显著低估了 CUA 的真实暴露面，且现有防御在流程中段几乎不再触发。

`环境: Desktop, 跨环境` ｜ [arXiv:2608.06477](https://arxiv.org/abs/2608.06477)

#### Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents (Invisible Ink) (2026-08)

研究攻击者如何把恶意目标伪装在看似合法的任务描述中，使 CUA 在执行用户确认过的正常任务时 顺带完成攻击者目标。核心发现是这类攻击能绕过 human-in-the-loop 确认机制——因为人工审核 看到的动作序列本身每一步都合理，只有组合起来才产生危害。这揭示了「逐步确认」这一主流 防御范式的结构性盲区。

`环境: Desktop` ｜ [arXiv:2608.02018](https://arxiv.org/abs/2608.02018)
