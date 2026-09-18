# Mobile

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### When Agents See Differently: Exposing UI Desynchronization Threats in Mobile Agents (UI Desynchronization) (2026-09)

人类监督 mobile agent 依赖一个未被言明的前提：用户与 agent 从同一界面看到一致的信息。 本文证明这个前提可被系统性打破。用户经由物理屏幕与人类视觉系统感知界面，受遮挡与亮度 对比度限制；而 agent 消费的是数字截图，还额外拿到暴露非视觉控件元数据的无障碍表示。 同一个 UI 状态因此向双方呈现实质不同的信息，作者称之为「人机 UI 失同步」。实验表明， 重打包的合法 APK 克隆可以利用这一失同步把 agent 引向攻击者指定的动作，同时对人类用户 保持功能与行为完全一致；扰动在部署前嵌入，无需获取运行时指令、无需检测 agent、无需在线 适配。在五个 mobile agent 框架、三个主干模型、546 个任务上，静态与动态误导率分别为 77.9% 与 66.9%。186 人的问卷研究进一步确认这些视觉扰动人眼难以察觉。

`环境: Mobile` ｜ [arXiv:2609.16732](https://arxiv.org/abs/2609.16732)

#### PriMobiBench: Characterizing Visual Privacy Leakage in VLM-Driven Mobile GUI Agents (PriMobiBench) (2026-09)

移动 GUI agent 通过解读截图流自动化手机任务，这一设计带来严重但研究不足的隐私风险： 既包括屏上敏感信息的直接泄露，也包括非预期的用户画像推断，而两者都缺少标准化基准来量化。 PriMobiBench 是首个系统评测截图驱动移动 agent 的视觉隐私泄露与画像风险的基准，提供 数据生成、轨迹构建与多模型评测的统一流水线，并附数据集 MobiLeak——来自 16 个应用的 执行轨迹，覆盖 25 类隐私属性、2960 个嵌入的隐私实例。结果相当刺眼：VLM 直接提取敏感 信息成功率最高 82.5%；即便没有显式泄露，也能从聚合的视觉证据中以约 70% 的成功率推断出 用户画像。作者提出的缓解方案在上云前遮蔽「隐私敏感但与任务无关」的 UI 元素，可将画像 成功率最多降低 58%，代价仅约 8% 的性能损失。

`环境: Mobile` ｜ [arXiv:2609.13873](https://arxiv.org/abs/2609.13873)

#### ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agents Across Devices (ADeptS-Bench) (2026-08)

针对「没有基准能同时考察 CUA 在视觉界面下的安全性与对模糊指令的处理」这一空缺，提出双流 可信度基准 ADeptS-Bench：Safety 流提供威胁嵌在视觉界面中的良性/恶意配对任务，Disambiguation 流考察 agent 在意图模糊时是否会主动澄清。评测 7 个模型的结论相当刺眼——没有模型能在任务 成功率超 80% 的同时把攻击成功率压到 30% 以下；所有模型都会毫不犹豫点下 2.5 万美元订单的 「结账」，也没有一个能识别出被标为「优化」的按钮实际是「恢复出厂设置」。

`环境: Desktop, Mobile` ｜ [arXiv:2608.26204](https://arxiv.org/abs/2608.26204)

#### Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments (AnTrap) (2026-08)

指出现有基准缺乏对 GUI agent 运行时异常鲁棒性的系统评估，而 Android 实机部署中意外弹窗、 动作误用等动态扰动十分常见。提出基准 AnTrap，把真实异常归纳为 State / Thinking / Action / Round 四层共十个细分类别，并设计了在注入对抗扰动的同时保持任务仍可完成的构造流程。评测 16 个主流 GUI 模型显示对动态异常存在普遍脆弱性，最强模型也出现显著性能下降；作者还在 原始与对抗环境下各做一轮 GRPO 训练，以区分环境难度与模型能力两个混杂因素。

`环境: Mobile` ｜ [arXiv:2608.24099](https://arxiv.org/abs/2608.24099)

#### MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps (MobileWorldSafety) (2026-08)

指出现有基准脱离日常使用场景，缺乏对移动 GUI agent 在环境注入下的系统评估——而这类 agent 已从研究原型走向真实部署，且日常操作中会不断处理不可信的环境内容。提出基于真实 Android 应用构建的基准 MobileWorldSafety，含 142 个风险任务，覆盖间接提示注入与对抗 指令等多种日常渠道，每个任务都定义了可程序化验证的判定条件，使攻击是否成功可被客观测量。

`环境: Mobile` ｜ [arXiv:2608.17659](https://arxiv.org/abs/2608.17659)

#### Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection (Not an A11y) (2026-08)

指出 Android 无障碍树（accessibility tree）是移动 agent 的一条被忽视的注入通道：任何 应用都能往无障碍节点写入文本，而 agent 会把这些内容当作可信的界面语义读取。攻击者无需 任何特殊权限即可通过普通应用注入指令。这条路径完全绕开了针对视觉截图或网页内容的 防御，暴露出移动 agent 输入通道治理的缺失。

`环境: Mobile` ｜ [arXiv:2608.08939](https://arxiv.org/abs/2608.08939)

#### "Allow" to Achieve, Over-Privileged Inadvertently: The Unintended Cost of Task-Completion-Driven Pop-up Decisions in Mobile GUI Agents (Allow to Achieve) (2026-08)

发现移动 GUI agent 在遇到权限弹窗时存在系统性的过度授权倾向，识别出两种偏差：App-Trust Bias（对已安装应用默认信任而一律点允许）与 Task-Prior Override（为达成任务目标而牺牲 权限最小化）。结果是 agent 在用户不知情的情况下累积远超任务所需的权限，把权限弹窗这一 最后防线变成了形式。

`环境: Mobile` ｜ [arXiv:2608.04755](https://arxiv.org/abs/2608.04755)

#### FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory (FocusMem) (2026-08)

潜在记忆把多模态 GUI 轨迹压缩成少量连续 token，但现有方法把每条轨迹映射到一个固定 记忆块，且主要靠下一动作监督来训练。由此带来三个实际问题：压缩过程中细节丢失、同一个 记忆块要服务所有决策阶段、检索到不相关的轨迹仍会误导 agent。FocusMem 把这些职责拆开： 角色感知的内容基底促使情景记忆保留可复用经验、工作记忆保留当前任务进展；状态条件化的 读出机制为同一份存储证据生成面向具体决策的视图；轻量的信任门可在检索不可靠时抑制记忆。 最后这一项正是它进入安全清单的理由——它把检索到的记忆当作需要设门的不可信输入， 而这正是对抗记忆投毒式操纵的结构性防御。

`环境: Mobile, Desktop, Web` ｜ [arXiv:2608.04530](https://arxiv.org/abs/2608.04530)

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)

提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。

`环境: Mobile, 跨环境` ｜ [arXiv:2607.29199](https://arxiv.org/abs/2607.29199)

#### SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction (SeerGuard) (2026-07)

指出移动 GUI agent 现有安全机制本质上都是被动响应，无法在动作触发前评估风险，而这类 agent 的单个错误动作往往不可逆。SeerGuard 是「后果感知」框架，将指令级筛查与动作级 风险评估结合：在当前 GUI 状态下分析 agent 拟执行的动作，预判可能结果再决定是否放行。 支撑能力来自一个多任务学习训练的安全增强世界模型（SAWM），把语义化的下一状态预测与 安全风险评估融进同一个模型，且该框架可跨不同底层 GUI agent 迁移。

`环境: Mobile` ｜ [arXiv:2607.15550](https://arxiv.org/abs/2607.15550)

#### Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure (Perception-Fusion Gap) (2026-07)

提出一个位于所有视觉攻击上游的问题：多模态 GUI agent 通过两条冗余通道读取界面——渲染后的 像素与序列化结构（DOM 或无障碍树）——并在行动前形成对当前状态的信念，但现有基准从不追问 **这个信念究竟来自哪条通道**。论文形式化了「视觉状态依赖」，用配对的单通道干预在覆盖真实 web / mobile / desktop 界面的 735 个探针上测量，其中 225 个是从线上生产网站挖掘的零编辑 分歧样本，全部采用确定性强制选择评分、不引入模型裁判。核心指标 Perception-Fusion Gap 刻画的是「模型感知正确、但在冲突时倒向结构」的探针占比——而这恰好告诉攻击者该污染哪条通道。

`环境: Web, Mobile, Desktop` ｜ [arXiv:2607.04334](https://arxiv.org/abs/2607.04334)

#### (A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents (AI Sees) (2026-07)

系统分析第三方移动 agent 引入的新攻击面，核心是「感知鸿沟」——agent 能读取到屏幕上用户 实际看不到或不会注意的内容（隐藏视图、后台通知、无障碍节点），攻击者可利用这一差异实施 用户完全无法察觉的诱导。指出第三方 agent 生态缺乏对 agent 可见性范围的约束机制。

`环境: Mobile` ｜ [arXiv:2607.00333](https://arxiv.org/abs/2607.00333)

#### AOHP: An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction (AOHP) (2026-06)

面向终端用户的操作系统是为「以应用为中心」的工作流设计的，对 AI agent 几乎没有原生支持； 因此在传统系统上跑 agent 会带来执行开销与安全风险。agent 原生操作系统的概念正在出现， 但社区缺少一个开放测试平台，来探索 agent 中介的交互究竟需要哪些架构原语。AOHP （Android Open Harness Project）是基于 AOSP 构建的 OS 级 agent harness，核心设计原则是 把 agent 当作一等的 OS 参与者，从而支持自适应用户界面与 agent 友好的运行时环境。收录 于此是因为它把安全问题从行为层面推到了结构层面：它提供了一个基底，可以在其上原型化并 对比面向 GUI agent 的 OS 级隔离与权限原语，而不是给「屏幕抓取」范式事后加装护栏。

`环境: Mobile` ｜ [arXiv:2606.23449](https://arxiv.org/abs/2606.23449)

#### CAPED: Context-Aware Privacy Exposure Defense for Mobile GUI Agents (CAPED) (2026-06)

指出一个截图范式特有的问题：由于 agent 以与人完全相同的方式「看」手机，每一次屏幕观测都 变成一道隐私边界，正常执行任务时就可能暴露联系人、消息、照片、健康线索等与请求毫无关系的 上下文。作者称之为「附带性视觉隐私暴露」，并说明两个极端为何都行不通——文本匿名化会漏掉 视觉与可推断线索，而通用遮蔽又会把 agent 完成任务所需的证据和控件一起抹掉。CAPED 是运行 在手机侧的上传前控制层，解析可见 UI 元素并选择性遮蔽，以任务需求和屏幕上下文作为隐私先验。

`环境: Mobile` ｜ [arXiv:2606.12666](https://arxiv.org/abs/2606.12666)

#### MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution (MaskClaw) (2026-05)

把 GUI agent 隐私问题定义为**裁决**问题而非检测问题：某项内容是否属于隐私取决于任务、接收方、 应用状态与用户角色，因此静态 PII 检测器抓不住这些边界，而云端 VLM 推理又会在决定「什么需要 保护」**之前**就把原始屏幕上传出去。MaskClaw 运行在边缘侧：抽取本地视觉证据、检索用户与任务 专属的策略记忆，在截图离开可信环境前判定 Allow / Mask / Ask。在五个 skill 演进场景中，它把 用户的纠正、取消与编辑转化为可复用的隐私 skill，并经沙箱门校验，评测基准为 P-GUI-Evo。

`环境: Mobile, Desktop` ｜ [arXiv:2605.28646](https://arxiv.org/abs/2605.28646)

#### MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content (MIRAGE (Mobile)) (2026-05)

把漏洞根源归到感知范式本身：移动 GUI agent 把屏幕当作渲染后的像素来看，并据所见选择动作， 因此无法可靠区分可信的界面框架与用户生成内容。MIRAGE 把正常截图转化为注入样本——将攻击者 文本放进普通 UGC 区域，**无需修改 agent、应用或操作系统**。三阶段流水线：Localizer 定位 用户可控区域，Generator 合成上下文感知载荷并以应用原生样式渲染，Curator 把控真实性并在 应用、区域类型与攻击意图之间平衡样本分布。

`环境: Mobile` ｜ [arXiv:2605.28116](https://arxiv.org/abs/2605.28116)

#### Mobile GUI Agent Privacy Personalization with Trajectory Induced Preference Optimization (TIPO) (2026-04)

把隐私重新框定为**个性化**问题而非一套固定策略：多数系统只优化任务成功率或效率，忽略了不同 用户想要的隐私姿态本就不同。技术上的关键观察是个性化会引起轨迹的系统性结构异质——隐私优先的 用户偏好拒绝权限、登出、最小化暴露这类保护性动作，产生与效用优先用户在逻辑上不同、长度也 不等的轨迹，从而使标准偏好优化变得不稳定且信息量下降。TIPO 用偏好强度加权突出关键隐私步骤， 并以 padding gating 抑制对齐噪声。

`环境: Mobile` ｜ [arXiv:2604.11259](https://arxiv.org/abs/2604.11259)

#### CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation (CORA) (2026-04)

现有 GUI agent 防护依赖 prompt 工程、脆弱的启发式规则与 VLM-as-critic，既无形式化验证也 不提供用户可调的保证。CORA 是一个「策略之后、动作之前」的防护框架，对已执行的有害动作 给出统计保证：把安全性重构为选择性动作执行，训练 Guardian 模型估计动作条件风险，再用 Conformal Risk Control 校准满足用户指定风险预算的执行/弃权边界，被拒动作交由 Diagnostician 做多模态推理并建议确认、反思或中止。另设 Goal-Lock 机制抵御视觉注入。

`环境: Mobile` ｜ [arXiv:2604.09155](https://arxiv.org/abs/2604.09155)

#### Do Phone-Use Agents Respect Your Privacy? (MyPhoneBench) (2026-04)

追问手机操作类 agent 在完成正常任务时是否尊重隐私。这一问题此前难以回答，因为隐私合规 行为从未被形式化定义，且普通应用不会暴露 agent 究竟把哪些数据填进了哪个表单项。 MyPhoneBench 用一份最小隐私契约把「尊重隐私」操作化为三条：授权访问、最小披露、用户可控 记忆，并配以插桩的模拟应用与规则化审计。在 5 个前沿模型、10 个应用、300 个任务上发现， 任务成功率、隐私合规完成度、后续会话中对已存偏好的使用是三种彼此独立的能力，无一模型全占优。

`环境: Mobile` ｜ [arXiv:2604.00986](https://arxiv.org/abs/2604.00986)

#### AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents (AgentRAE) (2026-03)

已有针对 web GUI agent 的后门依赖环境注入或欺骗性弹窗，但在基于截图的移动 agent 上失效—— 触发器设计空间受限、操作系统后台干扰、以及多个触发器与动作映射之间相互冲突。AgentRAE 用 视觉上自然的触发器（如通知栏里的正常应用图标）诱发远程动作执行，采用两阶段流程：先用 对比学习强化 agent 对细微图标差异的敏感度，再通过后门后训练把每个触发器绑定到特定动作。

`环境: Mobile` ｜ [arXiv:2603.23007](https://arxiv.org/abs/2603.23007)

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)

提出针对 VLM-based GUI agent 的效率后门：触发器不改变任务最终结果，只让 agent 的响应 延迟大幅增加或步数显著膨胀。这类后门极难被察觉——正确性检测全部通过，只有观察资源消耗 才能发现，因此可长期潜伏并造成持续的算力成本损失。拓展了 GUI agent 后门的威胁定义， 从「结果篡改」扩展到「可用性与经济性攻击」。

`环境: Mobile, 跨环境` ｜ [arXiv:2603.08316](https://arxiv.org/abs/2603.08316)

#### Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System (Aura) (2026-02)

本文主张当前主流的「屏幕即接口」范式本身就是病根而非细节：让 agent 依赖非结构化的视觉 数据，既继承了屏幕固有的结构性脆弱性，也与移动生态的经济基础相冲突。作者以一款已上线的 商用助手为案例做系统性安全分析，把威胁面拆为 Agent 身份、外部接口、内部推理、动作执行 四个维度，暴露出伪造应用身份、视觉欺骗、间接提示注入、越权提权等缺陷，并且都可追溯到 同一个根源——对非结构化像素的依赖。给出的答案是推倒重来：提出 Aura（Agent 通用运行时 架构），用以意图为中心的接口取代脆弱的 GUI 抓取，使安全性来自架构本身，而不是靠给感知层 打补丁。

`环境: Mobile` ｜ [arXiv:2602.10915](https://arxiv.org/abs/2602.10915)

#### Anonymization-Enhanced Privacy Protection for Mobile GUI Agents: Available but Invisible (Available but Invisible) (2026-02)

诊断出移动 GUI agent 现有隐私防御为何都不够用：减少 UI 暴露、只混淆与任务无关内容、或依赖 用户授权，这三条路都绕开了最难的情况——如何保护**本身就是任务必需**的敏感信息。论文提出的 原则是「可用但不可见」：敏感数据对执行仍然可用，但云端 agent 永远看不到其真实内容。实现上 结合 PII 感知的 UI 内容识别模型与匿名化，使 agent 在占位符上操作，真实值始终不越出可信边界。

`环境: Mobile` ｜ [arXiv:2602.10139](https://arxiv.org/abs/2602.10139)

#### GUIGuard-Bench: Toward a General Evaluation for Privacy-Preserving GUI Agents (GUIGuard-Bench) (2026-01)

指出现有视觉隐私数据集多为静态自然图像，因而无法刻画 GUI 工作流中界定隐私风险的两个性质： 上下文依赖与任务相关性。GUIGuard-Bench 提供 241 条真实 GUI agent 轨迹、涵盖 Android 与 PC 环境的 4080 张截图。真正的贡献在标注设计——每张截图在区域级标注隐私边界框、语义类别、 风险等级，以及关键的一项：该隐私信息是否为完成任务所必需。而这恰恰是遮蔽类防御必须判断 正确的那个区分。

`环境: Mobile, Desktop` ｜ [arXiv:2601.18842](https://arxiv.org/abs/2601.18842)

#### Mind the Gap: Action Rebinding Attacks against Android GUI Agents (Action Rebinding) (2026-01)

指出把 GUI agent 当作高权限操作者（跨应用边界感知屏幕、注入输入）与 Android 严格的应用 沙箱机制存在根本冲突。跨应用 Action Rebinding 攻击让一个不申请任何危险权限的恶意应用即可 劫持 agent 执行：先渲染一个无害的「上下文载体」诱导 agent 规划出某个动作，再在其推理延迟 窗口内把前台切换到敏感目标应用，agent 察觉不到切换、于是在特权上下文中执行了该动作。 作者进一步利用 agent 自身的任务恢复逻辑，把攻击武器化为可编程的多步利用循环。

`环境: Mobile` ｜ [arXiv:2601.12349](https://arxiv.org/abs/2601.12349)

#### DualTAP: A Dual-Task Adversarial Protector for Mobile MLLM Agents (DualTAP) (2025-11)

把隐私泄露定位到一个具体的架构环节：含 PII 的截图会被例行发送给不受信的第三方路由服务， 而这些服务可以用自己的 MLLM 挖掘其中数据。该场景提出了此前扰动类方法无法同时满足的矛盾 要求——既要让路由方的模型看不到 PII，又要保留足够信息让 agent 的模型完成任务。DualTAP 显式解耦这两个目标：用对比注意力模块精确定位仅 PII 敏感区域，并以双任务对抗目标在任务 保持损失与隐私干扰之间取得平衡。

`环境: Mobile` ｜ [arXiv:2511.13248](https://arxiv.org/abs/2511.13248)

#### Measuring the Security of Mobile LLM Agents under Adversarial Prompts from Untrusted Third-Party Channels (Mobile Agent Security Study) (2025-10)

首个针对移动 LLM agent 安全风险的系统性研究，对抗案例从弹窗广告这类机会主义操纵，一直延伸到 涉及恶意软件安装与跨应用数据外泄的端到端攻击流程。覆盖面很广——三种架构下的八个前沿移动 agent，超过 2000 组对抗与配对良性试验。结论是系统性的而非个例：欺诈广告这类低门槛向量成功率 超过 80%，而即便是需要绕过操作系统显式警告的流程（如安装恶意软件），依然能够走通。

`环境: Mobile` ｜ [arXiv:2510.27140](https://arxiv.org/abs/2510.27140)

#### OS-Sentinel: Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows (OS-Sentinel) (2025-10)

把核心难点归结为规模问题：系统沦陷、隐私泄露这类不安全操作需要在移动环境庞大而复杂的操作 空间中被检出，而任何单一检测器都覆盖不了。OS-Sentinel 的答案是刻意的混合式——形式化验证器 确定性地捕捉显式的系统级违规，VLM 上下文判别器处理形式化规则无法表达的语义情形。工作同时 贡献了 MobileRisk-Live：一个动态沙箱环境，配套由真实轨迹构成、带细粒度标注的安全检测基准， 正是它让这种混合式切分变得可测量，而不只是听起来合理。

`环境: Mobile` ｜ [arXiv:2510.24411](https://arxiv.org/abs/2510.24411)

#### GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments? (GhostEI-Bench) (2025-10)

把环境注入确立为区别于提示类攻击的、研究不足的威胁向量：它不改文本指令，而是把欺骗性 覆盖层、伪造通知这类对抗 UI 元素直接插入 GUI 以污染 agent 的视觉感知，从而绕开文本层 防护，可导致隐私泄漏、财务损失甚至不可逆的设备失陷。GhostEI-Bench 跳出静态图像评测， 在完整可运行的 Android 模拟器中把对抗事件注入真实应用工作流。

`环境: Mobile` ｜ [arXiv:2510.20333](https://arxiv.org/abs/2510.20333)

#### Invisible to Humans, Triggered by Agents: Stealthy Jailbreak Attacks on Mobile Vision-Language Agents (Agent-Only Perceptual Injection) (2025-10)

此前针对移动 agent 的视觉注入要么依赖用户能察觉的持续视觉篡改，要么需要系统级权限。 本文找到一个更干净的触发条件：人与 agent 的交互存在稳定差异——自动化 agent 产生的 接触式触摸信号近乎为零。这个信号被用作判别器，从而实现「仅对 agent 生效的感知注入」： 恶意内容只在 agent 交互时暴露，人类用户则不易感知。为适配移动 UI 约束与一次性交互场景， 作者提出 HG-IDA*，用单次优化构造可绕过 LVLM 安全过滤的越狱提示。这个机制的巧妙之处在于 它不是把载荷藏起来不让人看见，而是在证明「触摸者不是人」之前根本不投放载荷。

`环境: Mobile` ｜ [arXiv:2510.07809](https://arxiv.org/abs/2510.07809)

#### VeriOS: Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents (VeriOS) (2025-09)

多数 OS agent 是为理想化环境设计的，而真实环境常常并不可信——因此要防的失败模式是 「过度执行」。VeriOS 没有外挂一层过滤器，而是把「何时该问人」变成一种可学习的能力： 提出查询驱动的人-agent-GUI 交互框架，让 agent 在正常条件下自主执行、在不可信场景中 主动向用户发问。VeriOS-Agent 采用三阶段训练（监督微调 + 组相对策略优化），目的是把 关于「可信性」的元知识与任务知识解耦，使两者可以独立调用。这个设定对 §2.4 很有意义： 确认机制不再是硬加在上层的固定策略，而是 agent 自己必须学会有选择地做出的决策。

`环境: Mobile, Desktop` ｜ [arXiv:2509.07553](https://arxiv.org/abs/2509.07553)

#### MVISU-Bench: Benchmarking Mobile Agents for Real-World Tasks by Multi-App, Vague, Interactive, Single-App and Unethical Instructions (MVISU-Bench) (2025-08)

任务分类法来自用户问卷而非研究者直觉，由此得出五个类别——多应用、模糊、交互式、单应用、 不道德指令——覆盖 137 个真实移动应用上的 404 个双语任务。其中两个类别与安全直接相关： 不道德指令检验拒答能力，模糊指令检验 agent 是否会**主动询问**而不是擅自猜测。论文同时 发布 Aider，一个即插即用的动态 prompter，用于缓解风险并澄清用户意图，把总体成功率相比 此前 SOTA 提升 19.55%——这说明「主动澄清」与「有能力」并不互相矛盾。

`环境: Mobile` ｜ [arXiv:2508.09057](https://arxiv.org/abs/2508.09057)

#### VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation (VisualTrap) (2025-07)

把「视觉 grounding」——即从文本计划到具体 GUI 元素的映射——认定为一个独立的攻击面，与规划和 推理层面区分开来。其后果正是危险之处：植入 grounding 的后门会在 agent **拿到完全正确的 解题计划时**依然改变其行为，因此检查计划本身看不出任何问题。VisualTrap 通过误导 agent 把 文本计划定位到攻击者选定的位置来劫持 grounding，这意味着所有计划级审查与推理审计都能干净 通过，而动作却落在攻击者想要的地方。

`环境: Mobile, Desktop` ｜ [arXiv:2507.06899](https://arxiv.org/abs/2507.06899)

#### Poison Once, Control Anywhere: Clean-Text Visual Backdoors in VLM-based Mobile Agents (VIBMA) (2025-06)

利用移动 agent 构建方式上的结构性弱点：它们通常在小规模、用户自行收集的数据上微调，使 训练期投毒从理论威胁变成现实可行。VIBMA 是首个针对 VLM 移动 agent 的**纯净文本**后门—— 只修改视觉输入，prompt 与指令完全保持原样，因此没有任何文本异常可供检测。模型在投毒数据上 微调后，推理时加入预设的视觉触发图案即激活攻击者指定行为。其机制是把投毒样本的训练梯度与 攻击者指定目标实例的梯度对齐，从而把后门特征嵌进数据本身。

`环境: Mobile` ｜ [arXiv:2506.13205](https://arxiv.org/abs/2506.13205)

#### MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control (MobileSafetyBench) (2024-10)

填补了当时的一个完全空白——尽管移动设备控制 agent 会直接接触个人信息与设备设置，却没有任何 标准化的安全评测基准。该基准基于 Android 模拟器构建以保证真实性，覆盖消息、银行等类应用， 并刻意区分了两类常被混为一谈的风险：**滥用**（agent 被要求做有害之事）与**负面副作用** （agent 在追求正当目标的过程中造成危害）。任务同时覆盖日常场景与面对间接提示注入时的鲁棒性。

`环境: Mobile` ｜ [arXiv:2410.17520](https://arxiv.org/abs/2410.17520)
