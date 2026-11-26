# 3.4 Desktop 与 OS 环境基准

*Desktop & OS Environment*

[← 返回索引](../../../README.zh-CN.md#34-desktop-与-os-环境基准) ｜ [English](../en/3-4-desktop-os-environment.md)

*针对 desktop / OS 级 computer-use agent 的安全评测*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### SEAM: Computer-Use Agents Know the Harm Between Screens, and Commit It Anyway (SEAM) (2026-11)

现有 CUA 安全基准把危害放在任务意图里，或放在单一屏幕上（恶意指令、注入命令、钓鱼页面），因此一个分别 检查任务与每一屏的 agent 就能通过。但在委托式工作中，危害往往来自组合：一屏上有关于某人的事实，另一屏 上有关于某物的事实，再加上一个把两者绑在一起的合法任务。SEAM（跨多屏的安全执行）包含 600 个多步、跨 应用的 OSWorld 任务，其中指令和每一个单独的观测都是良性的，只有组合起来才有害；通过只差一处的最小对 变体、并以服务器日志而非 LLM 评审打分，可以精确定位 agent 在哪一步失守。通用开源权重模型与旗舰 agent 在最多 92% 的运行中实施了危害，可一旦用户用一句话直接说出来，它们就会拒绝；它们确实打开了关键页面， 被问到时也能指出危害，开启思考时还常把冲突写进推理里，然后照样确认执行。可见「认出风险」并不能可靠 转化为「安全执行」，且取决于信息通道：同样的警告放在用户指令里比放在屏幕上有效得多；闭源模型明显更谨慎。

`环境: Desktop` ｜ [arXiv:2611.22971](https://arxiv.org/abs/2611.22971)

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
