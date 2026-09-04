# 0 综述与威胁模型

*Surveys & Threat Models*

[← 返回索引](../../../README.zh-CN.md#0-综述与威胁模型) ｜ [English](../en/0-surveys-threat-models.md)

*领域综述、SoK、以及 OWASP ASI / MITRE ATLAS 等威胁分类框架的对照*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems (WebMASLab) (2026-07)

追问「角色分解」在安全上的代价：多 agent web 系统通过把工作拆给专职子 agent 来提升任务性能， 但这种拆分会产生单 agent 架构下不存在的结构性攻击面，而这些攻击面此前缺乏归类。论文提出 针对 web 多 agent 系统的攻击向量分类法，并构建 WebMASLab 来研究一个完全外部、仅通过网页 施加影响的攻击者。方法上相当严谨——固定用户任务、工具面与浏览器基座，只让架构一个变量变化， 覆盖三种对抗场景与三种条件（基线、prompt 加固、开启推理）。

`环境: Web` ｜ [arXiv:2608.00202](https://arxiv.org/abs/2608.00202)

#### Measuring the Security of Mobile LLM Agents under Adversarial Prompts from Untrusted Third-Party Channels (Mobile Agent Security Study) (2025-10)

首个针对移动 LLM agent 安全风险的系统性研究，对抗案例从弹窗广告这类机会主义操纵，一直延伸到 涉及恶意软件安装与跨应用数据外泄的端到端攻击流程。覆盖面很广——三种架构下的八个前沿移动 agent，超过 2000 组对抗与配对良性试验。结论是系统性的而非个例：欺诈广告这类低门槛向量成功率 超过 80%，而即便是需要绕过操作系统显式警告的流程（如安装恶意软件），依然能够走通。

`环境: Mobile` ｜ [arXiv:2510.27140](https://arxiv.org/abs/2510.27140)

#### A Systematization of Security Vulnerabilities in Computer Use Agents (CUA Vuln SoK) (2025-07)

对真实 CUA 做系统化威胁分析与对抗测试，归纳出七类该范式独有的风险，并深入剖析三个具体 利用链：用视觉覆盖层误导界面级推理的 clickjacking、经工具链串联实现远程代码执行的间接提示 注入、以及通过操纵隐式界面语境劫持多步推理的 CoT 暴露攻击。三个案例共同指向当前实现的 三处架构性缺陷：缺少输入来源追踪、界面与动作绑定薄弱、控制流完整性不足。

`环境: Desktop, Web` ｜ [arXiv:2507.05445](https://arxiv.org/abs/2507.05445)

#### Towards Trustworthy GUI Agents: A Survey (Trustworthy GUI Survey) (2025-03)

把「执行落差」（execution gap）确立为可信 GUI agent 的核心障碍——即在动态、部分可观测界面下 感知、推理与交互三者之间的错配。与对话系统不同，GUI agent 执行的是提交表单、授予权限、删除 数据这类不可逆操作。综述提出与工作流对齐的分类法，把信任拆为感知信任、推理信任、交互信任 三层，梳理失败如何在动作/观察循环中传播并累积，并主张仅用任务完成率评估可信度是不充分的。

`环境: 跨环境` ｜ [arXiv:2503.23434](https://arxiv.org/abs/2503.23434)
