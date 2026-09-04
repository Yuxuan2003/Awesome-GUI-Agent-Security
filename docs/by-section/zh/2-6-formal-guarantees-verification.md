# 2.6 形式化保证与验证

*Formal Guarantees & Verification*

[← 返回索引](../../../README.zh-CN.md#26-形式化保证与验证) ｜ [English](../en/2-6-formal-guarantees-verification.md)

*带可证明保证的防御：形式化验证、控制流完整性、共形风险控制*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation (CORA) (2026-04)

现有 GUI agent 防护依赖 prompt 工程、脆弱的启发式规则与 VLM-as-critic，既无形式化验证也 不提供用户可调的保证。CORA 是一个「策略之后、动作之前」的防护框架，对已执行的有害动作 给出统计保证：把安全性重构为选择性动作执行，训练 Guardian 模型估计动作条件风险，再用 Conformal Risk Control 校准满足用户指定风险预算的执行/弃权边界，被拒动作交由 Diagnostician 做多模态推理并建议确认、反思或中止。另设 Goal-Lock 机制抵御视觉注入。

`环境: Mobile` ｜ [arXiv:2604.09155](https://arxiv.org/abs/2604.09155)
