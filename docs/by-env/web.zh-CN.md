# Web

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### SIR: Self-improving Red-teaming for Compute Use Agents (SIR) (2026-08)

指出现有 CUA 安全基准用的都是人工手写的固定注入载荷，会低估自适应攻击者的真实威胁。提出 黑盒 IPI 攻击 SIR：从一个用自然语言描述的可复用「隐蔽性原则」小库中组合注入内容，再套一层 迭代反馈循环——诊断受害 agent 失败的攻击轨迹，把成功绕过的模式蒸馏回原则库。这把红队从 静态测试变成自我改进的过程，说明固定载荷的评测结论会随攻击者迭代迅速失效。

`环境: Desktop, Web` ｜ [arXiv:2608.30207](https://arxiv.org/abs/2608.30207)

#### LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents (LoginTrap) (2026-08)

登录对 web agent 而言是涉及凭据的敏感认证边界，但已有工作尚未考察恶意页面内容能否诱导 agent 登录并造成端到端的私密数据泄漏。LoginTrap 是一种与任务无关的诱导登录攻击，假设 黑盒攻击者只控制页面上下文与被诱导的登录流程，并不知道用户任务或 agent 内部实现：通过 类 fuzzing 的流程生成页面专属的间接注入内容，使「先登录」看起来是继续完成任务的合理 前置条件，从而把 agent 引导至攻击者控制的登录页。

`环境: Web` ｜ [arXiv:2608.04741](https://arxiv.org/abs/2608.04741)

#### From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems (WebMASLab) (2026-07)

追问「角色分解」在安全上的代价：多 agent web 系统通过把工作拆给专职子 agent 来提升任务性能， 但这种拆分会产生单 agent 架构下不存在的结构性攻击面，而这些攻击面此前缺乏归类。论文提出 针对 web 多 agent 系统的攻击向量分类法，并构建 WebMASLab 来研究一个完全外部、仅通过网页 施加影响的攻击者。方法上相当严谨——固定用户任务、工具面与浏览器基座，只让架构一个变量变化， 覆盖三种对抗场景与三种条件（基线、prompt 加固、开启推理）。

`环境: Web` ｜ [arXiv:2608.00202](https://arxiv.org/abs/2608.00202)

#### Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents (Broken Gates) (2026-07)

把通常的视角反转过来：不问「如何保护 agent」，而问「在浏览器 agent 能自主导航、理解页面内容、 按自然语言指令行动（而非回放预设脚本）之后，网络现有的 bot 管理系统还挡得住吗」。测量同时 覆盖交互式挑战型防御与非交互式信任型防御，面对两类攻击者——商业验证码破解服务与 LLM 浏览器 agent——涵盖 7 家破解服务与 6 种 agent 配置（云托管、自托管、AI 辅助、浏览器扩展），针对 hCaptcha、reCaptcha v2/v3、Cloudflare Turnstile。结论是：挑战型防御已经失守。

`环境: Web` ｜ [arXiv:2607.18659](https://arxiv.org/abs/2607.18659)

#### Prismata: Confining Cross-Site Prompt Injection in Web Agents (Prismata) (2026-07)

把 web agent 面临的注入风险类比为 XSS 的重现：XSS 已经证明混合可信与不可信内容是危险的， 而 agent 把自然语言当指令解释，使第三方与用户生成内容能够劫持 agent。核心难点在于推导 任务专属的安全策略需要理解页面结构，而页面结构本身已与攻击者内容纠缠。提出 Prismata， 借鉴经典完整性模型的思路做动态信任推导，为页面内容打上权限标签并提供结构性隔离保证， 同时约束 agent「能看到什么」与「能做什么」，实现上下文最小权限。

`环境: Web` ｜ [arXiv:2607.08147](https://arxiv.org/abs/2607.08147)

#### Untrusted Content Masking for Web Agents with Security Guarantees (UCM) (2026-07)

指出可证明的注入防御依赖可信指令与不可信数据之间的严格隔离，这在纯文本的 tool-use 场景 中天然成立（agent 可只依据接口定义推理，无需接触不可信内容），但 web agent 必须先观察 渲染后的页面才能感知环境，而页面把可信与不可信内容结构性地混在一起，导致安全保证赖以 成立的信任边界消失。提出 Untrusted Content Masking，利用页面的结构特性在 web 环境中 重建这一边界，使既有的可证明防御能够迁移过来。

`环境: Web` ｜ [arXiv:2607.05277](https://arxiv.org/abs/2607.05277)

#### Agent Data Injection Attacks are Realistic Threats to AI Agents (ADI) (2026-07)

指出间接提示注入的研究几乎全部集中在「指令注入」上——即不可信数据被当作指令解释——而针对 性构建的缓解措施也继承了这个狭窄的问题框架。论文提出 agent 数据注入（ADI）：把恶意数据 伪装成**可信数据**，例如安全关键元数据（资源标识符、数据来源）或 agent 上下文数据（工具 调用与响应格式）。其影响与指令注入相当，agent 依然会执行非预期动作，但那些专门用于识别 「嵌入指令」的防御，没有任何理由把一段格式规范的元数据标记为可疑。

`环境: Web, Desktop` ｜ [arXiv:2607.05120](https://arxiv.org/abs/2607.05120)

#### MIRAGE: Stealthy Visual Prompt Injection for Vulnerability Detection in Web Agents (MIRAGE) (2026-06)

批评现有针对多模态 web agent 的对抗评测普遍采用过于宽松的威胁模型、依赖视觉上显眼的 伪影。本文转向受约束的现实设定：评测者只是不具特权的第三方（如商家或广告主），仅能控制 广告位、赞助卡片这类语义合法且空间受限的区域。在此约束下提出视觉间接注入框架 MIRAGE， 实现对下一步动作的定向劫持，说明即便攻击者只掌握页面上一小块合法区域，也足以操纵 基于视觉的 agent。

`环境: Web` ｜ [arXiv:2606.20717](https://arxiv.org/abs/2606.20717)

#### OSGuard: A Benchmark for Safety in Computer-Use Agents (OSGuard) (2026-06)

针对一个测量盲区：computer-use agent 通常只以任务完成率评判，但「成功」会掩盖 agent 通过 不安全捷径达成名义目标的情况。OSGuard 在**良性、未被篡改**的用户指令下评估安全性——回路中 没有攻击者——并设计了两个粒度。动作级基准把语境化的候选动作标注为「允许 / 无关 / 不安全」， 每条都相对原始指令与当前界面状态判定。执行套件基于人工构造的 OSWorld 变体，原任务仍可完成， 但环境中埋入了破坏性覆写等潜在危害，并配套保留原成功信号的增强评测器。

`环境: Desktop, Web` ｜ [arXiv:2606.15034](https://arxiv.org/abs/2606.15034)

#### Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents (Who Pays the Price) (2026-06)

指出现有安全基准都采用「攻击视角」，只关注注入在技术上是否可行，忽略了危害在不同受害方 之间的分布差异。本文主张注入风险是**受害者依赖**的：同一个漏洞对不同利益相关方（用户、 平台、商家）造成的后果高度不对称，同一攻击模式的有效性也随目标不同而显著变化。据此构建 以利益相关方为中心的基准，聚焦电商这类动作直接带来财务后果的真实场景。

`环境: Web` ｜ [arXiv:2606.13385](https://arxiv.org/abs/2606.13385)

#### MemVenom: Triggered Poisoning of Multimodal Memories in Web Agents (MemVenom) (2026-06)

针对外部记忆——它已是现代 web agent 支撑长周期推理的核心组件——并指出其结构性后果：注入 记忆的内容会被持续召回、反复影响行为，因此一次成功投毒的影响能跨越会话存活。MemVenom 是 黑盒框架，用协同的图文证据污染图结构外部记忆，分两阶段：先以触发条件化的检索攻击确保恶意 记忆被高概率召回，再通过对抗扰动与隐蔽 OCR 注入在检索后诱导 agent 覆盖用户原目标。与 prompt 层或纯文本记忆攻击不同，其效果是持久且可复用的。

`环境: Web` ｜ [arXiv:2606.10742](https://arxiv.org/abs/2606.10742)

#### BraveGuard: From Open-World Threats to Safer Computer-Use Agents (BraveGuard) (2026-05)

从「CUA 的危害为何难以捕捉」出发：危害只在多步执行轨迹中浮现，而其中每个单独动作在局部看 都无害，因此孤立的 prompt 与最终回复都看不出问题。BraveGuard 是自我演进的流水线：从近期 研究来源中挖掘新兴风险与攻击模式，将其实例化为可执行的 computer-use 任务，收集 agent rollout，进而导出**轨迹级**监督信号训练护栏模型。由于新威胁与验证失败出现时可以重跑这个 闭环，防御能持续适应，而不是冻结在静态基准训练时所捕捉到的那个快照上。

`环境: Desktop, Web` ｜ [arXiv:2606.01166](https://arxiv.org/abs/2606.01166)

#### "I Strongly Suspect This Website Is a Scam": Benchmarking PII Leakage and Detection without Defense in Autonomous Web Agents (Scammer4U) (2026-05)

把社会工程攻击（互联网上早已普遍存在的欺骗性内容）作为一类攻击向量来研究，考察它如何操纵 自主 web agent 把用户 PII 提交到攻击者控制的端点。Scammer4U 是**预注册**基准，含 91 个 攻击者控制环境与 10 个「良性孪生」对照，覆盖 8 类攻击向量、16 类站点，构建在能隔离各设计 因子因果贡献的 8 轴因子分类上。良性孪生的设计承担了论证核心：无隐私提示时关键级 PII 泄露 达 54–93%，而孪生对照为 0%，证明泄露可归因于攻击本身，而非顺手填表的偶然行为。

`环境: Web` ｜ [arXiv:2606.00497](https://arxiv.org/abs/2606.00497)

#### WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections (WARD) (2026-05)

系统列出现有 web agent 护栏模型的四类实际失效：对未见域与新攻击模式泛化差、在正常内容上 误报率高、每步推理带来的延迟拖累部署、以及自身会成为攻击目标。WARD 基于 WARD-Base 构建——取自 719 个高流量 URL 与平台的约 17.7 万样本，另有专门针对「攻击护栏本身」的 WARD-PIG 数据集。并提出自适应对抗训练框架 A3T，正面回应了一个常被忽略的问题：护栏模型 本身也是一个攻击面。

`环境: Web` ｜ [arXiv:2605.15030](https://arxiv.org/abs/2605.15030)

#### Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces (DUDE) (2026-05)

指出以往工作的割裂之处：一类方法能检测欺骗但不与任务回路结合，另一类记录了攻击却不提出 防御。论文形式化了「欺骗感知的 web agent 防御」，提出两阶段框架 DUDE，把带非对称惩罚的 混合奖励学习与经验总结结合起来，将失败模式蒸馏为可迁移的指导。配套发布基准 RUC（Real UI Clickboxes），含跨四个领域与欺骗类别的 1407 个场景。DUDE 在保持任务性能的同时把易受骗 程度降低 53.8%——这一点很关键，因为多数安全干预都是以牺牲效用为代价。

`环境: Web` ｜ [arXiv:2605.09497](https://arxiv.org/abs/2605.09497)

#### WebTrap: Stealthy Mid-Task Hijacking of Browser Agents During Navigation (WebTrap) (2026-05)

诊断出现有针对浏览器 agent 的注入攻击有两个缺口：一是有效性低，在玩具基准上调优的攻击 放到真实环境、长步骤链条中就达不成端到端目标；二是隐蔽性弱，多数攻击把攻击目标与用户目标 对立起来，导致可用性明显崩塌，攻击相当于自我暴露。WebTrap 转而在**任务中途**劫持：用多步 指令融合引导把两个目标缝合起来，让 agent 在完成攻击目标后继续把用户原任务做完。配套的 上下文接地生成方法使注入内容与所处任务环境保持一致，看不出突兀。

`环境: Web` ｜ [arXiv:2605.08310](https://arxiv.org/abs/2605.08310)

#### Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces (WebDecept) (2026-04)

在电商场景下考察 web agent 面对真实欺骗性界面时的行为——这个场景里点错一下就有直接的财务 后果。WebDecept 是轻量可配置的插件框架，能把欺骗性界面模式注入既有网页环境，并实例化了 七种野外常见模式，含定向广告、域名重定向、购物操纵等。在任务执行过程中把它们注入前端， 即可对多个多模态 agent 做受控评测。两个结论值得注意：agent 对多类模式都高度易感；而基于 prompt 的约束往往不足以缓解这类失败。

`环境: Web` ｜ [arXiv:2606.13686](https://arxiv.org/abs/2606.13686)

#### SnapGuard: Lightweight Prompt Injection Detection for Screenshot-Based Web Agents (SnapGuard) (2026-04)

针对一个具体盲区：基于截图的 web agent 处理的是渲染后的视觉画面而非结构化文本，因此 主流的文本中心防御根本用不上。已有的多模态检测方法确实有效，但依赖大型 VLM，而论文精确 定位了瓶颈——VLM 必须理解整个现代网页的全局语义，推理时间与显存开销都被推高。SnapGuard 转而从「被注入的页面具有独特局部特征」这一观察出发，无需理解整页语义即可完成检测。

`环境: Web` ｜ [arXiv:2604.25562](https://arxiv.org/abs/2604.25562)

#### RiskWebWorld: A Realistic Interactive Benchmark for GUI Agents in E-commerce Risk Management (RiskWebWorld) (2026-04)

指出现有交互式基准都瞄准良性、可预测的消费者环境，把高风险的调查类场景留在了视野之外。 RiskWebWorld 从生产环境的风控流水线中取 1513 个任务、覆盖 8 个核心领域，并刻意保留风控 作业的真实困难——不配合的网站、部分环境劫持。配套的 Gymnasium 兼容基础设施把策略规划与 环境机制解耦，以支持 agentic RL。评测暴露出明显的能力落差：顶级通用模型成功率仅 49.1%， 说明对抗性的真实作业场景远未被解决。

`环境: Web` ｜ [arXiv:2604.13531](https://arxiv.org/abs/2604.13531)

#### WebAgentGuard: A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents (WebAgentGuard) (2026-04)

指出无论是 system prompt 防御还是直接微调 agent，对嵌在 HTML 或渲染截图中的注入效果 都有限。架构上的选择是让一个专职护栏 agent 与 web agent 并行运行，把注入检测与 agent 自身的推理解耦——这样推理链被污染时不会连带污染检测能力。WebAgentGuard 是推理驱动的 多模态护栏模型，训练数据覆盖 164 个主题与 230 种视觉/UI 设计风格，针对的正是训练集 过窄留下的泛化缺口。

`环境: Web` ｜ [arXiv:2604.12284](https://arxiv.org/abs/2604.12284)

#### Preference Redirection via Attention Concentration: An Attack on Computer Use Agents (PRAC) (2026-04)

指出以往 CUA 攻击工作集中在语言模态，视觉模态受到的关注远远不足，随后就攻在这里。PRAC 不 直接操纵 VLM 的输出，而是通过把注意力重定向到一个隐蔽的对抗补丁上，改变模型的**内部偏好**， 从而在网购平台上把 CUA 的商品选择引导到指定目标。攻击构造需要白盒访问，但真正值得注意的 结论是可迁移性：攻击对同一模型的微调版本依然有效——这意味着被众多部署 agent 共用的同一个 基座模型，会变成一处共享的软肋。

`环境: Desktop, Web` ｜ [arXiv:2604.08005](https://arxiv.org/abs/2604.08005)

#### WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks (WebSP-Eval) (2026-04)

开辟了一个与本清单其余部分正交的方向：现有基准要么测通用能力（WebArena），要么测抵御恶意 动作的能力（SafeArena），但没有一个去问 agent 能否胜任用户真正会委托给它的安全与隐私 事务——管理 cookie 偏好、配置隐私敏感的账户设置、吊销闲置会话。WebSP-Eval 贡献了跨 28 个 网站的 200 个人工构造任务实例、一套通过自定义 Chrome 扩展在多次运行间管理账号与初始状态的 agent 框架、以及自动评测器，并在 8 种 web agent 实例化配置上做了评估。

`环境: Web` ｜ [arXiv:2604.06367](https://arxiv.org/abs/2604.06367)

#### Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents (eTAMP) (2026-04)

记忆让 web agent 变得个性化，也使其可被利用：存储历史交互创造出跨站点、跨会话持续存在的 攻击面。已有研究假设攻击者能直接写入记忆或利用跨用户共享，而 eTAMP 仅靠环境观察就实现 跨会话跨站点污染——单次被污染的观察（如浏览一个被操纵的商品页）即可静默投毒记忆，并在 日后其他网站的任务中激活，绕开基于权限的防御。攻击成功率在 GPT-5-mini 上达 32.5%、 GPT-5.2 上 23.4%、GPT-OSS-120B 上 19.5%，另发现「挫败感利用」现象。

`环境: Web` ｜ [arXiv:2604.02623](https://arxiv.org/abs/2604.02623)

#### The Cognitive Firewall: Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense (Cognitive Firewall) (2026-03)

针对「云端防御语义分析能力强但引入延迟与隐私暴露」这一矛盾，提出三阶段拆分计算架构 Cognitive Firewall，把安全检查分布在客户端与云端：本地视觉 Sentinel、云端 Deep Planner、 以及在执行期强制策略的确定性 Guard。在 1000 个对抗样本上，纯边端防御漏检 86.9% 的语义 攻击，而完整混合架构把攻击成功率压到 1% 以下（静态评测 0.88%、自适应评测 0.67%），同时 对有副作用的动作保持确定性约束；由于表现层攻击在本地即被过滤，相比纯云端基线取得约 17000 倍的延迟优势。

`环境: Web` ｜ [arXiv:2603.23791](https://arxiv.org/abs/2603.23791)

#### WebPII: Benchmarking Visual PII Detection for Computer-Use Agents (WebPII) (2026-03)

CUA 从两个方向带来新的隐私风险：从真实网站采集的训练数据不可避免含敏感信息，而云端推理 会暴露用户截图。此前没有公开基准用于检测网页截图中的个人身份信息。WebPII 提供 44865 张 标注的电商 UI 图像，特点包括扩展的 PII 分类（含可用于重识别的交易级标识符）、针对用户 正在填写的半完成表单的前瞻式检测、以及基于 VLM 的可扩展 UI 复现。配套 WebRedact 把 文本抽取基线准确率翻倍以上（0.753 vs 0.357 mAP@50），CPU 延迟仅 20ms。

`环境: Web, Desktop` ｜ [arXiv:2603.17357](https://arxiv.org/abs/2603.17357)

#### Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks (DMAST) (2026-03)

定位到一处由架构本身造就的攻击面：多模态 web agent 同时消费截图与无障碍树，因此攻击者只需 注入 DOM 就能**同时**污染两个观测通道，并且两边叙述互相一致，使任何跨通道一致性检查都失效。 MiniWob++ 上的漏洞分析显示，带视觉成分的攻击远强于纯文本注入，暴露出以文本为中心的 VLM 安全训练所留下的缺口。DMAST 把 agent 与攻击者的交互形式化为二人零和马尔可夫博弈，通过模仿 学习、带「零确认」策略的 oracle 引导 SFT、以及最后的对抗阶段共训双方。

`环境: Web` ｜ [arXiv:2603.04364](https://arxiv.org/abs/2603.04364)

#### Atomicity for Agents: Exposing, Exploiting, and Mitigating TOCTOU Vulnerabilities in Browser-Use Agents (Atomicity for Agents) (2026-02)

把 agent 规划与执行之间的时间差刻画为经典的 TOCTOU 漏洞：网页在两者之间经常发生变化， 导致动作基于过期假设执行，而动态或对抗性内容可以刻意拉大这个窗口。论文在覆盖合成与真实 网站的基准上做了大规模实证，评测 10 个主流开源 agent，发现 TOCTOU 暴露是普遍现象而非 个例。提出的缓解方案刻意保持轻量——在规划阶段监控 DOM 与布局变化，并在动作真正执行前 立即校验页面状态。

`环境: Web` ｜ [arXiv:2603.00476](https://arxiv.org/abs/2603.00476)

#### SPILLage: Agentic Oversharing on the Web (SPILLage) (2026-02)

与在受控环境中回答问题的聊天机器人不同，web agent 是「在野」运行的：它能访问用户的邮件、 日历等资源，与第三方交互，并留下动作轨迹。本文把「自然的 agent 过度分享」形式化为—— 通过这条动作轨迹无意披露与任务无关的用户信息，并沿「通道」（内容 vs. 行为）与「直接性」 （显式 vs. 隐式）两个维度刻画。这揭示了一处盲区：已有工作聚焦文本泄漏，但 agent 还会通过 点击、滚动、导航模式等行为层面过度暴露，而这些可被第三方监测。在真实电商站点的 180 个 任务上做了基准评测。

`环境: Web` ｜ [arXiv:2602.13516](https://arxiv.org/abs/2602.13516)

#### MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks (MUZZLE) (2026-02)

批评现有安全评测依赖固定攻击模板、人工挑选的注入面或范围过窄的场景，都无法反映真实部署时 面对的自适应攻击者。MUZZLE 将这一过程自动化：利用目标 agent 自身的执行轨迹定位高显著性的 注入面，再自适应地生成上下文感知的恶意指令，针对机密性、完整性、可用性三类违背分别施压。 关键之处在于把注入面的选择建立在观测到的 agent 行为上而非人类直觉上——攻击会随 agent 真正关注的内容而调整。

`环境: Web` ｜ [arXiv:2602.09222](https://arxiv.org/abs/2602.09222)

#### WebSentinel: Detecting and Localizing Prompt Injection Attacks for Web Agents (WebSentinel) (2026-02)

观察到现有检测与定位方法在 web agent 场景下效果有限，因为其赖以成立的假设在这里不成立。 WebSentinel 采用两步法：第一步抽取可能被污染的「关注片段」，第二步以页面其余内容为上下文 检查每个片段的一致性。它不只给出二分类判断，还能定位被注入的具体片段——这在工程上很关键， 知道哪个元素被污染就能做精确剔除，而不必丢弃整个页面。

`环境: Web` ｜ [arXiv:2602.03792](https://arxiv.org/abs/2602.03792)

#### MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs (MalURLBench) (2026-01)

隔离出一个范围很窄但后果严重的失效环节：接受一个伪装过的恶意 URL 就会让 agent 进入不安全 网页，此后所有下游行为都继承了这次沦陷，而此前没有基准针对这一步。MalURLBench 提供 61845 个攻击实例，覆盖 10 类真实场景与 7 类真实恶意网站。在 12 个主流 LLM 上的实验显示，模型 难以识别精心伪装的恶意 URL。论文进一步分析影响攻击成功率的关键因素，并给出轻量防御模块 URLGuard，作用在同一咽喉点上。

`环境: Web` ｜ [arXiv:2601.18113](https://arxiv.org/abs/2601.18113)

#### When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent (AgentBait) (2026-01)

指出以往研究集中在提示注入、后门这类模型层威胁，而针对 web 自动化 agent 的社会工程攻击一直 无人探索——尽管 Browser Use、Skyvern-AI 等开源框架已显著扩大了攻击面。AgentBait 攻击范式 利用执行层面的内在弱点：诱导性上下文会扭曲 agent 的推理，把它引向与原任务不一致的目标， 而全程不需要注入任何指令。防御侧提出 SUPERVISOR，一个轻量可插拔的运行时模块，强制网页 上下文与预期目标之间的「环境—意图一致性」对齐。

`环境: Web` ｜ [arXiv:2601.07263](https://arxiv.org/abs/2601.07263)

#### DECEPTICON: How Dark Patterns Manipulate Web Agents (DECEPTICON) (2025-12)

把暗黑模式（dark patterns，即真实网络上早已泛滥的欺骗性 UI 设计）作为一类 agent 安全威胁 来研究——它不需要攻击者搭建任何基础设施，因为恶意界面本身就是现状。DECEPTICON 在 700 个 网页导航任务（600 合成 + 100 真实）中隔离测试单个暗黑模式。结果是暗黑模式在超过 70% 的 任务中成功把 agent 引向恶意结果，而人类平均只有 31%。最值得警惕的发现颠覆了通常的 scaling 直觉：操纵有效性与模型规模、测试时推理量**正相关**——越大越强的 agent 反而更易受骗。

`环境: Web` ｜ [arXiv:2512.22894](https://arxiv.org/abs/2512.22894)

#### ceLLMate: Sandboxing Browser AI Agents (ceLLMate) (2025-12)

不试图检测每一条恶意指令，而是通过限制 agent 的环境权限来压缩爆炸半径。核心洞察针对作者 所称的「语义鸿沟」：在点击、按键这类低层 UI 原语上编写和强制安全策略既脆弱又易错，因此 ceLLMate 选择在 HTTP 层做沙箱——依据是任何产生副作用的 UI 操作最终都会向网站后端发出 网络请求。这使策略面同时具备稳定性与语义可读性，实现形态是与 agent 无关的浏览器扩展。

`环境: Web` ｜ [arXiv:2512.12594](https://arxiv.org/abs/2512.12594)

#### Attention is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs (Rennervate) (2025-12)

走机制路线做注入防御——读取注意力特征而非对文本做分类：Rennervate 在 **token 级**粒度检出 隐蔽注入，从而实现精确净化，在中和注入的同时保留 LLM 其余功能完整。这与页面级或片段级防御 形成对比，后者必须把干净内容与被污染片段一起丢弃。token 级检测器采用两步注意力池化机制， 聚合注意力头与响应 token。工作同时发布细粒度 IPI 数据集 FIPI，并报告优于 15 种商业与学术 防御方法。

`环境: Web` ｜ [arXiv:2512.08417](https://arxiv.org/abs/2512.08417)

#### Privacy Practices of Browser Agents (Privacy Practices of Browser Agents) (2025-12)

少数评测**已上市浏览器 agent 产品**而非研究原型的工作之一，覆盖八款近期流行 agent。其紧迫性 论证是结构性的：让这些工具强大的自动化能力，同时使它们成为高风险的失效点；而它们所执行的 任务类型与被托付的信息类型，意味着任何漏洞都会直接转化为大规模隐私危害。评测框架含五大因子 共 15 项具体测量——组件自身漏洞、对网站行为的防护、跨站追踪阻断、对影响隐私的 prompt 的 响应方式、以及工具自身的日志记录行为。

`环境: Web` ｜ [arXiv:2512.07725](https://arxiv.org/abs/2512.07725)

#### BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents (BrowseSafe) (2025-11)

指出把 agent 集成进浏览器所带来的安全问题已超出传统 Web 应用威胁模型，而尽管提示注入是 已知攻击向量，其真实世界影响仍缺乏充分测量。该基准的贡献在于设计取向：强调那些能影响真实 **动作**（而非仅文本输出）的注入，并构造在复杂度与干扰项密度上贴近实际部署 agent 所遭遇 情形的载荷。在此基础上横向评测现有防御在多个前沿模型上的表现，并提出结合架构级与模型级 防御的多层策略。

`环境: Web` ｜ [arXiv:2511.20597](https://arxiv.org/abs/2511.20597)

#### Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming (Genesis) (2025-10)

论证依赖人工编写策略或离线训练的静态模型的红队方法，无法捕捉 web agent 的底层行为模式， 因而难以跨环境泛化——这个场景下的成功要求攻击策略被持续发现和演化。Genesis 是三模块 agentic 框架：Attacker 用遗传算法在混合策略表示上生成对抗注入，Scorer 评估目标 agent 的响应并提供 反馈，Strategist 从交互日志中挖掘有效策略并编纂进可复用的策略库。

`环境: Web` ｜ [arXiv:2510.18314](https://arxiv.org/abs/2510.18314)

#### WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents (WAInjectBench) (2025-10)

填补一个系统性空缺：针对 web agent 的注入攻击很多，通用注入检测方法也很多，但从未有人 在 web agent 场景下系统评测过后者。WAInjectBench 先按威胁模型对攻击做细粒度分类，再构建 覆盖两种模态、两种极性的数据集——来自不同攻击的恶意文本片段、四类正常文本、攻击生成的 恶意图像、两类正常图像。核心结论划出了一条清晰边界：检测器能应对带显式文本指令或可见图像 扰动的攻击，一旦越出这个范围性能急剧下降。

`环境: Web` ｜ [arXiv:2510.01354](https://arxiv.org/abs/2510.01354)

#### HarmonyGuard: Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization (HarmonyGuard) (2025-08)

把核心矛盾表述为在长动作序列中平衡任务性能与不断演化的网页隐藏威胁，并指出以往工作局限于 单目标优化或单轮场景。HarmonyGuard 是多 agent 框架，其中 Policy Agent 能从非结构化的 外部文档中自动抽取并维护结构化安全策略、持续更新，回应的是「手写策略会过期」这一现实 问题。双目标优化同时兼顾安全与效用，而非牺牲其一换取其二。

`环境: Web` ｜ [arXiv:2508.04010](https://arxiv.org/abs/2508.04010)

#### WebGuard: Building a Generalizable Guardrail for Web Agents (WebGuard) (2025-07)

主张 web agent 需要类似人类用户的访问控制机制，并发布首个支持 agent 动作风险评估的数据集： 来自 22 个领域、193 个网站（含常被忽视的长尾站点）的 4939 条人工标注状态改变动作，按 SAFE / LOW / HIGH 三级风险标注，并划分好训练测试集以支持泛化研究。核心结论相当刺眼—— 即便前沿 LLM 预测动作后果的准确率也不足 60%。

`环境: Web` ｜ [arXiv:2507.14293](https://arxiv.org/abs/2507.14293)

#### LaSM: Layer-wise Scaling Mechanism for Defending Pop-up Attack on GUI Agents (LaSM) (2025-07)

指出针对弹窗式环境注入的现有防御要么需要昂贵重训、要么在归纳性干扰下失效，转而走机制 可解释性路线。论文系统研究这类攻击如何改变 GUI agent 的注意力分布，发现正确输出与错误输出 之间存在**逐层的注意力发散模式**。LaSM 直接利用这一发现，选择性放大关键层的注意力与 MLP 模块，无需任何额外训练即把模型显著性重新对齐到任务相关的屏幕区域——这是把可解释性结论 转化为可部署 GUI agent 防御的少见案例。

`环境: Desktop, Web` ｜ [arXiv:2507.10610](https://arxiv.org/abs/2507.10610)

#### A Systematization of Security Vulnerabilities in Computer Use Agents (CUA Vuln SoK) (2025-07)

对真实 CUA 做系统化威胁分析与对抗测试，归纳出七类该范式独有的风险，并深入剖析三个具体 利用链：用视觉覆盖层误导界面级推理的 clickjacking、经工具链串联实现远程代码执行的间接提示 注入、以及通过操纵隐式界面语境劫持多步推理的 CoT 暴露攻击。三个案例共同指向当前实现的 三处架构性缺陷：缺少输入来源追踪、界面与动作绑定薄弱、控制流完整性不足。

`环境: Desktop, Web` ｜ [arXiv:2507.05445](https://arxiv.org/abs/2507.05445)

#### AdInject: Real-World Black-Box Attacks on Web Agents via Advertising Delivery (AdInject) (2025-05)

批评已有环境注入研究依赖不现实的假设——直接改 HTML、已知用户意图、或能访问模型参数。 AdInject 改用互联网广告投放这一真实渠道注入恶意内容，威胁模型严格得多：agent 为黑盒、 恶意内容静态不可变、且不掌握用户意图。方法上结合诱导 agent 点击的广告内容设计，以及 基于 VLM 从目标站点反推用户潜在意图的内容优化，是该方向最贴近真实部署的威胁模型之一。

`环境: Web` ｜ [arXiv:2505.21499](https://arxiv.org/abs/2505.21499)
