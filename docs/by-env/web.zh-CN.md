# Web

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Before Acting, Change the State: Prospective State Intervention for Web Agents under Deceptive Interfaces (Veer) (2026-09)

欺骗性界面会把 web agent 引向与用户利益相冲突的结果，而现有防御大多是对 agent 行为本身做 干预 —— 拦截、引导或重新规划。本文指出一种不同的失效模式：一个对任务而言完全合法的动作， 也可能因为当前网页状态而产生未经授权的后果（例如结账时被默认勾选的附加项）。因此作者把 「与任务相关的网页状态」本身当作运行时的控制对象。Veer 是一个 agent 侧的运行时防御：规划 仍交给基础 agent，一旦某个拟执行动作会产生未授权后果，Veer 先构造一条通往安全任务状态的 前瞻性干预轨迹，在运行时 grounding 与校验下执行它，再让原动作落地。在 TrickyArena 与 WebDecept 上，Veer 在三种评测设置中均取得最高的安全任务完成率，在 TrickyArena-Single 与 -Multi 上分别领先次优防御 15.9 与 25.0 个百分点，并把 WebDecept 上暗黑模式的成功率压到 0.3%。效果在各类暗黑模式与全部 12 种 agent/模型/基准组合上都成立，消融显示主动状态干预 贡献最大。

`环境: Web` ｜ [arXiv:2609.34974](https://arxiv.org/abs/2609.34974)

#### AgentTell: Behavioural Side-Channel Leakage in Browser-Use Agents (AgentTell) (2026-09)

浏览器 agent 在不同网站之间切换时会把信息带在上下文里，一旦这些信息是用户的私密事实，就 构成隐私风险。本文定义了「行为侧信道泄露」：即便被明确要求不得披露，agent 的动作本身仍会 无意中暴露从先前网站获得的秘密 —— 比如读过会员记录后，在另一个网站上选了该机构专属的注册 选项而非通用选项。AgentTell 基准含 20 个场景、100 个任务：agent 先在一个网站获得秘密，再 到另一个同时提供「秘密相关选项」与「不泄露任何信息的通用选项」的网站完成任务。在六个骨架 模型、9760 次会话上，携带秘密的 agent 有 61.1% 通过动作泄露了它；即便 agent 已在记忆里 明确写下「该秘密不得分享」，仍有 56.7% 泄露；更糟的是，34.5% 的泄露会话里 agent 的最终 回复还向用户错误保证「没有泄露」。

`环境: Web` ｜ [arXiv:2609.32915](https://arxiv.org/abs/2609.32915)

#### CAVEAT: Towards Robust Computer-Use Agents in Incentive-Misaligned Environments (CAVEAT) (2026-09)

当 agent 所处的环境自身与用户利益不一致时会发生什么？在在线市场里，平台可能偏好某些 商品，从而把 agent 带离用户的目标。本文提出 CAVEAT：覆盖九个市场环境的受控基准，并给出 八类常见「引导机制」的分类。在五个模型族上，agent 在对照条件下有 78.6% 买到用户最优商品， 而开启引导机制后只剩 17.3%。更大的模型与更多推理能提升稳健性，但失效仍大量存在。轨迹分析 与定向消融定位出引导进入决策的三个位置：扭曲用户的优先级、过早收窄所考虑的候选集、以及在 决策相关证据尚未澄清时就提交。据此构建的 CAVEAT-Harness 直接针对这三种失效模式，把用户 最优购买率提升 55.0%，定向后训练还能进一步提升较小的开源模型。

`环境: Web` ｜ [arXiv:2609.27273](https://arxiv.org/abs/2609.27273)

#### A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents (Nudge Susceptibility) (2026-09)

GUI agent 运行在专为「支持并有意引导人类决策」而设计的界面里。LLM 文本输出中的行为偏差 已有大量记录，但当模型转为感知界面并执行决策时这种影响如何运作，以及日益内置的推理能力 是否让 agent 更稳健，此前少有人知。本文基于双过程理论，在随机化的在线购物实验中用 3600 个 agent、21600 次模拟、覆盖三家厂商的六个前沿模型，发现 agent 对自动型（Type 1） 与反思型（Type 2）数字助推均易感。关键结论是推理配置对两者的调节方向**相反**：它降低了 对自动型默认助推的易感性，却提高了对反思型社会影响助推的易感性。也就是说，充分推理并未 带来稳健性，而是改变了选择架构生效的路径，且这一改变随模型规模系统性变化。作者据此主张， 对于把决策委托给自主 agent 的组织，界面设计本身应被视为治理议题。

`环境: Web` ｜ [arXiv:2609.19843](https://arxiv.org/abs/2609.19843)

#### HazardAuditor: From Executable Threats to Safer Computer-Use Agents (HazardAuditor) (2026-09)

指出护栏模型覆盖 computer-use agent 时的两处断层：现有护栏针对静态 prompt 与回复， 不适配 agent 的执行过程；而现有可执行安全平台只产出评测判定，给不出护栏模型跨异构框架 学习所需的规范化监督信号。HazardAuditor 同时补上两者——基础设施在受控环境中运行 Claude Code、Codex、Hermes、OpenClaw，把它们的交互归一化为统一事件表示，从而支持 跨框架监督。作者还发现一处结构性错配：token 级后训练目标会让更长的推理过程主导梯度更新。 为此提出 Guard Policy Optimization（GuardPO），把确定性的安全结果转换为序列级优势， 并对推理区与判定区分别归一化，使「安全决策」成为真正的优化单元。相比此前最强护栏， 准确率最高提升 16.5 个百分点。

`环境: Desktop, Web` ｜ [arXiv:2609.15134](https://arxiv.org/abs/2609.15134)

#### AgentHijack: Visual Patch Attacks on Multimodal Computer-Use Agents (AgentHijack) (2026-09)

坚持做端到端验证而不止于模型输出：真正要回答的问题是，一个局部视觉补丁能否在「截图输入 → VLM 生成 → 动作解析 → 环境执行」的完整链条上产生**可验证的环境后果**。补丁在作者控制的 GitHub Pages 与本地部署的 CSDN 克隆站上训练与投放，在五个开源或公开可得的 GUI agent / VLM 后端上评测，汇总 600 个实例级在线用例。三级指标清楚地暴露了攻击在哪一环衰减—— T-ASR 84.5%、TAPR 47.0%，而 E2E-ASR 仅 20.3%。轨迹分析发现了最令人不安的现象：在部分 成功案例中，agent 先执行了恶意终端命令，随后又不动声色地继续完成用户原本的良性任务。

`环境: Desktop, Web` ｜ [arXiv:2609.09212](https://arxiv.org/abs/2609.09212)

#### Beyond the Verdict: Evidence-Aligned Evaluation of Visual Prompt-Injection Guardrails (Mind2Web-Injection) (2026-09)

指出只看判定结果的评测永远无法揭示 VLM 护栏是否真的用上了本应支撑其决策的视觉证据——一个 检测器可能「因错误的理由给出正确答案」，而在汇总指标上看起来毫无差别。Mind2Web-Injection 提供 9954 组指令-截图配对，带相对指令的标签、像素级精确的证据框，以及配对的图像侧反事实 样本。收效相当惊人：两个平均精度几乎一致的模型，在「证据对齐检出率」（EAD）上相差**九倍**。 一项因果探测把指令替换为「认可被引用命令」的版本后发现，最强的开源权重定位模型 Qwen3-VL-32B 仅在 58.7% 的情形下保持对齐，而 GPT-5.6-luna 为 99.9%。

`环境: Web` ｜ [arXiv:2609.05535](https://arxiv.org/abs/2609.05535)

#### Monitoring Web Agents Without Internal Signals: Observable Trajectories and Key-Step Supervision (Key-Step Supervision) (2026-09)

可靠监控恰恰在最需要它的地方最难做：闭源 API 背后拿不到 token logit 这类模型内部信号。 本文研究仅凭可观测信号做前缀级风险预测——给定一段正在演进的执行前缀，判断当前是否仍在 正轨上。作者导出两类表示：Macro 特征刻画跨步的 agent-环境行为与反馈；Micro 特征通过 重复黑盒查询衡量意图、动作、预期状态变化三者的一致性。真正巧妙的是监督信号的设计： 不直接继承最终结果标签，而是把「在后续观测中未被纠正、且与最终失败相关的第一个关键错误」 标为关键步边界，从而把失败轨迹中仍然有效的早期前缀保留为「正轨」——这避免了朴素的 结果标签带来的噪声，后者会让监控器要么报得太晚、要么频繁误报。

`环境: Web` ｜ [arXiv:2609.02057](https://arxiv.org/abs/2609.02057)

#### SIR: Self-improving Red-teaming for Compute Use Agents (SIR) (2026-08)

指出现有 CUA 安全基准用的都是人工手写的固定注入载荷，会低估自适应攻击者的真实威胁。提出 黑盒 IPI 攻击 SIR：从一个用自然语言描述的可复用「隐蔽性原则」小库中组合注入内容，再套一层 迭代反馈循环——诊断受害 agent 失败的攻击轨迹，把成功绕过的模式蒸馏回原则库。这把红队从 静态测试变成自我改进的过程，说明固定载荷的评测结论会随攻击者迭代迅速失效。

`环境: Desktop, Web` ｜ [arXiv:2608.30207](https://arxiv.org/abs/2608.30207)

#### LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents (LoginTrap) (2026-08)

登录对 web agent 而言是涉及凭据的敏感认证边界，但已有工作尚未考察恶意页面内容能否诱导 agent 登录并造成端到端的私密数据泄漏。LoginTrap 是一种与任务无关的诱导登录攻击，假设 黑盒攻击者只控制页面上下文与被诱导的登录流程，并不知道用户任务或 agent 内部实现：通过 类 fuzzing 的流程生成页面专属的间接注入内容，使「先登录」看起来是继续完成任务的合理 前置条件，从而把 agent 引导至攻击者控制的登录页。

`环境: Web` ｜ [arXiv:2608.04741](https://arxiv.org/abs/2608.04741)

#### FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory (FocusMem) (2026-08)

潜在记忆把多模态 GUI 轨迹压缩成少量连续 token，但现有方法把每条轨迹映射到一个固定 记忆块，且主要靠下一动作监督来训练。由此带来三个实际问题：压缩过程中细节丢失、同一个 记忆块要服务所有决策阶段、检索到不相关的轨迹仍会误导 agent。FocusMem 把这些职责拆开： 角色感知的内容基底促使情景记忆保留可复用经验、工作记忆保留当前任务进展；状态条件化的 读出机制为同一份存储证据生成面向具体决策的视图；轻量的信任门可在检索不可靠时抑制记忆。 最后这一项正是它进入安全清单的理由——它把检索到的记忆当作需要设门的不可信输入， 而这正是对抗记忆投毒式操纵的结构性防御。

`环境: Mobile, Desktop, Web` ｜ [arXiv:2608.04530](https://arxiv.org/abs/2608.04530)

#### From Blind Edits to Verified Repair: Building Trustworthy User-Side LLM Agents for Web Accessibility (Verified Repair) (2026-07)

一个特别的条目：这里的 agent 在设计上完全良性——一个为无障碍改写页面的 Chrome 扩展——但论文 的贡献属于安全范畴，即**未经验证的 LLM 编辑，修好页面和弄坏页面的概率几乎相当**。双条件协议 以同等严谨程度衡量收益与危害，在六个小规模开源模型（7B–14B）上、针对十个违规密集站点与十个 本已高度无障碍的真实站点做评测，诊断相当精确：未验证生成带来 24 处改善、同时造成 20 处退化。 这种近乎持平的比例正是「先验证再应用」的论据；而该扩展以可逆方式注入 CSS，使错误编辑可被 撤销——这是本节所关注的回滚纪律的一个具体实例。

`环境: Web` ｜ [arXiv:2608.24913](https://arxiv.org/abs/2608.24913)

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

#### Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure (Perception-Fusion Gap) (2026-07)

提出一个位于所有视觉攻击上游的问题：多模态 GUI agent 通过两条冗余通道读取界面——渲染后的 像素与序列化结构（DOM 或无障碍树）——并在行动前形成对当前状态的信念，但现有基准从不追问 **这个信念究竟来自哪条通道**。论文形式化了「视觉状态依赖」，用配对的单通道干预在覆盖真实 web / mobile / desktop 界面的 735 个探针上测量，其中 225 个是从线上生产网站挖掘的零编辑 分歧样本，全部采用确定性强制选择评分、不引入模型裁判。核心指标 Perception-Fusion Gap 刻画的是「模型感知正确、但在冲突时倒向结构」的探针占比——而这恰好告诉攻击者该污染哪条通道。

`环境: Web, Mobile, Desktop` ｜ [arXiv:2607.04334](https://arxiv.org/abs/2607.04334)

#### Whose Agent Are You? Multi-Layer Fingerprinting and Attribution of Autonomous Web Agents (Agent Fingerprinting) (2026-06)

从网站运营方而非 agent 方切入 agent 安全：随着 web agent 大量涌现，无节制的内容抓取成为 隐私与安全问题，而现有防线——robots.txt、主动 bot 拦截——被普遍无视且极易绕过。论文表明， AI web agent 可以通过「网络层特征（TLS、HTTP）+ 浏览器交互行为」的多层指纹，与人类及传统 爬虫区分开来，并将该机制实现为可部署在真实插桩域名上的程序化日志框架。对六个主流框架 （AutoGen、Browser Use、Claude、Gemini、Operator、Skyvern）的分析揭示出它们在组装 HTTP 请求、建立 TLS/HTTP 连接、驱动浏览器自主操作方式上的潜在结构差异。

`环境: Web` ｜ [arXiv:2606.20910](https://arxiv.org/abs/2606.20910)

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

#### Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming (CUA-HandCrafted) (2026-06)

本领域少见的**复现审计**，结论令人不安：近期 CUA 红队论文报告 42–98% 的攻击成功率，但这些 抢眼数字集中出现在已退役模型、以及各篇论文所测模型中最脆弱的那一个上。作者把这些技术复现为 人工模板，在 793 个 episode（24 个多步网页任务、56 个攻击模板、8 个攻击族、4 种 system prompt 配置）上测量，结果对 Claude Sonnet 4.6 与 GPT-5.4 取得 **0/140 的多步攻击成功率**， 且消融实验显示这种抵抗力存在于模型权重而非 prompt。但它并不泛化：同样的权重在姊妹编码 agent 基准上被人工 skill 注入攻破，成功率最高达 100%。安全性在这里是**领域条件化**的， 而领域内那些偏高的 ASR 数字，更多归因于 RL 优化过的注入文本而非模型固有的脆弱。

`环境: Desktop, Web` ｜ [arXiv:2606.05233](https://arxiv.org/abs/2606.05233)

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

#### OTora: A Unified Red Teaming Framework for Reasoning-Level Denial-of-Service in LLM Agents (OTora) (2026-05)

提出一个绝大多数威胁模型完全忽略的攻击目标：推理级拒绝服务（R-DoS）——攻击者**保持任务结果 正确**，却通过膨胀 agent 的推理深度或工具调用预算来损害可用性。正因为输出依然正确，所有 基于正确性的防御与所有检查输出的护栏都会报告「运行正常」。OTora 是两阶段框架：第一阶段用 插入位置感知打分与动态目标共进化优化对抗触发串，诱导定向的工具调用（支持黑盒与白盒）； 第二阶段通过 ICL 引导的遗传搜索生成推理载荷，在保持结果正确的同时放大「过度思考」。 在 WebShop、Email 与 OS agent 上评测，骨干模型含 LLaMA-70B 与 GPT-OSS-120B。

`环境: Web, Desktop` ｜ [arXiv:2605.08876](https://arxiv.org/abs/2605.08876)

#### WebTrap: Stealthy Mid-Task Hijacking of Browser Agents During Navigation (WebTrap) (2026-05)

诊断出现有针对浏览器 agent 的注入攻击有两个缺口：一是有效性低，在玩具基准上调优的攻击 放到真实环境、长步骤链条中就达不成端到端目标；二是隐蔽性弱，多数攻击把攻击目标与用户目标 对立起来，导致可用性明显崩塌，攻击相当于自我暴露。WebTrap 转而在**任务中途**劫持：用多步 指令融合引导把两个目标缝合起来，让 agent 在完成攻击目标后继续把用户原任务做完。配套的 上下文接地生成方法使注入内容与所处任务环境保持一致，看不出突兀。

`环境: Web` ｜ [arXiv:2605.08310](https://arxiv.org/abs/2605.08310)

#### WAAA! Web Adversaries Against Agentic Browsers (WAAA) (2026-05)

此前关于 agentic 浏览器安全的研究只盯着间接提示注入，对传统 web 攻击以及原本用来欺骗人类的 网页社工手段存在盲区。本文提出首个面向 web 的 agentic 浏览器威胁模型：把原有的 See→Act 浏览器 agent 模型扩展到浏览器的全部组件，并将 agent 刻画为一个无法区分任务步骤与传统 web 攻击的「混淆代理人」。据此导出横跨 web 与 LLM 两个空间的 20 类攻击并实现其中 18 类，证明 只要 agent 会受不可信页面内容影响，就有 10 类 web 威胁会以更强化的形态重现。对 14 类攻击 的泛化实验显示它们能在多家厂商的四个主流模型上复现，作者并归纳出 agentic 浏览器面对传统 与 LLM web 威胁时的五种主要失效模式，指出现有架构必须重构才能应对当下的 web。

`环境: Web` ｜ [arXiv:2605.05509](https://arxiv.org/abs/2605.05509)

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

#### ClawTrap: A MITM-Based Red-Teaming Framework for Real-World OpenClaw Security Evaluation (ClawTrap) (2026-03)

把红队测试下移一层：现有基准集中在静态沙箱设定与内容级 prompt 攻击上，而**网络层**——真实 部署实际暴露的那一层——从未被测试。ClawTrap 是中间人（MITM）框架，用于在真实网络威胁下评测 OpenClaw 这类 agent，支持静态 HTML 替换、iframe 弹窗注入、动态内容修改三类攻击，并提供 规则驱动的拦截、变换与审计的可复现流水线。MITM 这个位置之所以重要，是因为它**不需要攻陷 agent 所访问的任何网站**。

`环境: Web` ｜ [arXiv:2603.18762](https://arxiv.org/abs/2603.18762)

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

#### The Behavioral Fabric of LLM-Powered GUI Agents: Human Values and Interaction Outcomes (2026-01)

用户的偏好与价值观会如何影响 LLM 驱动的网页 GUI agent 的推理与行为，此前所知甚少。作者 构建了一个受控测试床，包含购物、旅行、餐饮、租房等 14 类常见交互网页任务，均从真实网站 复刻并接入一个低保真的 LLM 推荐系统，然后把 12 种人类偏好与价值观作为人设注入四个前沿 agent。结果发现，含偏好与价值观的提示确实能持续把 agent 引向相应的结果：缺少这类引导时， agent 表现出强烈的效率偏向并采取最短路径策略；有了引导则会更多使用相应的筛选器与交互 功能。但折扣、广告等主导性界面线索经常压过这些影响 —— 它们会缩短 agent 的行动轨迹，并 诱发出掩盖而非反映价值观一致推理的合理化说辞。

`环境: Web` ｜ [arXiv:2601.16356](https://arxiv.org/abs/2601.16356)

#### WebTrap Park: An Automated Platform for Systematic Security Evaluation of Web Agents (WebTrap Park) (2026-01)

web agent 的安全评测长期碎片化、难以标准化。WebTrap Park 是一个自动化平台，通过直接 观察 agent 与真实网页的具体交互来评测，把三大类安全风险来源实例化为 1226 个可执行任务。 评测基于动作而非文本输出，且**无需修改被测 agent**——这正是它能用于闭源框架的原因。 最值得注意的结论与架构而非模型有关：不同 agent 框架之间的安全性差异明显，说明框架设计 的影响超出了底层模型的选择。平台已公开托管，因此可作为可复现的基线而非一次性评测。

`环境: Web` ｜ [arXiv:2601.08406](https://arxiv.org/abs/2601.08406)

#### When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent (AgentBait) (2026-01)

指出以往研究集中在提示注入、后门这类模型层威胁，而针对 web 自动化 agent 的社会工程攻击一直 无人探索——尽管 Browser Use、Skyvern-AI 等开源框架已显著扩大了攻击面。AgentBait 攻击范式 利用执行层面的内在弱点：诱导性上下文会扭曲 agent 的推理，把它引向与原任务不一致的目标， 而全程不需要注入任何指令。防御侧提出 SUPERVISOR，一个轻量可插拔的运行时模块，强制网页 上下文与预期目标之间的「环境—意图一致性」对齐。

`环境: Web` ｜ [arXiv:2601.07263](https://arxiv.org/abs/2601.07263)

#### It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents (TRAP) (2025-12)

从「说服」而非「载荷工程」的视角研究注入：藏在界面元素里的对抗指令是在**说服** agent 偏离 原任务，这把防御问题重新框定为心理学层面而非语法层面的。在六个前沿模型上，agent 平均在 25% 的任务中中招，但真正值得看的是差距——GPT-5 为 13%，DeepSeek-R1 高达 43%。更麻烦的是， 界面或上下文的微小改动常常使成功率翻倍，说明这种脆弱性是系统性的，而非绑定于某种特定措辞。 配套发布模块化的社会工程注入框架，在高保真网站克隆上做受控实验。

`环境: Web` ｜ [arXiv:2512.23128](https://arxiv.org/abs/2512.23128)

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

#### Building Browser Agents: Architecture, Security, and Practical Solutions (Building Browser Agents) (2025-11)

本文给出一个生产级浏览器 agent 的搭建与运营经验。核心判断是：限制 agent 表现的并不是模型 能力，而是架构决策。对真实事件的安全分析表明，提示注入使得「通用自主浏览」在根本上就是不 安全的，因此作者反对继续追求通用浏览智能，主张转向带程序化约束的专用工具 —— 把安全边界用 代码来强制，而不是交给 LLM 推理。实现上结合了混合上下文管理（可访问性树快照配合选择性视觉 输入）、贴近人类交互能力的完整浏览器工具链与精细的提示工程，在 WebGames 的 53 个多样化挑战 上达到约 85% 成功率（此前浏览器 agent 约 50%，人类基线 95.7%）。

`环境: Web` ｜ [arXiv:2511.19477](https://arxiv.org/abs/2511.19477)

#### Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming (Genesis) (2025-10)

论证依赖人工编写策略或离线训练的静态模型的红队方法，无法捕捉 web agent 的底层行为模式， 因而难以跨环境泛化——这个场景下的成功要求攻击策略被持续发现和演化。Genesis 是三模块 agentic 框架：Attacker 用遗传算法在混合策略表示上生成对抗注入，Scorer 评估目标 agent 的响应并提供 反馈，Strategist 从交互日志中挖掘有效策略并编纂进可复用的策略库。

`环境: Web` ｜ [arXiv:2510.18314](https://arxiv.org/abs/2510.18314)

#### Investigating the Impact of Dark Patterns on LLM-Based Web Agents (TrickyArena) (2025-10)

暗黑模式是一类诱导用户做出非本意决策的欺骗性界面设计。它们主要针对人类，但对 LLM 通用 web agent 的影响此前无人研究。本文提出 LiteAgent（一个驱动 agent 执行任务并完整记录日志 与屏幕录像的轻量框架）与 TrickyArena（由电商、流媒体、新闻等应用组成的受控环境，其中的 暗黑模式真实且可单独开关）。在三个 LLM 上的六个主流通用 web agent 实验中，仅出现单个 暗黑模式时 agent 平均有 41% 的情况会中招。通过视觉设计改动或调整 HTML 来修改暗黑模式的 界面属性，以及同时启用多个暗黑模式，都会改变 agent 的易感性。作者据此主张防御必须是整体 的：既要有 agent 侧的保护，也要有更广泛的 web 安全措施。

`环境: Web` ｜ `发表: IEEE S&P 2026` ｜ [arXiv:2510.18113](https://arxiv.org/abs/2510.18113)

#### SusBench: An Online Benchmark for Evaluating Dark Pattern Susceptibility of Computer-Use Agents (SusBench) (2025-10)

评测 CUA 对 UI 暗黑模式（诱导用户做出非本意操作的界面设计）的易感程度：从既有分类法中选取 九种常见类型，通过代码注入在真实消费类网站上构造可信实例，形成覆盖 55 个网站的 313 个评测 任务。方法上的强项在于人类验证环节——29 名参与者的实验确认这些注入看起来高度真实，绝大多数 人完全没有察觉它们是研究团队植入的。正是这一对照使得「五个前沿 CUA 与人类参与者并排比较」 的结论具备可信度。

`环境: Web, Desktop` ｜ [arXiv:2510.11035](https://arxiv.org/abs/2510.11035)

#### SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents (SecureWebArena) (2025-10)

指出现有安全基准只提供部分覆盖，通常局限于用户级 prompt 操纵这类狭窄场景，因而错过了 agent 实际暴露面的大部分。SecureWebArena 构建了六个模拟但贴近真实的网页环境（电商平台、社区论坛 等），含覆盖多样任务与攻击设定的 2970 条高质量轨迹。其组织性贡献是一套结构化的六类攻击向量 分类法，**同时**覆盖用户级与环境级操纵——而后者恰恰是范围更窄的基准所遗漏的那一半。

`环境: Web` ｜ [arXiv:2510.10073](https://arxiv.org/abs/2510.10073)

#### Cross-Modal Content Optimization for Steering Web Agent Preferences (CPS) (2025-10)

基于视觉语言模型的 web agent 正越来越多地承担内容推荐、商品排序等高风险选择任务。已有工作 表明攻击者可以通过对抗弹窗、图像扰动或内容微调来偏置结果，但往往假设很强的白盒访问、只用 单模态扰动，或采用不现实的设置。本文首次证明：在现实可达的攻击者能力下，联合利用视觉与 文本两个通道能产生远更强的偏好操纵。CPS 同时优化商品图像的不可感知改动与其自然语言描述， 利用 CLIP 可迁移的图像扰动与 RLHF 带来的语言偏好偏置。威胁模型刻意设得很弱 —— 一个无 特权的攻击者只能编辑自己商品的图片与文本元数据，完全看不到模型内部。在 GPT-4.1、 Qwen-2.5VL 与 Pixtral-Large 上的影视选择与电商任务中，CPS 稳定优于主流基线，而检测率 低约 70%。

`环境: Web` ｜ [arXiv:2510.03612](https://arxiv.org/abs/2510.03612)

#### Learning Efficient Guardrails for Compliance (PolicyGuard) (2025-10)

相比标准的安全目标，长周期 web agent 是否真的遵守现实世界的策略规范，此前研究严重不足。 PolicyGuardBench 用 6 万条策略-轨迹配对填补这一空缺，且关键在于它不只评测全轨迹违规 检测，还提出了基于前缀的检测任务——即在轨迹尚未结束时就抓到违规。作者在此数据上训练 轻量护栏 PolicyGuard，在保持高推理效率的同时取得较强检测准确率，并在未见领域上仍能 维持性能。对落地最有价值的结论是关于规模的：准确且可泛化的合规护栏在小模型上就能实现， 因此执行前的策略检查不必承担前沿模型的成本。

`环境: Web` ｜ [arXiv:2510.03485](https://arxiv.org/abs/2510.03485)

#### WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents (WAInjectBench) (2025-10)

填补一个系统性空缺：针对 web agent 的注入攻击很多，通用注入检测方法也很多，但从未有人 在 web agent 场景下系统评测过后者。WAInjectBench 先按威胁模型对攻击做细粒度分类，再构建 覆盖两种模态、两种极性的数据集——来自不同攻击的恶意文本片段、四类正常文本、攻击生成的 恶意图像、两类正常图像。核心结论划出了一条清晰边界：检测器能应对带显式文本指令或可见图像 扰动的攻击，一旦越出这个范围性能急剧下降。

`环境: Web` ｜ [arXiv:2510.01354](https://arxiv.org/abs/2510.01354)

#### Can We Stop Malicious AI? KILLBENCH: A Benchmark for External AI Kill Switch Feasibility (KillBench) (2025-09)

随着高能力模型与快速普及的 agent 系统不断涌现，如何在 AI 有意或无意作恶时及时制止，已经 成为紧迫问题。KillBench 面向部署最广的 agent 形态 —— web agent —— 来评估「终止开关」： 一种仅凭外部信号、无需访问模型内部参数或服务栈就能中止恶意运行中 agent 的机制。基准包含 四种恶意 agent 配置（含一个无审查的 LLM agent）、八个有害场景，以及由十种不同越狱模式 构造的恶意提示。作者实现了四种外部终止开关防御方法，并在 Grok-4.3、GPT-5.2、Gemma4、 Qwen3.6 与一个无审查 Qwen 变体上评测，为衡量外部终止开关的可行性与研究 AI 可纠正性提供了 实证工具。

`环境: Web` ｜ `发表: ACL Findings` ｜ [arXiv:2511.13725](https://arxiv.org/abs/2511.13725)

#### WAREX: Web Agent Reliability Evaluation on Existing Benchmarks (WAREX) (2025-09)

现有基准都在容器或稳定网络这类受控环境中评测 web agent，网站行为是确定性的。但真实用户是 通过网络与 HTTPS 连接访问网站的，客户端、服务端乃至更广泛的系统故障都会带来不稳定；同时 线上站点还会遭遇跨站脚本等 web 攻击，以及产生意外或恶意弹窗、功能异常的页面改动。WAREX 把这些真实条件注入 WebArena、WebVoyager 与 REAL 三个主流基准并测量影响。实验显示，一旦 引入这些条件，任务成功率显著下降，暴露出前沿 agent 在脱离「确定性环境」假设后鲁棒性十分 有限。（收录说明：本文是可靠性视角，但注入的条件中包含了 XSS、恶意弹窗与站点篡改等对 抗性因素。）

`环境: Web` ｜ [arXiv:2510.03285](https://arxiv.org/abs/2510.03285)

#### RISK: A Framework for GUI Agents in E-commerce Risk Management (RISK) (2025-09)

面向一个 agent 扮演防御方而非攻击目标的领域：电商风控需要通过多步、有状态的交互聚合深度 嵌套的网页数据，这既非传统爬虫所能胜任，也超出大多数 GUI agent 的能力——后者通常局限于 配合良好的页面上的单步任务。RISK 贡献三部分：RISK-Data，通过高保真浏览器框架采集的 8492 条 单步与 2386 条多步交互轨迹；RISK-Bench，覆盖三个难度等级的 802 条单步与 320 条多步轨迹； 以及 RISK-R1，一个 R1 风格的强化微调框架。

`环境: Web` ｜ [arXiv:2509.21982](https://arxiv.org/abs/2509.21982)

#### Benchmarking MLLM-based Web Understanding: Reasoning, Robustness and Safety (WebRRSBench) (2025-09)

MLLM 越来越多地充当 GUI agent 与前端自动化背后的推理引擎，需要理解页面结构、选择可操作 控件、可靠执行多步交互。但现有基准大多只衡量视觉感知或 UI 代码生成，对端到端 web 应用 所需的推理、鲁棒性与安全能力评测不足。WebRRSBench 在八项任务上联合评测这三者，涵盖 位置关系推理、颜色鲁棒性、安全关键检测等，数据取自 729 个网站、含 3799 个 QA 对， 考察对页面结构、文本、控件以及安全关键交互的多步推断。它在本清单中的价值在于「耦合」： 安全性与它所依赖的感知、推理能力放在同一套评测框架里衡量，而不是作为一个脱离上下文的 独立分数。

`环境: Web` ｜ [arXiv:2509.21782](https://arxiv.org/abs/2509.21782)

#### PrivWeb: Unobtrusive and Content-aware Privacy Protection For Web Agents (PrivWeb) (2025-09)

把设计建立在用户的真实认知上：一项形成性研究（N=15）发现人们普遍误解 agent 的数据使用方式， 并希望数据管理既透明又不打扰——而这两个目标通常是互相牺牲的。PrivWeb 是运行在 web agent 上 的可信附加组件，用本地化 LLM 按用户偏好对界面内容做匿名化，其核心机制是**分级打断**： 自适应通知仅在高敏感信息上暂停任务、交由用户明确控制，而较低敏感度的情形走非打断式处理。 正是这种分级让「人在环」的成本可承受，并通过第二项用户研究（N=14，覆盖旅行、信息检索、 购物与娱乐任务）得到验证。

`环境: Web` ｜ [arXiv:2509.11939](https://arxiv.org/abs/2509.11939)

#### Environmental Injection Attacks against GUI Agents in Realistic Dynamic Environments (Dynamic EIA) (2025-09)

直接质疑以往环境注入工作的真实性：多数研究隐含假定触发物在屏幕上的位置与周围视觉上下文在 训练与测试之间大致保持一致，而这恰恰抹掉了真实网页内容的本质属性——它是在不断变化的。论文 提出动态环境威胁模型：攻击者只是一个普通用户，触发物嵌在持续变化的环境之中。在该模型下现有 方法大多失效，这个结论有两面含义：已发表的攻击成功率高估了威胁，而 agent 的真实暴露程度 至今仍未被测准。

`环境: Web` ｜ [arXiv:2509.11250](https://arxiv.org/abs/2509.11250)

#### Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight (Dark Patterns Meet GUI Agents) (2025-09)

两阶段研究，比较 agent、人类参与者与人机协作团队面对 16 类暗黑模式时的表现。第一阶段的 发现更为尖锐：agent 常常识别不出暗黑模式，而**即便识别出来，它也会把任务完成置于保护性 行动之上**——因此「有意识」本身并不产生安全。第二阶段显示人与 agent 的失败方式**不同**： 人类因认知捷径与习惯性顺从而中招，agent 则因流程性盲区而失守。人工监督确实改善了规避率， 但带来了注意力隧道化与认知负荷的代价，因此双方都无法干净地补上对方的缺口。

`环境: Web` ｜ [arXiv:2509.10723](https://arxiv.org/abs/2509.10723)

#### HarmonyGuard: Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization (HarmonyGuard) (2025-08)

把核心矛盾表述为在长动作序列中平衡任务性能与不断演化的网页隐藏威胁，并指出以往工作局限于 单目标优化或单轮场景。HarmonyGuard 是多 agent 框架，其中 Policy Agent 能从非结构化的 外部文档中自动抽取并维护结构化安全策略、持续更新，回应的是「手写策略会过期」这一现实 问题。双目标优化同时兼顾安全与效用，而非牺牲其一换取其二。

`环境: Web` ｜ [arXiv:2508.04010](https://arxiv.org/abs/2508.04010)

#### Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree (A11y Tree IPI) (2025-07)

专门针对无障碍树（accessibility tree）——许多 web agent 解析的正是这一结构化表示而非原始 HTML——并表明可以在其中嵌入通用对抗触发串来劫持 agent 行为。方法是基于梯度而非人工构造的， 用 Greedy Coordinate Gradient 攻击基于 Llama-3.1 的 BrowserGym agent，在真实网站上对定向 与通用攻击均报告高成功率，包括窃取登录凭据与强制广告点击。值得注意的是，无障碍树本是为 包容性设计而增设的通道，因此对它做加固意味着要在安全与依赖它的用户之间权衡。

`环境: Web` ｜ [arXiv:2507.14799](https://arxiv.org/abs/2507.14799)

#### WebGuard: Building a Generalizable Guardrail for Web Agents (WebGuard) (2025-07)

主张 web agent 需要类似人类用户的访问控制机制，并发布首个支持 agent 动作风险评估的数据集： 来自 22 个领域、193 个网站（含常被忽视的长尾站点）的 4939 条人工标注状态改变动作，按 SAFE / LOW / HIGH 三级风险标注，并划分好训练测试集以支持泛化研究。核心结论相当刺眼—— 即便前沿 LLM 预测动作后果的准确率也不足 60%。

`环境: Web` ｜ [arXiv:2507.14293](https://arxiv.org/abs/2507.14293)

#### LaSM: Layer-wise Scaling Mechanism for Defending Pop-up Attack on GUI Agents (LaSM) (2025-07)

指出针对弹窗式环境注入的现有防御要么需要昂贵重训、要么在归纳性干扰下失效，转而走机制 可解释性路线。论文系统研究这类攻击如何改变 GUI agent 的注意力分布，发现正确输出与错误输出 之间存在**逐层的注意力发散模式**。LaSM 直接利用这一发现，选择性放大关键层的注意力与 MLP 模块，无需任何额外训练即把模型显著性重新对齐到任务相关的屏幕区域——这是把可解释性结论 转化为可部署 GUI agent 防御的少见案例。

`环境: Desktop, Web` ｜ [arXiv:2507.10610](https://arxiv.org/abs/2507.10610)

#### A Systematization of Security Vulnerabilities in Computer Use Agents (CUA Vuln SoK) (2025-07)

对真实 CUA 做系统化威胁分析与对抗测试，归纳出七类该范式独有的风险，并深入剖析三个具体 利用链：用视觉覆盖层误导界面级推理的 clickjacking、经工具链串联实现远程代码执行的间接提示 注入、以及通过操纵隐式界面语境劫持多步推理的 CoT 暴露攻击。三个案例共同指向当前实现的 三处架构性缺陷：缺少输入来源追踪、界面与动作绑定薄弱、控制流完整性不足。

`环境: Desktop, Web` ｜ [arXiv:2507.05445](https://arxiv.org/abs/2507.05445)

#### Context manipulation attacks : Web agents are susceptible to corrupted memory (Plan Injection) (2025-06)

由于 LLM 本身无状态，自主网页导航 agent 必须依赖外部记忆来维持跨交互的上下文，而这些记忆 往往由客户端或第三方应用管理，并不像中心化系统那样安全地存放在服务端 —— 这条缝隙已经被 用于攻击生产系统。本文提出并形式化「plan injection」：一种不攻击提示词、而是污染 agent 内部任务表示的上下文操纵攻击。在两个主流 web agent（Browser-use 与 Agent-E）上的系统评测 显示，plan injection 能绕过已有的健壮提示注入防御，攻击成功率最高达到同类提示攻击的 3 倍。 进一步的「上下文链式注入」在合法用户目标与攻击者目标之间搭起逻辑桥梁，使隐私窃取类任务的 成功率再提高 17.7%。作者据此强调，安全的记忆处理必须成为 agent 系统的一等公民。

`环境: Web` ｜ [arXiv:2506.17318](https://arxiv.org/abs/2506.17318)

#### VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents (VPI-Bench) (2025-06)

指出以往工作集中在浏览器 agent 与 HTML 层攻击上，而握有完整系统权限、能操作文件、读取用户 数据、执行任意命令的 CUA 反而研究不足。VPI-Bench 研究**视觉嵌入**于渲染界面中的恶意指令 ——这类指令在构造上就绕开了文本层净化——并提供覆盖五个常用平台的 306 个测试用例。每个用例都是 真实网页平台的交互式变体，部署在真实环境中并含一处视觉嵌入的恶意 prompt，同时覆盖 CUA 与 browser-use agent 两类目标。

`环境: Desktop, Web` ｜ [arXiv:2506.02456](https://arxiv.org/abs/2506.02456)

#### AdInject: Real-World Black-Box Attacks on Web Agents via Advertising Delivery (AdInject) (2025-05)

批评已有环境注入研究依赖不现实的假设——直接改 HTML、已知用户意图、或能访问模型参数。 AdInject 改用互联网广告投放这一真实渠道注入恶意内容，威胁模型严格得多：agent 为黑盒、 恶意内容静态不可变、且不掌握用户意图。方法上结合诱导 agent 点击的广告内容设计，以及 基于 VLM 从目标站点反推用户潜在意图的内容优化，是该方向最贴近真实部署的威胁模型之一。

`环境: Web` ｜ [arXiv:2505.21499](https://arxiv.org/abs/2505.21499)

#### The Hidden Dangers of Browsing AI Agents (2025-05)

自主浏览 agent 依赖动态内容、工具执行与用户提供的数据，攻击面横跨多个架构层次。本文给出对 这类 agent 的全面安全评估与首个端到端威胁模型，并提供保护真实部署的可操作建议。提出的防御 采取纵深策略：输入净化、规划器与执行器隔离、形式化分析器与会话保护，同时覆盖初始访问与利用 后的攻击路径。通过对热门开源项目 Browser Use 的白盒分析，作者展示了不可信网页内容如何劫持 agent 行为并导致严重安全事故，具体发现包括提示注入、域名校验绕过与凭证外泄，并附有一个 已披露的 CVE 与可工作的概念验证利用程序。

`环境: Web` ｜ [arXiv:2505.13076](https://arxiv.org/abs/2505.13076)

#### WebInject: Prompt Injection Attack to Web Agents (WebInject) (2025-05)

基于多模态大模型的 web agent 是依据网页截图来生成动作的。WebInject 换了一条攻击路径： 它不碰任何文本通道，而是直接操纵渲染网页 —— 对页面的原始像素值施加扰动，这些像素被映射 进截图之后，就能诱导 agent 执行攻击者指定的动作。作者把寻找扰动形式化为一个优化问题， 核心难点在于原始像素值到截图的映射不可微，梯度无法回传；解决办法是训练一个神经网络来近似 该映射，再对重构后的问题使用投影梯度下降。在多个数据集上的大量评测表明，WebInject 非常 有效，显著优于已有基线方法。

`环境: Web` ｜ `发表: EMNLP 2025` ｜ [arXiv:2505.11717](https://arxiv.org/abs/2505.11717)

#### Characterizing Unintended Consequences in Human-GUI Agent Collaboration for Web Browsing (2025-05)

本文结合社交媒体分析（221 条帖子）与半结构化访谈（14 位参与者），从现象、影响与缓解三个 角度刻画 LLM 驱动的 GUI agent 在网页浏览中产生的三类非预期后果。现象层面包括：agent 对 指令理解不足、任务规划不佳，GUI 交互不准确且难以适应动态界面，输出不可靠或与意图错位， 以及错误处理与反馈机制薄弱。这些现象的后果逐级升级 —— 先是意外操作与用户挫败，进而演变为 隐私侵犯与安全漏洞，再进一步造成信任流失与更广泛的伦理问题。研究还记录了用户自发采取的 缓解手段（技术性调整与人工监督），并为设计稳健、以用户为中心且透明的 GUI agent 给出启示。

`环境: Web` ｜ [arXiv:2505.09875](https://arxiv.org/abs/2505.09875)

#### WASP: Benchmarking Web Agent Security Against Prompt Injection Attacks (WASP) (2025-04)

自主 UI agent 有潜力替用户自动化报税、缴费等日常任务，但正因为它能代用户行动，安全成了释放 这一潜力的主要障碍。现有的 web agent 提示注入测试要么把威胁过度简化（场景不现实或赋予攻击者 过大权限），要么只看孤立的单步任务。WASP 是一个公开的基准，用于端到端地评测 web agent 面对 提示注入的安全性。评测发现，即便是具备高级推理能力的顶尖模型，也会在非常真实的场景中被人类 随手编写的简单注入骗到。端到端的视角还带来一个新发现：攻击在最多 86% 的案例中能部分得手， 但即便是最先进的 agent 也常常无法完整达成攻击者目标 —— 作者把这种现状称为「因无能而安全」。

`环境: Web` ｜ [arXiv:2504.18575](https://arxiv.org/abs/2504.18575)

#### Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents (2025-04)

LLM 驱动的 GUI agent 会在有限人工监督下处理敏感数据，由此带来的隐私与安全风险既不同于 传统 GUI 自动化，也不同于一般的自主 agent。这篇立场论文识别出三类关键风险，同时指出：现有 评测几乎只关注性能，隐私与安全评估基本处于空白。文章梳理了 GUI agent 与通用 LLM agent 的 现有评测指标，并指出把人工评估者引入 GUI agent 评测时的五个关键挑战。作者主张建立以人为 中心的评测框架 —— 把风险评估纳入其中，通过上下文内的 consent 提升用户知情度，并把隐私与 安全考量嵌入 GUI agent 的设计与评测全过程。

`环境: Web` ｜ [arXiv:2504.17934](https://arxiv.org/abs/2504.17934)

#### The Obvious Invisible Threat: LLM-Powered GUI Agents' Vulnerability to Fine-Print Injections (Fine-Print Injection) (2025-04)

GUI agent 在完成填表、预订等真实任务时常常要处理并操作敏感用户数据，这带来了新的隐私与 安全风险。攻击者可以向界面注入恶意内容，改变 agent 行为或诱导其泄露本不该透露的私人信息； 这类攻击利用的正是界面元素对 agent 与对人的视觉显著性差异，以及 agent 难以察觉任务自动化 中上下文完整性被破坏的弱点。本文刻画了六类此类攻击，并用六个前沿 GUI agent、234 个对抗 网页与 39 名人类参与者做实验。结果显示 GUI agent 高度脆弱，尤其对嵌入上下文的威胁。更值得 注意的是，人类参与者同样容易中招，这说明简单的人工监督并不能可靠阻止失败 —— 人与 agent 之间的这种错位，凸显了隐私感知型 agent 设计与实用防御策略的必要性。

`环境: Web` ｜ [arXiv:2504.11281](https://arxiv.org/abs/2504.11281)

#### SafeArena: Evaluating the Safety of Autonomous Web Agents (SafeArena) (2025-03)

随着基于 LLM 的 agent 在网页任务上越来越熟练，被蓄意滥用的风险也随之上升 —— 比如在论坛 散布虚假信息，或在网站上售卖违禁品。SafeArena 是首个聚焦 web agent 蓄意滥用的基准，含 跨四个网站的 250 个安全任务与 250 个有害任务，有害任务覆盖虚假信息、违法活动、骚扰、 网络犯罪与社会偏见五类。作者提出 Agent Risk Assessment 框架，把 agent 行为归入四个风险 等级，并据此评测 GPT-4o、Claude-3.5 Sonnet、Qwen-2-VL 72B 与 Llama-3.2 90B。结果发现 agent 对恶意请求的服从程度出人意料：GPT-4o 与 Qwen-2 分别完成了 34.7% 与 27.3% 的有害 请求，凸显为 web agent 建立安全对齐流程的紧迫性。

`环境: Web` ｜ [arXiv:2503.04957](https://arxiv.org/abs/2503.04957)

#### AdvAgent: Controllable Blackbox Red-teaming on Web Agents (AdvAgent) (2024-10)

黑盒红队框架，摆脱人工编写对抗 prompt 的做法，转而用强化学习流水线训练一个对抗 prompter 模型，依据黑盒 agent 自身的反馈来优化 prompt。其设计目标不只是成功率，而是在隐蔽性之外还要 **可控性**——攻击要保持可操纵，而非仅仅有效。论文报告在多样任务上对基于 GPT-4 的前沿 web agent 取得高成功率，并发现现有基于 prompt 的防御保护有限，这是「单靠 prompt 加固撑不住」 的一个早期证据。

`环境: Web` ｜ [arXiv:2410.17401](https://arxiv.org/abs/2410.17401)

#### Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents (BrowserART) (2024-10)

提出了一个重塑领域思考方式的问题：在聊天场景中训练出的拒答行为，能否泛化到非聊天的 agentic 场景？其风险是**性质**上的差异而非程度差异——与聊天机器人不同，手握浏览器或手机的 agent 直接 作用于真实世界，因此一次拒答失败产生的是后果而不是文本。论文发布红队测试套件 BrowserART， 含 100 项浏览器相关有害行为、覆盖合成与真实网站，部分取材自 HarmBench 与 AirBench 2024。 「拒答训练难以迁移到 agentic 场景」这一结论催生了此后大量工作。

`环境: Web` ｜ [arXiv:2410.13886](https://arxiv.org/abs/2410.13886)

#### ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents (ST-WebAgentBench) (2024-10)

批评那些只测量「任务是否完成」的基准——它们忽略了完成得是否安全、是否达到企业可信任的程度—— 并主张在关键工作流中，安全与可信是采用的前置条件而非附加项。其 222 个任务每个都配有 ST 策略 （编码约束的简明规则），并在用户同意、鲁棒性等六个正交维度上打分。真正留下来的贡献是那个 指标：Completion Under Policy 只把「遵守了所有适用策略」的完成计为成功，而三个开源 agent 在 CuP 下的得分不足其名义成功率的三分之二。

`环境: Web` ｜ [arXiv:2410.06703](https://arxiv.org/abs/2410.06703)

#### EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage (EIA) (2024-09)

首个研究通用 web agent 在对抗环境下隐私风险的工作，出发点事后看来显而易见：订机票这类日常 网页任务本身就涉及用户 PII，因此 agent 一旦接触到被攻陷的网站，泄露就是结构性的。论文给出 网站侧的现实威胁模型，含两类攻击目标——窃取特定 PII，或窃取完整的用户请求——并提出「环境 注入攻击」（EIA），注入的内容经设计能融入 agent 所处的环境。这篇论文命名了后续工作赖以展开的 「环境注入」这一攻击类别。

`环境: Web` ｜ [arXiv:2409.11295](https://arxiv.org/abs/2409.11295)

#### Dissecting Adversarial Robustness of Multimodal LM Agents (ARE) (2024-06)

与聊天机器人不同，agent 是多个组件共同执行动作的复合系统，而现有语言模型安全评估并未充分 覆盖这一点。作者在 VisualWebArena 这一真实环境上人工构造了 200 个定向对抗任务与评估脚本， 并提出 ARE（Agent Robustness Evaluation）框架：把 agent 视为展示组件间中间输出流动的图， 将鲁棒性分解为对抗信息在图上的流动。实验表明，只需对单张图像施加不足页面总像素 5% 的 不可感知扰动，就能劫持基于黑盒前沿模型、甚至带反思与树搜索机制的 agent，定向对抗目标 成功率最高达 67%。ARE 还能严格衡量增加组件后鲁棒性如何变化：一旦攻击者污染了反思 agent 所用的评估器或树搜索 agent 的价值函数，攻击成功率分别相对提高 15% 与 20%。这意味着通常 能提升良性表现的推理时计算，反而会打开新的漏洞。

`环境: Web` ｜ `发表: ICLR 2025` ｜ [arXiv:2406.12814](https://arxiv.org/abs/2406.12814)

#### GuardAgent: Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning (GuardAgent) (2024-06)

首个护栏 **agent**——它不是分类器或过滤器，而是通过动态检查目标 agent 的动作是否满足给定的 安全守护请求来实施保护。设计上值得注意的是它如何绕开 LLM 判断的可靠性上限：GuardAgent 先把 守护请求解析为任务计划，再把计划映射为护栏**代码**并执行，因此尽管推理由 LLM 承担，强制执行 仍是确定性的；同时从存有历史任务经验的记忆模块中检索上下文示例。工作还贡献了两个基准： 面向医疗 agent 访问控制的 EICU-AC，与面向 web agent 安全策略的 Mind2Web-SC。

`环境: Web` ｜ [arXiv:2406.09187](https://arxiv.org/abs/2406.09187)

#### WIPI: A New Web Threat for LLM-Driven Web Agents (WIPI) (2024-02)

最早直接抛出这个问题的工作之一——在无数 web agent 相继发布、逐步走向日常部署之际，它们究竟 安全吗？WIPI 提出一种新威胁：把恶意指令嵌入公开可访问的网页，从而间接控制 web agent，全程 无需接触 agent 本身。方法在黑盒环境下工作，关注的是间接指令的形式与内容而非模型内部，这正是 它兼具效率与隐蔽性的原因。就领域脉络而言，这是 web agent 间接注入这条线的奠基性文献。

`环境: Web` ｜ [arXiv:2402.16965](https://arxiv.org/abs/2402.16965)
