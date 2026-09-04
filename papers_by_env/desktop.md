# Desktop 环境

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)
- **简介**：针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI 基准 StepJack，构造 480 个测试用例，把注入载荷分散在多步任务的中间环节，模拟攻击者只能污染 流程某一环的现实约束。实验显示多步注入相比单步把攻击成功率最高抬升 31.2 个百分点， 说明单步评测显著低估了 CUA 的真实暴露面，且现有防御在流程中段几乎不再触发。
- **环境**：Desktop、跨环境
- **arXiv**：[2608.06477](https://arxiv.org/abs/2608.06477)

#### Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents (Invisible Ink) (2026-08)
- **简介**：研究攻击者如何把恶意目标伪装在看似合法的任务描述中，使 CUA 在执行用户确认过的正常任务时 顺带完成攻击者目标。核心发现是这类攻击能绕过 human-in-the-loop 确认机制——因为人工审核 看到的动作序列本身每一步都合理，只有组合起来才产生危害。这揭示了「逐步确认」这一主流 防御范式的结构性盲区。
- **环境**：Desktop
- **arXiv**：[2608.02018](https://arxiv.org/abs/2608.02018)

#### CUADebug: Diagnosing and Repairing Computer-Use Agent Failures (CUADebug) (2026-07)
- **简介**：面向 CUA 执行失败后的诊断与修复，提出定位失败步骤并生成修复方案的框架。虽以可靠性为 出发点，但其失败归因与状态回滚能力可直接用于安全事件的事后恢复——在 agent 被注入劫持后 判断从哪一步开始偏离、并回退到最后一个可信状态。是「事后恢复」这一防御层中较少见的 系统性工作。
- **环境**：Desktop
- **arXiv**：[2608.02643](https://arxiv.org/abs/2608.02643)

#### Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? (Capable but Careless) (2026-06)
- **简介**：用「上下文完整性」（contextual integrity）框架考察 CUA 在跨应用操作时是否会不当传播敏感 信息。结论是能力越强的 agent 反而越容易越界：它们为完成任务会主动把 A 应用中的私密数据 带入 B 应用的输入框，而这类行为不触发任何现有的隐私告警，因为每一次读写都在授权范围内。 提出了以信息流而非权限边界为判据的评估方法。
- **环境**：Desktop
- **arXiv**：[2606.23189](https://arxiv.org/abs/2606.23189)

#### AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents (AgentHazard) (2026-04)
- **简介**：针对 CUA 具备跨工具、跨文件持久化操作能力后产生的新型安全风险，构建覆盖多风险类别与 攻击策略的基准 AgentHazard，含 2653 个实例。关键结论是有害行为往往由一串「单看都合理、 合起来不安全」的动作累积产生。实测 Claude Code 搭配 Qwen3-Coder 的攻击成功率达 73.63%， 表明仅靠底座模型的对齐无法保障 agent 层面的安全。
- **环境**：Desktop
- **arXiv**：[2604.02947](https://arxiv.org/abs/2604.02947)
