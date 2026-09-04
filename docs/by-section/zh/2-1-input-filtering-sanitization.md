# 2.1 输入侧过滤与净化

*Input Filtering & Sanitization*

[← 返回索引](../../../README.zh-CN.md#21-输入侧过滤与净化) ｜ [English](../en/2-1-input-filtering-sanitization.md)

*在内容进入模型上下文前过滤或遮蔽不可信部分*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Untrusted Content Masking for Web Agents with Security Guarantees (UCM) (2026-07)

指出可证明的注入防御依赖可信指令与不可信数据之间的严格隔离，这在纯文本的 tool-use 场景 中天然成立（agent 可只依据接口定义推理，无需接触不可信内容），但 web agent 必须先观察 渲染后的页面才能感知环境，而页面把可信与不可信内容结构性地混在一起，导致安全保证赖以 成立的信任边界消失。提出 Untrusted Content Masking，利用页面的结构特性在 web 环境中 重建这一边界，使既有的可证明防御能够迁移过来。

`环境: Web` ｜ [arXiv:2607.05277](https://arxiv.org/abs/2607.05277)

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
