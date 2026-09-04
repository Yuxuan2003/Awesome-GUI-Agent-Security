# 1.5 数据泄露与隐私

*Data Exfiltration & Privacy*

[← 返回索引](../../../README.zh-CN.md#15-数据泄露与隐私) ｜ [English](../en/1-5-data-exfiltration-privacy.md)

*凭据窃取、PII 外泄、上下文完整性破坏、过度分享*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents (LoginTrap) (2026-08)

登录对 web agent 而言是涉及凭据的敏感认证边界，但已有工作尚未考察恶意页面内容能否诱导 agent 登录并造成端到端的私密数据泄漏。LoginTrap 是一种与任务无关的诱导登录攻击，假设 黑盒攻击者只控制页面上下文与被诱导的登录流程，并不知道用户任务或 agent 内部实现：通过 类 fuzzing 的流程生成页面专属的间接注入内容，使「先登录」看起来是继续完成任务的合理 前置条件，从而把 agent 引导至攻击者控制的登录页。

`环境: Web` ｜ [arXiv:2608.04741](https://arxiv.org/abs/2608.04741)

#### Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? (Capable but Careless) (2026-06)

用「上下文完整性」（contextual integrity）框架考察 CUA 在跨应用操作时是否会不当传播敏感 信息。结论是能力越强的 agent 反而越容易越界：它们为完成任务会主动把 A 应用中的私密数据 带入 B 应用的输入框，而这类行为不触发任何现有的隐私告警，因为每一次读写都在授权范围内。 提出了以信息流而非权限边界为判据的评估方法。

`环境: Desktop` ｜ [arXiv:2606.23189](https://arxiv.org/abs/2606.23189)

#### Do Phone-Use Agents Respect Your Privacy? (MyPhoneBench) (2026-04)

追问手机操作类 agent 在完成正常任务时是否尊重隐私。这一问题此前难以回答，因为隐私合规 行为从未被形式化定义，且普通应用不会暴露 agent 究竟把哪些数据填进了哪个表单项。 MyPhoneBench 用一份最小隐私契约把「尊重隐私」操作化为三条：授权访问、最小披露、用户可控 记忆，并配以插桩的模拟应用与规则化审计。在 5 个前沿模型、10 个应用、300 个任务上发现， 任务成功率、隐私合规完成度、后续会话中对已存偏好的使用是三种彼此独立的能力，无一模型全占优。

`环境: Mobile` ｜ [arXiv:2604.00986](https://arxiv.org/abs/2604.00986)

#### WebPII: Benchmarking Visual PII Detection for Computer-Use Agents (WebPII) (2026-03)

CUA 从两个方向带来新的隐私风险：从真实网站采集的训练数据不可避免含敏感信息，而云端推理 会暴露用户截图。此前没有公开基准用于检测网页截图中的个人身份信息。WebPII 提供 44865 张 标注的电商 UI 图像，特点包括扩展的 PII 分类（含可用于重识别的交易级标识符）、针对用户 正在填写的半完成表单的前瞻式检测、以及基于 VLM 的可扩展 UI 复现。配套 WebRedact 把 文本抽取基线准确率翻倍以上（0.753 vs 0.357 mAP@50），CPU 延迟仅 20ms。

`环境: Web, Desktop` ｜ [arXiv:2603.17357](https://arxiv.org/abs/2603.17357)

#### SPILLage: Agentic Oversharing on the Web (SPILLage) (2026-02)

与在受控环境中回答问题的聊天机器人不同，web agent 是「在野」运行的：它能访问用户的邮件、 日历等资源，与第三方交互，并留下动作轨迹。本文把「自然的 agent 过度分享」形式化为—— 通过这条动作轨迹无意披露与任务无关的用户信息，并沿「通道」（内容 vs. 行为）与「直接性」 （显式 vs. 隐式）两个维度刻画。这揭示了一处盲区：已有工作聚焦文本泄漏，但 agent 还会通过 点击、滚动、导航模式等行为层面过度暴露，而这些可被第三方监测。在真实电商站点的 180 个 任务上做了基准评测。

`环境: Web` ｜ [arXiv:2602.13516](https://arxiv.org/abs/2602.13516)
