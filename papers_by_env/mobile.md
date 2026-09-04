# Mobile 环境

*环境是交叉标签，同一篇论文可能出现在多个环境分组中。*

> 本文件由 `scripts/build.py` 生成，请勿手工编辑。

#### Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection (Not an A11y) (2026-08)
- **简介**：指出 Android 无障碍树（accessibility tree）是移动 agent 的一条被忽视的注入通道：任何 应用都能往无障碍节点写入文本，而 agent 会把这些内容当作可信的界面语义读取。攻击者无需 任何特殊权限即可通过普通应用注入指令。这条路径完全绕开了针对视觉截图或网页内容的 防御，暴露出移动 agent 输入通道治理的缺失。
- **环境**：Mobile
- **arXiv**：[2608.08939](https://arxiv.org/abs/2608.08939)

#### "Allow" to Achieve, Over-Privileged Inadvertently: The Unintended Cost of Task-Completion-Driven Pop-up Decisions in Mobile GUI Agents (Allow to Achieve) (2026-08)
- **简介**：发现移动 GUI agent 在遇到权限弹窗时存在系统性的过度授权倾向，识别出两种偏差：App-Trust Bias（对已安装应用默认信任而一律点允许）与 Task-Prior Override（为达成任务目标而牺牲 权限最小化）。结果是 agent 在用户不知情的情况下累积远超任务所需的权限，把权限弹窗这一 最后防线变成了形式。
- **环境**：Mobile
- **arXiv**：[2608.04755](https://arxiv.org/abs/2608.04755)

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)
- **简介**：提出成对诊断方法，衡量 GUI agent 的安全对齐在多轮用户说服下的退化程度。关键发现是对齐 具有「局部性」：agent 在单轮拒绝有害请求，但在用户连续追问、提供看似合理的理由后会逐步 让步，且这种退化不体现在任何单轮评测指标上。说明当前基于单轮的安全评测无法反映真实 多轮交互下的风险。
- **环境**：Mobile、跨环境
- **arXiv**：[2607.29199](https://arxiv.org/abs/2607.29199)

#### (A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents (AI Sees) (2026-07)
- **简介**：系统分析第三方移动 agent 引入的新攻击面，核心是「感知鸿沟」——agent 能读取到屏幕上用户 实际看不到或不会注意的内容（隐藏视图、后台通知、无障碍节点），攻击者可利用这一差异实施 用户完全无法察觉的诱导。指出第三方 agent 生态缺乏对 agent 可见性范围的约束机制。
- **环境**：Mobile
- **arXiv**：[2607.00333](https://arxiv.org/abs/2607.00333)

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)
- **简介**：提出针对 VLM-based GUI agent 的效率后门：触发器不改变任务最终结果，只让 agent 的响应 延迟大幅增加或步数显著膨胀。这类后门极难被察觉——正确性检测全部通过，只有观察资源消耗 才能发现，因此可长期潜伏并造成持续的算力成本损失。拓展了 GUI agent 后门的威胁定义， 从「结果篡改」扩展到「可用性与经济性攻击」。
- **环境**：Mobile、跨环境
- **arXiv**：[2603.08316](https://arxiv.org/abs/2603.08316)
