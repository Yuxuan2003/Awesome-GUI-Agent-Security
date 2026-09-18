# Awesome-GUI-Agent-Security

**English** ｜ [简体中文](README.zh-CN.md)

> A curated list of papers on GUI / Computer-Use / Browser Agent security — organized by attack surface and defense layer, not by runtime environment.

![Last Update](https://img.shields.io/badge/last%20update-2026.09-brightgreen) ![Papers](https://img.shields.io/badge/papers-130%2B-blue) ![Time Range](https://img.shields.io/badge/time-2024.01--2026.09-orange) [![Link Check](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml/badge.svg)](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml) ![Awesome](https://img.shields.io/badge/-awesome-ff69b4)

> This page is the **index** — one line per paper. Each section links to a page with a 3–5 sentence summary per paper.

> **Scope:** papers whose *primary subject* is a GUI / computer-use / browser / mobile agent, with a security contribution. **Not included:** general LLM/agent security that only uses GUI agents as a testbed · agents *for* security work (pentest, CTF) · pure capability work.

<details>
<summary>Why organized by attack surface instead of environment?</summary>

> Most GUI agent lists split papers by runtime environment (Web / Mobile / Desktop), which scatters a single attack class across sections: multi-step indirect injection lands under Desktop, efficiency backdoors under Mobile, pop-up attacks under both Web and Desktop. Answering "what visual-layer attacks exist?" means reading every section.
>
> Here the primary axis is **attack vector and defense intervention point**. Runtime environment is a cross-cutting tag, used as a primary dimension only inside the benchmarks chapter.

</details>

## Contents

- [0 Surveys & Threat Models](#0-surveys-threat-models) · 7
- [1 Attack Surfaces](#1-attack-surfaces)
  - [1.1 Indirect Prompt Injection](#11-indirect-prompt-injection) · 7
  - [1.2 Visual-Layer Attacks](#12-visual-layer-attacks) · 8
  - [1.3 Environmental Injection](#13-environmental-injection) · 8
  - [1.4 Privilege Escalation & Permission Abuse](#14-privilege-escalation-permission-abuse) · 5
  - [1.5 Data Exfiltration & Privacy](#15-data-exfiltration-privacy) · 6
  - [1.6 Backdoors & Poisoning](#16-backdoors-poisoning) · 6
  - [1.7 Unintended Harm from Benign Instructions](#17-unintended-harm-from-benign-instructions) · 8
- [2 Defense Layers](#2-defense-layers)
  - [2.1 Input Filtering & Sanitization](#21-input-filtering-sanitization) · 12
  - [2.2 Pre-execution Risk Assessment](#22-pre-execution-risk-assessment) · 7
  - [2.3 Runtime Interception & Access Control](#23-runtime-interception-access-control) · 13
  - [2.4 Human-in-the-Loop & Confirmation](#24-human-in-the-loop-confirmation) · 4
  - [2.5 Post-hoc Recovery & Rollback](#25-post-hoc-recovery-rollback) · 4
  - [2.6 Formal Guarantees & Verification](#26-formal-guarantees-verification) · 7
- [3 Benchmarks & Datasets](#3-benchmarks-datasets)
  - [3.1 Comprehensive & Cross-environment](#31-comprehensive-cross-environment) · 9
  - [3.2 Web Environment](#32-web-environment) · 17
  - [3.3 Mobile Environment](#33-mobile-environment) · 5
  - [3.4 Desktop & OS Environment](#34-desktop-os-environment) · 4
- [4 Commercial AI Browsers & Product Security](#4-commercial-ai-browsers-product-security) · 2

Browse by environment: [Web](docs/by-env/web.md) ｜ [Mobile](docs/by-env/mobile.md) ｜ [Desktop](docs/by-env/desktop.md) ｜ [Cross-env](docs/by-env/cross.md)

---

## 0 Surveys & Threat Models

*Surveys, SoKs, and mappings onto threat taxonomies such as OWASP ASI and MITRE ATLAS* · [Summaries →](docs/by-section/en/0-surveys-threat-models.md)

- **[WebMASLab](https://arxiv.org/abs/2608.00202)** — From Monoliths to Swarms: A Study of Attack Surface Evolution in the Transition to Multi-Agent Web Systems · 2026-07 · 🌐
- **[SafeFlow](https://arxiv.org/abs/2607.25255)** — Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems · 2026-07 · 🧩
- **[Architecture-Lifecycle Framework](https://arxiv.org/abs/2605.07110)** — Securing Computer-Use Agents: A Unified Architecture-Lifecycle Framework for Deployment-Grounded Reliability · 2026-05 · 🧩
- **[Mobile Agent Security Study](https://arxiv.org/abs/2510.27140)** — Measuring the Security of Mobile LLM Agents under Adversarial Prompts from Untrusted Third-Party Channels · 2025-10 · 📱
- **[CUA Vuln SoK](https://arxiv.org/abs/2507.05445)** — A Systematization of Security Vulnerabilities in Computer Use Agents · 2025-07 · 🖥️🌐
- **[Trustworthy GUI Survey](https://arxiv.org/abs/2503.23434)** — Towards Trustworthy GUI Agents: A Survey · 2025-03 · 🧩
- **[BrowserART](https://arxiv.org/abs/2410.13886)** — Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents · 2024-10 · 🌐

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
- **[WIPI](https://arxiv.org/abs/2402.16965)** — A New Web Threat for LLM-Driven Web Agents · 2024-02 · 🌐

### 1.2 Visual-Layer Attacks

*Adversarial patches, pop-up lures, typographic attacks, screenshot poisoning* · [Summaries →](docs/by-section/en/1-2-visual-layer-attacks.md)

- **[UI Desynchronization](https://arxiv.org/abs/2609.16732)** — When Agents See Differently: Exposing UI Desynchronization Threats in Mobile Agents · 2026-09 · 📱
- **[AgentHijack](https://arxiv.org/abs/2609.09212)** — Visual Patch Attacks on Multimodal Computer-Use Agents · 2026-09 · 🖥️🌐
- **[Perception-Fusion Gap](https://arxiv.org/abs/2607.04334)** — Do GUI Agents Believe Their Eyes? Diagnosing State-Belief Reliance on Pixels versus Structure · 2026-07 · 🌐📱🖥️
- **[MIRAGE](https://arxiv.org/abs/2606.20717)** — Stealthy Visual Prompt Injection for Vulnerability Detection in Web Agents · 2026-06 · 🌐
- **[PRAC](https://arxiv.org/abs/2604.08005)** — Preference Redirection via Attention Concentration: An Attack on Computer Use Agents · 2026-04 · 🖥️🌐
- **[Semantic UI Injection](https://arxiv.org/abs/2604.07831)** — Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection · 2026-04 · 🧩
- **[Visual Confused Deputy](https://arxiv.org/abs/2603.14707)** — Exploiting and Defending Perception Failures in Computer-Using Agents · 2026-03 · 🖥️
- **[Agent-Only Perceptual Injection](https://arxiv.org/abs/2510.07809)** — Invisible to Humans, Triggered by Agents: Stealthy Jailbreak Attacks on Mobile Vision-Language Agents · 2025-10 · 📱

### 1.3 Environmental Injection

*UI element injection, accessibility tree, spoofed notifications, overlays* · [Summaries →](docs/by-section/en/1-3-environmental-injection.md)

- **[AnTrap](https://arxiv.org/abs/2608.24099)** — Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments · 2026-08 · 📱
- **[Not an A11y](https://arxiv.org/abs/2608.08939)** — How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection · 2026-08 · 📱
- **[MIRAGE (Mobile)](https://arxiv.org/abs/2605.28116)** — MIRAGE: Context-Aware Prompt Injection against Mobile GUI Agents via User-Generated Content · 2026-05 · 📱
- **[eTAMP](https://arxiv.org/abs/2604.02623)** — Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents · 2026-04 · 🌐
- **[Dynamic EIA](https://arxiv.org/abs/2509.11250)** — Environmental Injection Attacks against GUI Agents in Realistic Dynamic Environments · 2025-09 · 🌐
- **[A11y Tree IPI](https://arxiv.org/abs/2507.14799)** — Manipulating LLM Web Agents with Indirect Prompt Injection Attack via HTML Accessibility Tree · 2025-07 · 🌐
- **[AdInject](https://arxiv.org/abs/2505.21499)** — Real-World Black-Box Attacks on Web Agents via Advertising Delivery · 2025-05 · 🌐
- **[EIA](https://arxiv.org/abs/2409.11295)** — Environmental Injection Attack on Generalist Web Agents for Privacy Leakage · 2024-09 · 🌐

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
- **[VisualTrap](https://arxiv.org/abs/2507.06899)** — A Stealthy Backdoor Attack on GUI Agents via Visual Grounding Manipulation · 2025-07 · 📱🖥️
- **[VIBMA](https://arxiv.org/abs/2506.13205)** — Poison Once, Control Anywhere: Clean-Text Visual Backdoors in VLM-based Mobile Agents · 2025-06 · 📱

### 1.7 Unintended Harm from Benign Instructions

*No adversary involved — harm arising from the agent's own behavior on normal tasks* · [Summaries →](docs/by-section/en/1-7-unintended-harm-from-benign-instructions.md)

- **[Nudge Susceptibility](https://arxiv.org/abs/2609.19843)** — A Dual-Process Perspective on Nudge Susceptibility in LLM-Based GUI Agents · 2026-09 · 🌐
- **[Alignment Is Local](https://arxiv.org/abs/2607.29199)** — A Paired Diagnostic for GUI Agents under User Persuasion · 2026-07 · 📱🧩
- **[OTora](https://arxiv.org/abs/2605.08876)** — A Unified Red Teaming Framework for Reasoning-Level Denial-of-Service in LLM Agents · 2026-05 · 🌐🖥️
- **[OS-BLIND](https://arxiv.org/abs/2604.10577)** — The Blind Spot of Agent Safety: How Benign User Instructions Expose Critical Vulnerabilities in Computer-Use Agents · 2026-04 · 🖥️
- **[AutoElicit](https://arxiv.org/abs/2602.08235)** — When Benign Inputs Lead to Severe Harms: Eliciting Unsafe Unintended Behaviors of Computer-Use Agents · 2026-02 · 🖥️
- **[AgentBait](https://arxiv.org/abs/2601.07263)** — When Bots Take the Bait: Exposing and Mitigating the Emerging Social Engineering Attack in Web Automation Agent · 2026-01 · 🌐
- **[DECEPTICON](https://arxiv.org/abs/2512.22894)** — How Dark Patterns Manipulate Web Agents · 2025-12 · 🌐
- **[Dark Patterns Meet GUI Agents](https://arxiv.org/abs/2509.10723)** — LLM Agent Susceptibility to Manipulative Interfaces and the Role of Human Oversight · 2025-09 · 🌐

## 2 Defense Layers

*Organized by where the defense intervenes in the execution chain*

### 2.1 Input Filtering & Sanitization

*Filtering or masking untrusted content before it enters the model context* · [Summaries →](docs/by-section/en/2-1-input-filtering-sanitization.md)

- **[FocusMem](https://arxiv.org/abs/2608.04530)** — Factorizing Content, Readout, and Trust in Latent GUI Memory · 2026-08 · 📱🖥️🌐
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
- **[MirrorGuard](https://arxiv.org/abs/2601.12822)** — Toward Secure Computer-Use Agents via Simulation-to-Real Reasoning Correction · 2026-01 · 🖥️
- **[PolicyGuard](https://arxiv.org/abs/2510.03485)** — Learning Efficient Guardrails for Compliance · 2025-10 · 🌐
- **[WebGuard](https://arxiv.org/abs/2507.14293)** — Building a Generalizable Guardrail for Web Agents · 2025-07 · 🌐

### 2.3 Runtime Interception & Access Control

*Information-flow tracking, OS-level policy enforcement, sandboxing* · [Summaries →](docs/by-section/en/2-3-runtime-interception-access-control.md)

- **[HazardAuditor](https://arxiv.org/abs/2609.15134)** — From Executable Threats to Safer Computer-Use Agents · 2026-09 · 🖥️🌐
- **[Key-Step Supervision](https://arxiv.org/abs/2609.02057)** — Monitoring Web Agents Without Internal Signals: Observable Trajectories and Key-Step Supervision · 2026-09 · 🌐
- **[CURA](https://arxiv.org/abs/2608.27808)** — Certified Runtime Alarms for Computer-Use Agents · 2026-08 · 🖥️
- **[Prismata](https://arxiv.org/abs/2607.08147)** — Confining Cross-Site Prompt Injection in Web Agents · 2026-07 · 🌐
- **[BraveGuard](https://arxiv.org/abs/2606.01166)** — From Open-World Threats to Safer Computer-Use Agents · 2026-05 · 🖥️🌐
- **[TEE-Backed Isolation](https://arxiv.org/abs/2605.06393)** — Constraining Host-Level Abuse in Self-Hosted Computer-Use Agents via TEE-Backed Isolation · 2026-05 · 🖥️
- **[ceLLMate](https://arxiv.org/abs/2512.12594)** — Sandboxing Browser AI Agents · 2025-12 · 🌐
- **[OS-Sentinel](https://arxiv.org/abs/2510.24411)** — Towards Safety-Enhanced Mobile GUI Agents via Hybrid Validation in Realistic Workflows · 2025-10 · 📱
- **[CSAgent](https://arxiv.org/abs/2509.22256)** — Secure and Efficient Access Control for Computer-Use Agents via Context Space · 2025-09 · 🖥️
- **[AgentSentinel](https://arxiv.org/abs/2509.07764)** — An End-to-End and Real-Time Security Defense Framework for Computer-Use Agents · 2025-09 · 🖥️
- **[CUA-SHADE-Arena](https://arxiv.org/abs/2508.19461)** — Reliable Weak-to-Strong Monitoring of LLM Agents · 2025-08 · 🖥️
- **[HarmonyGuard](https://arxiv.org/abs/2508.04010)** — Toward Safety and Utility in Web Agents via Adaptive Policy Enhancement and Dual-Objective Optimization · 2025-08 · 🌐
- **[GuardAgent](https://arxiv.org/abs/2406.09187)** — Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning · 2024-06 · 🌐

### 2.4 Human-in-the-Loop & Confirmation

*Confirmation before critical actions, approval gates, interruptibility* · [Summaries →](docs/by-section/en/2-4-human-in-the-loop-confirmation.md)

- **[TIPO](https://arxiv.org/abs/2604.11259)** — Mobile GUI Agent Privacy Personalization with Trajectory Induced Preference Optimization · 2026-04 · 📱
- **[PrivWeb](https://arxiv.org/abs/2509.11939)** — Unobtrusive and Content-aware Privacy Protection For Web Agents · 2025-09 · 🌐
- **[VeriOS](https://arxiv.org/abs/2509.07553)** — Query-Driven Proactive Human-Agent-GUI Interaction for Trustworthy OS Agents · 2025-09 · 📱🖥️
- **[VerificAgent](https://arxiv.org/abs/2506.02539)** — Domain-Specific Memory Verification for Scalable Oversight of Aligned Computer-Use Agents · 2025-06 · 🖥️

### 2.5 Post-hoc Recovery & Rollback

*Failure attribution, state rollback, repair after harm has occurred* · [Summaries →](docs/by-section/en/2-5-post-hoc-recovery-rollback.md)

- **[Verified Repair](https://arxiv.org/abs/2608.24913)** — From Blind Edits to Verified Repair: Building Trustworthy User-Side LLM Agents for Web Accessibility · 2026-07 · 🌐
- **[CUADebug](https://arxiv.org/abs/2608.02643)** — Diagnosing and Repairing Computer-Use Agent Failures · 2026-07 · 🖥️
- **[Agent Fingerprinting](https://arxiv.org/abs/2606.20910)** — Whose Agent Are You? Multi-Layer Fingerprinting and Attribution of Autonomous Web Agents · 2026-06 · 🌐
- **[What Did It Actually Do](https://arxiv.org/abs/2603.28551)** — "What Did It Actually Do?": Understanding Risk Awareness and Traceability for Computer-Use Agents · 2026-03 · 🖥️

### 2.6 Formal Guarantees & Verification

*Defenses with provable guarantees: formal verification, control-flow integrity, conformal risk control* · [Summaries →](docs/by-section/en/2-6-formal-guarantees-verification.md)

- **[AOHP](https://arxiv.org/abs/2606.23449)** — An Open-Source OS-Level Agent Harness for Personalized, Efficient and Secure Interaction · 2026-06 · 📱
- **[SkillHarness](https://arxiv.org/abs/2606.20636)** — Harnessing Safe Skills for Computer-Use Agents · 2026-06 · 🖥️
- **[CORA](https://arxiv.org/abs/2604.09155)** — Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation · 2026-04 · 📱
- **[DMAST](https://arxiv.org/abs/2603.04364)** — Dual-Modality Multi-Stage Adversarial Safety Training: Robustifying Multimodal Web Agents Against Cross-Modal Attacks · 2026-03 · 🌐
- **[Aura](https://arxiv.org/abs/2602.10915)** — Blind Gods and Broken Screens: Architecting a Secure, Intent-Centric Mobile Agent Operating System · 2026-02 · 📱
- **[NOVA](https://arxiv.org/abs/2601.09923)** — CaMeLs Can Use Computers Too: System-level Security for Computer Use Agents · 2026-01 · 🖥️
- **[LaSM](https://arxiv.org/abs/2507.10610)** — Layer-wise Scaling Mechanism for Defending Pop-up Attack on GUI Agents · 2025-07 · 🖥️🌐

## 3 Benchmarks & Datasets

*The only chapter where runtime environment serves as a primary organizing dimension*

### 3.1 Comprehensive & Cross-environment

*Benchmarks spanning multiple environments or threat classes* · [Summaries →](docs/by-section/en/3-1-comprehensive-cross-environment.md)

- **[Mind2Web-Injection](https://arxiv.org/abs/2609.05535)** — Beyond the Verdict: Evidence-Aligned Evaluation of Visual Prompt-Injection Guardrails · 2026-09 · 🌐
- **[ADeptS-Bench](https://arxiv.org/abs/2608.26204)** — Measuring the Trustworthiness of Computer Use Agents Across Devices · 2026-08 · 🖥️📱
- **[OSGuard](https://arxiv.org/abs/2606.15034)** — A Benchmark for Safety in Computer-Use Agents · 2026-06 · 🖥️🌐
- **[CUA-HandCrafted](https://arxiv.org/abs/2606.05233)** — Domain-Conditioned Safety in Frontier Computer-Using Agents: A 793-Episode Browser Benchmark, a Coding-Domain Cross-Reference, and a Reproducibility Audit of Recent Red-Teaming · 2026-06 · 🖥️🌐
- **[AgentHazard](https://arxiv.org/abs/2604.02947)** — A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents · 2026-04 · 🖥️
- **[GUIGuard-Bench](https://arxiv.org/abs/2601.18842)** — Toward a General Evaluation for Privacy-Preserving GUI Agents · 2026-01 · 📱🖥️
- **[SusBench](https://arxiv.org/abs/2510.11035)** — An Online Benchmark for Evaluating Dark Pattern Susceptibility of Computer-Use Agents · 2025-10 · 🌐🖥️
- **[CUAHarm](https://arxiv.org/abs/2508.00935)** — Measuring Harmfulness of Computer-Using Agents · 2025-07 · 🖥️
- **[RiOSWorld](https://arxiv.org/abs/2506.00618)** — Benchmarking the Risk of Multimodal Computer-Use Agents · 2025-05 · 🖥️

### 3.2 Web Environment

*Security evaluation for web / browser agents* · [Summaries →](docs/by-section/en/3-2-web-environment.md)

- **[Who Pays the Price](https://arxiv.org/abs/2606.13385)** — Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents · 2026-06 · 🌐
- **[WebDecept](https://arxiv.org/abs/2606.13686)** — Benchmarking Web Agent Safety under E-commerce Deceptive Interfaces · 2026-04 · 🌐
- **[RiskWebWorld](https://arxiv.org/abs/2604.13531)** — A Realistic Interactive Benchmark for GUI Agents in E-commerce Risk Management · 2026-04 · 🌐
- **[WebSP-Eval](https://arxiv.org/abs/2604.06367)** — Evaluating Web Agents on Website Security and Privacy Tasks · 2026-04 · 🌐
- **[ClawTrap](https://arxiv.org/abs/2603.18762)** — A MITM-Based Red-Teaming Framework for Real-World OpenClaw Security Evaluation · 2026-03 · 🌐
- **[MUZZLE](https://arxiv.org/abs/2602.09222)** — Adaptive Agentic Red-Teaming of Web Agents Against Indirect Prompt Injection Attacks · 2026-02 · 🌐
- **[MalURLBench](https://arxiv.org/abs/2601.18113)** — A Benchmark Evaluating Agents' Vulnerabilities When Processing Web URLs · 2026-01 · 🌐
- **[WebTrap Park](https://arxiv.org/abs/2601.08406)** — An Automated Platform for Systematic Security Evaluation of Web Agents · 2026-01 · 🌐
- **[TRAP](https://arxiv.org/abs/2512.23128)** — It's a TRAP! Task-Redirecting Agent Persuasion Benchmark for Web Agents · 2025-12 · 🌐
- **[BrowseSafe](https://arxiv.org/abs/2511.20597)** — Understanding and Preventing Prompt Injection Within AI Browser Agents · 2025-11 · 🌐
- **[Genesis](https://arxiv.org/abs/2510.18314)** — Evolving Attack Strategies for LLM Web Agent Red-Teaming · 2025-10 · 🌐
- **[SecureWebArena](https://arxiv.org/abs/2510.10073)** — A Holistic Security Evaluation Benchmark for LVLM-based Web Agents · 2025-10 · 🌐
- **[WAInjectBench](https://arxiv.org/abs/2510.01354)** — Benchmarking Prompt Injection Detections for Web Agents · 2025-10 · 🌐
- **[RISK](https://arxiv.org/abs/2509.21982)** — A Framework for GUI Agents in E-commerce Risk Management · 2025-09 · 🌐
- **[WebRRSBench](https://arxiv.org/abs/2509.21782)** — Benchmarking MLLM-based Web Understanding: Reasoning, Robustness and Safety · 2025-09 · 🌐
- **[AdvAgent](https://arxiv.org/abs/2410.17401)** — Controllable Blackbox Red-teaming on Web Agents · 2024-10 · 🌐
- **[ST-WebAgentBench](https://arxiv.org/abs/2410.06703)** — A Benchmark for Evaluating Safety and Trustworthiness in Web Agents · 2024-10 · 🌐

### 3.3 Mobile Environment

*Security evaluation for mobile / Android / iOS agents* · [Summaries →](docs/by-section/en/3-3-mobile-environment.md)

- **[PriMobiBench](https://arxiv.org/abs/2609.13873)** — Characterizing Visual Privacy Leakage in VLM-Driven Mobile GUI Agents · 2026-09 · 📱
- **[MobileWorldSafety](https://arxiv.org/abs/2608.17659)** — Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps · 2026-08 · 📱
- **[GhostEI-Bench](https://arxiv.org/abs/2510.20333)** — Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments? · 2025-10 · 📱
- **[MVISU-Bench](https://arxiv.org/abs/2508.09057)** — Benchmarking Mobile Agents for Real-World Tasks by Multi-App, Vague, Interactive, Single-App and Unethical Instructions · 2025-08 · 📱
- **[MobileSafetyBench](https://arxiv.org/abs/2410.17520)** — Evaluating Safety of Autonomous Agents in Mobile Device Control · 2024-10 · 📱

### 3.4 Desktop & OS Environment

*Security evaluation for desktop / OS-level computer-use agents* · [Summaries →](docs/by-section/en/3-4-desktop-os-environment.md)

- **[OS-SPEAR](https://arxiv.org/abs/2604.24348)** — A Toolkit for the Safety, Performance, Efficiency, and Robustness Analysis of OS Agents · 2026-04 · 🖥️
- **[LPS-Bench](https://arxiv.org/abs/2602.03255)** — Benchmarking Safety Awareness of Computer-Use Agents in Long-Horizon Planning under Benign and Adversarial Scenarios · 2026-02 · 🖥️
- **[OS-Harm](https://arxiv.org/abs/2506.14866)** — A Benchmark for Measuring Safety of Computer Use Agents · 2025-06 · 🖥️
- **[VPI-Bench](https://arxiv.org/abs/2506.02456)** — Visual Prompt Injection Attacks for Computer-Use Agents · 2025-06 · 🖥️🌐

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

