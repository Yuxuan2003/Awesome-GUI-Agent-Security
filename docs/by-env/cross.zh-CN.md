# 跨环境

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Beyond Task Completion: Training Capable and Safe Computer-Use Agents (SCOPE) (2026-08)

只以任务成功为目标的后训练，并不会带来可靠的安全行为。本文给出明确规范：可靠的 CUA 应当 以风险为条件决定执行方式 —— 普通良性任务照常完成，遇到环境风险时规避并在仍存在安全路径时 继续，而当目标本身有害或已无安全路径时应当拒绝。SCOPE 把任务执行能力与安全感知决策联合 后训练；SCOPE-Gen 自动合成可验证的能力任务，并把它转换为保持原目标的环境风险变体，由此 构建出含能力示范、安全续行与显式拒绝三类轨迹的数据集 SATraj-OS。SCOPE 先通过监督微调 学习这三类轨迹，再用在线强化学习提升任务完成度。从 Qwen3.5-9B 出发，SCOPE-RL 在 OSWorld 上任务成功率 54.17%、在 OS-BLIND 上攻击规避率 64.30%，能力与安全的综合得分 58.80% 为 参评 agent 最高。消融显示两类安全监督作用互补而不对称：拒绝轨迹贡献了大部分攻击规避提升， 而风险处理轨迹在同等规避水平下保住了更多任务效用。

`环境: 跨环境` ｜ [arXiv:2609.22178](https://arxiv.org/abs/2609.22178)

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)

针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI 基准 StepJack，构造 480 个测试用例，把注入载荷分散在多步任务的中间环节，模拟攻击者只能污染 流程某一环的现实约束。实验显示多步注入相比单步把攻击成功率最高抬升 31.2 个百分点， 说明单步评测显著低估了 CUA 的真实暴露面，且现有防御在流程中段几乎不再触发。

`环境: Desktop, 跨环境` ｜ [arXiv:2608.06477](https://arxiv.org/abs/2608.06477)

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)

提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。

`环境: Mobile, 跨环境` ｜ [arXiv:2607.29199](https://arxiv.org/abs/2607.29199)

#### SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems (SafeFlow) (2026-07)

指出正是那些让多 agent 系统变强的机制造就了盲点：任务分解与角色专职化使一个有害目标可以被 拆解成局部看来都合理的子任务，于是没有任何单个 agent 能看到足够信息来识别恶意意图。论文的 关键一步是把这个问题重新框定为**语义信息流**问题、而非单轮 prompt 分类任务——这个范畴转换 解释了为何逐条消息的过滤器注定无效。SafeFlow 为根请求附加结构化的语义污点标记，沿动态协作 图传播，并在工作流层面做整体校验。

`环境: 跨环境` ｜ [arXiv:2607.25255](https://arxiv.org/abs/2607.25255)

#### Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets (Argus) (2026-06)

计算机使用代理把视觉语言模型的预测变成可执行的 GUI 点击，因此可靠的不确定性估计对拒绝 执行、校准、失误严重性排序与空间安全区域都至关重要；但事后不确定性量化（UQ）的证据零散 分布在孤立的模型—数据集对上，难以判断排序是否稳定。Argus 是一个跨机制基准：包含覆盖 4 个 VLM agent 与 4 个数据集的 27 种方法开源矩阵，以及在无法取得 logit、隐藏状态与 注意力图的 3 家前沿厂商上的 8 种方法闭源矩阵。核心发现是「选择性迁移」：固定模型时 UQ 排序跨数据集稳定（Spearman rho 最高 0.969），但跨模型类别与可观测接口时退化，向闭源厂商 的跨层迁移平均只有 +0.08 —— 因此闭源场景的 UQ 应在目标上重新排序而非外推。共形点击区域 在校准后半径可缩小 40–60%，但在校准—测试或接口不匹配时覆盖率会下降。

`环境: 跨环境` ｜ [arXiv:2606.25760](https://arxiv.org/abs/2606.25760)

#### When AUC 0.998 Is Not Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect Prompt Injection in Multimodal Computer-Use Agents (IPI Probe Controls) (2026-06)

在冻结视觉语言模型的内部激活上训练线性分类器（hidden-state probing），因能在计算机使用代理 发出被污染的动作之前标记间接提示注入而受到关注。本文以单一骨架（Qwen2.5-VL-7B 在 Mind2Web 上的教师强制重放）做警示性案例研究，论证「干净 vs 攻击」划分下的高探测 AUC 本身并不能证明 探针真的检测到了恶意内容。两项事后诊断 —— 文本侧注入的配对构造标量基线，以及覆盖层上同 步骤的干扰匹配视觉对照 —— 都不支持对 headline 数字作无保留的「恶意内容检测」解读，但仍为 部分语义性解释留下空间。作者把诊断打包成候选对照集，并给出报告启发式，说明高 AUC 究竟能 支持什么、不能支持什么；同时强调标签只表示注入面是否存在，而非攻击是否成功，超出该骨架与 基准的泛化仍属猜想。

`环境: 跨环境` ｜ [arXiv:2606.22864](https://arxiv.org/abs/2606.22864)

#### Securing Computer-Use Agents: A Unified Architecture-Lifecycle Framework for Deployment-Grounded Reliability (Architecture-Lifecycle Framework) (2026-05)

论证当 CUA 走出受限基准、进入真实的浏览器、桌面、移动应用、文件系统、终端与工具后端之后， 任务成功率就不再是有意义的可靠性度量：感知错误、规划漂移、记忆使用、工具中介、权限范围与 运行时监督**共同**决定动作是否仍与用户意图对齐。现有综述按方法、平台、基准或威胁来组织 这个领域，但很少把「能力形成 → 权限暴露 → 失效显现 → 控制点放置」这条链条串起来。本框架 通过架构视角（把感知、决策、执行视为相互耦合的层）与生命周期视角提供了这一串联。

`环境: 跨环境` ｜ [arXiv:2605.07110](https://arxiv.org/abs/2605.07110)

#### Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection (Semantic UI Injection) (2026-04)

指出现有 GUI agent 红队研究的两个局限：对抗扰动需要商业部署中拿不到的白盒访问，而提示 注入正被日益增强的安全对齐所化解。提出黑盒范式「语义级 UI 元素注入」——把本身安全对齐、 内容无害的 UI 元素叠加到截图上以误导视觉 grounding，用模块化的 Editor-Overlapper-Victim 流水线配合迭代搜索。在 8 个模型家族共 19 个受害模型上，策略化优化相比随机注入在最鲁棒的 模型上高出 3.5–6.9 倍，且跨架构迁移性近乎完美。

`环境: 跨环境` ｜ [arXiv:2604.07831](https://arxiv.org/abs/2604.07831)

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)

提出针对 VLM-based GUI agent 的效率后门：触发器不改变任务最终结果，只让 agent 的响应 延迟大幅增加或步数显著膨胀。这类后门极难被察觉——正确性检测全部通过，只有观察资源消耗 才能发现，因此可长期潜伏并造成持续的算力成本损失。拓展了 GUI agent 后门的威胁定义， 从「结果篡改」扩展到「可用性与经济性攻击」。

`环境: Mobile, 跨环境` ｜ [arXiv:2603.08316](https://arxiv.org/abs/2603.08316)

#### Agent Skills for Large Language Models: Architecture, Acquisition, Security, and the Path Forward (Skill Trust Framework) (2026-02)

Agent skill —— 按需加载的指令、代码与资源的可组合包 —— 让模型无需重训就能动态扩展能力。 本文从四条轴线梳理这一领域：架构基础（SKILL.md 规范、渐进式上下文加载、skill 与 MCP 的 互补角色）；skill 获取（带 skill 库的强化学习、自主发现、组合式合成）；规模化部署，含 计算机使用代理技术栈与 OSWorld 上的 GUI grounding 进展；以及安全。在安全这条轴上，实证 分析发现社区贡献的 skill 中有 26.1% 含有漏洞，据此提出 Skill Trust 与生命周期治理框架： 一个四层、以关卡为单位的权限模型，把 skill 的来源映射到分级的部署能力上。文章还列出从 跨平台可移植性到基于能力的权限模型等七个开放挑战。这些结论对 GUI agent 直接相关。

`环境: 跨环境` ｜ [arXiv:2602.12430](https://arxiv.org/abs/2602.12430)

#### Just Do It!? Computer-Use Agents Exhibit Blind Goal-Directedness (BLIND-ACT) (2025-10)

本文指出计算机使用代理普遍存在「盲目目标导向」（BGD）：无论可行性、安全性、可靠性与上下文 如何，都倾向于继续执行既定目标。作者刻画了三类常见模式：缺乏上下文推理、在模糊条件下做 假设与决策、以及面对矛盾或不可行的目标。BLIND-ACT 是基于 OSWorld 构建的 90 个任务基准， 用 LLM 作为评判者，与人工标注的一致率达 93.75%。对包括 Claude Sonnet 与 Opus 4、 Computer-Use-Preview、GPT-5 在内的九个前沿模型评测，平均 BGD 率高达 80.8%。提示层面的 干预能降低 BGD，但风险依然显著，说明需要更强的训练期或推理期干预。定性分析归纳出三种失效 模式：执行优先偏差（只关心怎么做而不问该不该做）、思维与行动脱节、以及请求至上（因为是用户 要求就为行动辩护）。这说明即便输入本身无害，风险依然会产生。

`环境: 跨环境` ｜ [arXiv:2510.01670](https://arxiv.org/abs/2510.01670)

#### RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments (RedTeamCUA) (2025-05)

对计算机使用代理的间接提示注入评估，要么缺少真实且可控的环境，要么忽略同时横跨操作系统与 网页界面的混合攻击场景。RedTeamCUA 用一个混合沙箱补上这块：把基于虚拟机的操作系统环境与 基于 Docker 的网页平台整合在一起。它支持灵活的对抗场景配置，并能直接在注入点初始化测试， 从而把对抗评估与 agent 自身的导航能力限制解耦。在此基础上作者构建了含 864 个样例的 RTC-Bench，覆盖真实的混合 web-OS 攻击场景与基础性安全漏洞。对前沿 CUA 的评测显示脆弱性 相当严重：Claude 3.7 Sonnet | CUA 攻击成功率 42.9%，最安全的 Operator 仍有 7.6%；agent 的「尝试率」高达 92.5% —— 它们常常已经开始执行对抗任务，只是因为能力不足才失败；而在真实的 端到端场景中，当前最强的 Claude 4.5 Sonnet | CUA 攻击成功率达 60%。

`环境: 跨环境` ｜ `发表: ICLR 2026` ｜ [arXiv:2505.21936](https://arxiv.org/abs/2505.21936)

#### EVA: Evolving Semantic Adversaries for Red-Teaming GUI Agents Against Environmental Injection Attacks (EVA) (2025-05)

针对 GUI agent 的环境注入攻击做红队测试，一直受制于计算成本过高与适应性差，且攻击成败究竟 卡在视觉感知还是语义理解，此前并不清楚。本文的对照实验表明：决定攻击成败的是语义欺骗，而非 视觉外观。据此提出的 EVA 只在语义维度上演化对抗载荷，采用「发现—部署」框架挖掘语言层面的 脆弱模式并提炼为可泛化规则。在五个代表性受害 agent 上，EVA 的攻击成功率最高达 85%，把良性 种子演化成成功攻击只需 1.18–1.71 次迭代。这种快速收敛揭示了模型潜在表示中密集的语义攻击 空间，也暴露出一个对齐悖论：正是对齐训练所强化的指令遵循能力，使 agent 天生容易服从权威式 的、语义欺骗性的环境线索。

`环境: 跨环境` ｜ [arXiv:2505.14289](https://arxiv.org/abs/2505.14289)

#### GEM: Gaussian Embedding Modeling for Out-of-Distribution Detection in GUI Agents (GEM) (2025-05)

GUI agent 一旦遇到违反环境约束或超出自身能力的分布外指令，就可能任务崩溃甚至产生安全威胁， 因此有效的 OOD 检测十分必要。但传统 OOD 方法在这个场景表现不佳 —— 嵌入空间复杂，且 GUI 环境持续演化。作者观察到分布内输入的语义空间按到质心的距离呈聚类结构，据此提出 GEM：对从 GUI agent 提取的、反映其能力边界的输入嵌入距离拟合高斯混合模型。在覆盖手机、电脑与网页 浏览器的八个数据集上，GEM 的平均准确率比最佳基线提升 23.70%，而训练与测试时间仅分别增加 4.9% 与 6.5%。在检测到 OOD 样本时请求云端模型协助，还能把分步成功率提升 9.40%；九个不同 骨架上的实验验证了方法的泛化能力。

`环境: 跨环境` ｜ [arXiv:2505.12842](https://arxiv.org/abs/2505.12842)

#### A Survey on the Safety and Security Threats of Computer-Using Agents: JARVIS or Ultron? (JARVIS or Ultron?) (2025-05)

本文对计算机使用代理（CUA）的安全与安保威胁做系统化梳理 —— 这类 agent 能自主操作桌面 应用、网页与移动应用。作者围绕四个目标组织了一轮全面的文献综述：给出适合安全分析的 CUA 定义、对当前安全威胁进行分类、提出防御策略的完整分类体系、以及汇总用于评估 CUA 安全性与 性能的基准、数据集与评测指标。LLM 驱动推理本身的脆弱性，叠加多软件组件整合与多模态输入 带来的复杂度，使这一安全图景远比纯 LLM 安全研究所覆盖的范围更广。综述为研究者提供探索 未知漏洞的结构化基础，也为实践者给出设计与部署安全 CUA 的可操作建议。

`环境: 跨环境` ｜ `发表: ACL 2026` ｜ [arXiv:2505.10924](https://arxiv.org/abs/2505.10924)

#### DoomArena: A framework for Testing AI Agents Against Evolving Security Threats (DoomArena) (2025-04)

DoomArena 是一个基于三条原则构建的安全评估框架：可插拔，能轻松接入 BrowserGym（web agent） 与 τ-bench（工具调用 agent）等真实 agent 框架；可配置，支持细致的威胁建模 —— 指定框架中 哪些组件可被攻击以及攻击者的目标；模块化，把攻击开发与部署环境解耦，使同一批攻击能跨环境 复用。把该框架应用于前沿 web 与工具调用 agent，得到若干出人意料的结果：不同威胁模型下 （恶意用户 vs 恶意环境）agent 的脆弱程度各不相同，不存在帕累托占优的 agent；多个攻击同时 施加时往往产生建设性叠加；基于护栏模型的防御基本失效，而基于强大 LLM 的防御效果更好。

`环境: 跨环境` ｜ [arXiv:2504.14064](https://arxiv.org/abs/2504.14064)

#### Towards Trustworthy GUI Agents: A Survey (Trustworthy GUI Survey) (2025-03)

把「执行落差」（execution gap）确立为可信 GUI agent 的核心障碍——即在动态、部分可观测界面下 感知、推理与交互三者之间的错配。与对话系统不同，GUI agent 执行的是提交表单、授予权限、删除 数据这类不可逆操作。综述提出与工作流对齐的分类法，把信任拆为感知信任、推理信任、交互信任 三层，梳理失败如何在动作/观察循环中传播并累积，并主张仅用任务完成率评估可信度是不充分的。

`环境: 跨环境` ｜ [arXiv:2503.23434](https://arxiv.org/abs/2503.23434)

#### sudo rm -rf agentic_security (SUDO) (2025-03)

大模型正被部署为计算机使用代理，在真实桌面或网页环境中自主执行任务，这带来了严重的安全 暴露。本文提出 SUDO（Screen-based Universal Detox2Tox Offense），一个系统性绕过商用 计算机使用代理拒绝训练防护的攻击框架。其核心机制 Detox2Tox 分三步：把 agent 最初会拒绝的 有害请求「脱毒」成看似良性的请求，从先进视觉语言模型那里套出详细操作步骤，再在执行前通过 「复毒」把恶意内容重新引入。与常规越狱不同，SUDO 会依据内置的拒绝反馈迭代改进攻击，因而 对抗强策略过滤器时越来越有效。在 50 个真实任务与多个前沿 VLM 上，SUDO 对 Claude for Computer Use 的无 refinement 攻击成功率为 24.41%，经迭代 refinement 后可达 41.33%。

`环境: Desktop, 跨环境` ｜ `发表: ACL 2025` ｜ [arXiv:2503.20279](https://arxiv.org/abs/2503.20279)

#### MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents (MIP) (2025-03)

操作系统 agent 让视觉语言模型通过截图捕获、解析并调用鼠标点击与键盘输入等底层 API 直接 操控电脑，因此一旦失败或被操纵，后果是即时而具体的。本文揭示了一种新的攻击向量 —— 恶意 图像补丁（MIP）：对屏幕局部区域做对抗性扰动，OS agent 截图捕获到该区域后就会被诱导调用 特定 API 执行有害动作。例如把 MIP 嵌入桌面壁纸或在社交媒体上传播，就能让 OS agent 外泄 用户的敏感数据。实验表明 MIP 能跨不同的用户提示与屏幕配置泛化，并且即便 agent 正在执行 完全良性的指令也能被劫持，说明在大规模部署之前必须先解决这些关键安全漏洞。

`环境: 跨环境` ｜ `发表: NeurIPS 2025` ｜ [arXiv:2503.10809](https://arxiv.org/abs/2503.10809)

#### Caution for the Environment: Multimodal LLM Agents are Susceptible to Environmental Distractions (2024-08)

本文考察多模态大模型 agent 在 GUI 环境中的忠实度，核心问题是：它们会不会被环境上下文带偏？ 所设定的场景是 —— 用户与 agent 都是善意的，环境也并非恶意，只是含有与任务无关的内容。 作者在模拟数据集上以三种感知层级不同的工作模式，评估了大量多模态大模型作为 GUI agent 的 表现。结果显示，即便是最强的模型，无论通用 agent 还是专用 GUI agent，都会受到这类干扰。 已有研究大多只关注 agent 的有用性，本文则首次指出 agent 容易受到环境干扰；作者进一步 实现了对抗性环境注入，并分析了提升忠实度的方法。

`环境: 跨环境` ｜ `发表: ACL 2025` ｜ [arXiv:2408.02544](https://arxiv.org/abs/2408.02544)
