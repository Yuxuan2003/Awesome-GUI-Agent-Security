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

#### Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward (Skill Trust Framework) (2026-02)

Agent skill —— 按需加载的指令、代码与资源的可组合包 —— 让模型无需重训就能动态扩展能力。 本文从四条轴线梳理这一领域：架构基础（SKILL.md 规范、渐进式上下文加载、skill 与 MCP 的 互补角色）；skill 获取（带 skill 库的强化学习、自主发现、组合式合成）；规模化部署，含 计算机使用代理技术栈与 OSWorld 上的 GUI grounding 进展；以及安全。在安全这条轴上，实证 分析发现社区贡献的 skill 中有 26.1% 含有漏洞，据此提出 Skill Trust 与生命周期治理框架： 一个四层、以关卡为单位的权限模型，把 skill 的来源映射到分级的部署能力上。文章还列出从 跨平台可移植性到基于能力的权限模型等七个开放挑战。这些结论对 GUI agent 直接相关。

`环境: 跨环境` ｜ [arXiv:2602.12430](https://arxiv.org/abs/2602.12430)

#### VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation (VisualTrap) (2025-07)

把「视觉 grounding」——即从文本计划到具体 GUI 元素的映射——认定为一个独立的攻击面，与规划和 推理层面区分开来。其后果正是危险之处：植入 grounding 的后门会在 agent **拿到完全正确的 解题计划时**依然改变其行为，因此检查计划本身看不出任何问题。VisualTrap 通过误导 agent 把 文本计划定位到攻击者选定的位置来劫持 grounding，这意味着所有计划级审查与推理审计都能干净 通过，而动作却落在攻击者想要的地方。

`环境: Mobile, Desktop` ｜ [arXiv:2507.06899](https://arxiv.org/abs/2507.06899)

#### Poison Once, Control Anywhere: Clean-Text Visual Backdoors in VLM-based Mobile Agents (VIBMA) (2025-06)

利用移动 agent 构建方式上的结构性弱点：它们通常在小规模、用户自行收集的数据上微调，使 训练期投毒从理论威胁变成现实可行。VIBMA 是首个针对 VLM 移动 agent 的**纯净文本**后门—— 只修改视觉输入，prompt 与指令完全保持原样，因此没有任何文本异常可供检测。模型在投毒数据上 微调后，推理时加入预设的视觉触发图案即激活攻击者指定行为。其机制是把投毒样本的训练梯度与 攻击者指定目标实例的梯度对齐，从而把后门特征嵌进数据本身。

`环境: Mobile` ｜ [arXiv:2506.13205](https://arxiv.org/abs/2506.13205)

#### Hidden Ghost Hand: Unveiling Backdoor Vulnerabilities in MLLM-Powered Mobile GUI Agents (AgentGhost) (2025-05)

由于微调成本高，用户往往直接使用开源 GUI agent 或厂商提供的 API，由此引入一条尚未被充分 研究的供应链威胁 —— 后门攻击。本文首先指出，多模态大模型驱动的 GUI agent 天然暴露多个 交互级触发器：历史步骤、环境状态、任务进度。AgentGhost 把这些与目标级触发器组合成复合 触发器，使 agent 在无意中激活后门，同时不影响正常任务效用。后门注入被形式化为一个 Min-Max 优化：用监督对比学习最大化样本类间在表示空间中的特征差异以提升后门灵活性，用 监督微调最小化后门行为与干净行为生成之间的差异以增强有效性与实用性。在两个成熟的移动 基准上，三个攻击目标的攻击准确率达 99.7%，而效用仅下降 1%。作者提出的针对性防御可把 攻击准确率压到 22.1%。

`环境: Mobile` ｜ `发表: EMNLP 2025 Findings` ｜ [arXiv:2505.14418](https://arxiv.org/abs/2505.14418)
