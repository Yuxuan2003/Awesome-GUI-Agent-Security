# 3.4 Desktop 与 OS 环境基准

*Desktop & OS Environment*

[← 返回索引](../../../README.zh-CN.md#34-desktop-与-os-环境基准) ｜ [English](../en/3-4-desktop-os-environment.md)

*针对 desktop / OS 级 computer-use agent 的安全评测*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents (OS-Harm) (2025-06)

指出 CUA 已在快速部署但安全性长期被忽视，基于 OSWorld 环境构建 OS-Harm，考察三类危害： 用户故意滥用、提示注入攻击、模型自身失当行为。含 150 个任务，覆盖骚扰、侵犯版权、虚假 信息、数据外泄等违规类型，要求 agent 操作邮件客户端、代码编辑器、浏览器等多种应用。 配套自动评判器同时评估准确性与安全性，与人工标注一致性达 0.76 / 0.79 F1。

`环境: Desktop` ｜ [arXiv:2506.14866](https://arxiv.org/abs/2506.14866)
