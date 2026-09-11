# 3.4 Desktop 与 OS 环境基准

*Desktop & OS Environment*

[← 返回索引](../../../README.zh-CN.md#34-desktop-与-os-环境基准) ｜ [English](../en/3-4-desktop-os-environment.md)

*针对 desktop / OS 级 computer-use agent 的安全评测*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### OS-SPEAR: A Toolkit for the Safety, Performance, Efficiency, and Robustness Analysis of OS Agents (OS-SPEAR) (2026-04)

诊断出当前 OS agent 基准的三个具体缺陷——安全场景狭窄、轨迹标注噪声大、鲁棒性指标有限—— 并以覆盖安全性、性能、效率、鲁棒性四个维度的工具包作答。各子集是分别构建而非从同一池中 重新加权得来：安全子集同时覆盖环境诱发与人为诱发的危害，性能子集通过轨迹价值估计与分层 采样策划，效率子集从双重视角度量。把安全作为四个耦合维度之一、而非一个独立分数来处理， 这个框定方式值得借鉴。

`环境: Desktop` ｜ [arXiv:2604.24348](https://arxiv.org/abs/2604.24348)

#### LPS-Bench: Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios (LPS-Bench) (2026-02)

指出现有基准在**时机**上的缺口：它们聚焦短周期或 GUI 层任务、评判执行期错误，却从未检验 agent 能否在**规划阶段**（任何动作发生之前）预见风险。LPS-Bench 评测基于 MCP 的 CUA 在 长周期任务下的规划期安全意识，覆盖良性与对抗两类交互，含 7 个任务域、9 类风险的 65 个场景， 配以多 agent 自动化数据生成流水线与针对规划轨迹的 LLM-as-a-judge 评测协议。实验显示现有 CUA 在长程规划中维持安全意识的能力存在明显不足。

`环境: Desktop` ｜ [arXiv:2602.03255](https://arxiv.org/abs/2602.03255)

#### OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents (OS-Harm) (2025-06)

指出 CUA 已在快速部署但安全性长期被忽视，基于 OSWorld 环境构建 OS-Harm，考察三类危害： 用户故意滥用、提示注入攻击、模型自身失当行为。含 150 个任务，覆盖骚扰、侵犯版权、虚假 信息、数据外泄等违规类型，要求 agent 操作邮件客户端、代码编辑器、浏览器等多种应用。 配套自动评判器同时评估准确性与安全性，与人工标注一致性达 0.76 / 0.79 F1。

`环境: Desktop` ｜ [arXiv:2506.14866](https://arxiv.org/abs/2506.14866)

#### VPI-Bench: Visual Prompt Injection Attacks for Computer-Use Agents (VPI-Bench) (2025-06)

指出以往工作集中在浏览器 agent 与 HTML 层攻击上，而握有完整系统权限、能操作文件、读取用户 数据、执行任意命令的 CUA 反而研究不足。VPI-Bench 研究**视觉嵌入**于渲染界面中的恶意指令 ——这类指令在构造上就绕开了文本层净化——并提供覆盖五个常用平台的 306 个测试用例。每个用例都是 真实网页平台的交互式变体，部署在真实环境中并含一处视觉嵌入的恶意 prompt，同时覆盖 CUA 与 browser-use agent 两类目标。

`环境: Desktop, Web` ｜ [arXiv:2506.02456](https://arxiv.org/abs/2506.02456)
