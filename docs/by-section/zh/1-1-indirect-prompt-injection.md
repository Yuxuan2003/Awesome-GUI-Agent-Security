# 1.1 间接提示注入

*Indirect Prompt Injection*

[← 返回索引](../../../README.zh-CN.md#11-间接提示注入) ｜ [English](../en/1-1-indirect-prompt-injection.md)

*经网页、文档、邮件等外部内容承载的注入*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### SIR: Self-improving Red-teaming for Compute Use Agents (SIR) (2026-08)

指出现有 CUA 安全基准用的都是人工手写的固定注入载荷，会低估自适应攻击者的真实威胁。提出 黑盒 IPI 攻击 SIR：从一个用自然语言描述的可复用「隐蔽性原则」小库中组合注入内容，再套一层 迭代反馈循环——诊断受害 agent 失败的攻击轨迹，把成功绕过的模式蒸馏回原则库。这把红队从 静态测试变成自我改进的过程，说明固定载荷的评测结论会随攻击者迭代迅速失效。

`环境: Desktop, Web` ｜ [arXiv:2608.30207](https://arxiv.org/abs/2608.30207)

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)

针对现有间接提示注入评测多为单步、无法刻画真实 CUA 长流程风险的问题，提出多步 IPI 基准 StepJack，构造 480 个测试用例，把注入载荷分散在多步任务的中间环节，模拟攻击者只能污染 流程某一环的现实约束。实验显示多步注入相比单步把攻击成功率最高抬升 31.2 个百分点， 说明单步评测显著低估了 CUA 的真实暴露面，且现有防御在流程中段几乎不再触发。

`环境: Desktop, 跨环境` ｜ [arXiv:2608.06477](https://arxiv.org/abs/2608.06477)

#### Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents (Invisible Ink) (2026-08)

研究攻击者如何把恶意目标伪装在看似合法的任务描述中，使 CUA 在执行用户确认过的正常任务时 顺带完成攻击者目标。核心发现是这类攻击能绕过 human-in-the-loop 确认机制——因为人工审核 看到的动作序列本身每一步都合理，只有组合起来才产生危害。这揭示了「逐步确认」这一主流 防御范式的结构性盲区。

`环境: Desktop` ｜ [arXiv:2608.02018](https://arxiv.org/abs/2608.02018)

#### Agent Data Injection Attacks are Realistic Threats to AI Agents (ADI) (2026-07)

指出间接提示注入的研究几乎全部集中在「指令注入」上——即不可信数据被当作指令解释——而针对 性构建的缓解措施也继承了这个狭窄的问题框架。论文提出 agent 数据注入（ADI）：把恶意数据 伪装成**可信数据**，例如安全关键元数据（资源标识符、数据来源）或 agent 上下文数据（工具 调用与响应格式）。其影响与指令注入相当，agent 依然会执行非预期动作，但那些专门用于识别 「嵌入指令」的防御，没有任何理由把一段格式规范的元数据标记为可疑。

`环境: Web, Desktop` ｜ [arXiv:2607.05120](https://arxiv.org/abs/2607.05120)

#### WebTrap: Stealthy Mid-Task Hijacking of Browser Agents During Navigation (WebTrap) (2026-05)

诊断出现有针对浏览器 agent 的注入攻击有两个缺口：一是有效性低，在玩具基准上调优的攻击 放到真实环境、长步骤链条中就达不成端到端目标；二是隐蔽性弱，多数攻击把攻击目标与用户目标 对立起来，导致可用性明显崩塌，攻击相当于自我暴露。WebTrap 转而在**任务中途**劫持：用多步 指令融合引导把两个目标缝合起来，让 agent 在完成攻击目标后继续把用户原任务做完。配套的 上下文接地生成方法使注入内容与所处任务环境保持一致，看不出突兀。

`环境: Web` ｜ [arXiv:2605.08310](https://arxiv.org/abs/2605.08310)

#### You Told Me to Do It: Measuring Instructional Text-induced Private Data Leakage in LLM Agents (ReadSecBench) (2026-03)

把这一结构性问题命名为「可信执行者困境」（Trusted Executor Dilemma）：高权限 agent 被授予 终端访问、文件系统控制与出网能力，然后被要求阅读并执行项目文档——但它无法区分恶意指令与 正常的安装配置说明，因此会以很高的比率执行嵌在文档里的对抗指令。论文强调这是「指令遵循」 设计范式的必然后果，而非实现层面的 bug。测量以三维分类法（语言伪装、结构混淆、语义抽象） 组织，基准 ReadSecBench 由 500 个真实 README 文件构成。

`环境: Desktop` ｜ [arXiv:2603.11862](https://arxiv.org/abs/2603.11862)
