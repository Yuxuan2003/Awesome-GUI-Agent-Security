# 1.6 后门与投毒

*Backdoors & Poisoning*

[← 返回索引](../../../README.zh-CN.md#16-后门与投毒) ｜ [English](../en/1-6-backdoors-poisoning.md)

*grounding 后门、效率后门、记忆投毒*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### SynChain: Inducing Computer-Use Agent Systems to Construct Their Own Attack Chains (SynChain) (2026-08)

指出把攻击视为「外部触发、时间有界」的现有防御留下的缺口：CUA 如今会自行生成、存储并复用 skill 与记忆条目这类产物，因此沦陷可以通过 agent 自身的持久化状态在**内部**传播。论文表明 恶意影响能被隐蔽地嵌入自主合成产物的结构冗余中，从而在内部状态更新后存活、并绕过常规审查 机制。SynChain 用「持久化感知的定向监督微调」将这一威胁形式化，诱导 agent 产出被投毒却 外观无害的产物，并在 CUAChain（30 条良性任务链 + 三类攻击目标）上评测其潜伏激活效果。

`环境: Desktop` ｜ [arXiv:2608.06862](https://arxiv.org/abs/2608.06862)

#### MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents (MemVenom) (2026-06)

针对外部记忆——它已是现代 web agent 支撑长周期推理的核心组件——并指出其结构性后果：注入 记忆的内容会被持续召回、反复影响行为，因此一次成功投毒的影响能跨越会话存活。MemVenom 是 黑盒框架，用协同的图文证据污染图结构外部记忆，分两阶段：先以触发条件化的检索攻击确保恶意 记忆被高概率召回，再通过对抗扰动与隐蔽 OCR 注入在检索后诱导 agent 覆盖用户原目标。与 prompt 层或纯文本记忆攻击不同，其效果是持久且可复用的。

`环境: Web` ｜ [arXiv:2606.10742](https://arxiv.org/abs/2606.10742)

#### AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents (AgentRAE) (2026-03)

已有针对 web GUI agent 的后门依赖环境注入或欺骗性弹窗，但在基于截图的移动 agent 上失效—— 触发器设计空间受限、操作系统后台干扰、以及多个触发器与动作映射之间相互冲突。AgentRAE 用 视觉上自然的触发器（如通知栏里的正常应用图标）诱发远程动作执行，采用两阶段流程：先用 对比学习强化 agent 对细微图标差异的敏感度，再通过后门后训练把每个触发器绑定到特定动作。

`环境: Mobile` ｜ [arXiv:2603.23007](https://arxiv.org/abs/2603.23007)

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)

提出针对 VLM-based GUI agent 的效率后门：触发器不改变任务最终结果，只让 agent 的响应 延迟大幅增加或步数显著膨胀。这类后门极难被察觉——正确性检测全部通过，只有观察资源消耗 才能发现，因此可长期潜伏并造成持续的算力成本损失。拓展了 GUI agent 后门的威胁定义， 从「结果篡改」扩展到「可用性与经济性攻击」。

`环境: Mobile, 跨环境` ｜ [arXiv:2603.08316](https://arxiv.org/abs/2603.08316)

#### Poison Once, Control Anywhere: Clean-Text Visual Backdoors in VLM-based Mobile Agents (VIBMA) (2025-06)

利用移动 agent 构建方式上的结构性弱点：它们通常在小规模、用户自行收集的数据上微调，使 训练期投毒从理论威胁变成现实可行。VIBMA 是首个针对 VLM 移动 agent 的**纯净文本**后门—— 只修改视觉输入，prompt 与指令完全保持原样，因此没有任何文本异常可供检测。模型在投毒数据上 微调后，推理时加入预设的视觉触发图案即激活攻击者指定行为。其机制是把投毒样本的训练梯度与 攻击者指定目标实例的梯度对齐，从而把后门特征嵌进数据本身。

`环境: Mobile` ｜ [arXiv:2506.13205](https://arxiv.org/abs/2506.13205)
