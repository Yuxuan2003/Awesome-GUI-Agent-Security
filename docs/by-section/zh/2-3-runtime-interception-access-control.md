# 2.3 执行中拦截与权限控制

*Runtime Interception & Access Control*

[← 返回索引](../../../README.zh-CN.md#23-执行中拦截与权限控制) ｜ [English](../en/2-3-runtime-interception-access-control.md)

*信息流追踪、OS 级策略强制、沙箱*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### CURA: Certified Runtime Alarms for Computer-Use Agents (CURA) (2026-08)

揭示 self-report 这一最廉价的监督通道恰恰在最需要它的地方失效：在 361 个 OSWorld 任务上， 流水线平均分 82.9（超过人类基线 72.4），但 71 次失败里有 64 次（90%）以「成功」收尾， 61 次声称没有遇到任何阻碍，约 9100 次调用中显式的失败上报机制从未被使用。提出外部监控器 CURA，只读 harness 可见的遥测数据，不需模型内部状态、额外 LLM 调用或改 prompt，把运行 轨迹转成带误报率保证的序贯检验：α=0.10 时 CUSUM 告警能在终止前中位 31 步检出 42.3% 的 失败，实测误报率 0.066。

`环境: Desktop` ｜ [arXiv:2608.27808](https://arxiv.org/abs/2608.27808)

#### Prismata: Confining Cross-Site Prompt Injection in Web Agents (Prismata) (2026-07)

把 web agent 面临的注入风险类比为 XSS 的重现：XSS 已经证明混合可信与不可信内容是危险的， 而 agent 把自然语言当指令解释，使第三方与用户生成内容能够劫持 agent。核心难点在于推导 任务专属的安全策略需要理解页面结构，而页面结构本身已与攻击者内容纠缠。提出 Prismata， 借鉴经典完整性模型的思路做动态信任推导，为页面内容打上权限标签并提供结构性隔离保证， 同时约束 agent「能看到什么」与「能做什么」，实现上下文最小权限。

`环境: Web` ｜ [arXiv:2607.08147](https://arxiv.org/abs/2607.08147)

#### BraveGuard: From Open-World Threats to Safer Computer-Use Agents (BraveGuard) (2026-05)

从「CUA 的危害为何难以捕捉」出发：危害只在多步执行轨迹中浮现，而其中每个单独动作在局部看 都无害，因此孤立的 prompt 与最终回复都看不出问题。BraveGuard 是自我演进的流水线：从近期 研究来源中挖掘新兴风险与攻击模式，将其实例化为可执行的 computer-use 任务，收集 agent rollout，进而导出**轨迹级**监督信号训练护栏模型。由于新威胁与验证失败出现时可以重跑这个 闭环，防御能持续适应，而不是冻结在静态基准训练时所捕捉到的那个快照上。

`环境: Desktop, Web` ｜ [arXiv:2606.01166](https://arxiv.org/abs/2606.01166)

#### ceLLMate: Sandboxing Browser AI Agents (ceLLMate) (2025-12)

不试图检测每一条恶意指令，而是通过限制 agent 的环境权限来压缩爆炸半径。核心洞察针对作者 所称的「语义鸿沟」：在点击、按键这类低层 UI 原语上编写和强制安全策略既脆弱又易错，因此 ceLLMate 选择在 HTTP 层做沙箱——依据是任何产生副作用的 UI 操作最终都会向网站后端发出 网络请求。这使策略面同时具备稳定性与语义可读性，实现形态是与 agent 无关的浏览器扩展。

`环境: Web` ｜ [arXiv:2512.12594](https://arxiv.org/abs/2512.12594)

#### Secure and Efficient Access Control for Computer-Use Agents via Context Space (CSAgent) (2025-09)

主张把计算机控制权交给 agent 之所以危险，根源在 LLM 固有的不确定性——一旦动作偏离用户 意图，后果可能不可逆；而用户确认与基于 LLM 的动态校验分别在可用性、安全性或性能上有短板。 CSAgent 是系统级、基于静态策略的访问控制框架，通过「意图感知 + 上下文感知」策略弥合静态 策略与动态上下文之间的落差，并提供自动化工具链协助开发者构造与精炼策略，最终由优化过的 操作系统服务强制执行，确保动作只在特定用户意图与上下文下才被允许。

`环境: Desktop` ｜ [arXiv:2509.22256](https://arxiv.org/abs/2509.22256)

#### AgentSentinel: An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents (AgentSentinel) (2025-09)

把威胁模型与传统的 prompt 安全区分开：这里的危险不只来自不安全的用户输入，还来自 agent 自身不稳定的 LLM 决策所生成的工具调用，而这类漏洞横跨 computer-use agent 的每个组件。 AgentSentinel 拦截 agent 相关服务内的所有敏感操作并暂停执行，直到安全审计完成——也就是 把强制点放在服务边界而非 prompt 层。其审计机制会跨组件关联证据，而不是孤立地判断每次调用。

`环境: Desktop` ｜ [arXiv:2509.07764](https://arxiv.org/abs/2509.07764)

#### Reliable Weak-to-Strong Monitoring of LLM Agents (CUA-SHADE-Arena) (2025-08)

压力测试针对 agent 隐蔽违规（如私下分享隐私信息）的监控系统：设计「监控器红队」工作流， 变化 agent 与监控器各自的情境感知程度，施加含提示注入的规避策略，并在面向工具调用 agent 的 SHADE-Arena 与新构建的 CUA-SHADE-Arena（把 TheAgentCompany 扩展到 computer-use agent） 上运行。核心发现不对称且反直觉：**agent 的感知压制监控器的感知**——agent 一旦知道自己正被 监控，监控可靠性显著下降；而反过来给监控器提供更多关于 agent 的信息，帮助要小得多。

`环境: Desktop` ｜ [arXiv:2508.19461](https://arxiv.org/abs/2508.19461)

#### HarmonyGuard: Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization (HarmonyGuard) (2025-08)

把核心矛盾表述为在长动作序列中平衡任务性能与不断演化的网页隐藏威胁，并指出以往工作局限于 单目标优化或单轮场景。HarmonyGuard 是多 agent 框架，其中 Policy Agent 能从非结构化的 外部文档中自动抽取并维护结构化安全策略、持续更新，回应的是「手写策略会过期」这一现实 问题。双目标优化同时兼顾安全与效用，而非牺牲其一换取其二。

`环境: Web` ｜ [arXiv:2508.04010](https://arxiv.org/abs/2508.04010)
