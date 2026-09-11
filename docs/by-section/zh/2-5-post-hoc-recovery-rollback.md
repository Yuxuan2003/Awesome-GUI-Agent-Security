# 2.5 事后恢复与回滚

*Post-hoc Recovery & Rollback*

[← 返回索引](../../../README.zh-CN.md#25-事后恢复与回滚) ｜ [English](../en/2-5-post-hoc-recovery-rollback.md)

*失败归因、状态回滚、危害发生后的修复*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### From Blind Edits to Verified Repair: Building Trustworthy User-Side LLM Agents for Web Accessibility (Verified Repair) (2026-07)

一个特别的条目：这里的 agent 在设计上完全良性——一个为无障碍改写页面的 Chrome 扩展——但论文 的贡献属于安全范畴，即**未经验证的 LLM 编辑，修好页面和弄坏页面的概率几乎相当**。双条件协议 以同等严谨程度衡量收益与危害，在六个小规模开源模型（7B–14B）上、针对十个违规密集站点与十个 本已高度无障碍的真实站点做评测，诊断相当精确：未验证生成带来 24 处改善、同时造成 20 处退化。 这种近乎持平的比例正是「先验证再应用」的论据；而该扩展以可逆方式注入 CSS，使错误编辑可被 撤销——这是本节所关注的回滚纪律的一个具体实例。

`环境: Web` ｜ [arXiv:2608.24913](https://arxiv.org/abs/2608.24913)

#### CUADebug: Diagnosing and Repairing Computer-Use Agent Failures (CUADebug) (2026-07)

面向 CUA 执行失败后的诊断与修复，提出定位失败步骤并生成修复方案的框架。虽以可靠性为 出发点，但其失败归因与状态回滚能力可直接用于安全事件的事后恢复——在 agent 被注入劫持后 判断从哪一步开始偏离、并回退到最后一个可信状态。是「事后恢复」这一防御层中较少见的 系统性工作。

`环境: Desktop` ｜ [arXiv:2608.02643](https://arxiv.org/abs/2608.02643)

#### Whose Agent Are You? Multi-Layer Fingerprinting and Attribution of Autonomous Web Agents (Agent Fingerprinting) (2026-06)

从网站运营方而非 agent 方切入 agent 安全：随着 web agent 大量涌现，无节制的内容抓取成为 隐私与安全问题，而现有防线——robots.txt、主动 bot 拦截——被普遍无视且极易绕过。论文表明， AI web agent 可以通过「网络层特征（TLS、HTTP）+ 浏览器交互行为」的多层指纹，与人类及传统 爬虫区分开来，并将该机制实现为可部署在真实插桩域名上的程序化日志框架。对六个主流框架 （AutoGen、Browser Use、Claude、Gemini、Operator、Skyvern）的分析揭示出它们在组装 HTTP 请求、建立 TLS/HTTP 连接、驱动浏览器自主操作方式上的潜在结构差异。

`环境: Web` ｜ [arXiv:2606.20910](https://arxiv.org/abs/2606.20910)

#### "What Did It Actually Do?": Understanding Risk Awareness and Traceability for Computer-Use Agents (What Did It Actually Do) (2026-03)

在个人化 agent 从专家圈走向大众使用的背景下研究 CUA 风险的人因侧：这类系统会安装 skill、 调用工具、访问私有资源、修改本地环境，但用户通常并不清楚自己授予了什么权限、agent 实际 做了什么、以及事后是否被干净卸载。工作把 OpenClaw 生态的多来源语料（安全事件、公告、恶意 skill 报告、新闻报道、教程、社交媒体叙述）与面向用户和从业者的访谈研究结合起来。发现是： 受访者在抽象层面认得出这类系统有风险，却缺乏关于权限与持久化的具体心智模型。

`环境: Desktop` ｜ [arXiv:2603.28551](https://arxiv.org/abs/2603.28551)
