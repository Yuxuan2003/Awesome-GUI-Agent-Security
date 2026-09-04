# 1.3 环境注入

*Environmental Injection*

[← 返回索引](../../../README.zh-CN.md#13-环境注入) ｜ [English](../en/1-3-environmental-injection.md)

*UI 元素注入、无障碍树、伪造通知、覆盖层*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments (AnTrap) (2026-08)

指出现有基准缺乏对 GUI agent 运行时异常鲁棒性的系统评估，而 Android 实机部署中意外弹窗、 动作误用等动态扰动十分常见。提出基准 AnTrap，把真实异常归纳为 State / Thinking / Action / Round 四层共十个细分类别，并设计了在注入对抗扰动的同时保持任务仍可完成的构造流程。评测 16 个主流 GUI 模型显示对动态异常存在普遍脆弱性，最强模型也出现显著性能下降；作者还在 原始与对抗环境下各做一轮 GRPO 训练，以区分环境难度与模型能力两个混杂因素。

`环境: Mobile` ｜ [arXiv:2608.24099](https://arxiv.org/abs/2608.24099)

#### Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection (Not an A11y) (2026-08)

指出 Android 无障碍树（accessibility tree）是移动 agent 的一条被忽视的注入通道：任何 应用都能往无障碍节点写入文本，而 agent 会把这些内容当作可信的界面语义读取。攻击者无需 任何特殊权限即可通过普通应用注入指令。这条路径完全绕开了针对视觉截图或网页内容的 防御，暴露出移动 agent 输入通道治理的缺失。

`环境: Mobile` ｜ [arXiv:2608.08939](https://arxiv.org/abs/2608.08939)

#### MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content (MIRAGE (Mobile)) (2026-05)

把漏洞根源归到感知范式本身：移动 GUI agent 把屏幕当作渲染后的像素来看，并据所见选择动作， 因此无法可靠区分可信的界面框架与用户生成内容。MIRAGE 把正常截图转化为注入样本——将攻击者 文本放进普通 UGC 区域，**无需修改 agent、应用或操作系统**。三阶段流水线：Localizer 定位 用户可控区域，Generator 合成上下文感知载荷并以应用原生样式渲染，Curator 把控真实性并在 应用、区域类型与攻击意图之间平衡样本分布。

`环境: Mobile` ｜ [arXiv:2605.28116](https://arxiv.org/abs/2605.28116)

#### Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents (eTAMP) (2026-04)

记忆让 web agent 变得个性化，也使其可被利用：存储历史交互创造出跨站点、跨会话持续存在的 攻击面。已有研究假设攻击者能直接写入记忆或利用跨用户共享，而 eTAMP 仅靠环境观察就实现 跨会话跨站点污染——单次被污染的观察（如浏览一个被操纵的商品页）即可静默投毒记忆，并在 日后其他网站的任务中激活，绕开基于权限的防御。攻击成功率在 GPT-5-mini 上达 32.5%、 GPT-5.2 上 23.4%、GPT-OSS-120B 上 19.5%，另发现「挫败感利用」现象。

`环境: Web` ｜ [arXiv:2604.02623](https://arxiv.org/abs/2604.02623)

#### AdInject: Real-World Black-Box Attacks on Web Agents via Advertising Delivery (AdInject) (2025-05)

批评已有环境注入研究依赖不现实的假设——直接改 HTML、已知用户意图、或能访问模型参数。 AdInject 改用互联网广告投放这一真实渠道注入恶意内容，威胁模型严格得多：agent 为黑盒、 恶意内容静态不可变、且不掌握用户意图。方法上结合诱导 agent 点击的广告内容设计，以及 基于 VLM 从目标站点反推用户潜在意图的内容优化，是该方向最贴近真实部署的威胁模型之一。

`环境: Web` ｜ [arXiv:2505.21499](https://arxiv.org/abs/2505.21499)
