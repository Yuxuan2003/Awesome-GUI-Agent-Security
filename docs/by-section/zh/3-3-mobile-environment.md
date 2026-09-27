# 3.3 Mobile 环境基准

*Mobile Environment*

[← 返回索引](../../../README.zh-CN.md#33-mobile-环境基准) ｜ [English](../en/3-3-mobile-environment.md)

*针对移动 / Android / iOS agent 的安全评测*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### PriMobiBench: Characterizing Visual Privacy Leakage in VLM-Driven Mobile GUI Agents (PriMobiBench) (2026-09)

移动 GUI agent 通过解读截图流自动化手机任务，这一设计带来严重但研究不足的隐私风险： 既包括屏上敏感信息的直接泄露，也包括非预期的用户画像推断，而两者都缺少标准化基准来量化。 PriMobiBench 是首个系统评测截图驱动移动 agent 的视觉隐私泄露与画像风险的基准，提供 数据生成、轨迹构建与多模型评测的统一流水线，并附数据集 MobiLeak——来自 16 个应用的 执行轨迹，覆盖 25 类隐私属性、2960 个嵌入的隐私实例。结果相当刺眼：VLM 直接提取敏感 信息成功率最高 82.5%；即便没有显式泄露，也能从聚合的视觉证据中以约 70% 的成功率推断出 用户画像。作者提出的缓解方案在上云前遮蔽「隐私敏感但与任务无关」的 UI 元素，可将画像 成功率最多降低 58%，代价仅约 8% 的性能损失。

`环境: Mobile` ｜ [arXiv:2609.13873](https://arxiv.org/abs/2609.13873)

#### MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps (MobileWorldSafety) (2026-08)

指出现有基准脱离日常使用场景，缺乏对移动 GUI agent 在环境注入下的系统评估——而这类 agent 已从研究原型走向真实部署，且日常操作中会不断处理不可信的环境内容。提出基于真实 Android 应用构建的基准 MobileWorldSafety，含 142 个风险任务，覆盖间接提示注入与对抗 指令等多种日常渠道，每个任务都定义了可程序化验证的判定条件，使攻击是否成功可被客观测量。

`环境: Mobile` ｜ [arXiv:2608.17659](https://arxiv.org/abs/2608.17659)

#### GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments? (GhostEI-Bench) (2025-10)

把环境注入确立为区别于提示类攻击的、研究不足的威胁向量：它不改文本指令，而是把欺骗性 覆盖层、伪造通知这类对抗 UI 元素直接插入 GUI 以污染 agent 的视觉感知，从而绕开文本层 防护，可导致隐私泄漏、财务损失甚至不可逆的设备失陷。GhostEI-Bench 跳出静态图像评测， 在完整可运行的 Android 模拟器中把对抗事件注入真实应用工作流。

`环境: Mobile` ｜ [arXiv:2510.20333](https://arxiv.org/abs/2510.20333)

#### Mind the Third Eye! Benchmarking Privacy Awareness in MLLM-powered Smartphone Agents (SAPA-Bench) (2025-08)

手机在带来便利的同时，也让设备得以大量记录各类个人信息；而智能手机 agent 在执行任务时被 授予了对这些敏感信息的相当大访问权。本文提出首个面向多模态大模型智能手机 agent 隐私意识的 大规模基准，含 7138 个场景，并对每个场景中的隐私上下文标注类型（如账户凭证）、敏感度等级 与出现位置。对七个主流 agent 的评测显示，几乎所有 agent 的隐私意识都难以令人满意 —— 即便 给出明确提示，表现仍低于 60%。闭源 agent 整体优于开源，Gemini 2.0-flash 以 67% 最佳。 agent 的隐私识别能力与场景敏感度高度相关：越敏感的场景反而越容易被识别出来。作者希望这些 结果能促使社区重新审视手机 agent 上效用与隐私之间的失衡。

`环境: Mobile` ｜ [arXiv:2508.19493](https://arxiv.org/abs/2508.19493)

#### MVISU-Bench: Benchmarking Mobile Agents for Real-World Tasks by Multi-App, Vague, Interactive, Single-App and Unethical Instructions (MVISU-Bench) (2025-08)

任务分类法来自用户问卷而非研究者直觉，由此得出五个类别——多应用、模糊、交互式、单应用、 不道德指令——覆盖 137 个真实移动应用上的 404 个双语任务。其中两个类别与安全直接相关： 不道德指令检验拒答能力，模糊指令检验 agent 是否会**主动询问**而不是擅自猜测。论文同时 发布 Aider，一个即插即用的动态 prompter，用于缓解风险并澄清用户意图，把总体成功率相比 此前 SOTA 提升 19.55%——这说明「主动澄清」与「有能力」并不互相矛盾。

`环境: Mobile` ｜ [arXiv:2508.09057](https://arxiv.org/abs/2508.09057)

#### From Assistants to Adversaries: Exploring the Security Risks of Mobile LLM Agents (AgentScan) (2025-05)

本文首次对移动 LLM agent 做全面安全分析，覆盖三类代表性形态：厂商的系统级 AI 助手 （如 YOYO Assistant）、第三方通用 agent（如 AutoGLM）与新兴 agent 框架（如 Mobile Agent）。 作者先梳理移动 agent 的通用工作流，再沿语言推理、GUI 交互、系统执行三个核心能力维度识别 安全威胁，最终归纳出 11 个不同的攻击面 —— 它们都根植于移动 agent 独有的能力与交互模式， 并贯穿其完整运行生命周期。配套的半自动分析框架 AgentScan 在这 11 个场景上系统评估 agent， 对九个广泛部署的 agent 的实测结果是：每一个都存在可被利用的漏洞，最严重的在八个不同攻击 向量上同时失守。后果包括行为偏离、隐私泄露乃至完整的执行劫持，相关披露已获两家主要设备 厂商的正面回应。

`环境: Mobile` ｜ [arXiv:2505.12981](https://arxiv.org/abs/2505.12981)

#### MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control (MobileSafetyBench) (2024-10)

填补了当时的一个完全空白——尽管移动设备控制 agent 会直接接触个人信息与设备设置，却没有任何 标准化的安全评测基准。该基准基于 Android 模拟器构建以保证真实性，覆盖消息、银行等类应用， 并刻意区分了两类常被混为一谈的风险：**滥用**（agent 被要求做有害之事）与**负面副作用** （agent 在追求正当目标的过程中造成危害）。任务同时覆盖日常场景与面对间接提示注入时的鲁棒性。

`环境: Mobile` ｜ [arXiv:2410.17520](https://arxiv.org/abs/2410.17520)

#### Systematic Categorization, Construction and Evaluation of New Attacks against Multi-modal Mobile GUI Agents (2024-07)

把 LLM 与多模态大模型引入移动 GUI agent 显著提升了用户效率与体验，但也带来了尚未被充分 探索的安全漏洞。本文给出系统性的安全调查，贡献有两方面：一是提出一套新的威胁建模方法论， 据此发现并对 34 种此前未有报告的攻击做可行性分析；二是设计一个攻击框架，用于系统地构造 与评估这些威胁。结合真实案例研究与大规模数据集实验，作者验证了这些攻击的严重性与可实现性， 指出移动 GUI 系统亟需健壮的安全防护措施。

`环境: Mobile` ｜ [arXiv:2407.09295](https://arxiv.org/abs/2407.09295)
