# 4 商用 AI 浏览器与产品安全

*Commercial AI Browsers & Product Security*

[← 返回索引](../../../README.zh-CN.md#4-商用-ai-浏览器与产品安全) ｜ [English](../en/4-commercial-ai-browsers-product-security.md)

*本章以非 arXiv 来源为主：厂商安全公告、CVE、安全博客、漏洞披露。 维护时的完整检索流程见 docs/MAINTENANCE.md。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Broken Gates: Re-evaluating Web Bot Defenses in the Age of LLM Agents (Broken Gates) (2026-07)

把通常的视角反转过来：不问「如何保护 agent」，而问「在浏览器 agent 能自主导航、理解页面内容、 按自然语言指令行动（而非回放预设脚本）之后，网络现有的 bot 管理系统还挡得住吗」。测量同时 覆盖交互式挑战型防御与非交互式信任型防御，面对两类攻击者——商业验证码破解服务与 LLM 浏览器 agent——涵盖 7 家破解服务与 6 种 agent 配置（云托管、自托管、AI 辅助、浏览器扩展），针对 hCaptcha、reCaptcha v2/v3、Cloudflare Turnstile。结论是：挑战型防御已经失守。

`环境: Web` ｜ [arXiv:2607.18659](https://arxiv.org/abs/2607.18659)

#### Privacy Practices of Browser Agents (Privacy Practices of Browser Agents) (2025-12)

少数评测**已上市浏览器 agent 产品**而非研究原型的工作之一，覆盖八款近期流行 agent。其紧迫性 论证是结构性的：让这些工具强大的自动化能力，同时使它们成为高风险的失效点；而它们所执行的 任务类型与被托付的信息类型，意味着任何漏洞都会直接转化为大规模隐私危害。评测框架含五大因子 共 15 项具体测量——组件自身漏洞、对网站行为的防护、跨站追踪阻断、对影响隐私的 prompt 的 响应方式、以及工具自身的日志记录行为。

`环境: Web` ｜ [arXiv:2512.07725](https://arxiv.org/abs/2512.07725)
