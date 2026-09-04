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
