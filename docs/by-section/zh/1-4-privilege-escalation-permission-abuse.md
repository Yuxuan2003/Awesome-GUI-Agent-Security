# 1.4 越权与权限滥用

*Privilege Escalation & Permission Abuse*

[← 返回索引](../../../README.zh-CN.md#14-越权与权限滥用) ｜ [English](../en/1-4-privilege-escalation-permission-abuse.md)

*OS 级越权、跨应用提权、权限弹窗诱导、TOCTOU*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### "Allow" to Achieve, Over-Privileged Inadvertently: The Unintended Cost of Task-Completion-Driven Pop-up Decisions in Mobile GUI Agents (Allow to Achieve) (2026-08)

发现移动 GUI agent 在遇到权限弹窗时存在系统性的过度授权倾向，识别出两种偏差：App-Trust Bias（对已安装应用默认信任而一律点允许）与 Task-Prior Override（为达成任务目标而牺牲 权限最小化）。结果是 agent 在用户不知情的情况下累积远超任务所需的权限，把权限弹窗这一 最后防线变成了形式。

`环境: Mobile` ｜ [arXiv:2608.04755](https://arxiv.org/abs/2608.04755)

#### (A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents (AI Sees) (2026-07)

系统分析第三方移动 agent 引入的新攻击面，核心是「感知鸿沟」——agent 能读取到屏幕上用户 实际看不到或不会注意的内容（隐藏视图、后台通知、无障碍节点），攻击者可利用这一差异实施 用户完全无法察觉的诱导。指出第三方 agent 生态缺乏对 agent 可见性范围的约束机制。

`环境: Mobile` ｜ [arXiv:2607.00333](https://arxiv.org/abs/2607.00333)

#### Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents (PUSV) (2026-04)

把「截图—点击」循环中的观察到动作间隔（真实 OSWorld 负载下平均 6.51 秒）形式化为「视觉 原子性破坏」，指出这构成一个 TOCTOU 窗口，无特权攻击者可在其中篡改 UI 状态。刻画三种攻击 原语：通知覆盖劫持、窗口焦点操纵、网页 DOM 注入——其中第二种是 Android Action Rebinding 的桌面对应物，动作重定向成功率 100% 且在观察时刻不留任何视觉痕迹。提出 PUSV 防御，在每次 动作派发前立即复验 UI 状态（点击目标处的掩码像素 SSIM、全局截图差分、X Window 快照差分）， 在 180 次对抗试验中拦截率 100%、零误报、开销低于 0.1 秒。

`环境: Desktop` ｜ [arXiv:2604.18860](https://arxiv.org/abs/2604.18860)

#### Atomicity for Agents: Exposing, Exploiting, and Mitigating TOCTOU Vulnerabilities in Browser-Use Agents (Atomicity for Agents) (2026-02)

把 agent 规划与执行之间的时间差刻画为经典的 TOCTOU 漏洞：网页在两者之间经常发生变化， 导致动作基于过期假设执行，而动态或对抗性内容可以刻意拉大这个窗口。论文在覆盖合成与真实 网站的基准上做了大规模实证，评测 10 个主流开源 agent，发现 TOCTOU 暴露是普遍现象而非 个例。提出的缓解方案刻意保持轻量——在规划阶段监控 DOM 与布局变化，并在动作真正执行前 立即校验页面状态。

`环境: Web` ｜ [arXiv:2603.00476](https://arxiv.org/abs/2603.00476)

#### Mind the Gap: Action Rebinding Attacks against Android GUI Agents (Action Rebinding) (2026-01)

指出把 GUI agent 当作高权限操作者（跨应用边界感知屏幕、注入输入）与 Android 严格的应用 沙箱机制存在根本冲突。跨应用 Action Rebinding 攻击让一个不申请任何危险权限的恶意应用即可 劫持 agent 执行：先渲染一个无害的「上下文载体」诱导 agent 规划出某个动作，再在其推理延迟 窗口内把前台切换到敏感目标应用，agent 察觉不到切换、于是在特权上下文中执行了该动作。 作者进一步利用 agent 自身的任务恢复逻辑，把攻击武器化为可编程的多步利用循环。

`环境: Mobile` ｜ [arXiv:2601.12349](https://arxiv.org/abs/2601.12349)
