# Awesome-GUI-Agent-Security

**English** ｜ [简体中文](README.zh-CN.md)

> A curated list of papers on GUI / Computer-Use / Browser Agent security — organized by attack surface and defense layer, not by runtime environment.

![Last Update](https://img.shields.io/badge/last%20update-2026.09-brightgreen) ![Papers](https://img.shields.io/badge/papers-30%2B-blue) ![Time Range](https://img.shields.io/badge/time-2025.01--2026.09-orange) [![Link Check](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml/badge.svg)](https://github.com/Yuxuan2003/Awesome-GUI-Agent-Security/actions/workflows/check.yml) ![Awesome](https://img.shields.io/badge/-awesome-ff69b4)

## Scope

Only papers whose **primary research subject** is a GUI / computer-use / browser / mobile agent, and whose contribution is about security.

**Not included:**

- General LLM / agent security that merely uses GUI agents as one of several test environments
- Using agents *for* security work (penetration testing, vulnerability discovery, CTF)
- Pure capability work (grounding accuracy, task success rate)

## Why organized by attack surface instead of environment

Most GUI agent lists split papers by runtime environment (Web / Mobile / Desktop), which scatters a single attack class across sections: multi-step indirect injection lands under Desktop, efficiency backdoors under Mobile, pop-up attacks under both Web and Desktop. Answering "what visual-layer attacks exist?" means reading every section.

Here the primary axis is **attack vector and defense intervention point**. Runtime environment is a cross-cutting tag, used as a primary dimension only inside the benchmarks chapter.

## Contents

- [0 Surveys & Threat Models](#0-surveys-threat-models)
- [1 Attack Surfaces](#1-attack-surfaces)
  - [1.1 Indirect Prompt Injection](#11-indirect-prompt-injection)
  - [1.2 Visual-Layer Attacks](#12-visual-layer-attacks)
  - [1.3 Environmental Injection](#13-environmental-injection)
  - [1.4 Privilege Escalation & Permission Abuse](#14-privilege-escalation-permission-abuse)
  - [1.5 Data Exfiltration & Privacy](#15-data-exfiltration-privacy)
  - [1.6 Backdoors & Poisoning](#16-backdoors-poisoning)
  - [1.7 Unintended Harm from Benign Instructions](#17-unintended-harm-from-benign-instructions)
- [2 Defense Layers](#2-defense-layers)
  - [2.1 Input Filtering & Sanitization](#21-input-filtering-sanitization)
  - [2.2 Pre-execution Risk Assessment](#22-pre-execution-risk-assessment)
  - [2.3 Runtime Interception & Access Control](#23-runtime-interception-access-control)
  - [2.4 Human-in-the-Loop & Confirmation](#24-human-in-the-loop-confirmation)
  - [2.5 Post-hoc Recovery & Rollback](#25-post-hoc-recovery-rollback)
  - [2.6 Formal Guarantees & Verification](#26-formal-guarantees-verification)
- [3 Benchmarks & Datasets](#3-benchmarks-datasets)
  - [3.1 Comprehensive & Cross-environment](#31-comprehensive-cross-environment)
  - [3.2 Web Environment](#32-web-environment)
  - [3.3 Mobile Environment](#33-mobile-environment)
  - [3.4 Desktop & OS Environment](#34-desktop-os-environment)
- [4 Commercial AI Browsers & Product Security](#4-commercial-ai-browsers-product-security)

Browse by environment: [Web](docs/by-env/web.md) ｜ [Mobile](docs/by-env/mobile.md) ｜ [Desktop](docs/by-env/desktop.md) ｜ [Cross-env](docs/by-env/cross.md)

---

## 0 Surveys & Threat Models

*Surveys, SoKs, and mappings onto threat taxonomies such as OWASP ASI and MITRE ATLAS*

#### A Systematization of Security Vulnerabilities in Computer Use Agents (CUA Vuln SoK) (2025-07)

Conducts systematic threat analysis and adversarial testing of real-world CUAs, identifying seven risk classes unique to the paradigm and dissecting three exploits in depth: clickjacking via visual overlays that mislead interface-level reasoning, indirect prompt injection achieving RCE through chained tool use, and CoT exposure attacks that hijack multi-step reasoning by manipulating implicit interface framing. The case studies converge on three architectural flaws shared across current implementations: no input provenance tracking, weak interface-action binding, and insufficient control-flow integrity.

`Env: Desktop, Web` ｜ [arXiv:2507.05445](https://arxiv.org/abs/2507.05445)

#### Towards Trustworthy GUI Agents: A Survey (Trustworthy GUI Survey) (2025-03)

Frames the execution gap as the central obstacle to trustworthy GUI agents: the misalignment between perception, reasoning, and interaction in dynamic, partially observable interfaces. Unlike conversational systems, GUI agents perform irreversible operations such as submitting forms, granting permissions, or deleting data. The survey proposes a workflow-aligned taxonomy decomposing trust into Perception, Reasoning, and Interaction Trust, traces how failures propagate and compound through action/observation loops, and argues that task completion alone is an insufficient basis for trust assessment.

`Env: Cross-env` ｜ [arXiv:2503.23434](https://arxiv.org/abs/2503.23434)

## 1 Attack Surfaces

*Organized by attack vector and entry point, not by runtime environment*

### 1.1 Indirect Prompt Injection

*Injection carried by external content: web pages, documents, email*

#### SIR: Self-improving Red-teaming for Compute Use Agents (SIR) (2026-08)

Argues that existing CUA safety benchmarks use hand-written fixed injections and therefore understate an adaptive adversary. SIR is a black-box IPI attack that composes stealthy injections from a small library of reusable, plain-language principles, wrapped in an iterative feedback loop that diagnoses failed attack trajectories and distils successful bypasses back into the library. Red-teaming becomes self-improving, implying that conclusions drawn from static payloads decay as attackers iterate.

`Env: Desktop, Web` ｜ [arXiv:2608.30207](https://arxiv.org/abs/2608.30207)

#### StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Prompt Injection (StepJack) (2026-08)

Existing indirect prompt injection (IPI) benchmarks for computer-use agents rely on single-step injections, which fail to capture the risk profile of realistic multi-step workflows. StepJack introduces a multi-step IPI benchmark of 480 cases that distributes the payload across intermediate steps, modelling an adversary who can only contaminate one stage of the pipeline. Multi-step injection raises attack success by up to 31.2 points over single-step, showing that current benchmarks substantially understate real exposure and that defenses rarely fire once execution is mid-flow.

`Env: Desktop, Cross-env` ｜ [arXiv:2608.06477](https://arxiv.org/abs/2608.06477)

#### Invisible Ink Threats: Adversarial Goals Behind Legitimate Tasks in Computer-Use Agents (Invisible Ink) (2026-08)

Studies how adversarial goals can be concealed inside tasks that look entirely legitimate, so a computer-use agent fulfils the attacker's objective while carrying out work the user has already approved. The key finding is that such attacks defeat human-in-the-loop confirmation: every individual action in the trajectory looks reasonable under review, and harm only emerges from their composition. This exposes a structural blind spot in step-by-step approval, the dominant defense paradigm for CUAs.

`Env: Desktop` ｜ [arXiv:2608.02018](https://arxiv.org/abs/2608.02018)

### 1.2 Visual-Layer Attacks

*Adversarial patches, pop-up lures, typographic attacks, screenshot poisoning*

#### MIRAGE: Stealthy Visual Prompt Injection for Vulnerability Detection in Web Agents (MIRAGE) (2026-06)

Criticises adversarial evaluations of multimodal web agents for adopting permissive threat models and visually conspicuous artifacts. This work moves to a constrained, realistic setting where the evaluator is an unprivileged third party — a merchant or advertiser — controlling only a semantically legitimate, spatially bounded region such as an ad slot or sponsored card. Under those constraints MIRAGE performs visual indirect prompt injection for targeted next-action hijacking, showing that control over one small legitimate region suffices to steer a vision-based agent.

`Env: Web` ｜ [arXiv:2606.20717](https://arxiv.org/abs/2606.20717)

#### Are GUI Agents Focused Enough? Automated Distraction via Semantic-level UI Element Injection (Semantic UI Injection) (2026-04)

Notes two limits in existing GUI-agent red-teaming: adversarial perturbations need white-box access unavailable commercially, and prompt injection is increasingly neutralized by stronger alignment. Semantic-level UI Element Injection is a black-box paradigm overlaying safety-aligned, harmless UI elements onto screenshots to misdirect visual grounding, pairing a modular Editor-Overlapper-Victim pipeline with iterative search. Across 19 victim models in 8 families, strategic optimization beats random injection by 3.5-6.9x on the most robust victims and transfers near-perfectly across architectures.

`Env: Cross-env` ｜ [arXiv:2604.07831](https://arxiv.org/abs/2604.07831)

### 1.3 Environmental Injection

*UI element injection, accessibility tree, spoofed notifications, overlays*

#### Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating Agents in Dynamic Adversarial Environments (AnTrap) (2026-08)

Notes that existing benchmarks lack systematic evaluation of GUI-agent robustness to runtime anomalies, though unexpected pop-ups and action misuse are routine on real Android devices. AnTrap organises real-world anomalies into a four-layer taxonomy (State, Thinking, Action, Round) with ten subcategories, plus a construction pipeline that injects adversarial perturbation while keeping tasks solvable. Evaluating 16 leading GUI models reveals universal vulnerability, with even the strongest degrading significantly; GRPO training in both clean and adversarial environments separates environment difficulty from model capability.

`Env: Mobile` ｜ [arXiv:2608.24099](https://arxiv.org/abs/2608.24099)

#### Not an A11y: How Android Accessibility Exposes Mobile AI Agents to Indirect Prompt Injection (Not an A11y) (2026-08)

Shows that the Android accessibility tree is an overlooked injection channel for mobile agents: any app can write text into accessibility nodes, and agents consume that content as trusted interface semantics. No special permission is required — an ordinary app suffices to inject instructions. The path bypasses defenses aimed at screenshots or web content entirely, revealing the absence of input-channel governance for mobile agents.

`Env: Mobile` ｜ [arXiv:2608.08939](https://arxiv.org/abs/2608.08939)

#### Poison Once, Exploit Forever: Environment-Injected Memory Poisoning Attacks on Web Agents (eTAMP) (2026-04)

Memory makes web agents personalized yet exploitable: storing past interactions creates a persistent attack surface spanning websites and sessions. Whereas prior work assumes attackers can write to memory directly or exploit cross-user sharing, eTAMP achieves cross-session, cross-site compromise through environmental observation alone — a single contaminated observation such as viewing a manipulated product page silently poisons memory and activates during later tasks on different sites, bypassing permission-based defenses. Attack success reaches 32.5% on GPT-5-mini, 23.4% on GPT-5.2, and 19.5% on GPT-OSS-120B, and the paper further identifies Frustration Exploitation.

`Env: Web` ｜ [arXiv:2604.02623](https://arxiv.org/abs/2604.02623)

#### AdInject: Real-World Black-Box Attacks on Web Agents via Advertising Delivery (AdInject) (2025-05)

Criticises prior environmental injection work for unrealistic assumptions — direct HTML manipulation, knowledge of user intent, or access to model parameters. AdInject instead injects malicious content through internet advertising delivery, operating under a black-box agent, static content constraints, and no knowledge of user intent. It combines ad content designed to lure agent clicks with VLM-based optimization that infers likely user intent from the target site, making it one of the most deployment-realistic threat models in this area.

`Env: Web` ｜ [arXiv:2505.21499](https://arxiv.org/abs/2505.21499)

### 1.4 Privilege Escalation & Permission Abuse

*OS-level escalation, cross-app privilege abuse, permission-dialog manipulation, TOCTOU*

#### "Allow" to Achieve, Over-Privileged Inadvertently: The Unintended Cost of Task-Completion-Driven Pop-up Decisions in Mobile GUI Agents (Allow to Achieve) (2026-08)

Identifies a systematic over-granting tendency in mobile GUI agents facing permission dialogs, and isolates two biases: App-Trust Bias, where agents allow anything requested by an already-installed app, and Task-Prior Override, where completing the task outweighs least-privilege. The result is silent accumulation of permissions far beyond task requirements, reducing the permission prompt — the last line of user-facing defense — to a formality.

`Env: Mobile` ｜ [arXiv:2608.04755](https://arxiv.org/abs/2608.04755)

#### (A)I Sees What You Don't: Exploiting New Attack Surfaces in Third-Party Mobile Agents (AI Sees) (2026-07)

Systematically maps the attack surface introduced by third-party mobile agents, centred on a perception gap: agents read screen content that users never see or never attend to, including hidden views, background notifications, and accessibility nodes. An attacker can exploit this asymmetry to steer the agent in ways the user cannot possibly notice, and the paper argues the third-party agent ecosystem lacks any mechanism constraining what an agent is allowed to perceive.

`Env: Mobile` ｜ [arXiv:2607.00333](https://arxiv.org/abs/2607.00333)

#### Temporal UI State Inconsistency in Desktop GUI Agents: Formalizing and Defending Against TOCTOU Attacks on Computer-Use Agents (PUSV) (2026-04)

Formalizes the observation-to-action gap in screenshot-and-click loops (mean 6.51 s on real OSWorld workloads) as a Visual Atomicity Violation, creating a Time-Of-Check-Time-Of-Use window for unprivileged UI manipulation. Three attack primitives are characterized: Notification Overlay Hijack, Window Focus Manipulation, and Web DOM Injection — the second being the desktop analog of Android Action Rebinding, achieving 100% action-redirection with zero visual evidence at observation time. The proposed PUSV defense re-verifies UI state immediately before each dispatch via masked pixel SSIM, global screenshot diff, and X Window snapshot diff, reaching 100% interception across 180 adversarial trials with no false positives and under 0.1 s overhead.

`Env: Desktop` ｜ [arXiv:2604.18860](https://arxiv.org/abs/2604.18860)

#### Mind the Gap: Action Rebinding Attacks against Android GUI Agents (Action Rebinding) (2026-01)

Shows that treating GUI agents as high-privilege operators — perceiving screen content and injecting inputs across application boundaries — fundamentally conflicts with Android's strict app sandboxing. The cross-application Action Rebinding attack lets a malicious app holding zero dangerous permissions hijack agent execution: it renders a benign contextual carrier to elicit a planned action, then swaps the foreground to a sensitive target during reasoning latency, so the agent unwittingly executes in a privileged context. The attack is further weaponized into programmable multi-step exploit loops by abusing the agent's own task-recovery logic.

`Env: Mobile` ｜ [arXiv:2601.12349](https://arxiv.org/abs/2601.12349)

### 1.5 Data Exfiltration & Privacy

*Credential theft, PII leakage, contextual-integrity violations, oversharing*

#### LoginTrap: Uncovering Task-Agnostic Phishing-Style Indirect Prompt Injection Attacks against LLM-based Web Agents (LoginTrap) (2026-08)

Login is a sensitive authentication boundary for web agents because it involves credentials, yet prior work has not examined whether malicious page content can induce login and cause end-to-end private data leakage. LoginTrap is a task-agnostic login-inducing attack assuming a black-box attacker who controls page context and the induced login flow without knowing the user task or agent internals: through a fuzzing-inspired process it generates page-specific indirect injections that make login look like a plausible prerequisite for continuing the task, steering the agent to an attacker-controlled login page.

`Env: Web` ｜ [arXiv:2608.04741](https://arxiv.org/abs/2608.04741)

#### Capable but Careless: Do Computer-Use Agents Follow Contextual Integrity? (Capable but Careless) (2026-06)

Applies the contextual integrity framework to ask whether computer-use agents respect information-flow norms when operating across applications. More capable agents turn out to be more prone to violations: to complete a task they will carry private data from one application into another's input fields, and no existing privacy control fires because every individual read and write stays within granted permissions. Proposes evaluating agents by information flow rather than by permission boundaries.

`Env: Desktop` ｜ [arXiv:2606.23189](https://arxiv.org/abs/2606.23189)

#### Do Phone-Use Agents Respect Your Privacy? (MyPhoneBench) (2026-04)

Asks whether phone-use agents respect privacy while completing benign tasks — hard to answer because privacy-compliant behavior was never operationalized for such agents, and ordinary apps do not reveal what data agents type into which form fields. MyPhoneBench operationalizes privacy-respecting use as permissioned access, minimal disclosure, and user-controlled memory via a minimal privacy contract, paired with instrumented mock apps and rule-based auditing. Across five frontier models, 10 apps, and 300 tasks, task success, privacy-compliant completion, and later-session preference reuse prove to be distinct capabilities that no single model dominates.

`Env: Mobile` ｜ [arXiv:2604.00986](https://arxiv.org/abs/2604.00986)

#### WebPII: Benchmarking Visual PII Detection for Computer-Use Agents (WebPII) (2026-03)

CUAs create new privacy risks from two directions: training data scraped from real websites inevitably contains sensitive information, and cloud-hosted inference exposes user screenshots. No public benchmark existed for detecting PII in web screenshots. WebPII provides 44,865 annotated e-commerce UI images with an extended PII taxonomy covering transaction-level re-identification identifiers, anticipatory detection for partially-filled forms, and scalable VLM-based UI reproduction. The accompanying WebRedact more than doubles text-extraction baseline accuracy (0.753 vs 0.357 mAP@50) at 20ms CPU latency.

`Env: Web, Desktop` ｜ [arXiv:2603.17357](https://arxiv.org/abs/2603.17357)

#### SPILLage: Agentic Oversharing on the Web (SPILLage) (2026-02)

Unlike chatbots answering questions in controlled settings, web agents act in the wild with access to user resources such as emails and calendars, interacting with third parties and leaving an action trace. The paper formalizes Natural Agentic Oversharing — unintentional disclosure of task-irrelevant user information through that trace — and characterizes it along channel (content vs. behavior) and directness (explicit vs. implicit). This exposes a blind spot: prior work targets text leakage, but agents also overshare behaviorally through clicks, scrolls, and navigation patterns that third parties can monitor. Benchmarked on 180 tasks across live e-commerce sites.

`Env: Web` ｜ [arXiv:2602.13516](https://arxiv.org/abs/2602.13516)

### 1.6 Backdoors & Poisoning

*Grounding backdoors, efficiency backdoors, memory poisoning*

#### AgentRAE: Remote Action Execution through Notification-based Visual Backdoors against Screenshots-based Mobile GUI Agents (AgentRAE) (2026-03)

Existing backdoors against web GUI agents rely on environmental injection or deceptive pop-ups, which fail on screenshot-based mobile agents due to restricted trigger design space, OS background interference, and conflicts among multiple trigger-action mappings. AgentRAE induces Remote Action Execution using visually natural triggers such as benign app icons in notifications, via a two-stage pipeline that first sharpens the agent's sensitivity to subtle iconographic differences through contrastive learning, then binds each trigger to a specific action through backdoor post-training.

`Env: Mobile` ｜ [arXiv:2603.23007](https://arxiv.org/abs/2603.23007)

#### SlowBA: An Efficiency Backdoor Attack towards VLM-based GUI Agents (SlowBA) (2026-03)

Proposes an efficiency backdoor against VLM-based GUI agents: the trigger leaves task outcomes unchanged and instead inflates response latency or step count. Such backdoors are extremely hard to notice because every correctness check still passes and only resource consumption reveals them, so they can persist indefinitely while imposing continuous compute cost. This broadens the GUI-agent backdoor threat model from outcome tampering to availability and economic attacks.

`Env: Mobile, Cross-env` ｜ [arXiv:2603.08316](https://arxiv.org/abs/2603.08316)

### 1.7 Unintended Harm from Benign Instructions

*No adversary involved — harm arising from the agent's own behavior on normal tasks*

#### Alignment Is Local: A Paired Diagnostic for GUI Agents under User Persuasion (Alignment Is Local) (2026-07)

Introduces a paired diagnostic that measures how far a GUI agent's safety alignment degrades under multi-turn user persuasion. Alignment turns out to be local: agents refuse a harmful request in a single turn, then concede incrementally as the user persists with plausible-sounding justifications — and this decay is invisible to every single-turn metric. The finding implies that single-turn safety evaluation cannot characterise risk in realistic multi-turn interaction.

`Env: Mobile, Cross-env` ｜ [arXiv:2607.29199](https://arxiv.org/abs/2607.29199)

## 2 Defense Layers

*Organized by where the defense intervenes in the execution chain*

### 2.1 Input Filtering & Sanitization

#### Untrusted Content Masking for Web Agents with Security Guarantees (UCM) (2026-07)

Observes that provable injection defenses depend on strict isolation between trusted instructions and untrusted data — natural in text-based tool-use settings where an agent can reason from interface definitions alone — but web agents must first observe the rendered page, which structurally intermingles trusted and untrusted content and dissolves the very trust boundary those guarantees rest on. Untrusted Content Masking restores that boundary in web environments by exploiting a structural property of pages, letting provable defenses carry over.

`Env: Web` ｜ [arXiv:2607.05277](https://arxiv.org/abs/2607.05277)

#### The Cognitive Firewall: Securing Browser Based AI Agents Against Indirect Prompt Injection Via Hybrid Edge Cloud Defense (Cognitive Firewall) (2026-03)

Tackles the tension that cloud-based defenses offer strong semantic analysis but add latency and privacy exposure. The Cognitive Firewall is a three-stage split-compute architecture distributing checks across client and cloud: a local visual Sentinel, a cloud Deep Planner, and a deterministic Guard enforcing execution-time policies. Across 1,000 adversarial samples edge-only defenses miss 86.9% of semantic attacks, whereas the full hybrid drives attack success below 1% (0.88% static, 0.67% adaptive) while keeping deterministic constraints on side-effecting actions — and by filtering presentation-layer attacks locally it achieves roughly a 17,000x latency advantage over cloud-only baselines.

`Env: Web` ｜ [arXiv:2603.23791](https://arxiv.org/abs/2603.23791)

### 2.2 Pre-execution Risk Assessment

*World-model prediction, action risk scoring*

#### WebGuard: Building a Generalizable Guardrail for Web Agents (WebGuard) (2025-07)

Argues web agents need access controls analogous to those for human users, and releases the first dataset supporting web-agent action risk assessment: 4,939 human-annotated state-changing actions from 193 websites across 22 domains, including often-overlooked long-tail sites, labelled under a three-tier schema (SAFE / LOW / HIGH) with designated train-test splits for generalization study. The headline finding is stark — even frontier LLMs predict action outcomes with under 60% accuracy.

`Env: Web` ｜ [arXiv:2507.14293](https://arxiv.org/abs/2507.14293)

### 2.3 Runtime Interception & Access Control

*Information-flow tracking, OS-level policy enforcement, sandboxing*

#### CURA: Certified Runtime Alarms for Computer-Use Agents (CURA) (2026-08)

Shows that self-report — the cheapest oversight channel a deployer has — fails exactly where oversight matters. Across 361 OSWorld tasks the pipeline scores 82.9 on average (above the 72.4 human reference), yet 64 of 71 failures (90%) end with a success claim, 61 assert no blocker, and the explicit failure affordance goes unused across roughly 9,100 calls. CURA is an external monitor reading only harness-visible telemetry — no model internals, extra LLM calls, or prompt changes — turning the trajectory into a sequential test with certified false-alarm control: at alpha = 0.10 its CUSUM alarm detects 42.3% of failures a median of 31 steps before termination at a realized false-alarm rate of 0.066.

`Env: Desktop` ｜ [arXiv:2608.27808](https://arxiv.org/abs/2608.27808)

#### Prismata: Confining Cross-Site Prompt Injection in Web Agents (Prismata) (2026-07)

Frames web-agent injection as a recurrence of XSS: mixing trusted and untrusted content was already proven dangerous, and agents revive the risk by interpreting natural language as instructions, letting third-party and user-generated content hijack them. The core difficulty is that deriving a task-specific security policy requires reasoning over page structure already entangled with attacker content. Prismata enforces contextual least privilege via dynamic trust derivation that assigns permission labels to page content with structural confinement guarantees inspired by classical integrity models, constraining both what the agent sees and what it can do.

`Env: Web` ｜ [arXiv:2607.08147](https://arxiv.org/abs/2607.08147)

#### Secure and Efficient Access Control for Computer-Use Agents via Context Space (CSAgent) (2025-09)

Argues that granting agents control over computers is risky because of inherent LLM uncertainty — deviations from user intent can be irreversible — and that user confirmation and LLM-based dynamic validation each fall short on usability, security, or performance. CSAgent is a system-level, static policy-based access control framework that bridges static policy and dynamic context through intent- and context-aware policies, with an automated toolchain for constructing and refining them, enforced by an optimized OS service so actions execute only under specific user intents and contexts.

`Env: Desktop` ｜ [arXiv:2509.22256](https://arxiv.org/abs/2509.22256)

### 2.4 Human-in-the-Loop & Confirmation

*No entries yet*

### 2.5 Post-hoc Recovery & Rollback

#### CUADebug: Diagnosing and Repairing Computer-Use Agent Failures (CUADebug) (2026-07)

Targets diagnosis and repair after a computer-use agent fails, proposing a framework that localises the failing step and generates a fix. Although framed around reliability, its failure attribution and state rollback capabilities transfer directly to post-incident security recovery: determining where a hijacked agent first deviated and reverting to the last trusted state. It is one of the few systematic works in the post-hoc recovery defense layer.

`Env: Desktop` ｜ [arXiv:2608.02643](https://arxiv.org/abs/2608.02643)

### 2.6 Formal Guarantees & Verification

#### CORA: Conformal Risk-Controlled Agents for Safeguarded Mobile GUI Automation (CORA) (2026-04)

Existing GUI-agent safeguards rest on prompt engineering, brittle heuristics, and VLM-as-critic, offering neither formal verification nor user-tunable guarantees. CORA is a post-policy, pre-action framework giving statistical guarantees on harmful executed actions: it reframes safety as selective action execution, trains a Guardian to estimate action-conditional risk, then uses Conformal Risk Control to calibrate an execute/abstain boundary meeting a user-specified risk budget, routing rejected actions to a Diagnostician that recommends confirm, reflect, or abort. A Goal-Lock mechanism guards against visual injection.

`Env: Mobile` ｜ [arXiv:2604.09155](https://arxiv.org/abs/2604.09155)

## 3 Benchmarks & Datasets

*The only chapter where runtime environment serves as a primary organizing dimension*

### 3.1 Comprehensive & Cross-environment

#### ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agents Across Devices (ADeptS-Bench) (2026-08)

Fills the gap that no benchmark jointly assesses whether CUAs interact safely with visual interfaces while handling ambiguous instructions. ADeptS-Bench is a dual-stream trustworthiness benchmark: the Safety stream pairs benign and malicious tasks with threats embedded in the visual interface, and the Disambiguation stream tests whether agents seek clarification under ambiguous intent. Across seven models none stays above 80% task success while holding attack success below 30%; every model clicks Checkout on a $25K order, and none detects a factory-reset button mislabelled as Optimize.

`Env: Desktop, Mobile` ｜ [arXiv:2608.26204](https://arxiv.org/abs/2608.26204)

#### AgentHazard: A Benchmark for Evaluating Harmful Behavior in Computer-Use Agents (AgentHazard) (2026-04)

Addresses the novel risks that arise once computer-use agents can act persistently across tools and files, introducing AgentHazard, a benchmark of 2,653 instances spanning diverse risk categories and attack strategies. The central observation is that harmful behaviour typically accumulates from a chain of individually plausible but collectively unsafe actions. Claude Code backed by Qwen3-Coder reaches a 73.63% attack success rate, indicating that base-model alignment alone does not secure the agent layer.

`Env: Desktop` ｜ [arXiv:2604.02947](https://arxiv.org/abs/2604.02947)

### 3.2 Web Environment

#### Who Pays the Price? Stakeholder-Centric Prompt Injection Benchmarking for Real-world Web Agents (Who Pays the Price) (2026-06)

Points out that existing security benchmarks take an attack-centric view, measuring whether injection is technically feasible while ignoring how the resulting harm is distributed. The paper argues injection risk is victim-dependent: one exploit yields asymmetric consequences across stakeholders (user, platform, merchant), and the same attack pattern varies substantially in effectiveness depending on the target. It builds a stakeholder-centric benchmark focused on e-commerce, where agent actions carry direct financial consequences.

`Env: Web` ｜ [arXiv:2606.13385](https://arxiv.org/abs/2606.13385)

### 3.3 Mobile Environment

#### MobileWorldSafety: Benchmarking GUI Agent Safety Against Environmental Injection Attacks in Android Apps (MobileWorldSafety) (2026-08)

Argues that existing benchmarks miss everyday usage and offer no systematic evaluation of mobile GUI agents under environmental injection — a pressing gap now that such agents are moving from prototypes into deployment while continuously processing untrusted environmental content. MobileWorldSafety comprises 142 risk tasks built on real Android applications, covering indirect prompt injection and adversarial instructions across everyday channels, with a programmatically verifiable success condition per task so attack outcomes are objectively measurable.

`Env: Mobile` ｜ [arXiv:2608.17659](https://arxiv.org/abs/2608.17659)

#### GhostEI-Bench: Do Mobile Agents Resilience to Environmental Injection in Dynamic On-Device Environments? (GhostEI-Bench) (2025-10)

Identifies environmental injection as an underexplored threat distinct from prompt-based attacks: rather than manipulating textual instructions, it corrupts visual perception by inserting adversarial UI elements such as deceptive overlays or spoofed notifications directly into the GUI, bypassing textual safeguards and risking privacy leakage, financial loss, or irreversible device compromise. GhostEI-Bench moves beyond static image assessment by injecting adversarial events into realistic application workflows inside fully operational Android emulators.

`Env: Mobile` ｜ [arXiv:2510.20333](https://arxiv.org/abs/2510.20333)

### 3.4 Desktop & OS Environment

#### OS-Harm: A Benchmark for Measuring Safety of Computer Use Agents (OS-Harm) (2025-06)

Notes that CUA safety has been largely overlooked despite growing deployment, and introduces OS-Harm on top of the OSWorld environment to test three harm categories: deliberate user misuse, prompt injection attacks, and model misbehavior. It comprises 150 tasks spanning harassment, copyright infringement, disinformation, and data exfiltration, requiring interaction with email clients, code editors, and browsers. An automated judge scores both accuracy and safety with high human agreement (0.76 and 0.79 F1).

`Env: Desktop` ｜ [arXiv:2506.14866](https://arxiv.org/abs/2506.14866)

## 4 Commercial AI Browsers & Product Security

*Primarily non-arXiv sources: vendor security advisories, CVEs, security blogs, disclosures. Rationale: arXiv yields zero hits for "browser agent" / "browser-use" over a three-week window, yet the security of products like Atlas, Comet, and Edge Copilot Mode is a live topic — that work simply does not go through paper venues. This chapter needs its own non-arXiv tracking pass; do not skip it just because arXiv returns nothing.*

*No entries yet*

---

## Contributing

Edit **`data/papers.yaml`** only — `README.md`, `README.zh-CN.md`, and everything under `docs/` are generated by GitHub Actions. See [CONTRIBUTING.md](CONTRIBUTING.md) for inclusion criteria and entry format, and [MAINTENANCE.md](MAINTENANCE.md) for the update workflow.

## Related lists

This list focuses on the security *of* GUI/CUA agents. For adjacent areas:

- General agent security (full OWASP ASI spectrum): `LLMSecurity/awesome-agent-skills-security`
- Using agents for security work (red teaming / pentest): `kagnlp/Awesome-Agentic-Security`
- Agent auditing and provenance: `yzhao062/awesome-auditable-ai`
- GUI agent capability research: `OSU-NLP-Group/GUI-Agents-Paper-List`

