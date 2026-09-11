# 3.2 Web 环境基准

*Web Environment*

[← 返回索引](../../../README.zh-CN.md#32-web-环境基准) ｜ [English](../en/3-2-web-environment.md)

*针对 web / 浏览器 agent 的安全评测*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents (Who Pays the Price) (2026-06)

指出现有安全基准都采用「攻击视角」，只关注注入在技术上是否可行，忽略了危害在不同受害方 之间的分布差异。本文主张注入风险是**受害者依赖**的：同一个漏洞对不同利益相关方（用户、 平台、商家）造成的后果高度不对称，同一攻击模式的有效性也随目标不同而显著变化。据此构建 以利益相关方为中心的基准，聚焦电商这类动作直接带来财务后果的真实场景。

`环境: Web` ｜ [arXiv:2606.13385](https://arxiv.org/abs/2606.13385)

#### Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces (WebDecept) (2026-04)

在电商场景下考察 web agent 面对真实欺骗性界面时的行为——这个场景里点错一下就有直接的财务 后果。WebDecept 是轻量可配置的插件框架，能把欺骗性界面模式注入既有网页环境，并实例化了 七种野外常见模式，含定向广告、域名重定向、购物操纵等。在任务执行过程中把它们注入前端， 即可对多个多模态 agent 做受控评测。两个结论值得注意：agent 对多类模式都高度易感；而基于 prompt 的约束往往不足以缓解这类失败。

`环境: Web` ｜ [arXiv:2606.13686](https://arxiv.org/abs/2606.13686)

#### RiskWebWorld: A Realistic Interactive Benchmark for GUI Agents in E-commerce Risk Management (RiskWebWorld) (2026-04)

指出现有交互式基准都瞄准良性、可预测的消费者环境，把高风险的调查类场景留在了视野之外。 RiskWebWorld 从生产环境的风控流水线中取 1513 个任务、覆盖 8 个核心领域，并刻意保留风控 作业的真实困难——不配合的网站、部分环境劫持。配套的 Gymnasium 兼容基础设施把策略规划与 环境机制解耦，以支持 agentic RL。评测暴露出明显的能力落差：顶级通用模型成功率仅 49.1%， 说明对抗性的真实作业场景远未被解决。

`环境: Web` ｜ [arXiv:2604.13531](https://arxiv.org/abs/2604.13531)

#### WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks (WebSP-Eval) (2026-04)

开辟了一个与本清单其余部分正交的方向：现有基准要么测通用能力（WebArena），要么测抵御恶意 动作的能力（SafeArena），但没有一个去问 agent 能否胜任用户真正会委托给它的安全与隐私 事务——管理 cookie 偏好、配置隐私敏感的账户设置、吊销闲置会话。WebSP-Eval 贡献了跨 28 个 网站的 200 个人工构造任务实例、一套通过自定义 Chrome 扩展在多次运行间管理账号与初始状态的 agent 框架、以及自动评测器，并在 8 种 web agent 实例化配置上做了评估。

`环境: Web` ｜ [arXiv:2604.06367](https://arxiv.org/abs/2604.06367)

#### ClawTrap: A MITM-Based Red-Teaming Framework for Real-World OpenClaw Security Evaluation (ClawTrap) (2026-03)

把红队测试下移一层：现有基准集中在静态沙箱设定与内容级 prompt 攻击上，而**网络层**——真实 部署实际暴露的那一层——从未被测试。ClawTrap 是中间人（MITM）框架，用于在真实网络威胁下评测 OpenClaw 这类 agent，支持静态 HTML 替换、iframe 弹窗注入、动态内容修改三类攻击，并提供 规则驱动的拦截、变换与审计的可复现流水线。MITM 这个位置之所以重要，是因为它**不需要攻陷 agent 所访问的任何网站**。

`环境: Web` ｜ [arXiv:2603.18762](https://arxiv.org/abs/2603.18762)

#### MUZZLE: Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks (MUZZLE) (2026-02)

批评现有安全评测依赖固定攻击模板、人工挑选的注入面或范围过窄的场景，都无法反映真实部署时 面对的自适应攻击者。MUZZLE 将这一过程自动化：利用目标 agent 自身的执行轨迹定位高显著性的 注入面，再自适应地生成上下文感知的恶意指令，针对机密性、完整性、可用性三类违背分别施压。 关键之处在于把注入面的选择建立在观测到的 agent 行为上而非人类直觉上——攻击会随 agent 真正关注的内容而调整。

`环境: Web` ｜ [arXiv:2602.09222](https://arxiv.org/abs/2602.09222)

#### MalURLBench: A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs (MalURLBench) (2026-01)

隔离出一个范围很窄但后果严重的失效环节：接受一个伪装过的恶意 URL 就会让 agent 进入不安全 网页，此后所有下游行为都继承了这次沦陷，而此前没有基准针对这一步。MalURLBench 提供 61845 个攻击实例，覆盖 10 类真实场景与 7 类真实恶意网站。在 12 个主流 LLM 上的实验显示，模型 难以识别精心伪装的恶意 URL。论文进一步分析影响攻击成功率的关键因素，并给出轻量防御模块 URLGuard，作用在同一咽喉点上。

`环境: Web` ｜ [arXiv:2601.18113](https://arxiv.org/abs/2601.18113)

#### It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents (TRAP) (2025-12)

从「说服」而非「载荷工程」的视角研究注入：藏在界面元素里的对抗指令是在**说服** agent 偏离 原任务，这把防御问题重新框定为心理学层面而非语法层面的。在六个前沿模型上，agent 平均在 25% 的任务中中招，但真正值得看的是差距——GPT-5 为 13%，DeepSeek-R1 高达 43%。更麻烦的是， 界面或上下文的微小改动常常使成功率翻倍，说明这种脆弱性是系统性的，而非绑定于某种特定措辞。 配套发布模块化的社会工程注入框架，在高保真网站克隆上做受控实验。

`环境: Web` ｜ [arXiv:2512.23128](https://arxiv.org/abs/2512.23128)

#### BrowseSafe: Understanding and Preventing Prompt Injection Within AI Browser Agents (BrowseSafe) (2025-11)

指出把 agent 集成进浏览器所带来的安全问题已超出传统 Web 应用威胁模型，而尽管提示注入是 已知攻击向量，其真实世界影响仍缺乏充分测量。该基准的贡献在于设计取向：强调那些能影响真实 **动作**（而非仅文本输出）的注入，并构造在复杂度与干扰项密度上贴近实际部署 agent 所遭遇 情形的载荷。在此基础上横向评测现有防御在多个前沿模型上的表现，并提出结合架构级与模型级 防御的多层策略。

`环境: Web` ｜ [arXiv:2511.20597](https://arxiv.org/abs/2511.20597)

#### Genesis: Evolving Attack Strategies for LLM Web Agent Red-Teaming (Genesis) (2025-10)

论证依赖人工编写策略或离线训练的静态模型的红队方法，无法捕捉 web agent 的底层行为模式， 因而难以跨环境泛化——这个场景下的成功要求攻击策略被持续发现和演化。Genesis 是三模块 agentic 框架：Attacker 用遗传算法在混合策略表示上生成对抗注入，Scorer 评估目标 agent 的响应并提供 反馈，Strategist 从交互日志中挖掘有效策略并编纂进可复用的策略库。

`环境: Web` ｜ [arXiv:2510.18314](https://arxiv.org/abs/2510.18314)

#### SecureWebArena: A Holistic Security Evaluation Benchmark for LVLM-based Web Agents (SecureWebArena) (2025-10)

指出现有安全基准只提供部分覆盖，通常局限于用户级 prompt 操纵这类狭窄场景，因而错过了 agent 实际暴露面的大部分。SecureWebArena 构建了六个模拟但贴近真实的网页环境（电商平台、社区论坛 等），含覆盖多样任务与攻击设定的 2970 条高质量轨迹。其组织性贡献是一套结构化的六类攻击向量 分类法，**同时**覆盖用户级与环境级操纵——而后者恰恰是范围更窄的基准所遗漏的那一半。

`环境: Web` ｜ [arXiv:2510.10073](https://arxiv.org/abs/2510.10073)

#### WAInjectBench: Benchmarking Prompt Injection Detections for Web Agents (WAInjectBench) (2025-10)

填补一个系统性空缺：针对 web agent 的注入攻击很多，通用注入检测方法也很多，但从未有人 在 web agent 场景下系统评测过后者。WAInjectBench 先按威胁模型对攻击做细粒度分类，再构建 覆盖两种模态、两种极性的数据集——来自不同攻击的恶意文本片段、四类正常文本、攻击生成的 恶意图像、两类正常图像。核心结论划出了一条清晰边界：检测器能应对带显式文本指令或可见图像 扰动的攻击，一旦越出这个范围性能急剧下降。

`环境: Web` ｜ [arXiv:2510.01354](https://arxiv.org/abs/2510.01354)

#### RISK: A Framework for GUI Agents in E-commerce Risk Management (RISK) (2025-09)

面向一个 agent 扮演防御方而非攻击目标的领域：电商风控需要通过多步、有状态的交互聚合深度 嵌套的网页数据，这既非传统爬虫所能胜任，也超出大多数 GUI agent 的能力——后者通常局限于 配合良好的页面上的单步任务。RISK 贡献三部分：RISK-Data，通过高保真浏览器框架采集的 8492 条 单步与 2386 条多步交互轨迹；RISK-Bench，覆盖三个难度等级的 802 条单步与 320 条多步轨迹； 以及 RISK-R1，一个 R1 风格的强化微调框架。

`环境: Web` ｜ [arXiv:2509.21982](https://arxiv.org/abs/2509.21982)

#### AdvAgent: Controllable Blackbox Red-teaming on Web Agents (AdvAgent) (2024-10)

黑盒红队框架，摆脱人工编写对抗 prompt 的做法，转而用强化学习流水线训练一个对抗 prompter 模型，依据黑盒 agent 自身的反馈来优化 prompt。其设计目标不只是成功率，而是在隐蔽性之外还要 **可控性**——攻击要保持可操纵，而非仅仅有效。论文报告在多样任务上对基于 GPT-4 的前沿 web agent 取得高成功率，并发现现有基于 prompt 的防御保护有限，这是「单靠 prompt 加固撑不住」 的一个早期证据。

`环境: Web` ｜ [arXiv:2410.17401](https://arxiv.org/abs/2410.17401)

#### ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents (ST-WebAgentBench) (2024-10)

批评那些只测量「任务是否完成」的基准——它们忽略了完成得是否安全、是否达到企业可信任的程度—— 并主张在关键工作流中，安全与可信是采用的前置条件而非附加项。其 222 个任务每个都配有 ST 策略 （编码约束的简明规则），并在用户同意、鲁棒性等六个正交维度上打分。真正留下来的贡献是那个 指标：Completion Under Policy 只把「遵守了所有适用策略」的完成计为成功，而三个开源 agent 在 CuP 下的得分不足其名义成功率的三分之二。

`环境: Web` ｜ [arXiv:2410.06703](https://arxiv.org/abs/2410.06703)
