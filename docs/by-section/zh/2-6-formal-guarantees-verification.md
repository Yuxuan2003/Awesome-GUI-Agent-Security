# 2.6 形式化保证与验证

*Formal Guarantees & Verification*

[← 返回索引](../../../README.zh-CN.md#26-形式化保证与验证) ｜ [English](../en/2-6-formal-guarantees-verification.md)

*带可证明保证的防御：形式化验证、控制流完整性、共形风险控制*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### SkillHarness: Harnessing Safe Skills for Computer-Use Agents (SkillHarness) (2026-06)

针对 skill 学习类方法中一个被默认接受的假设：它们从成功轨迹中蒸馏可复用 skill，却隐含假定 环境是静态且安全的，既忽略提示注入这类对抗交互，也忽略弹窗这类环境动态。在动态环境下，这个 假设会产出有风险的 skill 与脆弱的执行——也就是说漏洞被**固化进**了 agent 的可复用库里。 SkillHarness 把 skill 的学习与使用建模为受安全约束的交互过程，引入「skill 边界」以取代 静态的 skill 抽象。

`环境: Desktop` ｜ [arXiv:2606.20636](https://arxiv.org/abs/2606.20636)

#### CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation (CORA) (2026-04)

现有 GUI agent 防护依赖 prompt 工程、脆弱的启发式规则与 VLM-as-critic，既无形式化验证也 不提供用户可调的保证。CORA 是一个「策略之后、动作之前」的防护框架，对已执行的有害动作 给出统计保证：把安全性重构为选择性动作执行，训练 Guardian 模型估计动作条件风险，再用 Conformal Risk Control 校准满足用户指定风险预算的执行/弃权边界，被拒动作交由 Diagnostician 做多模态推理并建议确认、反思或中止。另设 Goal-Lock 机制抵御视觉注入。

`环境: Mobile` ｜ [arXiv:2604.09155](https://arxiv.org/abs/2604.09155)

#### Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks (DMAST) (2026-03)

定位到一处由架构本身造就的攻击面：多模态 web agent 同时消费截图与无障碍树，因此攻击者只需 注入 DOM 就能**同时**污染两个观测通道，并且两边叙述互相一致，使任何跨通道一致性检查都失效。 MiniWob++ 上的漏洞分析显示，带视觉成分的攻击远强于纯文本注入，暴露出以文本为中心的 VLM 安全训练所留下的缺口。DMAST 把 agent 与攻击者的交互形式化为二人零和马尔可夫博弈，通过模仿 学习、带「零确认」策略的 oracle 引导 SFT、以及最后的对抗阶段共训双方。

`环境: Web` ｜ [arXiv:2603.04364](https://arxiv.org/abs/2603.04364)

#### LaSM: Layer-wise Scaling Mechanism for Defending Pop-up Attack on GUI Agents (LaSM) (2025-07)

指出针对弹窗式环境注入的现有防御要么需要昂贵重训、要么在归纳性干扰下失效，转而走机制 可解释性路线。论文系统研究这类攻击如何改变 GUI agent 的注意力分布，发现正确输出与错误输出 之间存在**逐层的注意力发散模式**。LaSM 直接利用这一发现，选择性放大关键层的注意力与 MLP 模块，无需任何额外训练即把模型显著性重新对齐到任务相关的屏幕区域——这是把可解释性结论 转化为可部署 GUI agent 防御的少见案例。

`环境: Desktop, Web` ｜ [arXiv:2507.10610](https://arxiv.org/abs/2507.10610)
