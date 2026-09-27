# 1.7 良性指令下的意外危害

*Unintended Harm from Benign Instructions*

[← 返回索引](../../../README.zh-CN.md#17-良性指令下的意外危害) ｜ [English](../en/1-7-unintended-harm-from-benign-instructions.md)

*无恶意攻击者，agent 自身在正常指令下造成危害*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### CAVEAT: Towards Robust Computer-Use Agents in Incentive-Misaligned Environments (CAVEAT) (2026-09)

当 agent 所处的环境自身与用户利益不一致时会发生什么？在在线市场里，平台可能偏好某些 商品，从而把 agent 带离用户的目标。本文提出 CAVEAT：覆盖九个市场环境的受控基准，并给出 八类常见「引导机制」的分类。在五个模型族上，agent 在对照条件下有 78.6% 买到用户最优商品， 而开启引导机制后只剩 17.3%。更大的模型与更多推理能提升稳健性，但失效仍大量存在。轨迹分析 与定向消融定位出引导进入决策的三个位置：扭曲用户的优先级、过早收窄所考虑的候选集、以及在 决策相关证据尚未澄清时就提交。据此构建的 CAVEAT-Harness 直接针对这三种失效模式，把用户 最优购买率提升 55.0%，定向后训练还能进一步提升较小的开源模型。

`环境: Web` ｜ [arXiv:2609.27273](https://arxiv.org/abs/2609.27273)

#### A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents (Nudge Susceptibility) (2026-09)

GUI agent 运行在专为「支持并有意引导人类决策」而设计的界面里。LLM 文本输出中的行为偏差 已有大量记录，但当模型转为感知界面并执行决策时这种影响如何运作，以及日益内置的推理能力 是否让 agent 更稳健，此前少有人知。本文基于双过程理论，在随机化的在线购物实验中用 3600 个 agent、21600 次模拟、覆盖三家厂商的六个前沿模型，发现 agent 对自动型（Type 1） 与反思型（Type 2）数字助推均易感。关键结论是推理配置对两者的调节方向**相反**：它降低了 对自动型默认助推的易感性，却提高了对反思型社会影响助推的易感性。也就是说，充分推理并未 带来稳健性，而是改变了选择架构生效的路径，且这一改变随模型规模系统性变化。作者据此主张， 对于把决策委托给自主 agent 的组织，界面设计本身应被视为治理议题。

`环境: Web` ｜ [arXiv:2609.19843](https://arxiv.org/abs/2609.19843)

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)

提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。

`环境: Mobile, 跨环境` ｜ [arXiv:2607.29199](https://arxiv.org/abs/2607.29199)

#### OTora: A Unified Red Teaming Framework for Reasoning-Level Denial-of-Service in LLM Agents (OTora) (2026-05)

提出一个绝大多数威胁模型完全忽略的攻击目标：推理级拒绝服务（R-DoS）——攻击者**保持任务结果 正确**，却通过膨胀 agent 的推理深度或工具调用预算来损害可用性。正因为输出依然正确，所有 基于正确性的防御与所有检查输出的护栏都会报告「运行正常」。OTora 是两阶段框架：第一阶段用 插入位置感知打分与动态目标共进化优化对抗触发串，诱导定向的工具调用（支持黑盒与白盒）； 第二阶段通过 ICL 引导的遗传搜索生成推理载荷，在保持结果正确的同时放大「过度思考」。 在 WebShop、Email 与 OS agent 上评测，骨干模型含 LLaMA-70B 与 GPT-OSS-120B。

`环境: Web, Desktop` ｜ [arXiv:2605.08876](https://arxiv.org/abs/2605.08876)

#### The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents (OS-BLIND) (2026-04)

隔离出现有安全评测跳过的那个场景：用户指令完全良性，危害来自任务上下文或执行后果，既无 滥用也无注入。OS-BLIND 提供 300 个人工构造任务，覆盖 12 个类别、8 个应用，分为「环境 嵌入型威胁」与「agent 自发危害」两簇。数字相当刺眼——多数 CUA 的攻击成功率超过 90%， 即便经过安全对齐的 Claude 4.5 Sonnet 也达到 73.0%。更糟的是，同一模型置于多 agent 配置中时 ASR 从 73.0% 升至 92.7%，说明编排本身就在侵蚀对齐效果。

`环境: Desktop` ｜ [arXiv:2604.10577](https://arxiv.org/abs/2604.10577)

#### When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents (AutoElicit) (2026-02)

观察到 CUA 即便在良性输入下也确实会产生不安全的非预期行为，但对这类风险的探索一直停留在 个案层面——既无具体刻画，也无自动化手段挖掘长尾情形。论文提供了首个关于 CUA 非预期行为的 概念与方法框架：定义其关键特征、自动化诱发、并分析它如何从良性输入中产生。AutoElicit 利用 CUA 的执行反馈迭代扰动良性指令，同时保持扰动本身真实且无恶意，从 Claude 4.5 Haiku、Opus 等前沿模型上挖掘出数百个有害行为。

`环境: Desktop` ｜ [arXiv:2602.08235](https://arxiv.org/abs/2602.08235)

#### The Behavioral Fabric of LLM-Powered GUI Agents: Human Values and Interaction Outcomes (2026-01)

用户的偏好与价值观会如何影响 LLM 驱动的网页 GUI agent 的推理与行为，此前所知甚少。作者 构建了一个受控测试床，包含购物、旅行、餐饮、租房等 14 类常见交互网页任务，均从真实网站 复刻并接入一个低保真的 LLM 推荐系统，然后把 12 种人类偏好与价值观作为人设注入四个前沿 agent。结果发现，含偏好与价值观的提示确实能持续把 agent 引向相应的结果：缺少这类引导时， agent 表现出强烈的效率偏向并采取最短路径策略；有了引导则会更多使用相应的筛选器与交互 功能。但折扣、广告等主导性界面线索经常压过这些影响 —— 它们会缩短 agent 的行动轨迹，并 诱发出掩盖而非反映价值观一致推理的合理化说辞。

`环境: Web` ｜ [arXiv:2601.16356](https://arxiv.org/abs/2601.16356)

#### When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent (AgentBait) (2026-01)

指出以往研究集中在提示注入、后门这类模型层威胁，而针对 web 自动化 agent 的社会工程攻击一直 无人探索——尽管 Browser Use、Skyvern-AI 等开源框架已显著扩大了攻击面。AgentBait 攻击范式 利用执行层面的内在弱点：诱导性上下文会扭曲 agent 的推理，把它引向与原任务不一致的目标， 而全程不需要注入任何指令。防御侧提出 SUPERVISOR，一个轻量可插拔的运行时模块，强制网页 上下文与预期目标之间的「环境—意图一致性」对齐。

`环境: Web` ｜ [arXiv:2601.07263](https://arxiv.org/abs/2601.07263)

#### DECEPTICON: How Dark Patterns Manipulate Web Agents (DECEPTICON) (2025-12)

把暗黑模式（dark patterns，即真实网络上早已泛滥的欺骗性 UI 设计）作为一类 agent 安全威胁 来研究——它不需要攻击者搭建任何基础设施，因为恶意界面本身就是现状。DECEPTICON 在 700 个 网页导航任务（600 合成 + 100 真实）中隔离测试单个暗黑模式。结果是暗黑模式在超过 70% 的 任务中成功把 agent 引向恶意结果，而人类平均只有 31%。最值得警惕的发现颠覆了通常的 scaling 直觉：操纵有效性与模型规模、测试时推理量**正相关**——越大越强的 agent 反而更易受骗。

`环境: Web` ｜ [arXiv:2512.22894](https://arxiv.org/abs/2512.22894)

#### Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness (BLIND-ACT) (2025-10)

本文指出计算机使用代理普遍存在「盲目目标导向」（BGD）：无论可行性、安全性、可靠性与上下文 如何，都倾向于继续执行既定目标。作者刻画了三类常见模式：缺乏上下文推理、在模糊条件下做 假设与决策、以及面对矛盾或不可行的目标。BLIND-ACT 是基于 OSWorld 构建的 90 个任务基准， 用 LLM 作为评判者，与人工标注的一致率达 93.75%。对包括 Claude Sonnet 与 Opus 4、 Computer-Use-Preview、GPT-5 在内的九个前沿模型评测，平均 BGD 率高达 80.8%。提示层面的 干预能降低 BGD，但风险依然显著，说明需要更强的训练期或推理期干预。定性分析归纳出三种失效 模式：执行优先偏差（只关心怎么做而不问该不该做）、思维与行动脱节、以及请求至上（因为是用户 要求就为行动辩护）。这说明即便输入本身无害，风险依然会产生。

`环境: 跨环境` ｜ [arXiv:2510.01670](https://arxiv.org/abs/2510.01670)

#### Dark Patterns Meet GUI Agents: LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight (Dark Patterns Meet GUI Agents) (2025-09)

两阶段研究，比较 agent、人类参与者与人机协作团队面对 16 类暗黑模式时的表现。第一阶段的 发现更为尖锐：agent 常常识别不出暗黑模式，而**即便识别出来，它也会把任务完成置于保护性 行动之上**——因此「有意识」本身并不产生安全。第二阶段显示人与 agent 的失败方式**不同**： 人类因认知捷径与习惯性顺从而中招，agent 则因流程性盲区而失守。人工监督确实改善了规避率， 但带来了注意力隧道化与认知负荷的代价，因此双方都无法干净地补上对方的缺口。

`环境: Web` ｜ [arXiv:2509.10723](https://arxiv.org/abs/2509.10723)

#### Characterizing Unintended Consequences in Human-GUI Agent Collaboration for Web Browsing (2025-05)

本文结合社交媒体分析（221 条帖子）与半结构化访谈（14 位参与者），从现象、影响与缓解三个 角度刻画 LLM 驱动的 GUI agent 在网页浏览中产生的三类非预期后果。现象层面包括：agent 对 指令理解不足、任务规划不佳，GUI 交互不准确且难以适应动态界面，输出不可靠或与意图错位， 以及错误处理与反馈机制薄弱。这些现象的后果逐级升级 —— 先是意外操作与用户挫败，进而演变为 隐私侵犯与安全漏洞，再进一步造成信任流失与更广泛的伦理问题。研究还记录了用户自发采取的 缓解手段（技术性调整与人工监督），并为设计稳健、以用户为中心且透明的 GUI agent 给出启示。

`环境: Web` ｜ [arXiv:2505.09875](https://arxiv.org/abs/2505.09875)
