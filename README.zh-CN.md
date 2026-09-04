# Awesome-GUI-Agent-Security

[English](README.md) ｜ **简体中文**

> GUI / Computer-Use / 浏览器 Agent 安全论文清单 —— 按攻防轴组织，而非按运行环境。

![Last Update](https://img.shields.io/badge/last%20update-2026.09-brightgreen) ![Papers](https://img.shields.io/badge/papers-30%2B-blue) ![Time Range](https://img.shields.io/badge/time-2025.01--2026.09-orange) [![Link Check](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml/badge.svg)](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml) ![Awesome](https://img.shields.io/badge/-awesome-ff69b4)

> 本页是**索引**，每篇一行；每节链接到带 2-4 句中文简介的小节页。

> **收录范围：** 主要研究对象是 GUI / computer-use / browser / mobile agent、且贡献属于安全范畴的论文。**不收录：** 仅把 GUI agent 当试验场的通用 LLM/agent 安全 · 用 agent 做安全工作（渗透、CTF）· 纯能力向工作。

<details>
<summary>为什么按攻防轴而不按环境组织？</summary>

现有的 GUI agent 清单大多按运行环境（Web / Mobile / Desktop）切分，结果是同一类攻击被打散：多步间接注入落在 Desktop、效率后门落在 Mobile、弹窗攻击横跨 Web 与 Desktop 两处。想回答「视觉层攻击有哪些」就得翻遍所有分组。

本仓库以**攻击载体与防御介入时点**为一级维度，运行环境降为交叉标签，仅在评测基准一章内作为一级维度使用。

</details>

## 目录

- [0 综述与威胁模型](#0-综述与威胁模型) · 2
- [1 攻击面](#1-攻击面)
  - [1.1 间接提示注入](#11-间接提示注入) · 3
  - [1.2 视觉层攻击](#12-视觉层攻击) · 2
  - [1.3 环境注入](#13-环境注入) · 4
  - [1.4 越权与权限滥用](#14-越权与权限滥用) · 4
  - [1.5 数据泄露与隐私](#15-数据泄露与隐私) · 5
  - [1.6 后门与投毒](#16-后门与投毒) · 2
  - [1.7 良性指令下的意外危害](#17-良性指令下的意外危害) · 1
- [2 防御层](#2-防御层)
  - [2.1 输入侧过滤与净化](#21-输入侧过滤与净化) · 2
  - [2.2 执行前风险评估](#22-执行前风险评估) · 1
  - [2.3 执行中拦截与权限控制](#23-执行中拦截与权限控制) · 3
  - [2.4 人在环与确认机制](#24-人在环与确认机制)
  - [2.5 事后恢复与回滚](#25-事后恢复与回滚) · 1
  - [2.6 形式化保证与验证](#26-形式化保证与验证) · 1
- [3 评测基准与数据集](#3-评测基准与数据集)
  - [3.1 综合与跨环境基准](#31-综合与跨环境基准) · 2
  - [3.2 Web 环境基准](#32-web-环境基准) · 1
  - [3.3 Mobile 环境基准](#33-mobile-环境基准) · 2
  - [3.4 Desktop 与 OS 环境基准](#34-desktop-与-os-环境基准) · 1
- [4 商用 AI 浏览器与产品安全](#4-商用-ai-浏览器与产品安全)

按环境浏览： [Web](docs/by-env/web.zh-CN.md) ｜ [Mobile](docs/by-env/mobile.zh-CN.md) ｜ [Desktop](docs/by-env/desktop.zh-CN.md) ｜ [跨环境](docs/by-env/cross.zh-CN.md)

---

## 0 综述与威胁模型

*领域综述、SoK、以及 OWASP ASI / MITRE ATLAS 等威胁分类框架的对照* · [简介 →](docs/by-section/zh/0-surveys-threat-models.md)

- **[CUA Vuln SoK](https://arxiv.org/abs/2507.05445)** — A Systematization of Security Vulnerabilities in Computer Use Agents · 2025-07 · 🖥️🌐
- **[Trustworthy GUI Survey](https://arxiv.org/abs/2503.23434)** — Towards Trustworthy GUI Agents: A Survey · 2025-03 · 🧩

## 1 攻击面

*按攻击载体与入口组织，而非按运行环境*

### 1.1 间接提示注入

*经网页、文档、邮件等外部内容承载的注入* · [简介 →](docs/by-section/zh/1-1-indirect-prompt-injection.md)

- **[SIR](https://arxiv.org/abs/2608.30207)** — Self-improving Red-teaming for Compute Use Agents · 2026-08 · 🖥️🌐
- **[StepJack](https://arxiv.org/abs/2608.06477)** — Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection · 2026-08 · 🖥️🧩
- **[Invisible Ink](https://arxiv.org/abs/2608.02018)** — Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents · 2026-08 · 🖥️

### 1.2 视觉层攻击

*对抗补丁、弹窗诱导、排版攻击、截图污染* · [简介 →](docs/by-section/zh/1-2-visual-layer-attacks.md)

- **[MIRAGE](https://arxiv.org/abs/2606.20717)** — Stealthy Visual Prompt Injection for Vulnerability Detection in Web Agents · 2026-06 · 🌐
- **[Semantic UI Injection](https://arxiv.org/abs/2604.07831)** — Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection · 2026-04 · 🧩

### 1.3 环境注入

*UI 元素注入、无障碍树、伪造通知、覆盖层* · [简介 →](docs/by-section/zh/1-3-environmental-injection.md)

- **[AnTrap](https://arxiv.org/abs/2608.24099)** — Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments · 2026-08 · 📱
- **[Not an A11y](https://arxiv.org/abs/2608.08939)** — How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection · 2026-08 · 📱
- **[eTAMP](https://arxiv.org/abs/2604.02623)** — Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents · 2026-04 · 🌐
- **[AdInject](https://arxiv.org/abs/2505.21499)** — Real-World Black-Box Attacks on Web Agents via Advertising Delivery · 2025-05 · 🌐

### 1.4 越权与权限滥用

*OS 级越权、跨应用提权、权限弹窗诱导、TOCTOU* · [简介 →](docs/by-section/zh/1-4-privilege-escalation-permission-abuse.md)

- **[Allow to Achieve](https://arxiv.org/abs/2608.04755)** — "Allow" to Achieve, Over-Privileged Inadvertently: The Unintended Cost of Task-Completion-Driven Pop-up Decisions in Mobile GUI Agents · 2026-08 · 📱
- **[AI Sees](https://arxiv.org/abs/2607.00333)** — (A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents · 2026-07 · 📱
- **[PUSV](https://arxiv.org/abs/2604.18860)** — Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents · 2026-04 · 🖥️
- **[Action Rebinding](https://arxiv.org/abs/2601.12349)** — Mind the Gap: Action Rebinding Attacks against Android GUI Agents · 2026-01 · 📱

### 1.5 数据泄露与隐私

*凭据窃取、PII 外泄、上下文完整性破坏、过度分享* · [简介 →](docs/by-section/zh/1-5-data-exfiltration-privacy.md)

- **[LoginTrap](https://arxiv.org/abs/2608.04741)** — Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents · 2026-08 · 🌐
- **[Capable but Careless](https://arxiv.org/abs/2606.23189)** — Do Computer-Use Agents Follow Contextual Integrity? · 2026-06 · 🖥️
- **[MyPhoneBench](https://arxiv.org/abs/2604.00986)** — Do Phone-Use Agents Respect Your Privacy? · 2026-04 · 📱
- **[WebPII](https://arxiv.org/abs/2603.17357)** — Benchmarking Visual PII Detection for Computer-Use Agents · 2026-03 · 🌐🖥️
- **[SPILLage](https://arxiv.org/abs/2602.13516)** — Agentic Oversharing on the Web · 2026-02 · 🌐

### 1.6 后门与投毒

*grounding 后门、效率后门、记忆投毒* · [简介 →](docs/by-section/zh/1-6-backdoors-poisoning.md)

- **[AgentRAE](https://arxiv.org/abs/2603.23007)** — Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents · 2026-03 · 📱
- **[SlowBA](https://arxiv.org/abs/2603.08316)** — An Efficiency Backdoor Attack towards VLM-based GUI Agents · 2026-03 · 📱🧩

### 1.7 良性指令下的意外危害

*无恶意攻击者，agent 自身在正常指令下造成危害* · [简介 →](docs/by-section/zh/1-7-unintended-harm-from-benign-instructions.md)

- **[Alignment Is Local](https://arxiv.org/abs/2607.29199)** — A Paired Diagnostic for GUI Agents under User Persuasion · 2026-07 · 📱🧩

## 2 防御层

*按防御在执行链上的介入时点组织*

### 2.1 输入侧过滤与净化

*在内容进入模型上下文前过滤或遮蔽不可信部分* · [简介 →](docs/by-section/zh/2-1-input-filtering-sanitization.md)

- **[UCM](https://arxiv.org/abs/2607.05277)** — Untrusted Content Masking for Web Agents with Security Guarantees · 2026-07 · 🌐
- **[Cognitive Firewall](https://arxiv.org/abs/2603.23791)** — The Cognitive Firewall: Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense · 2026-03 · 🌐

### 2.2 执行前风险评估

*世界模型预测、动作风险打分* · [简介 →](docs/by-section/zh/2-2-pre-execution-risk-assessment.md)

- **[WebGuard](https://arxiv.org/abs/2507.14293)** — Building a Generalizable Guardrail for Web Agents · 2025-07 · 🌐

### 2.3 执行中拦截与权限控制

*信息流追踪、OS 级策略强制、沙箱* · [简介 →](docs/by-section/zh/2-3-runtime-interception-access-control.md)

- **[CURA](https://arxiv.org/abs/2608.27808)** — Certified Runtime Alarms for Computer-Use Agents · 2026-08 · 🖥️
- **[Prismata](https://arxiv.org/abs/2607.08147)** — Confining Cross-Site Prompt Injection in Web Agents · 2026-07 · 🌐
- **[CSAgent](https://arxiv.org/abs/2509.22256)** — Secure and Efficient Access Control for Computer-Use Agents via Context Space · 2025-09 · 🖥️

### 2.4 人在环与确认机制

*关键动作前的人工确认、审批门、可打断性*

*本节暂无收录条目*

### 2.5 事后恢复与回滚

*失败归因、状态回滚、危害发生后的修复* · [简介 →](docs/by-section/zh/2-5-post-hoc-recovery-rollback.md)

- **[CUADebug](https://arxiv.org/abs/2608.02643)** — Diagnosing and Repairing Computer-Use Agent Failures · 2026-07 · 🖥️

### 2.6 形式化保证与验证

*带可证明保证的防御：形式化验证、控制流完整性、共形风险控制* · [简介 →](docs/by-section/zh/2-6-formal-guarantees-verification.md)

- **[CORA](https://arxiv.org/abs/2604.09155)** — Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation · 2026-04 · 📱

## 3 评测基准与数据集

*本章二级按运行环境切分（这是环境标签唯一作为一级组织维度的地方）*

### 3.1 综合与跨环境基准

*同时覆盖多个环境或威胁类别的基准* · [简介 →](docs/by-section/zh/3-1-comprehensive-cross-environment.md)

- **[ADeptS-Bench](https://arxiv.org/abs/2608.26204)** — Measuring the Trustworthiness of Computer Use Agents Across Devices · 2026-08 · 🖥️📱
- **[AgentHazard](https://arxiv.org/abs/2604.02947)** — A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents · 2026-04 · 🖥️

### 3.2 Web 环境基准

*针对 web / 浏览器 agent 的安全评测* · [简介 →](docs/by-section/zh/3-2-web-environment.md)

- **[Who Pays the Price](https://arxiv.org/abs/2606.13385)** — Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents · 2026-06 · 🌐

### 3.3 Mobile 环境基准

*针对移动 / Android / iOS agent 的安全评测* · [简介 →](docs/by-section/zh/3-3-mobile-environment.md)

- **[MobileWorldSafety](https://arxiv.org/abs/2608.17659)** — Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps · 2026-08 · 📱
- **[GhostEI-Bench](https://arxiv.org/abs/2510.20333)** — Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments? · 2025-10 · 📱

### 3.4 Desktop 与 OS 环境基准

*针对 desktop / OS 级 computer-use agent 的安全评测* · [简介 →](docs/by-section/zh/3-4-desktop-os-environment.md)

- **[OS-Harm](https://arxiv.org/abs/2506.14866)** — A Benchmark for Measuring Safety of Computer Use Agents · 2025-06 · 🖥️

## 4 商用 AI 浏览器与产品安全

*本章以非 arXiv 来源为主：厂商安全公告、CVE、安全博客、漏洞披露。 维护时的完整检索流程见 MAINTENANCE.md。*

*本节暂无收录条目*

---

## 贡献

只需修改 **`data/papers.yaml`** —— `README.md`、`README.zh-CN.md` 与 `docs/` 下所有文件均由 GitHub Actions 自动生成。收录标准与条目格式见 [CONTRIBUTING.md](CONTRIBUTING.md)，维护流程见 [MAINTENANCE.md](MAINTENANCE.md)。

## 相关仓库

本仓库聚焦 GUI/CUA agent 自身安全，以下方向请见：

- 通用 agent 安全（OWASP ASI 全谱系）：`LLMSecurity/awesome-agent-skills-security`
- 用 agent 做安全工作（红队 / 渗透测试）：`kagnlp/Awesome-Agentic-Security`
- agent 审计与溯源：`yzhao062/awesome-auditable-ai`
- GUI agent 能力向研究：`OSU-NLP-Group/GUI-Agents-Paper-List`

