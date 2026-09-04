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

#### Secure and Efficient Access Control for Computer-Use Agents via Context Space (CSAgent) (2025-09)

主张把计算机控制权交给 agent 之所以危险，根源在 LLM 固有的不确定性——一旦动作偏离用户 意图，后果可能不可逆；而用户确认与基于 LLM 的动态校验分别在可用性、安全性或性能上有短板。 CSAgent 是系统级、基于静态策略的访问控制框架，通过「意图感知 + 上下文感知」策略弥合静态 策略与动态上下文之间的落差，并提供自动化工具链协助开发者构造与精炼策略，最终由优化过的 操作系统服务强制执行，确保动作只在特定用户意图与上下文下才被允许。

`环境: Desktop` ｜ [arXiv:2509.22256](https://arxiv.org/abs/2509.22256)
