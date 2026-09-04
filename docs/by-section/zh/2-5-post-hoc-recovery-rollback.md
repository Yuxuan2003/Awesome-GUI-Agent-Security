# 2.5 事后恢复与回滚

*Post-hoc Recovery & Rollback*

[← 返回索引](../../../README.zh-CN.md#25-事后恢复与回滚) ｜ [English](../en/2-5-post-hoc-recovery-rollback.md)

*失败归因、状态回滚、危害发生后的修复*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### CUADebug: Diagnosing and Repairing Computer-Use Agent Failures (CUADebug) (2026-07)

面向 CUA 执行失败后的诊断与修复，提出定位失败步骤并生成修复方案的框架。虽以可靠性为 出发点，但其失败归因与状态回滚能力可直接用于安全事件的事后恢复——在 agent 被注入劫持后 判断从哪一步开始偏离、并回退到最后一个可信状态。是「事后恢复」这一防御层中较少见的 系统性工作。

`环境: Desktop` ｜ [arXiv:2608.02643](https://arxiv.org/abs/2608.02643)

#### "What Did It Actually Do?": Understanding Risk Awareness and Traceability for Computer-Use Agents (What Did It Actually Do) (2026-03)

在个人化 agent 从专家圈走向大众使用的背景下研究 CUA 风险的人因侧：这类系统会安装 skill、 调用工具、访问私有资源、修改本地环境，但用户通常并不清楚自己授予了什么权限、agent 实际 做了什么、以及事后是否被干净卸载。工作把 OpenClaw 生态的多来源语料（安全事件、公告、恶意 skill 报告、新闻报道、教程、社交媒体叙述）与面向用户和从业者的访谈研究结合起来。发现是： 受访者在抽象层面认得出这类系统有风险，却缺乏关于权限与持久化的具体心智模型。

`环境: Desktop` ｜ [arXiv:2603.28551](https://arxiv.org/abs/2603.28551)
