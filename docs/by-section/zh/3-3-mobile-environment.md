# 3.3 Mobile 环境基准

*Mobile Environment*

[← 返回索引](../../../README.zh-CN.md#33-mobile-环境基准) ｜ [English](../en/3-3-mobile-environment.md)

*针对移动 / Android / iOS agent 的安全评测*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps (MobileWorldSafety) (2026-08)

指出现有基准脱离日常使用场景，缺乏对移动 GUI agent 在环境注入下的系统评估——而这类 agent 已从研究原型走向真实部署，且日常操作中会不断处理不可信的环境内容。提出基于真实 Android 应用构建的基准 MobileWorldSafety，含 142 个风险任务，覆盖间接提示注入与对抗 指令等多种日常渠道，每个任务都定义了可程序化验证的判定条件，使攻击是否成功可被客观测量。

`环境: Mobile` ｜ [arXiv:2608.17659](https://arxiv.org/abs/2608.17659)

#### GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments? (GhostEI-Bench) (2025-10)

把环境注入确立为区别于提示类攻击的、研究不足的威胁向量：它不改文本指令，而是把欺骗性 覆盖层、伪造通知这类对抗 UI 元素直接插入 GUI 以污染 agent 的视觉感知，从而绕开文本层 防护，可导致隐私泄漏、财务损失甚至不可逆的设备失陷。GhostEI-Bench 跳出静态图像评测， 在完整可运行的 Android 模拟器中把对抗事件注入真实应用工作流。

`环境: Mobile` ｜ [arXiv:2510.20333](https://arxiv.org/abs/2510.20333)

#### MVISU-Bench: Benchmarking Mobile Agents for Real-World Tasks by Multi-App, Vague, Interactive, Single-App and Unethical Instructions (MVISU-Bench) (2025-08)

任务分类法来自用户问卷而非研究者直觉，由此得出五个类别——多应用、模糊、交互式、单应用、 不道德指令——覆盖 137 个真实移动应用上的 404 个双语任务。其中两个类别与安全直接相关： 不道德指令检验拒答能力，模糊指令检验 agent 是否会**主动询问**而不是擅自猜测。论文同时 发布 Aider，一个即插即用的动态 prompter，用于缓解风险并澄清用户意图，把总体成功率相比 此前 SOTA 提升 19.55%——这说明「主动澄清」与「有能力」并不互相矛盾。

`环境: Mobile` ｜ [arXiv:2508.09057](https://arxiv.org/abs/2508.09057)

#### MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control (MobileSafetyBench) (2024-10)

填补了当时的一个完全空白——尽管移动设备控制 agent 会直接接触个人信息与设备设置，却没有任何 标准化的安全评测基准。该基准基于 Android 模拟器构建以保证真实性，覆盖消息、银行等类应用， 并刻意区分了两类常被混为一谈的风险：**滥用**（agent 被要求做有害之事）与**负面副作用** （agent 在追求正当目标的过程中造成危害）。任务同时覆盖日常场景与面对间接提示注入时的鲁棒性。

`环境: Mobile` ｜ [arXiv:2410.17520](https://arxiv.org/abs/2410.17520)
