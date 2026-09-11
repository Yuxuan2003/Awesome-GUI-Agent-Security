# 3.1 综合与跨环境基准

*Comprehensive & Cross-environment*

[← 返回索引](../../../README.zh-CN.md#31-综合与跨环境基准) ｜ [English](../en/3-1-comprehensive-cross-environment.md)

*同时覆盖多个环境或威胁类别的基准*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agents Across Devices (ADeptS-Bench) (2026-08)

针对「没有基准能同时考察 CUA 在视觉界面下的安全性与对模糊指令的处理」这一空缺，提出双流 可信度基准 ADeptS-Bench：Safety 流提供威胁嵌在视觉界面中的良性/恶意配对任务，Disambiguation 流考察 agent 在意图模糊时是否会主动澄清。评测 7 个模型的结论相当刺眼——没有模型能在任务 成功率超 80% 的同时把攻击成功率压到 30% 以下；所有模型都会毫不犹豫点下 2.5 万美元订单的 「结账」，也没有一个能识别出被标为「优化」的按钮实际是「恢复出厂设置」。

`环境: Desktop, Mobile` ｜ [arXiv:2608.26204](https://arxiv.org/abs/2608.26204)

#### OSGuard: A Benchmark for Safety in Computer-Use Agents (OSGuard) (2026-06)

针对一个测量盲区：computer-use agent 通常只以任务完成率评判，但「成功」会掩盖 agent 通过 不安全捷径达成名义目标的情况。OSGuard 在**良性、未被篡改**的用户指令下评估安全性——回路中 没有攻击者——并设计了两个粒度。动作级基准把语境化的候选动作标注为「允许 / 无关 / 不安全」， 每条都相对原始指令与当前界面状态判定。执行套件基于人工构造的 OSWorld 变体，原任务仍可完成， 但环境中埋入了破坏性覆写等潜在危害，并配套保留原成功信号的增强评测器。

`环境: Desktop, Web` ｜ [arXiv:2606.15034](https://arxiv.org/abs/2606.15034)

#### AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents (AgentHazard) (2026-04)

针对 CUA 具备跨工具、跨文件持久化操作能力后产生的新型安全风险，构建覆盖多风险类别与 攻击策略的基准 AgentHazard，含 2653 个实例。关键结论是有害行为往往由一串「单看都合理、 合起来不安全」的动作累积产生。实测 Claude Code 搭配 Qwen3-Coder 的攻击成功率达 73.63%， 表明仅靠底座模型的对齐无法保障 agent 层面的安全。

`环境: Desktop` ｜ [arXiv:2604.02947](https://arxiv.org/abs/2604.02947)

#### GUIGuard-Bench: Toward a General Evaluation for Privacy-Preserving GUI Agents (GUIGuard-Bench) (2026-01)

指出现有视觉隐私数据集多为静态自然图像，因而无法刻画 GUI 工作流中界定隐私风险的两个性质： 上下文依赖与任务相关性。GUIGuard-Bench 提供 241 条真实 GUI agent 轨迹、涵盖 Android 与 PC 环境的 4080 张截图。真正的贡献在标注设计——每张截图在区域级标注隐私边界框、语义类别、 风险等级，以及关键的一项：该隐私信息是否为完成任务所必需。而这恰恰是遮蔽类防御必须判断 正确的那个区分。

`环境: Mobile, Desktop` ｜ [arXiv:2601.18842](https://arxiv.org/abs/2601.18842)

#### SusBench: An Online Benchmark for Evaluating Dark Pattern Susceptibility of Computer-Use Agents (SusBench) (2025-10)

评测 CUA 对 UI 暗黑模式（诱导用户做出非本意操作的界面设计）的易感程度：从既有分类法中选取 九种常见类型，通过代码注入在真实消费类网站上构造可信实例，形成覆盖 55 个网站的 313 个评测 任务。方法上的强项在于人类验证环节——29 名参与者的实验确认这些注入看起来高度真实，绝大多数 人完全没有察觉它们是研究团队植入的。正是这一对照使得「五个前沿 CUA 与人类参与者并排比较」 的结论具备可信度。

`环境: Web, Desktop` ｜ [arXiv:2510.11035](https://arxiv.org/abs/2510.11035)

#### RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents (RiOSWorld) (2025-05)

正面提出「迁移性」问题：为对话场景下的通用 MLLM 设计并对齐的安全风险原则，能否有效迁移到 真实的计算机操作场景？论文指出以往的风险评测总在两点之一上失守——要么缺乏真实的交互环境， 要么把范围收窄到少数几类特定风险——而这两种失守都忽略了真实环境所固有的复杂性与多变性。 RiOSWorld 在真实的计算机操作过程中评测风险，已成为多模态 CUA 风险评测中被较多引用的基准之一。

`环境: Desktop` ｜ [arXiv:2506.00618](https://arxiv.org/abs/2506.00618)
