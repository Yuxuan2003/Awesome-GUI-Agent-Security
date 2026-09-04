# Mobile

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

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

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)

提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。

`环境: Mobile, 跨环境` ｜ [arXiv:2607.29199](https://arxiv.org/abs/2607.29199)

#### SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction (SeerGuard) (2026-07)

指出移动 GUI agent 现有安全机制本质上都是被动响应，无法在动作触发前评估风险，而这类 agent 的单个错误动作往往不可逆。SeerGuard 是「后果感知」框架，将指令级筛查与动作级 风险评估结合：在当前 GUI 状态下分析 agent 拟执行的动作，预判可能结果再决定是否放行。 支撑能力来自一个多任务学习训练的安全增强世界模型（SAWM），把语义化的下一状态预测与 安全风险评估融进同一个模型，且该框架可跨不同底层 GUI agent 迁移。

`环境: Mobile` ｜ [arXiv:2607.15550](https://arxiv.org/abs/2607.15550)

#### (A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents (AI Sees) (2026-07)

系统分析第三方移动 agent 引入的新攻击面，核心是「感知鸿沟」——agent 能读取到屏幕上用户 实际看不到或不会注意的内容（隐藏视图、后台通知、无障碍节点），攻击者可利用这一差异实施 用户完全无法察觉的诱导。指出第三方 agent 生态缺乏对 agent 可见性范围的约束机制。

`环境: Mobile` ｜ [arXiv:2607.00333](https://arxiv.org/abs/2607.00333)

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

#### GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments? (GhostEI-Bench) (2025-10)

把环境注入确立为区别于提示类攻击的、研究不足的威胁向量：它不改文本指令，而是把欺骗性 覆盖层、伪造通知这类对抗 UI 元素直接插入 GUI 以污染 agent 的视觉感知，从而绕开文本层 防护，可导致隐私泄漏、财务损失甚至不可逆的设备失陷。GhostEI-Bench 跳出静态图像评测， 在完整可运行的 Android 模拟器中把对抗事件注入真实应用工作流。

`环境: Mobile` ｜ [arXiv:2510.20333](https://arxiv.org/abs/2510.20333)

#### Poison Once, Control Anywhere: Clean-Text Visual Backdoors in VLM-based Mobile Agents (VIBMA) (2025-06)

利用移动 agent 构建方式上的结构性弱点：它们通常在小规模、用户自行收集的数据上微调，使 训练期投毒从理论威胁变成现实可行。VIBMA 是首个针对 VLM 移动 agent 的**纯净文本**后门—— 只修改视觉输入，prompt 与指令完全保持原样，因此没有任何文本异常可供检测。模型在投毒数据上 微调后，推理时加入预设的视觉触发图案即激活攻击者指定行为。其机制是把投毒样本的训练梯度与 攻击者指定目标实例的梯度对齐，从而把后门特征嵌进数据本身。

`环境: Mobile` ｜ [arXiv:2506.13205](https://arxiv.org/abs/2506.13205)
