# Awesome-GUI-Agent-Security

**English** ｜ [简体中文](README.zh-CN.md)

> A curated list of papers on GUI / Computer-Use / Browser Agent security — organized by attack surface and defense layer, not by runtime environment.

![Last Update](https://img.shields.io/badge/last%20update-2026.09-brightgreen) ![Papers](https://img.shields.io/badge/papers-90%2B-blue) ![Time Range](https://img.shields.io/badge/time-2025.01--2026.09-orange) [![Link Check](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml/badge.svg)](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml) ![Awesome](https://img.shields.io/badge/-awesome-ff69b4)

> This page is the **index** — one line per paper. Each section links to a page with a 3–5 sentence summary per paper.

> **Scope:** papers whose *primary subject* is a GUI / computer-use / browser / mobile agent, with a security contribution. **Not included:** general LLM/agent security that only uses GUI agents as a testbed · agents *for* security work (pentest, CTF) · pure capability work.

<details>
<summary>Why organized by attack surface instead of environment?</summary>

> Most GUI agent lists split papers by runtime environment (Web / Mobile / Desktop), which scatters a single attack class across sections: multi-step indirect injection lands under Desktop, efficiency backdoors under Mobile, pop-up attacks under both Web and Desktop. Answering "what visual-layer attacks exist?" means reading every section.

> Here the primary axis is **attack vector and defense intervention point**. Runtime environment is a cross-cutting tag, used as a primary dimension only inside the benchmarks chapter.

</details>

## Contents

- [0 Surveys & Threat Models](#0-surveys-threat-models) · 4
- [1 Attack Surfaces](#1-attack-surfaces)
  - [1.1 Indirect Prompt Injection](#11-indirect-prompt-injection) · 6
  - [1.2 Visual-Layer Attacks](#12-visual-layer-attacks) · 4
  - [1.3 Environmental Injection](#13-environmental-injection) · 5
  - [1.4 Privilege Escalation & Permission Abuse](#14-privilege-escalation-permission-abuse) · 5
  - [1.5 Data Exfiltration & Privacy](#15-data-exfiltration-privacy) · 6
  - [1.6 Backdoors & Poisoning](#16-backdoors-poisoning) · 5
  - [1.7 Unintended Harm from Benign Instructions](#17-unintended-harm-from-benign-instructions) · 5
- [2 Defense Layers](#2-defense-layers)
  - [2.1 Input Filtering & Sanitization](#21-input-filtering-sanitization) · 11
  - [2.2 Pre-execution Risk Assessment](#22-pre-execution-risk-assessment) · 5
  - [2.3 Runtime Interception & Access Control](#23-runtime-interception-access-control) · 8
  - [2.4 Human-in-the-Loop & Confirmation](#24-human-in-the-loop-confirmation) · 2
  - [2.5 Post-hoc Recovery & Rollback](#25-post-hoc-recovery-rollback) · 2
  - [2.6 Formal Guarantees & Verification](#26-formal-guarantees-verification) · 4
- [3 Benchmarks & Datasets](#3-benchmarks-datasets)
  - [3.1 Comprehensive & Cross-environment](#31-comprehensive-cross-environment) · 4
  - [3.2 Web Environment](#32-web-environment) · 9
  - [3.3 Mobile Environment](#33-mobile-environment) · 2
  - [3.4 Desktop & OS Environment](#34-desktop-os-environment) · 1
- [4 Commercial AI Browsers & Product Security](#4-commercial-ai-browsers-product-security) · 2

Browse by environment: [Web](docs/by-env/web.md) ｜ [Mobile](docs/by-env/mobile.md) ｜ [Desktop](docs/by-env/desktop.md) ｜ [Cross-env](docs/by-env/cross.md)

---

## 0 Surveys & Threat Models

*Surveys, SoKs, and mappings onto threat taxonomies such as OWASP ASI and MITRE ATLAS* · [Summaries →](docs/by-section/en/0-surveys-threat-models.md)

- **[WebMASLab](https://arxiv.org/abs/2608.00202)** — From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems · 2026-07 · 🌐
- **[Mobile Agent Security Study](https://arxiv.org/abs/2510.27140)** — Measuring the Security of Mobile LLM Agents under Adversarial Prompts from Untrusted Third-Party Channels · 2025-10 · 📱
- **[CUA Vuln SoK](https://arxiv.org/abs/2507.05445)** — A Systematization of Security Vulnerabilities in Computer Use Agents · 2025-07 · 🖥️🌐
- **[Trustworthy GUI Survey](https://arxiv.org/abs/2503.23434)** — Towards Trustworthy GUI Agents: A Survey · 2025-03 · 🧩

## 1 Attack Surfaces

*Organized by attack vector and entry point, not by runtime environment*

### 1.1 Indirect Prompt Injection

*Injection carried by external content: web pages, documents, email* · [Summaries →](docs/by-section/en/1-1-indirect-prompt-injection.md)

- **[SIR](https://arxiv.org/abs/2608.30207)** — Self-improving Red-teaming for Compute Use Agents · 2026-08 · 🖥️🌐
- **[StepJack](https://arxiv.org/abs/2608.06477)** — Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection · 2026-08 · 🖥️🧩
- **[Invisible Ink](https://arxiv.org/abs/2608.02018)** — Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents · 2026-08 · 🖥️
- **[ADI](https://arxiv.org/abs/2607.05120)** — Agent Data Injection Attacks are Realistic Threats to AI Agents · 2026-07 · 🌐🖥️
- **[WebTrap](https://arxiv.org/abs/2605.08310)** — Stealthy Mid-Task Hijacking of Browser Agents During Navigation · 2026-05 · 🌐
- **[ReadSecBench](https://arxiv.org/abs/2603.11862)** — You Told Me to Do It: Measuring Instructional Text-induced Private Data Leakage in LLM Agents · 2026-03 · 🖥️

### 1.2 Visual-Layer Attacks

*Adversarial patches, pop-up lures, typographic attacks, screenshot poisoning* · [Summaries →](docs/by-section/en/1-2-visual-layer-attacks.md)

- **[MIRAGE](https://arxiv.org/abs/2606.20717)** — Stealthy Visual Prompt Injection for Vulnerability Detection in Web Agents · 2026-06 · 🌐
- **[PRAC](https://arxiv.org/abs/2604.08005)** — Preference Redirection via Attention Concentration: An Attack on Computer Use Agents · 2026-04 · 🖥️🌐
- **[Semantic UI Injection](https://arxiv.org/abs/2604.07831)** — Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection · 2026-04 · 🧩
- **[Visual Confused Deputy](https://arxiv.org/abs/2603.14707)** — Exploiting and Defending Perception Failures in Computer-Using Agents · 2026-03 · 🖥️

### 1.3 Environmental Injection

*UI element injection, accessibility tree, spoofed notifications, overlays* · [Summaries →](docs/by-section/en/1-3-environmental-injection.md)

- **[AnTrap](https://arxiv.org/abs/2608.24099)** — Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments · 2026-08 · 📱
- **[Not an A11y](https://arxiv.org/abs/2608.08939)** — How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection · 2026-08 · 📱
- **[MIRAGE (Mobile)](https://arxiv.org/abs/2605.28116)** — MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content · 2026-05 · 📱
- **[eTAMP](https://arxiv.org/abs/2604.02623)** — Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents · 2026-04 · 🌐
- **[AdInject](https://arxiv.org/abs/2505.21499)** — Real-World Black-Box Attacks on Web Agents via Advertising Delivery · 2025-05 · 🌐

### 1.4 Privilege Escalation & Permission Abuse

*OS-level escalation, cross-app privilege abuse, permission-dialog manipulation, TOCTOU* · [Summaries →](docs/by-section/en/1-4-privilege-escalation-permission-abuse.md)

- **[Allow to Achieve](https://arxiv.org/abs/2608.04755)** — "Allow" to Achieve, Over-Privileged Inadvertently: The Unintended Cost of Task-Completion-Driven Pop-up Decisions in Mobile GUI Agents · 2026-08 · 📱
- **[AI Sees](https://arxiv.org/abs/2607.00333)** — (A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents · 2026-07 · 📱
- **[PUSV](https://arxiv.org/abs/2604.18860)** — Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents · 2026-04 · 🖥️
- **[Atomicity for Agents](https://arxiv.org/abs/2603.00476)** — Exposing, Exploiting, and Mitigating TOCTOU Vulnerabilities in Browser-Use Agents · 2026-02 · 🌐
- **[Action Rebinding](https://arxiv.org/abs/2601.12349)** — Mind the Gap: Action Rebinding Attacks against Android GUI Agents · 2026-01 · 📱

### 1.5 Data Exfiltration & Privacy

*Credential theft, PII leakage, contextual-integrity violations, oversharing* · [Summaries →](docs/by-section/en/1-5-data-exfiltration-privacy.md)

- **[LoginTrap](https://arxiv.org/abs/2608.04741)** — Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents · 2026-08 · 🌐
- **[Capable but Careless](https://arxiv.org/abs/2606.23189)** — Do Computer-Use Agents Follow Contextual Integrity? · 2026-06 · 🖥️
- **[Scammer4U](https://arxiv.org/abs/2606.00497)** — "I Strongly Suspect This Website Is a Scam": Benchmarking PII Leakage and Detection without Defense in Autonomous Web Agents · 2026-05 · 🌐
- **[MyPhoneBench](https://arxiv.org/abs/2604.00986)** — Do Phone-Use Agents Respect Your Privacy? · 2026-04 · 📱
- **[WebPII](https://arxiv.org/abs/2603.17357)** — Benchmarking Visual PII Detection for Computer-Use Agents · 2026-03 · 🌐🖥️
- **[SPILLage](https://arxiv.org/abs/2602.13516)** — Agentic Oversharing on the Web · 2026-02 · 🌐

### 1.6 Backdoors & Poisoning

*Grounding backdoors, efficiency backdoors, memory poisoning* · [Summaries →](docs/by-section/en/1-6-backdoors-poisoning.md)

- **[SynChain](https://arxiv.org/abs/2608.06862)** — Inducing Computer-Use Agent Systems to Construct Their Own Attack Chains · 2026-08 · 🖥️
- **[MemVenom](https://arxiv.org/abs/2606.10742)** — Triggered Poisoning of Multimodal Memories in Web Agents · 2026-06 · 🌐
- **[AgentRAE](https://arxiv.org/abs/2603.23007)** — Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents · 2026-03 · 📱
- **[SlowBA](https://arxiv.org/abs/2603.08316)** — An Efficiency Backdoor Attack towards VLM-based GUI Agents · 2026-03 · 📱🧩
- **[VIBMA](https://arxiv.org/abs/2506.13205)** — Poison Once, Control Anywhere: Clean-Text Visual Backdoors in VLM-based Mobile Agents · 2025-06 · 📱

### 1.7 Unintended Harm from Benign Instructions

*No adversary involved — harm arising from the agent's own behavior on normal tasks* · [Summaries →](docs/by-section/en/1-7-unintended-harm-from-benign-instructions.md)

- **[Alignment Is Local](https://arxiv.org/abs/2607.29199)** — A Paired Diagnostic for GUI Agents under User Persuasion · 2026-07 · 📱🧩
- **[OS-BLIND](https://arxiv.org/abs/2604.10577)** — The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents · 2026-04 · 🖥️
- **[AutoElicit](https://arxiv.org/abs/2602.08235)** — When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents · 2026-02 · 🖥️
- **[AgentBait](https://arxiv.org/abs/2601.07263)** — When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent · 2026-01 · 🌐
- **[DECEPTICON](https://arxiv.org/abs/2512.22894)** — How Dark Patterns Manipulate Web Agents · 2025-12 · 🌐

## 2 Defense Layers

*Organized by where the defense intervenes in the execution chain*

### 2.1 Input Filtering & Sanitization

*Filtering or masking untrusted content before it enters the model context* · [Summaries →](docs/by-section/en/2-1-input-filtering-sanitization.md)

- **[UCM](https://arxiv.org/abs/2607.05277)** — Untrusted Content Masking for Web Agents with Security Guarantees · 2026-07 · 🌐
- **[CAPED](https://arxiv.org/abs/2606.12666)** — Context-Aware Privacy Exposure Defense for Mobile GUI Agents · 2026-06 · 📱
- **[MaskClaw](https://arxiv.org/abs/2605.28646)** — Edge-Side Personalized Privacy Arbitration for GUI Agents with Behavior-Driven Skill Evolution · 2026-05 · 📱🖥️
- **[WARD](https://arxiv.org/abs/2605.15030)** — Adversarially Robust Defense of Web Agents Against Prompt Injections · 2026-05 · 🌐
- **[SnapGuard](https://arxiv.org/abs/2604.25562)** — Lightweight Prompt Injection Detection for Screenshot-Based Web Agents · 2026-04 · 🌐
- **[WebAgentGuard](https://arxiv.org/abs/2604.12284)** — A Reasoning-Driven Guard Model for Detecting Prompt Injection Attacks in Web Agents · 2026-04 · 🌐
- **[Cognitive Firewall](https://arxiv.org/abs/2603.23791)** — The Cognitive Firewall: Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense · 2026-03 · 🌐
- **[Available but Invisible](https://arxiv.org/abs/2602.10139)** — Anonymization-Enhanced Privacy Protection for Mobile GUI Agents: Available but Invisible · 2026-02 · 📱
- **[WebSentinel](https://arxiv.org/abs/2602.03792)** — Detecting and Localizing Prompt Injection Attacks for Web Agents · 2026-02 · 🌐
- **[Rennervate](https://arxiv.org/abs/2512.08417)** — Attention is All You Need to Defend Against Indirect Prompt Injection Attacks in LLMs · 2025-12 · 🌐
- **[DualTAP](https://arxiv.org/abs/2511.13248)** — A Dual-Task Adversarial Protector for Mobile MLLM Agents · 2025-11 · 📱

### 2.2 Pre-execution Risk Assessment

*World-model prediction, action risk scoring* · [Summaries →](docs/by-section/en/2-2-pre-execution-risk-assessment.md)

- **[SeerGuard](https://arxiv.org/abs/2607.15550)** — A Safety Framework for Mobile GUI Agents via World Model Prediction · 2026-07 · 📱
- **[DUDE](https://arxiv.org/abs/2605.09497)** — Don't Click That: Teaching Web Agents to Resist Deceptive Interfaces · 2026-05 · 🌐
- **[DeAction](https://arxiv.org/abs/2602.08995)** — When Actions Go Off-Task: Detecting and Correcting Misaligned Actions in Computer-Use Agents · 2026-02 · 🖥️
- **[SafePred](https://arxiv.org/abs/2602.01725)** — A Predictive Guardrail for Computer-Using Agents via World Models · 2026-02 · 🖥️
- **[WebGuard](https://arxiv.org/abs/2507.14293)** — Building a Generalizable Guardrail for Web Agents · 2025-07 · 🌐

### 2.3 Runtime Interception & Access Control

*Information-flow tracking, OS-level policy enforcement, sandboxing* · [Summaries →](docs/by-section/en/2-3-runtime-interception-access-control.md)

- **[CURA](https://arxiv.org/abs/2608.27808)** — Certified Runtime Alarms for Computer-Use Agents · 2026-08 · 🖥️
- **[Prismata](https://arxiv.org/abs/2607.08147)** — Confining Cross-Site Prompt Injection in Web Agents · 2026-07 · 🌐
- **[BraveGuard](https://arxiv.org/abs/2606.01166)** — From Open-World Threats to Safer Computer-Use Agents · 2026-05 · 🖥️🌐
- **[ceLLMate](https://arxiv.org/abs/2512.12594)** — Sandboxing Browser AI Agents · 2025-12 · 🌐
- **[CSAgent](https://arxiv.org/abs/2509.22256)** — Secure and Efficient Access Control for Computer-Use Agents via Context Space · 2025-09 · 🖥️
- **[AgentSentinel](https://arxiv.org/abs/2509.07764)** — An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents · 2025-09 · 🖥️
- **[CUA-SHADE-Arena](https://arxiv.org/abs/2508.19461)** — Reliable Weak-to-Strong Monitoring of LLM Agents · 2025-08 · 🖥️
- **[HarmonyGuard](https://arxiv.org/abs/2508.04010)** — Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization · 2025-08 · 🌐

### 2.4 Human-in-the-Loop & Confirmation

*Confirmation before critical actions, approval gates, interruptibility* · [Summaries →](docs/by-section/en/2-4-human-in-the-loop-confirmation.md)

- **[TIPO](https://arxiv.org/abs/2604.11259)** — Mobile GUI Agent Privacy Personalization with Trajectory Induced Preference Optimization · 2026-04 · 📱
- **[VerificAgent](https://arxiv.org/abs/2506.02539)** — Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents · 2025-06 · 🖥️

### 2.5 Post-hoc Recovery & Rollback

*Failure attribution, state rollback, repair after harm has occurred* · [Summaries →](docs/by-section/en/2-5-post-hoc-recovery-rollback.md)

- **[CUADebug](https://arxiv.org/abs/2608.02643)** — Diagnosing and Repairing Computer-Use Agent Failures · 2026-07 · 🖥️
- **[What Did It Actually Do](https://arxiv.org/abs/2603.28551)** — "What Did It Actually Do?": Understanding Risk Awareness and Traceability for Computer-Use Agents · 2026-03 · 🖥️

### 2.6 Formal Guarantees & Verification

*Defenses with provable guarantees: formal verification, control-flow integrity, conformal risk control* · [Summaries →](docs/by-section/en/2-6-formal-guarantees-verification.md)

- **[SkillHarness](https://arxiv.org/abs/2606.20636)** — Harnessing Safe Skills for Computer-Use Agents · 2026-06 · 🖥️
- **[CORA](https://arxiv.org/abs/2604.09155)** — Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation · 2026-04 · 📱
- **[DMAST](https://arxiv.org/abs/2603.04364)** — Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks · 2026-03 · 🌐
- **[LaSM](https://arxiv.org/abs/2507.10610)** — Layer-wise Scaling Mechanism for Defending Pop-up Attack on GUI Agents · 2025-07 · 🖥️🌐

## 3 Benchmarks & Datasets

*The only chapter where runtime environment serves as a primary organizing dimension*

### 3.1 Comprehensive & Cross-environment

*Benchmarks spanning multiple environments or threat classes* · [Summaries →](docs/by-section/en/3-1-comprehensive-cross-environment.md)

- **[ADeptS-Bench](https://arxiv.org/abs/2608.26204)** — Measuring the Trustworthiness of Computer Use Agents Across Devices · 2026-08 · 🖥️📱
- **[OSGuard](https://arxiv.org/abs/2606.15034)** — A Benchmark for Safety in Computer-Use Agents · 2026-06 · 🖥️🌐
- **[AgentHazard](https://arxiv.org/abs/2604.02947)** — A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents · 2026-04 · 🖥️
- **[GUIGuard-Bench](https://arxiv.org/abs/2601.18842)** — Toward a General Evaluation for Privacy-Preserving GUI Agents · 2026-01 · 📱🖥️

### 3.2 Web Environment

*Security evaluation for web / browser agents* · [Summaries →](docs/by-section/en/3-2-web-environment.md)

- **[Who Pays the Price](https://arxiv.org/abs/2606.13385)** — Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents · 2026-06 · 🌐
- **[WebDecept](https://arxiv.org/abs/2606.13686)** — Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces · 2026-04 · 🌐
- **[RiskWebWorld](https://arxiv.org/abs/2604.13531)** — A Realistic Interactive Benchmark for GUI Agents in E-commerce Risk Management · 2026-04 · 🌐
- **[WebSP-Eval](https://arxiv.org/abs/2604.06367)** — Evaluating Web Agents on Website Security and Privacy Tasks · 2026-04 · 🌐
- **[MUZZLE](https://arxiv.org/abs/2602.09222)** — Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks · 2026-02 · 🌐
- **[MalURLBench](https://arxiv.org/abs/2601.18113)** — A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs · 2026-01 · 🌐
- **[BrowseSafe](https://arxiv.org/abs/2511.20597)** — Understanding and Preventing Prompt Injection Within AI Browser Agents · 2025-11 · 🌐
- **[Genesis](https://arxiv.org/abs/2510.18314)** — Evolving Attack Strategies for LLM Web Agent Red-Teaming · 2025-10 · 🌐
- **[WAInjectBench](https://arxiv.org/abs/2510.01354)** — Benchmarking Prompt Injection Detections for Web Agents · 2025-10 · 🌐

### 3.3 Mobile Environment

*Security evaluation for mobile / Android / iOS agents* · [Summaries →](docs/by-section/en/3-3-mobile-environment.md)

- **[MobileWorldSafety](https://arxiv.org/abs/2608.17659)** — Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps · 2026-08 · 📱
- **[GhostEI-Bench](https://arxiv.org/abs/2510.20333)** — Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments? · 2025-10 · 📱

### 3.4 Desktop & OS Environment

*Security evaluation for desktop / OS-level computer-use agents* · [Summaries →](docs/by-section/en/3-4-desktop-os-environment.md)

- **[OS-Harm](https://arxiv.org/abs/2506.14866)** — A Benchmark for Measuring Safety of Computer Use Agents · 2025-06 · 🖥️

## 4 Commercial AI Browsers & Product Security

*Primarily non-arXiv sources: vendor security advisories, CVEs, security blogs, disclosures. See docs/MAINTENANCE.md for how this chapter is tracked.* · [Summaries →](docs/by-section/en/4-commercial-ai-browsers-product-security.md)

- **[Broken Gates](https://arxiv.org/abs/2607.18659)** — Re-evaluating Web Bot Defenses in the Age of LLM Agents · 2026-07 · 🌐
- **[Privacy Practices of Browser Agents](https://arxiv.org/abs/2512.07725)** — Privacy Practices of Browser Agents · 2025-12 · 🌐

---

## Contributing

Edit **`data/papers.yaml`** only — `README.md`, `README.zh-CN.md`, and everything under `docs/` are generated by GitHub Actions. See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for inclusion criteria and entry format, and [MAINTENANCE.md](docs/MAINTENANCE.md) for the update workflow.

## Related lists

This list focuses on the security *of* GUI/CUA agents. For adjacent areas:

- General agent security (full OWASP ASI spectrum): `LLMSecurity/awesome-agent-skills-security`
- Using agents for security work (red teaming / pentest): `kagnlp/Awesome-Agentic-Security`
- Agent auditing and provenance: `yzhao062/awesome-auditable-ai`
- GUI agent capability research: `OSU-NLP-Group/GUI-Agents-Paper-List`

