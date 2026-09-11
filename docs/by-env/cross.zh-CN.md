# 跨环境

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)

针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI 基准 StepJack，构造 480 个测试用例，把注入载荷分散在多步任务的中间环节，模拟攻击者只能污染 流程某一环的现实约束。实验显示多步注入相比单步把攻击成功率最高抬升 31.2 个百分点， 说明单步评测显著低估了 CUA 的真实暴露面，且现有防御在流程中段几乎不再触发。

`环境: Desktop, 跨环境` ｜ [arXiv:2608.06477](https://arxiv.org/abs/2608.06477)

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)

提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。

`环境: Mobile, 跨环境` ｜ [arXiv:2607.29199](https://arxiv.org/abs/2607.29199)

#### SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems (SafeFlow) (2026-07)

指出正是那些让多 agent 系统变强的机制造就了盲点：任务分解与角色专职化使一个有害目标可以被 拆解成局部看来都合理的子任务，于是没有任何单个 agent 能看到足够信息来识别恶意意图。论文的 关键一步是把这个问题重新框定为**语义信息流**问题、而非单轮 prompt 分类任务——这个范畴转换 解释了为何逐条消息的过滤器注定无效。SafeFlow 为根请求附加结构化的语义污点标记，沿动态协作 图传播，并在工作流层面做整体校验。

`环境: 跨环境` ｜ [arXiv:2607.25255](https://arxiv.org/abs/2607.25255)

#### Securing Computer-Use Agents: A Unified Architecture-Lifecycle Framework for Deployment-Grounded Reliability (Architecture-Lifecycle Framework) (2026-05)

论证当 CUA 走出受限基准、进入真实的浏览器、桌面、移动应用、文件系统、终端与工具后端之后， 任务成功率就不再是有意义的可靠性度量：感知错误、规划漂移、记忆使用、工具中介、权限范围与 运行时监督**共同**决定动作是否仍与用户意图对齐。现有综述按方法、平台、基准或威胁来组织 这个领域，但很少把「能力形成 → 权限暴露 → 失效显现 → 控制点放置」这条链条串起来。本框架 通过架构视角（把感知、决策、执行视为相互耦合的层）与生命周期视角提供了这一串联。

`环境: 跨环境` ｜ [arXiv:2605.07110](https://arxiv.org/abs/2605.07110)

#### Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection (Semantic UI Injection) (2026-04)

指出现有 GUI agent 红队研究的两个局限：对抗扰动需要商业部署中拿不到的白盒访问，而提示 注入正被日益增强的安全对齐所化解。提出黑盒范式「语义级 UI 元素注入」——把本身安全对齐、 内容无害的 UI 元素叠加到截图上以误导视觉 grounding，用模块化的 Editor-Overlapper-Victim 流水线配合迭代搜索。在 8 个模型家族共 19 个受害模型上，策略化优化相比随机注入在最鲁棒的 模型上高出 3.5–6.9 倍，且跨架构迁移性近乎完美。

`环境: 跨环境` ｜ [arXiv:2604.07831](https://arxiv.org/abs/2604.07831)

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)

提出针对 VLM-based GUI agent 的效率后门：触发器不改变任务最终结果，只让 agent 的响应 延迟大幅增加或步数显著膨胀。这类后门极难被察觉——正确性检测全部通过，只有观察资源消耗 才能发现，因此可长期潜伏并造成持续的算力成本损失。拓展了 GUI agent 后门的威胁定义， 从「结果篡改」扩展到「可用性与经济性攻击」。

`环境: Mobile, 跨环境` ｜ [arXiv:2603.08316](https://arxiv.org/abs/2603.08316)

#### Towards Trustworthy GUI Agents: A Survey (Trustworthy GUI Survey) (2025-03)

把「执行落差」（execution gap）确立为可信 GUI agent 的核心障碍——即在动态、部分可观测界面下 感知、推理与交互三者之间的错配。与对话系统不同，GUI agent 执行的是提交表单、授予权限、删除 数据这类不可逆操作。综述提出与工作流对齐的分类法，把信任拆为感知信任、推理信任、交互信任 三层，梳理失败如何在动作/观察循环中传播并累积，并主张仅用任务完成率评估可信度是不充分的。

`环境: 跨环境` ｜ [arXiv:2503.23434](https://arxiv.org/abs/2503.23434)
