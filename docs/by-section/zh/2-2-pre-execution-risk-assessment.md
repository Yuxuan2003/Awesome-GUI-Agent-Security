# 2.2 执行前风险评估

*Pre-execution Risk Assessment*

[← 返回索引](../../../README.zh-CN.md#22-执行前风险评估) ｜ [English](../en/2-2-pre-execution-risk-assessment.md)

*世界模型预测、动作风险打分*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Beyond Task Completion: Training Capable and Safe Computer-Use Agents (SCOPE) (2026-08)

只以任务成功为目标的后训练，并不会带来可靠的安全行为。本文给出明确规范：可靠的 CUA 应当 以风险为条件决定执行方式 —— 普通良性任务照常完成，遇到环境风险时规避并在仍存在安全路径时 继续，而当目标本身有害或已无安全路径时应当拒绝。SCOPE 把任务执行能力与安全感知决策联合 后训练；SCOPE-Gen 自动合成可验证的能力任务，并把它转换为保持原目标的环境风险变体，由此 构建出含能力示范、安全续行与显式拒绝三类轨迹的数据集 SATraj-OS。SCOPE 先通过监督微调 学习这三类轨迹，再用在线强化学习提升任务完成度。从 Qwen3.5-9B 出发，SCOPE-RL 在 OSWorld 上任务成功率 54.17%、在 OS-BLIND 上攻击规避率 64.30%，能力与安全的综合得分 58.80% 为 参评 agent 最高。消融显示两类安全监督作用互补而不对称：拒绝轨迹贡献了大部分攻击规避提升， 而风险处理轨迹在同等规避水平下保住了更多任务效用。

`环境: 跨环境` ｜ [arXiv:2609.22178](https://arxiv.org/abs/2609.22178)

#### SeerGuard: A Safety Framework for Mobile GUI Agents via World Model Prediction (SeerGuard) (2026-07)

指出移动 GUI agent 现有安全机制本质上都是被动响应，无法在动作触发前评估风险，而这类 agent 的单个错误动作往往不可逆。SeerGuard 是「后果感知」框架，将指令级筛查与动作级 风险评估结合：在当前 GUI 状态下分析 agent 拟执行的动作，预判可能结果再决定是否放行。 支撑能力来自一个多任务学习训练的安全增强世界模型（SAWM），把语义化的下一状态预测与 安全风险评估融进同一个模型，且该框架可跨不同底层 GUI agent 迁移。

`环境: Mobile` ｜ [arXiv:2607.15550](https://arxiv.org/abs/2607.15550)

#### Uncertainty Quantification for Computer-Use Agents: A Benchmark across Vision-Language Models and GUI Grounding Datasets (Argus) (2026-06)

计算机使用代理把视觉语言模型的预测变成可执行的 GUI 点击，因此可靠的不确定性估计对拒绝 执行、校准、失误严重性排序与空间安全区域都至关重要；但事后不确定性量化（UQ）的证据零散 分布在孤立的模型—数据集对上，难以判断排序是否稳定。Argus 是一个跨机制基准：包含覆盖 4 个 VLM agent 与 4 个数据集的 27 种方法开源矩阵，以及在无法取得 logit、隐藏状态与 注意力图的 3 家前沿厂商上的 8 种方法闭源矩阵。核心发现是「选择性迁移」：固定模型时 UQ 排序跨数据集稳定（Spearman rho 最高 0.969），但跨模型类别与可观测接口时退化，向闭源厂商 的跨层迁移平均只有 +0.08 —— 因此闭源场景的 UQ 应在目标上重新排序而非外推。共形点击区域 在校准后半径可缩小 40–60%，但在校准—测试或接口不匹配时覆盖率会下降。

`环境: 跨环境` ｜ [arXiv:2606.25760](https://arxiv.org/abs/2606.25760)

#### Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces (DUDE) (2026-05)

指出以往工作的割裂之处：一类方法能检测欺骗但不与任务回路结合，另一类记录了攻击却不提出 防御。论文形式化了「欺骗感知的 web agent 防御」，提出两阶段框架 DUDE，把带非对称惩罚的 混合奖励学习与经验总结结合起来，将失败模式蒸馏为可迁移的指导。配套发布基准 RUC（Real UI Clickboxes），含跨四个领域与欺骗类别的 1407 个场景。DUDE 在保持任务性能的同时把易受骗 程度降低 53.8%——这一点很关键，因为多数安全干预都是以牺牲效用为代价。

`环境: Web` ｜ [arXiv:2605.09497](https://arxiv.org/abs/2605.09497)

#### When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents (DeAction) (2026-02)

把通常被分开研究的两类失效来源统一起来：源自外部攻击（如间接提示注入）的偏离动作，与源自 内部局限（如推理错误）的偏离动作——两者都背离用户意图、都损害安全性与任务可靠性，因此只针对 攻击设计的检测器会漏掉一半问题。工作定义了 CUA 的「偏离动作检测」任务，归纳出真实部署中的 三类常见情形，并基于真实轨迹构建带人工标注的动作级对齐标签基准 MisActBench。DeAction 是 通用护栏，在执行前检出偏离动作，并通过结构化反馈迭代纠正。

`环境: Desktop` ｜ [arXiv:2602.08995](https://arxiv.org/abs/2602.08995)

#### SafePred: A Predictive Guardrail for Computer-Using Agents via World Models (SafePred) (2026-02)

指出现有 CUA 护栏的共同盲区：它们都是被动式的，只在当前观测空间内约束行为，因此能拦下 「点击钓鱼链接」这类即时危害，却看不见长周期风险。文中的例子很到位——清理日志在局部看 完全合理，但会导致未来审计无从追溯，而这个后果在当前观测里根本不可见。SafePred 转而把 预测出的未来风险与当前决策对齐，建立「风险到决策」的闭环，使延迟发生、不可逆的后果能被 计入每一步的判断。

`环境: Desktop` ｜ [arXiv:2602.01725](https://arxiv.org/abs/2602.01725)

#### MirrorGuard: Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction (MirrorGuard) (2026-01)

点明基于检测的防御悄悄付出的代价：拦截虽能避免损害，但常常过早中止任务，等于用效用换安全。 MirrorGuard 转而去**纠正不安全的推理**，并用神经符号仿真流水线解决训练成本问题——完全在 文本化的模拟环境中生成真实感的高风险 GUI 交互轨迹，捕捉不安全推理模式与潜在系统危害， 而无需在真实操作系统上执行任何破坏性操作。最终得到的是即插即用的防御，把仿真中训练出的 纠正能力迁移到真实部署。

`环境: Desktop` ｜ [arXiv:2601.12822](https://arxiv.org/abs/2601.12822)

#### Learning Efficient Guardrails for Compliance (PolicyGuard) (2025-10)

相比标准的安全目标，长周期 web agent 是否真的遵守现实世界的策略规范，此前研究严重不足。 PolicyGuardBench 用 6 万条策略-轨迹配对填补这一空缺，且关键在于它不只评测全轨迹违规 检测，还提出了基于前缀的检测任务——即在轨迹尚未结束时就抓到违规。作者在此数据上训练 轻量护栏 PolicyGuard，在保持高推理效率的同时取得较强检测准确率，并在未见领域上仍能 维持性能。对落地最有价值的结论是关于规模的：准确且可泛化的合规护栏在小模型上就能实现， 因此执行前的策略检查不必承担前沿模型的成本。

`环境: Web` ｜ [arXiv:2510.03485](https://arxiv.org/abs/2510.03485)

#### WebGuard: Building a Generalizable Guardrail for Web Agents (WebGuard) (2025-07)

主张 web agent 需要类似人类用户的访问控制机制，并发布首个支持 agent 动作风险评估的数据集： 来自 22 个领域、193 个网站（含常被忽视的长尾站点）的 4939 条人工标注状态改变动作，按 SAFE / LOW / HIGH 三级风险标注，并划分好训练测试集以支持泛化研究。核心结论相当刺眼—— 即便前沿 LLM 预测动作后果的准确率也不足 60%。

`环境: Web` ｜ [arXiv:2507.14293](https://arxiv.org/abs/2507.14293)
