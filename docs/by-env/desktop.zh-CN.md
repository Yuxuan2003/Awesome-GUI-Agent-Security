# Desktop

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### HazardAuditor: From Executable Threats to Safer Computer-Use Agents (HazardAuditor) (2026-09)

指出护栏模型覆盖 computer-use agent 时的两处断层：现有护栏针对静态 prompt 与回复， 不适配 agent 的执行过程；而现有可执行安全平台只产出评测判定，给不出护栏模型跨异构框架 学习所需的规范化监督信号。HazardAuditor 同时补上两者——基础设施在受控环境中运行 Claude Code、Codex、Hermes、OpenClaw，把它们的交互归一化为统一事件表示，从而支持 跨框架监督。作者还发现一处结构性错配：token 级后训练目标会让更长的推理过程主导梯度更新。 为此提出 Guard Policy Optimization（GuardPO），把确定性的安全结果转换为序列级优势， 并对推理区与判定区分别归一化，使「安全决策」成为真正的优化单元。相比此前最强护栏， 准确率最高提升 16.5 个百分点。

`环境: Desktop, Web` ｜ [arXiv:2609.15134](https://arxiv.org/abs/2609.15134)

#### AgentHijack: Visual Patch Attacks on Multimodal Computer-Use Agents (AgentHijack) (2026-09)

坚持做端到端验证而不止于模型输出：真正要回答的问题是，一个局部视觉补丁能否在「截图输入 → VLM 生成 → 动作解析 → 环境执行」的完整链条上产生**可验证的环境后果**。补丁在作者控制的 GitHub Pages 与本地部署的 CSDN 克隆站上训练与投放，在五个开源或公开可得的 GUI agent / VLM 后端上评测，汇总 600 个实例级在线用例。三级指标清楚地暴露了攻击在哪一环衰减—— T-ASR 84.5%、TAPR 47.0%，而 E2E-ASR 仅 20.3%。轨迹分析发现了最令人不安的现象：在部分 成功案例中，agent 先执行了恶意终端命令，随后又不动声色地继续完成用户原本的良性任务。

`环境: Desktop, Web` ｜ [arXiv:2609.09212](https://arxiv.org/abs/2609.09212)

#### SIR: Self-improving Red-teaming for Compute Use Agents (SIR) (2026-08)

指出现有 CUA 安全基准用的都是人工手写的固定注入载荷，会低估自适应攻击者的真实威胁。提出 黑盒 IPI 攻击 SIR：从一个用自然语言描述的可复用「隐蔽性原则」小库中组合注入内容，再套一层 迭代反馈循环——诊断受害 agent 失败的攻击轨迹，把成功绕过的模式蒸馏回原则库。这把红队从 静态测试变成自我改进的过程，说明固定载荷的评测结论会随攻击者迭代迅速失效。

`环境: Desktop, Web` ｜ [arXiv:2608.30207](https://arxiv.org/abs/2608.30207)

#### CURA: Certified Runtime Alarms for Computer-Use Agents (CURA) (2026-08)

揭示 self-report 这一最廉价的监督通道恰恰在最需要它的地方失效：在 361 个 OSWorld 任务上， 流水线平均分 82.9（超过人类基线 72.4），但 71 次失败里有 64 次（90%）以「成功」收尾， 61 次声称没有遇到任何阻碍，约 9100 次调用中显式的失败上报机制从未被使用。提出外部监控器 CURA，只读 harness 可见的遥测数据，不需模型内部状态、额外 LLM 调用或改 prompt，把运行 轨迹转成带误报率保证的序贯检验：α=0.10 时 CUSUM 告警能在终止前中位 31 步检出 42.3% 的 失败，实测误报率 0.066。

`环境: Desktop` ｜ [arXiv:2608.27808](https://arxiv.org/abs/2608.27808)

#### ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agents Across Devices (ADeptS-Bench) (2026-08)

针对「没有基准能同时考察 CUA 在视觉界面下的安全性与对模糊指令的处理」这一空缺，提出双流 可信度基准 ADeptS-Bench：Safety 流提供威胁嵌在视觉界面中的良性/恶意配对任务，Disambiguation 流考察 agent 在意图模糊时是否会主动澄清。评测 7 个模型的结论相当刺眼——没有模型能在任务 成功率超 80% 的同时把攻击成功率压到 30% 以下；所有模型都会毫不犹豫点下 2.5 万美元订单的 「结账」，也没有一个能识别出被标为「优化」的按钮实际是「恢复出厂设置」。

`环境: Desktop, Mobile` ｜ [arXiv:2608.26204](https://arxiv.org/abs/2608.26204)

#### SynChain: Inducing Computer-Use Agent Systems to Construct Their Own Attack Chains (SynChain) (2026-08)

指出把攻击视为「外部触发、时间有界」的现有防御留下的缺口：CUA 如今会自行生成、存储并复用 skill 与记忆条目这类产物，因此沦陷可以通过 agent 自身的持久化状态在**内部**传播。论文表明 恶意影响能被隐蔽地嵌入自主合成产物的结构冗余中，从而在内部状态更新后存活、并绕过常规审查 机制。SynChain 用「持久化感知的定向监督微调」将这一威胁形式化，诱导 agent 产出被投毒却 外观无害的产物，并在 CUAChain（30 条良性任务链 + 三类攻击目标）上评测其潜伏激活效果。

`环境: Desktop` ｜ [arXiv:2608.06862](https://arxiv.org/abs/2608.06862)

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)

针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI 基准 StepJack，构造 480 个测试用例，把注入载荷分散在多步任务的中间环节，模拟攻击者只能污染 流程某一环的现实约束。实验显示多步注入相比单步把攻击成功率最高抬升 31.2 个百分点， 说明单步评测显著低估了 CUA 的真实暴露面，且现有防御在流程中段几乎不再触发。

`环境: Desktop, 跨环境` ｜ [arXiv:2608.06477](https://arxiv.org/abs/2608.06477)

#### FocusMem: Factorizing Content, Readout, and Trust in Latent GUI Memory (FocusMem) (2026-08)

潜在记忆把多模态 GUI 轨迹压缩成少量连续 token，但现有方法把每条轨迹映射到一个固定 记忆块，且主要靠下一动作监督来训练。由此带来三个实际问题：压缩过程中细节丢失、同一个 记忆块要服务所有决策阶段、检索到不相关的轨迹仍会误导 agent。FocusMem 把这些职责拆开： 角色感知的内容基底促使情景记忆保留可复用经验、工作记忆保留当前任务进展；状态条件化的 读出机制为同一份存储证据生成面向具体决策的视图；轻量的信任门可在检索不可靠时抑制记忆。 最后这一项正是它进入安全清单的理由——它把检索到的记忆当作需要设门的不可信输入， 而这正是对抗记忆投毒式操纵的结构性防御。

`环境: Mobile, Desktop, Web` ｜ [arXiv:2608.04530](https://arxiv.org/abs/2608.04530)

#### Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents (Invisible Ink) (2026-08)

研究攻击者如何把恶意目标伪装在看似合法的任务描述中，使 CUA 在执行用户确认过的正常任务时 顺带完成攻击者目标。核心发现是这类攻击能绕过 human-in-the-loop 确认机制——因为人工审核 看到的动作序列本身每一步都合理，只有组合起来才产生危害。这揭示了「逐步确认」这一主流 防御范式的结构性盲区。

`环境: Desktop` ｜ [arXiv:2608.02018](https://arxiv.org/abs/2608.02018)

#### CUADebug: Diagnosing and Repairing Computer-Use Agent Failures (CUADebug) (2026-07)

面向 CUA 执行失败后的诊断与修复，提出定位失败步骤并生成修复方案的框架。虽以可靠性为 出发点，但其失败归因与状态回滚能力可直接用于安全事件的事后恢复——在 agent 被注入劫持后 判断从哪一步开始偏离、并回退到最后一个可信状态。是「事后恢复」这一防御层中较少见的 系统性工作。

`环境: Desktop` ｜ [arXiv:2608.02643](https://arxiv.org/abs/2608.02643)

#### Agent Data Injection Attacks are Realistic Threats to AI Agents (ADI) (2026-07)

指出间接提示注入的研究几乎全部集中在「指令注入」上——即不可信数据被当作指令解释——而针对 性构建的缓解措施也继承了这个狭窄的问题框架。论文提出 agent 数据注入（ADI）：把恶意数据 伪装成**可信数据**，例如安全关键元数据（资源标识符、数据来源）或 agent 上下文数据（工具 调用与响应格式）。其影响与指令注入相当，agent 依然会执行非预期动作，但那些专门用于识别 「嵌入指令」的防御，没有任何理由把一段格式规范的元数据标记为可疑。

`环境: Web, Desktop` ｜ [arXiv:2607.05120](https://arxiv.org/abs/2607.05120)

#### Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure (Perception-Fusion Gap) (2026-07)

提出一个位于所有视觉攻击上游的问题：多模态 GUI agent 通过两条冗余通道读取界面——渲染后的 像素与序列化结构（DOM 或无障碍树）——并在行动前形成对当前状态的信念，但现有基准从不追问 **这个信念究竟来自哪条通道**。论文形式化了「视觉状态依赖」，用配对的单通道干预在覆盖真实 web / mobile / desktop 界面的 735 个探针上测量，其中 225 个是从线上生产网站挖掘的零编辑 分歧样本，全部采用确定性强制选择评分、不引入模型裁判。核心指标 Perception-Fusion Gap 刻画的是「模型感知正确、但在冲突时倒向结构」的探针占比——而这恰好告诉攻击者该污染哪条通道。

`环境: Web, Mobile, Desktop` ｜ [arXiv:2607.04334](https://arxiv.org/abs/2607.04334)

#### Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? (Capable but Careless) (2026-06)

用「上下文完整性」（contextual integrity）框架考察 CUA 在跨应用操作时是否会不当传播敏感 信息。结论是能力越强的 agent 反而越容易越界：它们为完成任务会主动把 A 应用中的私密数据 带入 B 应用的输入框，而这类行为不触发任何现有的隐私告警，因为每一次读写都在授权范围内。 提出了以信息流而非权限边界为判据的评估方法。

`环境: Desktop` ｜ [arXiv:2606.23189](https://arxiv.org/abs/2606.23189)

#### SkillHarness: Harnessing Safe Skills for Computer-Use Agents (SkillHarness) (2026-06)

针对 skill 学习类方法中一个被默认接受的假设：它们从成功轨迹中蒸馏可复用 skill，却隐含假定 环境是静态且安全的，既忽略提示注入这类对抗交互，也忽略弹窗这类环境动态。在动态环境下，这个 假设会产出有风险的 skill 与脆弱的执行——也就是说漏洞被**固化进**了 agent 的可复用库里。 SkillHarness 把 skill 的学习与使用建模为受安全约束的交互过程，引入「skill 边界」以取代 静态的 skill 抽象。

`环境: Desktop` ｜ [arXiv:2606.20636](https://arxiv.org/abs/2606.20636)

#### OSGuard: A Benchmark for Safety in Computer-Use Agents (OSGuard) (2026-06)

针对一个测量盲区：computer-use agent 通常只以任务完成率评判，但「成功」会掩盖 agent 通过 不安全捷径达成名义目标的情况。OSGuard 在**良性、未被篡改**的用户指令下评估安全性——回路中 没有攻击者——并设计了两个粒度。动作级基准把语境化的候选动作标注为「允许 / 无关 / 不安全」， 每条都相对原始指令与当前界面状态判定。执行套件基于人工构造的 OSWorld 变体，原任务仍可完成， 但环境中埋入了破坏性覆写等潜在危害，并配套保留原成功信号的增强评测器。

`环境: Desktop, Web` ｜ [arXiv:2606.15034](https://arxiv.org/abs/2606.15034)

#### Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming (CUA-HandCrafted) (2026-06)

本领域少见的**复现审计**，结论令人不安：近期 CUA 红队论文报告 42–98% 的攻击成功率，但这些 抢眼数字集中出现在已退役模型、以及各篇论文所测模型中最脆弱的那一个上。作者把这些技术复现为 人工模板，在 793 个 episode（24 个多步网页任务、56 个攻击模板、8 个攻击族、4 种 system prompt 配置）上测量，结果对 Claude Sonnet 4.6 与 GPT-5.4 取得 **0/140 的多步攻击成功率**， 且消融实验显示这种抵抗力存在于模型权重而非 prompt。但它并不泛化：同样的权重在姊妹编码 agent 基准上被人工 skill 注入攻破，成功率最高达 100%。安全性在这里是**领域条件化**的， 而领域内那些偏高的 ASR 数字，更多归因于 RL 优化过的注入文本而非模型固有的脆弱。

`环境: Desktop, Web` ｜ [arXiv:2606.05233](https://arxiv.org/abs/2606.05233)

#### BraveGuard: From Open-World Threats to Safer Computer-Use Agents (BraveGuard) (2026-05)

从「CUA 的危害为何难以捕捉」出发：危害只在多步执行轨迹中浮现，而其中每个单独动作在局部看 都无害，因此孤立的 prompt 与最终回复都看不出问题。BraveGuard 是自我演进的流水线：从近期 研究来源中挖掘新兴风险与攻击模式，将其实例化为可执行的 computer-use 任务，收集 agent rollout，进而导出**轨迹级**监督信号训练护栏模型。由于新威胁与验证失败出现时可以重跑这个 闭环，防御能持续适应，而不是冻结在静态基准训练时所捕捉到的那个快照上。

`环境: Desktop, Web` ｜ [arXiv:2606.01166](https://arxiv.org/abs/2606.01166)

#### MaskClaw: Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution (MaskClaw) (2026-05)

把 GUI agent 隐私问题定义为**裁决**问题而非检测问题：某项内容是否属于隐私取决于任务、接收方、 应用状态与用户角色，因此静态 PII 检测器抓不住这些边界，而云端 VLM 推理又会在决定「什么需要 保护」**之前**就把原始屏幕上传出去。MaskClaw 运行在边缘侧：抽取本地视觉证据、检索用户与任务 专属的策略记忆，在截图离开可信环境前判定 Allow / Mask / Ask。在五个 skill 演进场景中，它把 用户的纠正、取消与编辑转化为可复用的隐私 skill，并经沙箱门校验，评测基准为 P-GUI-Evo。

`环境: Mobile, Desktop` ｜ [arXiv:2605.28646](https://arxiv.org/abs/2605.28646)

#### OTora: A Unified Red Teaming Framework for Reasoning-Level Denial-of-Service in LLM Agents (OTora) (2026-05)

提出一个绝大多数威胁模型完全忽略的攻击目标：推理级拒绝服务（R-DoS）——攻击者**保持任务结果 正确**，却通过膨胀 agent 的推理深度或工具调用预算来损害可用性。正因为输出依然正确，所有 基于正确性的防御与所有检查输出的护栏都会报告「运行正常」。OTora 是两阶段框架：第一阶段用 插入位置感知打分与动态目标共进化优化对抗触发串，诱导定向的工具调用（支持黑盒与白盒）； 第二阶段通过 ICL 引导的遗传搜索生成推理载荷，在保持结果正确的同时放大「过度思考」。 在 WebShop、Email 与 OS agent 上评测，骨干模型含 LLaMA-70B 与 GPT-OSS-120B。

`环境: Web, Desktop` ｜ [arXiv:2605.08876](https://arxiv.org/abs/2605.08876)

#### Constraining Host-Level Abuse in Self-Hosted Computer-Use Agents via TEE-Backed Isolation (TEE-Backed Isolation) (2026-05)

针对 OpenClaw 这类自托管 CUA——它们把自然语言交互与对浏览器、文件、脚本、系统命令、外发 通道的直接访问绑在一起，这种组合使任何一次成功的引导都会演变成主机级滥用，无论引导来自恶意 消息、间接注入、不安全 skill，还是对主机侧控制路径的篡改。核心论点在于解释「为何黑名单行 不通」：一个操作的安全关键性由动作类型、目标对象、执行上下文与潜在影响**共同**决定，任何 静态规则都刻画不了。设计上让普通功能留在受约束的 REE 路径，而把安全关键的分类判定移到 TEE 边界之后。

`环境: Desktop` ｜ [arXiv:2605.06393](https://arxiv.org/abs/2605.06393)

#### OS-SPEAR: A Toolkit for the Safety, Performance, Efficiency, and Robustness Analysis of OS Agents (OS-SPEAR) (2026-04)

诊断出当前 OS agent 基准的三个具体缺陷——安全场景狭窄、轨迹标注噪声大、鲁棒性指标有限—— 并以覆盖安全性、性能、效率、鲁棒性四个维度的工具包作答。各子集是分别构建而非从同一池中 重新加权得来：安全子集同时覆盖环境诱发与人为诱发的危害，性能子集通过轨迹价值估计与分层 采样策划，效率子集从双重视角度量。把安全作为四个耦合维度之一、而非一个独立分数来处理， 这个框定方式值得借鉴。

`环境: Desktop` ｜ [arXiv:2604.24348](https://arxiv.org/abs/2604.24348)

#### Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents (PUSV) (2026-04)

把「截图—点击」循环中的观察到动作间隔（真实 OSWorld 负载下平均 6.51 秒）形式化为「视觉 原子性破坏」，指出这构成一个 TOCTOU 窗口，无特权攻击者可在其中篡改 UI 状态。刻画三种攻击 原语：通知覆盖劫持、窗口焦点操纵、网页 DOM 注入——其中第二种是 Android Action Rebinding 的桌面对应物，动作重定向成功率 100% 且在观察时刻不留任何视觉痕迹。提出 PUSV 防御，在每次 动作派发前立即复验 UI 状态（点击目标处的掩码像素 SSIM、全局截图差分、X Window 快照差分）， 在 180 次对抗试验中拦截率 100%、零误报、开销低于 0.1 秒。

`环境: Desktop` ｜ [arXiv:2604.18860](https://arxiv.org/abs/2604.18860)

#### The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents (OS-BLIND) (2026-04)

隔离出现有安全评测跳过的那个场景：用户指令完全良性，危害来自任务上下文或执行后果，既无 滥用也无注入。OS-BLIND 提供 300 个人工构造任务，覆盖 12 个类别、8 个应用，分为「环境 嵌入型威胁」与「agent 自发危害」两簇。数字相当刺眼——多数 CUA 的攻击成功率超过 90%， 即便经过安全对齐的 Claude 4.5 Sonnet 也达到 73.0%。更糟的是，同一模型置于多 agent 配置中时 ASR 从 73.0% 升至 92.7%，说明编排本身就在侵蚀对齐效果。

`环境: Desktop` ｜ [arXiv:2604.10577](https://arxiv.org/abs/2604.10577)

#### Preference Redirection via Attention Concentration: An Attack on Computer Use Agents (PRAC) (2026-04)

指出以往 CUA 攻击工作集中在语言模态，视觉模态受到的关注远远不足，随后就攻在这里。PRAC 不 直接操纵 VLM 的输出，而是通过把注意力重定向到一个隐蔽的对抗补丁上，改变模型的**内部偏好**， 从而在网购平台上把 CUA 的商品选择引导到指定目标。攻击构造需要白盒访问，但真正值得注意的 结论是可迁移性：攻击对同一模型的微调版本依然有效——这意味着被众多部署 agent 共用的同一个 基座模型，会变成一处共享的软肋。

`环境: Desktop, Web` ｜ [arXiv:2604.08005](https://arxiv.org/abs/2604.08005)

#### AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents (AgentHazard) (2026-04)

针对 CUA 具备跨工具、跨文件持久化操作能力后产生的新型安全风险，构建覆盖多风险类别与 攻击策略的基准 AgentHazard，含 2653 个实例。关键结论是有害行为往往由一串「单看都合理、 合起来不安全」的动作累积产生。实测 Claude Code 搭配 Qwen3-Coder 的攻击成功率达 73.63%， 表明仅靠底座模型的对齐无法保障 agent 层面的安全。

`环境: Desktop` ｜ [arXiv:2604.02947](https://arxiv.org/abs/2604.02947)

#### "What Did It Actually Do?": Understanding Risk Awareness and Traceability for Computer-Use Agents (What Did It Actually Do) (2026-03)

在个人化 agent 从专家圈走向大众使用的背景下研究 CUA 风险的人因侧：这类系统会安装 skill、 调用工具、访问私有资源、修改本地环境，但用户通常并不清楚自己授予了什么权限、agent 实际 做了什么、以及事后是否被干净卸载。工作把 OpenClaw 生态的多来源语料（安全事件、公告、恶意 skill 报告、新闻报道、教程、社交媒体叙述）与面向用户和从业者的访谈研究结合起来。发现是： 受访者在抽象层面认得出这类系统有风险，却缺乏关于权限与持久化的具体心智模型。

`环境: Desktop` ｜ [arXiv:2603.28551](https://arxiv.org/abs/2603.28551)

#### WebPII: Benchmarking Visual PII Detection for Computer-Use Agents (WebPII) (2026-03)

CUA 从两个方向带来新的隐私风险：从真实网站采集的训练数据不可避免含敏感信息，而云端推理 会暴露用户截图。此前没有公开基准用于检测网页截图中的个人身份信息。WebPII 提供 44865 张 标注的电商 UI 图像，特点包括扩展的 PII 分类（含可用于重识别的交易级标识符）、针对用户 正在填写的半完成表单的前瞻式检测、以及基于 VLM 的可扩展 UI 复现。配套 WebRedact 把 文本抽取基线准确率翻倍以上（0.753 vs 0.357 mAP@50），CPU 延迟仅 20ms。

`环境: Web, Desktop` ｜ [arXiv:2603.17357](https://arxiv.org/abs/2603.17357)

#### Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents (Visual Confused Deputy) (2026-03)

把 CUA 的感知失败从「性能局限」重新定义为安全问题：以往工作只问动作是否成功，不问 agent 作用的对象是否正确。论文形式化了「视觉混淆代理」这一失效模式——agent 基于误判的 屏幕状态授权动作，成因可以是 grounding 错误、对抗性截图篡改或 TOCTOU 竞态。关键之处 在于，简单的屏幕层篡改就能把常规点击重定向为特权操作，而表现上与普通 agent 失误无法 区分，使攻击具备可否认性。提出的护栏是首个运行在 agent 感知回路之外的方案，用双通道 对比分类独立校验点击目标。

`环境: Desktop` ｜ [arXiv:2603.14707](https://arxiv.org/abs/2603.14707)

#### You Told Me to Do It: Measuring Instructional Text-induced Private Data Leakage in LLM Agents (ReadSecBench) (2026-03)

把这一结构性问题命名为「可信执行者困境」（Trusted Executor Dilemma）：高权限 agent 被授予 终端访问、文件系统控制与出网能力，然后被要求阅读并执行项目文档——但它无法区分恶意指令与 正常的安装配置说明，因此会以很高的比率执行嵌在文档里的对抗指令。论文强调这是「指令遵循」 设计范式的必然后果，而非实现层面的 bug。测量以三维分类法（语言伪装、结构混淆、语义抽象） 组织，基准 ReadSecBench 由 500 个真实 README 文件构成。

`环境: Desktop` ｜ [arXiv:2603.11862](https://arxiv.org/abs/2603.11862)

#### When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents (DeAction) (2026-02)

把通常被分开研究的两类失效来源统一起来：源自外部攻击（如间接提示注入）的偏离动作，与源自 内部局限（如推理错误）的偏离动作——两者都背离用户意图、都损害安全性与任务可靠性，因此只针对 攻击设计的检测器会漏掉一半问题。工作定义了 CUA 的「偏离动作检测」任务，归纳出真实部署中的 三类常见情形，并基于真实轨迹构建带人工标注的动作级对齐标签基准 MisActBench。DeAction 是 通用护栏，在执行前检出偏离动作，并通过结构化反馈迭代纠正。

`环境: Desktop` ｜ [arXiv:2602.08995](https://arxiv.org/abs/2602.08995)

#### When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents (AutoElicit) (2026-02)

观察到 CUA 即便在良性输入下也确实会产生不安全的非预期行为，但对这类风险的探索一直停留在 个案层面——既无具体刻画，也无自动化手段挖掘长尾情形。论文提供了首个关于 CUA 非预期行为的 概念与方法框架：定义其关键特征、自动化诱发、并分析它如何从良性输入中产生。AutoElicit 利用 CUA 的执行反馈迭代扰动良性指令，同时保持扰动本身真实且无恶意，从 Claude 4.5 Haiku、Opus 等前沿模型上挖掘出数百个有害行为。

`环境: Desktop` ｜ [arXiv:2602.08235](https://arxiv.org/abs/2602.08235)

#### LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios (LPS-Bench) (2026-02)

指出现有基准在**时机**上的缺口：它们聚焦短周期或 GUI 层任务、评判执行期错误，却从未检验 agent 能否在**规划阶段**（任何动作发生之前）预见风险。LPS-Bench 评测基于 MCP 的 CUA 在 长周期任务下的规划期安全意识，覆盖良性与对抗两类交互，含 7 个任务域、9 类风险的 65 个场景， 配以多 agent 自动化数据生成流水线与针对规划轨迹的 LLM-as-a-judge 评测协议。实验显示现有 CUA 在长程规划中维持安全意识的能力存在明显不足。

`环境: Desktop` ｜ [arXiv:2602.03255](https://arxiv.org/abs/2602.03255)

#### SafePred: A Predictive Guardrail for Computer-Using Agents via World Models (SafePred) (2026-02)

指出现有 CUA 护栏的共同盲区：它们都是被动式的，只在当前观测空间内约束行为，因此能拦下 「点击钓鱼链接」这类即时危害，却看不见长周期风险。文中的例子很到位——清理日志在局部看 完全合理，但会导致未来审计无从追溯，而这个后果在当前观测里根本不可见。SafePred 转而把 预测出的未来风险与当前决策对齐，建立「风险到决策」的闭环，使延迟发生、不可逆的后果能被 计入每一步的判断。

`环境: Desktop` ｜ [arXiv:2602.01725](https://arxiv.org/abs/2602.01725)

#### GUIGuard-Bench: Toward a General Evaluation for Privacy-Preserving GUI Agents (GUIGuard-Bench) (2026-01)

指出现有视觉隐私数据集多为静态自然图像，因而无法刻画 GUI 工作流中界定隐私风险的两个性质： 上下文依赖与任务相关性。GUIGuard-Bench 提供 241 条真实 GUI agent 轨迹、涵盖 Android 与 PC 环境的 4080 张截图。真正的贡献在标注设计——每张截图在区域级标注隐私边界框、语义类别、 风险等级，以及关键的一项：该隐私信息是否为完成任务所必需。而这恰恰是遮蔽类防御必须判断 正确的那个区分。

`环境: Mobile, Desktop` ｜ [arXiv:2601.18842](https://arxiv.org/abs/2601.18842)

#### MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction (MirrorGuard) (2026-01)

点明基于检测的防御悄悄付出的代价：拦截虽能避免损害，但常常过早中止任务，等于用效用换安全。 MirrorGuard 转而去**纠正不安全的推理**，并用神经符号仿真流水线解决训练成本问题——完全在 文本化的模拟环境中生成真实感的高风险 GUI 交互轨迹，捕捉不安全推理模式与潜在系统危害， 而无需在真实操作系统上执行任何破坏性操作。最终得到的是即插即用的防御，把仿真中训练出的 纠正能力迁移到真实部署。

`环境: Desktop` ｜ [arXiv:2601.12822](https://arxiv.org/abs/2601.12822)

#### CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents (NOVA) (2026-01)

正面处理一个真实的架构僵局：架构隔离通过严格分离「可信规划」与「不可信观测」提供了最强的 注入防护保证，但 CUA 必须持续观测 UI 才能决定每一步动作——这两项要求直接冲突。论文用一个 经检验成立的经验判断来破局：UI 工作流虽然是动态的，但在**结构上是可预测的**。因此 NOVA 采用单次规划：由可信规划器预先给出一份覆盖所有可预期运行时状态的完整分支计划，从而对任意 指令注入提供控制流完整性**保证**，而不是尽力而为的检测。

`环境: Desktop` ｜ [arXiv:2601.09923](https://arxiv.org/abs/2601.09923)

#### SusBench: An Online Benchmark for Evaluating Dark Pattern Susceptibility of Computer-Use Agents (SusBench) (2025-10)

评测 CUA 对 UI 暗黑模式（诱导用户做出非本意操作的界面设计）的易感程度：从既有分类法中选取 九种常见类型，通过代码注入在真实消费类网站上构造可信实例，形成覆盖 55 个网站的 313 个评测 任务。方法上的强项在于人类验证环节——29 名参与者的实验确认这些注入看起来高度真实，绝大多数 人完全没有察觉它们是研究团队植入的。正是这一对照使得「五个前沿 CUA 与人类参与者并排比较」 的结论具备可信度。

`环境: Web, Desktop` ｜ [arXiv:2510.11035](https://arxiv.org/abs/2510.11035)

#### Secure and Efficient Access Control for Computer-Use Agents via Context Space (CSAgent) (2025-09)

主张把计算机控制权交给 agent 之所以危险，根源在 LLM 固有的不确定性——一旦动作偏离用户 意图，后果可能不可逆；而用户确认与基于 LLM 的动态校验分别在可用性、安全性或性能上有短板。 CSAgent 是系统级、基于静态策略的访问控制框架，通过「意图感知 + 上下文感知」策略弥合静态 策略与动态上下文之间的落差，并提供自动化工具链协助开发者构造与精炼策略，最终由优化过的 操作系统服务强制执行，确保动作只在特定用户意图与上下文下才被允许。

`环境: Desktop` ｜ [arXiv:2509.22256](https://arxiv.org/abs/2509.22256)

#### AgentSentinel: An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents (AgentSentinel) (2025-09)

把威胁模型与传统的 prompt 安全区分开：这里的危险不只来自不安全的用户输入，还来自 agent 自身不稳定的 LLM 决策所生成的工具调用，而这类漏洞横跨 computer-use agent 的每个组件。 AgentSentinel 拦截 agent 相关服务内的所有敏感操作并暂停执行，直到安全审计完成——也就是 把强制点放在服务边界而非 prompt 层。其审计机制会跨组件关联证据，而不是孤立地判断每次调用。

`环境: Desktop` ｜ [arXiv:2509.07764](https://arxiv.org/abs/2509.07764)

#### VeriOS: Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents (VeriOS) (2025-09)

多数 OS agent 是为理想化环境设计的，而真实环境常常并不可信——因此要防的失败模式是 「过度执行」。VeriOS 没有外挂一层过滤器，而是把「何时该问人」变成一种可学习的能力： 提出查询驱动的人-agent-GUI 交互框架，让 agent 在正常条件下自主执行、在不可信场景中 主动向用户发问。VeriOS-Agent 采用三阶段训练（监督微调 + 组相对策略优化），目的是把 关于「可信性」的元知识与任务知识解耦，使两者可以独立调用。这个设定对 §2.4 很有意义： 确认机制不再是硬加在上层的固定策略，而是 agent 自己必须学会有选择地做出的决策。

`环境: Mobile, Desktop` ｜ [arXiv:2509.07553](https://arxiv.org/abs/2509.07553)

#### Reliable Weak-to-Strong Monitoring of LLM Agents (CUA-SHADE-Arena) (2025-08)

压力测试针对 agent 隐蔽违规（如私下分享隐私信息）的监控系统：设计「监控器红队」工作流， 变化 agent 与监控器各自的情境感知程度，施加含提示注入的规避策略，并在面向工具调用 agent 的 SHADE-Arena 与新构建的 CUA-SHADE-Arena（把 TheAgentCompany 扩展到 computer-use agent） 上运行。核心发现不对称且反直觉：**agent 的感知压制监控器的感知**——agent 一旦知道自己正被 监控，监控可靠性显著下降；而反过来给监控器提供更多关于 agent 的信息，帮助要小得多。

`环境: Desktop` ｜ [arXiv:2508.19461](https://arxiv.org/abs/2508.19461)

#### Measuring Harmfulness of Computer-Using Agents (CUAHarm) (2025-07)

指出现有基准评测的是聊天机器人或简单工具调用场景下的 LM，无法测量一个 CUA 实际能对机器做到 什么。CUAHarm 提供 104 项专家撰写的真实滥用风险——关闭防火墙、外泄数据、安装后门——置于带 规则化可验证奖励的沙箱中，因此指标是防火墙**是否真的被关掉**，而不是模型是否口头拒绝。 结果很难被轻描淡写：在完全不加越狱提示的情况下，前沿模型的执行成功率就很高，Gemini 2.5 Pro 达到 90%。论文还观察到，那些在以往基准上更安全的新模型，在这里并没有更安全。

`环境: Desktop` ｜ [arXiv:2508.00935](https://arxiv.org/abs/2508.00935)

#### LaSM: Layer-wise Scaling Mechanism for Defending Pop-up Attack on GUI Agents (LaSM) (2025-07)

指出针对弹窗式环境注入的现有防御要么需要昂贵重训、要么在归纳性干扰下失效，转而走机制 可解释性路线。论文系统研究这类攻击如何改变 GUI agent 的注意力分布，发现正确输出与错误输出 之间存在**逐层的注意力发散模式**。LaSM 直接利用这一发现，选择性放大关键层的注意力与 MLP 模块，无需任何额外训练即把模型显著性重新对齐到任务相关的屏幕区域——这是把可解释性结论 转化为可部署 GUI agent 防御的少见案例。

`环境: Desktop, Web` ｜ [arXiv:2507.10610](https://arxiv.org/abs/2507.10610)

#### VisualTrap: A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation (VisualTrap) (2025-07)

把「视觉 grounding」——即从文本计划到具体 GUI 元素的映射——认定为一个独立的攻击面，与规划和 推理层面区分开来。其后果正是危险之处：植入 grounding 的后门会在 agent **拿到完全正确的 解题计划时**依然改变其行为，因此检查计划本身看不出任何问题。VisualTrap 通过误导 agent 把 文本计划定位到攻击者选定的位置来劫持 grounding，这意味着所有计划级审查与推理审计都能干净 通过，而动作却落在攻击者想要的地方。

`环境: Mobile, Desktop` ｜ [arXiv:2507.06899](https://arxiv.org/abs/2507.06899)

#### A Systematization of Security Vulnerabilities in Computer Use Agents (CUA Vuln SoK) (2025-07)

对真实 CUA 做系统化威胁分析与对抗测试，归纳出七类该范式独有的风险，并深入剖析三个具体 利用链：用视觉覆盖层误导界面级推理的 clickjacking、经工具链串联实现远程代码执行的间接提示 注入、以及通过操纵隐式界面语境劫持多步推理的 CoT 暴露攻击。三个案例共同指向当前实现的 三处架构性缺陷：缺少输入来源追踪、界面与动作绑定薄弱、控制流完整性不足。

`环境: Desktop, Web` ｜ [arXiv:2507.05445](https://arxiv.org/abs/2507.05445)

#### OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents (OS-Harm) (2025-06)

指出 CUA 已在快速部署但安全性长期被忽视，基于 OSWorld 环境构建 OS-Harm，考察三类危害： 用户故意滥用、提示注入攻击、模型自身失当行为。含 150 个任务，覆盖骚扰、侵犯版权、虚假 信息、数据外泄等违规类型，要求 agent 操作邮件客户端、代码编辑器、浏览器等多种应用。 配套自动评判器同时评估准确性与安全性，与人工标注一致性达 0.76 / 0.79 F1。

`环境: Desktop` ｜ [arXiv:2506.14866](https://arxiv.org/abs/2506.14866)

#### VerificAgent: Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents (VerificAgent) (2025-06)

把持久化记忆当作一个**显式的对齐面**来处理，理由是：持续的记忆增强让 CUA 能从过往交互中学习， 但未经审核的记忆会编码领域不适当或不安全的启发式规则——这些伪规则会悄然偏离用户意图与安全 约束。VerificAgent 结合三部分：专家策划的领域知识种子、训练期基于轨迹的迭代记忆增长、以及 部署前的人工事实核查环节。真正的贡献在其框定方式：让人类**一次性**纠正高影响错误，就把 经核验的记忆变成一份「冻结的安全契约」，后续所有动作都必须满足它，且无需微调模型。

`环境: Desktop` ｜ [arXiv:2506.02539](https://arxiv.org/abs/2506.02539)

#### VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents (VPI-Bench) (2025-06)

指出以往工作集中在浏览器 agent 与 HTML 层攻击上，而握有完整系统权限、能操作文件、读取用户 数据、执行任意命令的 CUA 反而研究不足。VPI-Bench 研究**视觉嵌入**于渲染界面中的恶意指令 ——这类指令在构造上就绕开了文本层净化——并提供覆盖五个常用平台的 306 个测试用例。每个用例都是 真实网页平台的交互式变体，部署在真实环境中并含一处视觉嵌入的恶意 prompt，同时覆盖 CUA 与 browser-use agent 两类目标。

`环境: Desktop, Web` ｜ [arXiv:2506.02456](https://arxiv.org/abs/2506.02456)

#### RiOSWorld: Benchmarking the Risk of Multimodal Computer-Use Agents (RiOSWorld) (2025-05)

正面提出「迁移性」问题：为对话场景下的通用 MLLM 设计并对齐的安全风险原则，能否有效迁移到 真实的计算机操作场景？论文指出以往的风险评测总在两点之一上失守——要么缺乏真实的交互环境， 要么把范围收窄到少数几类特定风险——而这两种失守都忽略了真实环境所固有的复杂性与多变性。 RiOSWorld 在真实的计算机操作过程中评测风险，已成为多模态 CUA 风险评测中被较多引用的基准之一。

`环境: Desktop` ｜ [arXiv:2506.00618](https://arxiv.org/abs/2506.00618)
