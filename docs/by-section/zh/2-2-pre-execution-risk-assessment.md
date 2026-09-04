# 2.2 执行前风险评估

*Pre-execution Risk Assessment*

[← 返回索引](../../../README.zh-CN.md#22-执行前风险评估) ｜ [English](../en/2-2-pre-execution-risk-assessment.md)

*世界模型预测、动作风险打分*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### WebGuard: Building a Generalizable Guardrail for Web Agents (WebGuard) (2025-07)

主张 web agent 需要类似人类用户的访问控制机制，并发布首个支持 agent 动作风险评估的数据集： 来自 22 个领域、193 个网站（含常被忽视的长尾站点）的 4939 条人工标注状态改变动作，按 SAFE / LOW / HIGH 三级风险标注，并划分好训练测试集以支持泛化研究。核心结论相当刺眼—— 即便前沿 LLM 预测动作后果的准确率也不足 60%。

`环境: Web` ｜ [arXiv:2507.14293](https://arxiv.org/abs/2507.14293)
