# 2.1 输入侧过滤与净化

*Input Filtering & Sanitization*

[← 返回索引](../../../README.zh-CN.md#21-输入侧过滤与净化) ｜ [English](../en/2-1-input-filtering-sanitization.md)

*在内容进入模型上下文前过滤或遮蔽不可信部分*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Untrusted Content Masking for Web Agents with Security Guarantees (UCM) (2026-07)

指出可证明的注入防御依赖可信指令与不可信数据之间的严格隔离，这在纯文本的 tool-use 场景 中天然成立（agent 可只依据接口定义推理，无需接触不可信内容），但 web agent 必须先观察 渲染后的页面才能感知环境，而页面把可信与不可信内容结构性地混在一起，导致安全保证赖以 成立的信任边界消失。提出 Untrusted Content Masking，利用页面的结构特性在 web 环境中 重建这一边界，使既有的可证明防御能够迁移过来。

`环境: Web` ｜ [arXiv:2607.05277](https://arxiv.org/abs/2607.05277)

#### The Cognitive Firewall: Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense (Cognitive Firewall) (2026-03)

针对「云端防御语义分析能力强但引入延迟与隐私暴露」这一矛盾，提出三阶段拆分计算架构 Cognitive Firewall，把安全检查分布在客户端与云端：本地视觉 Sentinel、云端 Deep Planner、 以及在执行期强制策略的确定性 Guard。在 1000 个对抗样本上，纯边端防御漏检 86.9% 的语义 攻击，而完整混合架构把攻击成功率压到 1% 以下（静态评测 0.88%、自适应评测 0.67%），同时 对有副作用的动作保持确定性约束；由于表现层攻击在本地即被过滤，相比纯云端基线取得约 17000 倍的延迟优势。

`环境: Web` ｜ [arXiv:2603.23791](https://arxiv.org/abs/2603.23791)
