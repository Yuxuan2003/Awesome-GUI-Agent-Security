# 跨环境 环境

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)
- **简介**：针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI 基准 StepJack，构造 480 个测试用例，把注入载荷分散在多步任务的中间环节，模拟攻击者只能污染 流程某一环的现实约束。实验显示多步注入相比单步把攻击成功率最高抬升 31.2 个百分点， 说明单步评测显著低估了 CUA 的真实暴露面，且现有防御在流程中段几乎不再触发。
- **环境**：Desktop、跨环境
- **arXiv**：[2608.06477](https://arxiv.org/abs/2608.06477)

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)
- **简介**：提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。
- **环境**：Mobile、跨环境
- **arXiv**：[2607.29199](https://arxiv.org/abs/2607.29199)

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)
- **简介**：提出针对 VLM-based GUI agent 的效率后门：触发器不改变任务最终结果，只让 agent 的响应 延迟大幅增加或步数显著膨胀。这类后门极难被察觉——正确性检测全部通过，只有观察资源消耗 才能发现，因此可长期潜伏并造成持续的算力成本损失。拓展了 GUI agent 后门的威胁定义， 从「结果篡改」扩展到「可用性与经济性攻击」。
- **环境**：Mobile、跨环境
- **arXiv**：[2603.08316](https://arxiv.org/abs/2603.08316)
