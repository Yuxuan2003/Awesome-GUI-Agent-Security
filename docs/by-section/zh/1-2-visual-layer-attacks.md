# 1.2 视觉层攻击

*Visual-Layer Attacks*

[← 返回索引](../../../README.zh-CN.md#12-视觉层攻击) ｜ [English](../en/1-2-visual-layer-attacks.md)

*对抗补丁、弹窗诱导、排版攻击、截图污染*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### When Agents See Differently: Exposing UI Desynchronization Threats in Mobile Agents (UI Desynchronization) (2026-09)

人类监督 mobile agent 依赖一个未被言明的前提：用户与 agent 从同一界面看到一致的信息。 本文证明这个前提可被系统性打破。用户经由物理屏幕与人类视觉系统感知界面，受遮挡与亮度 对比度限制；而 agent 消费的是数字截图，还额外拿到暴露非视觉控件元数据的无障碍表示。 同一个 UI 状态因此向双方呈现实质不同的信息，作者称之为「人机 UI 失同步」。实验表明， 重打包的合法 APK 克隆可以利用这一失同步把 agent 引向攻击者指定的动作，同时对人类用户 保持功能与行为完全一致；扰动在部署前嵌入，无需获取运行时指令、无需检测 agent、无需在线 适配。在五个 mobile agent 框架、三个主干模型、546 个任务上，静态与动态误导率分别为 77.9% 与 66.9%。186 人的问卷研究进一步确认这些视觉扰动人眼难以察觉。

`环境: Mobile` ｜ [arXiv:2609.16732](https://arxiv.org/abs/2609.16732)

#### AgentHijack: Visual Patch Attacks on Multimodal Computer-Use Agents (AgentHijack) (2026-09)

坚持做端到端验证而不止于模型输出：真正要回答的问题是，一个局部视觉补丁能否在「截图输入 → VLM 生成 → 动作解析 → 环境执行」的完整链条上产生**可验证的环境后果**。补丁在作者控制的 GitHub Pages 与本地部署的 CSDN 克隆站上训练与投放，在五个开源或公开可得的 GUI agent / VLM 后端上评测，汇总 600 个实例级在线用例。三级指标清楚地暴露了攻击在哪一环衰减—— T-ASR 84.5%、TAPR 47.0%，而 E2E-ASR 仅 20.3%。轨迹分析发现了最令人不安的现象：在部分 成功案例中，agent 先执行了恶意终端命令，随后又不动声色地继续完成用户原本的良性任务。

`环境: Desktop, Web` ｜ [arXiv:2609.09212](https://arxiv.org/abs/2609.09212)

#### Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure (Perception-Fusion Gap) (2026-07)

提出一个位于所有视觉攻击上游的问题：多模态 GUI agent 通过两条冗余通道读取界面——渲染后的 像素与序列化结构（DOM 或无障碍树）——并在行动前形成对当前状态的信念，但现有基准从不追问 **这个信念究竟来自哪条通道**。论文形式化了「视觉状态依赖」，用配对的单通道干预在覆盖真实 web / mobile / desktop 界面的 735 个探针上测量，其中 225 个是从线上生产网站挖掘的零编辑 分歧样本，全部采用确定性强制选择评分、不引入模型裁判。核心指标 Perception-Fusion Gap 刻画的是「模型感知正确、但在冲突时倒向结构」的探针占比——而这恰好告诉攻击者该污染哪条通道。

`环境: Web, Mobile, Desktop` ｜ [arXiv:2607.04334](https://arxiv.org/abs/2607.04334)

#### MIRAGE: Stealthy Visual Prompt Injection for Vulnerability Detection in Web Agents (MIRAGE) (2026-06)

批评现有针对多模态 web agent 的对抗评测普遍采用过于宽松的威胁模型、依赖视觉上显眼的 伪影。本文转向受约束的现实设定：评测者只是不具特权的第三方（如商家或广告主），仅能控制 广告位、赞助卡片这类语义合法且空间受限的区域。在此约束下提出视觉间接注入框架 MIRAGE， 实现对下一步动作的定向劫持，说明即便攻击者只掌握页面上一小块合法区域，也足以操纵 基于视觉的 agent。

`环境: Web` ｜ [arXiv:2606.20717](https://arxiv.org/abs/2606.20717)

#### Penny Wise, Pixel Foolish: Bypassing Price Constraints in Multimodal Agents via Visual Adversarial Perturbations (PriceBlind) (2026-04)

基于多模态大模型的移动 agent 已开始执行高风险的金融交易，但其对抗鲁棒性研究不足。本文提出 「视觉支配幻觉」：在基于截图、受价格约束的场景中，不可感知的视觉线索会压过文本价格证据， 使 agent 做出非理性决策。PriceBlind 是一个隐蔽的白盒攻击框架，利用 CLIP 系列编码器的模态 间隙，通过「语义解耦损失」把图像嵌入对齐到低成本、与价格相关的锚点上，同时保持像素级保真。 在 E-ShopBench 上白盒评测的攻击成功率约 80%；在简化的单轮坐标选择协议下，Ensemble-DI-FGSM 对 GPT-4o、Gemini-1.5-Pro 与 Claude-3.5-Sonnet 的迁移成功率约 35–41%。鲁棒编码器与 Verify-then-Act 防御能大幅降低攻击成功率，代价是部分干净准确率损失。

`环境: Mobile` ｜ [arXiv:2604.16515](https://arxiv.org/abs/2604.16515)

#### Preference Redirection via Attention Concentration: An Attack on Computer Use Agents (PRAC) (2026-04)

指出以往 CUA 攻击工作集中在语言模态，视觉模态受到的关注远远不足，随后就攻在这里。PRAC 不 直接操纵 VLM 的输出，而是通过把注意力重定向到一个隐蔽的对抗补丁上，改变模型的**内部偏好**， 从而在网购平台上把 CUA 的商品选择引导到指定目标。攻击构造需要白盒访问，但真正值得注意的 结论是可迁移性：攻击对同一模型的微调版本依然有效——这意味着被众多部署 agent 共用的同一个 基座模型，会变成一处共享的软肋。

`环境: Desktop, Web` ｜ [arXiv:2604.08005](https://arxiv.org/abs/2604.08005)

#### Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection (Semantic UI Injection) (2026-04)

指出现有 GUI agent 红队研究的两个局限：对抗扰动需要商业部署中拿不到的白盒访问，而提示 注入正被日益增强的安全对齐所化解。提出黑盒范式「语义级 UI 元素注入」——把本身安全对齐、 内容无害的 UI 元素叠加到截图上以误导视觉 grounding，用模块化的 Editor-Overlapper-Victim 流水线配合迭代搜索。在 8 个模型家族共 19 个受害模型上，策略化优化相比随机注入在最鲁棒的 模型上高出 3.5–6.9 倍，且跨架构迁移性近乎完美。

`环境: 跨环境` ｜ [arXiv:2604.07831](https://arxiv.org/abs/2604.07831)

#### Visual Confused Deputy: Exploiting and Defending Perception Failures in Computer-Using Agents (Visual Confused Deputy) (2026-03)

把 CUA 的感知失败从「性能局限」重新定义为安全问题：以往工作只问动作是否成功，不问 agent 作用的对象是否正确。论文形式化了「视觉混淆代理」这一失效模式——agent 基于误判的 屏幕状态授权动作，成因可以是 grounding 错误、对抗性截图篡改或 TOCTOU 竞态。关键之处 在于，简单的屏幕层篡改就能把常规点击重定向为特权操作，而表现上与普通 agent 失误无法 区分，使攻击具备可否认性。提出的护栏是首个运行在 agent 感知回路之外的方案，用双通道 对比分类独立校验点击目标。

`环境: Desktop` ｜ [arXiv:2603.14707](https://arxiv.org/abs/2603.14707)

#### Invisible to Humans, Triggered by Agents: Stealthy Jailbreak Attacks on Mobile Vision-Language Agents (Agent-Only Perceptual Injection) (2025-10)

此前针对移动 agent 的视觉注入要么依赖用户能察觉的持续视觉篡改，要么需要系统级权限。 本文找到一个更干净的触发条件：人与 agent 的交互存在稳定差异——自动化 agent 产生的 接触式触摸信号近乎为零。这个信号被用作判别器，从而实现「仅对 agent 生效的感知注入」： 恶意内容只在 agent 交互时暴露，人类用户则不易感知。为适配移动 UI 约束与一次性交互场景， 作者提出 HG-IDA*，用单次优化构造可绕过 LVLM 安全过滤的越狱提示。这个机制的巧妙之处在于 它不是把载荷藏起来不让人看见，而是在证明「触摸者不是人」之前根本不投放载荷。

`环境: Mobile` ｜ [arXiv:2510.07809](https://arxiv.org/abs/2510.07809)

#### Cross-Modal Content Optimization for Steering Web Agent Preferences (CPS) (2025-10)

基于视觉语言模型的 web agent 正越来越多地承担内容推荐、商品排序等高风险选择任务。已有工作 表明攻击者可以通过对抗弹窗、图像扰动或内容微调来偏置结果，但往往假设很强的白盒访问、只用 单模态扰动，或采用不现实的设置。本文首次证明：在现实可达的攻击者能力下，联合利用视觉与 文本两个通道能产生远更强的偏好操纵。CPS 同时优化商品图像的不可感知改动与其自然语言描述， 利用 CLIP 可迁移的图像扰动与 RLHF 带来的语言偏好偏置。威胁模型刻意设得很弱 —— 一个无 特权的攻击者只能编辑自己商品的图片与文本元数据，完全看不到模型内部。在 GPT-4.1、 Qwen-2.5VL 与 Pixtral-Large 上的影视选择与电商任务中，CPS 稳定优于主流基线，而检测率 低约 70%。

`环境: Web` ｜ [arXiv:2510.03612](https://arxiv.org/abs/2510.03612)

#### WebInject: Prompt Injection Attack to Web Agents (WebInject) (2025-05)

基于多模态大模型的 web agent 是依据网页截图来生成动作的。WebInject 换了一条攻击路径： 它不碰任何文本通道，而是直接操纵渲染网页 —— 对页面的原始像素值施加扰动，这些像素被映射 进截图之后，就能诱导 agent 执行攻击者指定的动作。作者把寻找扰动形式化为一个优化问题， 核心难点在于原始像素值到截图的映射不可微，梯度无法回传；解决办法是训练一个神经网络来近似 该映射，再对重构后的问题使用投影梯度下降。在多个数据集上的大量评测表明，WebInject 非常 有效，显著优于已有基线方法。

`环境: Web` ｜ `发表: EMNLP 2025` ｜ [arXiv:2505.11717](https://arxiv.org/abs/2505.11717)

#### MIP against Agent: Malicious Image Patches Hijacking Multimodal OS Agents (MIP) (2025-03)

操作系统 agent 让视觉语言模型通过截图捕获、解析并调用鼠标点击与键盘输入等底层 API 直接 操控电脑，因此一旦失败或被操纵，后果是即时而具体的。本文揭示了一种新的攻击向量 —— 恶意 图像补丁（MIP）：对屏幕局部区域做对抗性扰动，OS agent 截图捕获到该区域后就会被诱导调用 特定 API 执行有害动作。例如把 MIP 嵌入桌面壁纸或在社交媒体上传播，就能让 OS agent 外泄 用户的敏感数据。实验表明 MIP 能跨不同的用户提示与屏幕配置泛化，并且即便 agent 正在执行 完全良性的指令也能被劫持，说明在大规模部署之前必须先解决这些关键安全漏洞。

`环境: 跨环境` ｜ `发表: NeurIPS 2025` ｜ [arXiv:2503.10809](https://arxiv.org/abs/2503.10809)

#### Dissecting Adversarial Robustness of Multimodal LM Agents (ARE) (2024-06)

与聊天机器人不同，agent 是多个组件共同执行动作的复合系统，而现有语言模型安全评估并未充分 覆盖这一点。作者在 VisualWebArena 这一真实环境上人工构造了 200 个定向对抗任务与评估脚本， 并提出 ARE（Agent Robustness Evaluation）框架：把 agent 视为展示组件间中间输出流动的图， 将鲁棒性分解为对抗信息在图上的流动。实验表明，只需对单张图像施加不足页面总像素 5% 的 不可感知扰动，就能劫持基于黑盒前沿模型、甚至带反思与树搜索机制的 agent，定向对抗目标 成功率最高达 67%。ARE 还能严格衡量增加组件后鲁棒性如何变化：一旦攻击者污染了反思 agent 所用的评估器或树搜索 agent 的价值函数，攻击成功率分别相对提高 15% 与 20%。这意味着通常 能提升良性表现的推理时计算，反而会打开新的漏洞。

`环境: Web` ｜ `发表: ICLR 2025` ｜ [arXiv:2406.12814](https://arxiv.org/abs/2406.12814)
