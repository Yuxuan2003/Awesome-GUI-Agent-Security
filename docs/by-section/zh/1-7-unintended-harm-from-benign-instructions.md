# 1.7 良性指令下的意外危害

*Unintended Harm from Benign Instructions*

[← 返回索引](../../../README.zh-CN.md#17-良性指令下的意外危害) ｜ [English](../en/1-7-unintended-harm-from-benign-instructions.md)

*无恶意攻击者，agent 自身在正常指令下造成危害*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)

提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。

`环境: Mobile, 跨环境` ｜ [arXiv:2607.29199](https://arxiv.org/abs/2607.29199)
