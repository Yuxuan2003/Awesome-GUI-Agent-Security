# 2.1 输入侧过滤与净化

*Input Filtering & Sanitization*

[← 返回索引](../../../README.zh-CN.md#21-输入侧过滤与净化) ｜ [English](../en/2-1-input-filtering-sanitization.md)

*在内容进入模型上下文前过滤或遮蔽不可信部分*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### MPIDetector: Detecting Multi-modal Prompt Injection via LLM-based Reasoning (MPIDetector) (2026-10)

攻击者可以把恶意指令藏在文本叙述或视觉输入里绕过安全对齐，而基于签名或困惑度的检测方法依赖 模式匹配，难以识别复杂的跨模态提示注入载荷。MPIDetector 改用 LLM 自身的推理能力：不微调， 只通过少样本上下文学习提供提示模板与代表性攻击样例，让模型跨模态审视输入的语义意图。评测基准 含 8 类文本恶意类别、7 类视觉恶意类别，并配良性数据集检验误报。在 Gemini-2.0-Flash、 Qwen3-VL-32B-Instruct 与 Doubao-seed-1.6-flash 上，文本任务最高 90.91% 准确率、100% 召回， 视觉任务最高 99.28% 准确率且所有模型均保持 100% 精确率。关键在于，面对 WebInject 中 500 条 高度混淆的环境 web-agent 注入，检出率最高达 99.80%，优于两个文本基线与两个视觉基线。 （边界条目：该检测器并非专为 GUI agent 设计，但其威胁模型包含针对 web agent 的环境注入， 且 §2.1 已收录同类的注入检测评估工作，故收录并在 PR 中列明理由。）

`环境: 跨环境` ｜ [arXiv:2610.30202](https://arxiv.org/abs/2610.30202)

#### PrivacyGuard: Source-Linked Sanitization and Locally Resolvable PII References for Cloud GUI Agents (PrivacyGuard) (2026-10)

云端 GUI agent 会把指令和截图发给远程规划器，从而暴露个人身份信息（PII）。现有的占位符防御 只遮蔽检测到的片段、并复用完全相同的字符串，一旦 PII 以碎片化或变形的形式出现，仍可能泄露， 或者在多轮之间断开实体的连续性。PrivacyGuard 用两部分解决这个「私密引用」问题：一是与来源 绑定的净化（SAN），重建碎片化或重叠的证据并改写完整的来源范围；二是结构化的引用生命周期 （REF），把变形后的出现关联到会话实体，支持在本地解析引用，原始值不会回到上传路径。在五轮会话 中，相比最接近的已有全流程系统，它在全部四种读取器—语言组合下把可审计的来源值泄露降低 33.55%–82.60%；REF 把严格跨形式连续性从「精确值复用」下的 0.04 提升到 0.81。在需要引用的 Android 任务上，验证完成数从 8/30、7/30 提升到 17/30、20/30；在 AndroidLab 上，四个规划器 下它的任务成功率在各防护方案中均为最高或并列最高；在 PrivScreen 上，固定读取器的字段暴露降低 约 63%。

`环境: Mobile` ｜ [arXiv:2610.16778](https://arxiv.org/abs/2610.16778)

#### FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory (FocusMem) (2026-08)

潜在记忆把多模态 GUI 轨迹压缩成少量连续 token，但现有方法把每条轨迹映射到一个固定 记忆块，且主要靠下一动作监督来训练。由此带来三个实际问题：压缩过程中细节丢失、同一个 记忆块要服务所有决策阶段、检索到不相关的轨迹仍会误导 agent。FocusMem 把这些职责拆开： 角色感知的内容基底促使情景记忆保留可复用经验、工作记忆保留当前任务进展；状态条件化的 读出机制为同一份存储证据生成面向具体决策的视图；轻量的信任门可在检索不可靠时抑制记忆。 最后这一项正是它进入安全清单的理由——它把检索到的记忆当作需要设门的不可信输入， 而这正是对抗记忆投毒式操纵的结构性防御。

`环境: Mobile, Desktop, Web` ｜ [arXiv:2608.04530](https://arxiv.org/abs/2608.04530)

#### Untrusted Content Masking for Web Agents with Security Guarantees (UCM) (2026-07)

指出可证明的注入防御依赖可信指令与不可信数据之间的严格隔离，这在纯文本的 tool-use 场景 中天然成立（agent 可只依据接口定义推理，无需接触不可信内容），但 web agent 必须先观察 渲染后的页面才能感知环境，而页面把可信与不可信内容结构性地混在一起，导致安全保证赖以 成立的信任边界消失。提出 Untrusted Content Masking，利用页面的结构特性在 web 环境中 重建这一边界，使既有的可证明防御能够迁移过来。

`环境: Web` ｜ [arXiv:2607.05277](https://arxiv.org/abs/2607.05277)

#### When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents (IPI Probe Controls) (2026-06)

在冻结视觉语言模型的内部激活上训练线性分类器（hidden-state probing），因能在计算机使用代理 发出被污染的动作之前标记间接提示注入而受到关注。本文以单一骨架（Qwen2.5-VL-7B 在 Mind2Web 上的教师强制重放）做警示性案例研究，论证「干净 vs 攻击」划分下的高探测 AUC 本身并不能证明 探针真的检测到了恶意内容。两项事后诊断 —— 文本侧注入的配对构造标量基线，以及覆盖层上同 步骤的干扰匹配视觉对照 —— 都不支持对 headline 数字作无保留的「恶意内容检测」解读，但仍为 部分语义性解释留下空间。作者把诊断打包成候选对照集，并给出报告启发式，说明高 AUC 究竟能 支持什么、不能支持什么；同时强调标签只表示注入面是否存在，而非攻击是否成功，超出该骨架与 基准的泛化仍属猜想。

`环境: 跨环境` ｜ [arXiv:2606.22864](https://arxiv.org/abs/2606.22864)

#### CAPED: Context-Aware Privacy Exposure Defense for Mobile GUI Agents (CAPED) (2026-06)

指出一个截图范式特有的问题：由于 agent 以与人完全相同的方式「看」手机，每一次屏幕观测都 变成一道隐私边界，正常执行任务时就可能暴露联系人、消息、照片、健康线索等与请求毫无关系的 上下文。作者称之为「附带性视觉隐私暴露」，并说明两个极端为何都行不通——文本匿名化会漏掉 视觉与可推断线索，而通用遮蔽又会把 agent 完成任务所需的证据和控件一起抹掉。CAPED 是运行 在手机侧的上传前控制层，解析可见 UI 元素并选择性遮蔽，以任务需求和屏幕上下文作为隐私先验。

`环境: Mobile` ｜ [arXiv:2606.12666](https://arxiv.org/abs/2606.12666)

#### MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution (MaskClaw) (2026-05)

把 GUI agent 隐私问题定义为**裁决**问题而非检测问题：某项内容是否属于隐私取决于任务、接收方、 应用状态与用户角色，因此静态 PII 检测器抓不住这些边界，而云端 VLM 推理又会在决定「什么需要 保护」**之前**就把原始屏幕上传出去。MaskClaw 运行在边缘侧：抽取本地视觉证据、检索用户与任务 专属的策略记忆，在截图离开可信环境前判定 Allow / Mask / Ask。在五个 skill 演进场景中，它把 用户的纠正、取消与编辑转化为可复用的隐私 skill，并经沙箱门校验，评测基准为 P-GUI-Evo。

`环境: Mobile, Desktop` ｜ [arXiv:2605.28646](https://arxiv.org/abs/2605.28646)

#### WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections (WARD) (2026-05)

系统列出现有 web agent 护栏模型的四类实际失效：对未见域与新攻击模式泛化差、在正常内容上 误报率高、每步推理带来的延迟拖累部署、以及自身会成为攻击目标。WARD 基于 WARD-Base 构建——取自 719 个高流量 URL 与平台的约 17.7 万样本，另有专门针对「攻击护栏本身」的 WARD-PIG 数据集。并提出自适应对抗训练框架 A3T，正面回应了一个常被忽略的问题：护栏模型 本身也是一个攻击面。

`环境: Web` ｜ [arXiv:2605.15030](https://arxiv.org/abs/2605.15030)

#### SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents (SnapGuard) (2026-04)

针对一个具体盲区：基于截图的 web agent 处理的是渲染后的视觉画面而非结构化文本，因此 主流的文本中心防御根本用不上。已有的多模态检测方法确实有效，但依赖大型 VLM，而论文精确 定位了瓶颈——VLM 必须理解整个现代网页的全局语义，推理时间与显存开销都被推高。SnapGuard 转而从「被注入的页面具有独特局部特征」这一观察出发，无需理解整页语义即可完成检测。

`环境: Web` ｜ [arXiv:2604.25562](https://arxiv.org/abs/2604.25562)

#### WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents (WebAgentGuard) (2026-04)

指出无论是 system prompt 防御还是直接微调 agent，对嵌在 HTML 或渲染截图中的注入效果 都有限。架构上的选择是让一个专职护栏 agent 与 web agent 并行运行，把注入检测与 agent 自身的推理解耦——这样推理链被污染时不会连带污染检测能力。WebAgentGuard 是推理驱动的 多模态护栏模型，训练数据覆盖 164 个主题与 230 种视觉/UI 设计风格，针对的正是训练集 过窄留下的泛化缺口。

`环境: Web` ｜ [arXiv:2604.12284](https://arxiv.org/abs/2604.12284)

#### The Cognitive Firewall: Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense (Cognitive Firewall) (2026-03)

针对「云端防御语义分析能力强但引入延迟与隐私暴露」这一矛盾，提出三阶段拆分计算架构 Cognitive Firewall，把安全检查分布在客户端与云端：本地视觉 Sentinel、云端 Deep Planner、 以及在执行期强制策略的确定性 Guard。在 1000 个对抗样本上，纯边端防御漏检 86.9% 的语义 攻击，而完整混合架构把攻击成功率压到 1% 以下（静态评测 0.88%、自适应评测 0.67%），同时 对有副作用的动作保持确定性约束；由于表现层攻击在本地即被过滤，相比纯云端基线取得约 17000 倍的延迟优势。

`环境: Web` ｜ [arXiv:2603.23791](https://arxiv.org/abs/2603.23791)

#### Anonymization-Enhanced Privacy Protection for Mobile GUI Agents: Available but Invisible (Available but Invisible) (2026-02)

诊断出移动 GUI agent 现有隐私防御为何都不够用：减少 UI 暴露、只混淆与任务无关内容、或依赖 用户授权，这三条路都绕开了最难的情况——如何保护**本身就是任务必需**的敏感信息。论文提出的 原则是「可用但不可见」：敏感数据对执行仍然可用，但云端 agent 永远看不到其真实内容。实现上 结合 PII 感知的 UI 内容识别模型与匿名化，使 agent 在占位符上操作，真实值始终不越出可信边界。

`环境: Mobile` ｜ [arXiv:2602.10139](https://arxiv.org/abs/2602.10139)

#### WebSentinel: Detecting and Localizing Prompt Injection Attacks for Web Agents (WebSentinel) (2026-02)

观察到现有检测与定位方法在 web agent 场景下效果有限，因为其赖以成立的假设在这里不成立。 WebSentinel 采用两步法：第一步抽取可能被污染的「关注片段」，第二步以页面其余内容为上下文 检查每个片段的一致性。它不只给出二分类判断，还能定位被注入的具体片段——这在工程上很关键， 知道哪个元素被污染就能做精确剔除，而不必丢弃整个页面。

`环境: Web` ｜ [arXiv:2602.03792](https://arxiv.org/abs/2602.03792)

#### Attention is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs (Rennervate) (2025-12)

走机制路线做注入防御——读取注意力特征而非对文本做分类：Rennervate 在 **token 级**粒度检出 隐蔽注入，从而实现精确净化，在中和注入的同时保留 LLM 其余功能完整。这与页面级或片段级防御 形成对比，后者必须把干净内容与被污染片段一起丢弃。token 级检测器采用两步注意力池化机制， 聚合注意力头与响应 token。工作同时发布细粒度 IPI 数据集 FIPI，并报告优于 15 种商业与学术 防御方法。

`环境: Web` ｜ [arXiv:2512.08417](https://arxiv.org/abs/2512.08417)

#### DualTAP: A Dual-Task Adversarial Protector for Mobile MLLM Agents (DualTAP) (2025-11)

把隐私泄露定位到一个具体的架构环节：含 PII 的截图会被例行发送给不受信的第三方路由服务， 而这些服务可以用自己的 MLLM 挖掘其中数据。该场景提出了此前扰动类方法无法同时满足的矛盾 要求——既要让路由方的模型看不到 PII，又要保留足够信息让 agent 的模型完成任务。DualTAP 显式解耦这两个目标：用对比注意力模块精确定位仅 PII 敏感区域，并以双任务对抗目标在任务 保持损失与隐私干扰之间取得平衡。

`环境: Mobile` ｜ [arXiv:2511.13248](https://arxiv.org/abs/2511.13248)

#### CORE: Reducing UI Exposure in Mobile Agents via Collaboration Between Cloud and Local LLMs (CORE) (2025-10)

云端 LLM 让移动 agent 任务准确率高，但每一步都要上传完整 UI 状态，暴露大量不必要且常常 无关的信息；本地 LLM 避免了上传，却受限于能力不足、任务成功率偏低。CORE 是一个兼顾两者的 协同框架，用三个组件减少 UI 暴露：基于 XML 屏幕层级的布局感知分块，把语义相关的 UI 元素 分组；协同规划，由本地与云端 LLM 共同确定当前子任务；协同决策，本地 LLM 对相关 UI 块排序， 云端 LLM 只在排名最高的块内选择具体元素。多轮累积机制用于缓解本地误判与上下文受限。在多个 应用与任务上，CORE 把 UI 暴露减少最多 55.6%，而任务成功率仅略低于纯云端方案，实质降低了 不必要的隐私外泄。

`环境: Mobile` ｜ [arXiv:2510.15455](https://arxiv.org/abs/2510.15455)

#### GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents (GEM) (2025-05)

GUI agent 一旦遇到违反环境约束或超出自身能力的分布外指令，就可能任务崩溃甚至产生安全威胁， 因此有效的 OOD 检测十分必要。但传统 OOD 方法在这个场景表现不佳 —— 嵌入空间复杂，且 GUI 环境持续演化。作者观察到分布内输入的语义空间按到质心的距离呈聚类结构，据此提出 GEM：对从 GUI agent 提取的、反映其能力边界的输入嵌入距离拟合高斯混合模型。在覆盖手机、电脑与网页 浏览器的八个数据集上，GEM 的平均准确率比最佳基线提升 23.70%，而训练与测试时间仅分别增加 4.9% 与 6.5%。在检测到 OOD 样本时请求云端模型协助，还能把分步成功率提升 9.40%；九个不同 骨架上的实验验证了方法的泛化能力。

`环境: 跨环境` ｜ [arXiv:2505.12842](https://arxiv.org/abs/2505.12842)
