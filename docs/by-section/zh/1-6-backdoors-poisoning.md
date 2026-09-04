# 1.6 后门与投毒

*Backdoors & Poisoning*

[← 返回索引](../../../README.zh-CN.md#16-后门与投毒) ｜ [English](../en/1-6-backdoors-poisoning.md)

*grounding 后门、效率后门、记忆投毒*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents (AgentRAE) (2026-03)

已有针对 web GUI agent 的后门依赖环境注入或欺骗性弹窗，但在基于截图的移动 agent 上失效—— 触发器设计空间受限、操作系统后台干扰、以及多个触发器与动作映射之间相互冲突。AgentRAE 用 视觉上自然的触发器（如通知栏里的正常应用图标）诱发远程动作执行，采用两阶段流程：先用 对比学习强化 agent 对细微图标差异的敏感度，再通过后门后训练把每个触发器绑定到特定动作。

`环境: Mobile` ｜ [arXiv:2603.23007](https://arxiv.org/abs/2603.23007)

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)

提出针对 VLM-based GUI agent 的效率后门：触发器不改变任务最终结果，只让 agent 的响应 延迟大幅增加或步数显著膨胀。这类后门极难被察觉——正确性检测全部通过，只有观察资源消耗 才能发现，因此可长期潜伏并造成持续的算力成本损失。拓展了 GUI agent 后门的威胁定义， 从「结果篡改」扩展到「可用性与经济性攻击」。

`环境: Mobile, 跨环境` ｜ [arXiv:2603.08316](https://arxiv.org/abs/2603.08316)
