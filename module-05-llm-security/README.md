# Module 05 – Generative AI Security Cyber Range

## Overview

This module demonstrates security testing and defensive architecture for Large Language Model (LLM) applications.

A deliberately vulnerable AI application is exposed to common GenAI attack techniques before deterministic security controls are introduced around the model.

The objective is to demonstrate why LLM security cannot depend on the model correctly interpreting security instructions.

---

## Attack Scenarios

The laboratory evaluates:

- Direct prompt injection
- Indirect prompt injection
- System-prompt extraction
- Sensitive-data leakage
- Jailbreak attempts
- Excessive agency
- Unauthorized tool execution
- Malicious API/tool calls

---

## Vulnerable Architecture

```text
User
 ↓
LLM
 ↓
Enterprise Data / Tools
```

In this architecture, the model receives user instructions and has direct access to sensitive resources.

This creates the risk that manipulated natural-language instructions can influence access to protected information or functionality.

## Defensive Architecture

```text
User
 ↓
Identity / IAM
 ↓
AI Gateway
 ↓
Input Security
 ↓
LLM
 ↓
Tool / API Security
 ↓
Output Security
 ↓
DLP
 ↓
Security Logging
 ↓
SIEM / SOC
```

Security decisions are moved outside the probabilistic model and enforced through deterministic controls.

## Security Objectives

This laboratory demonstrates:

* Prompt-injection testing
* Jailbreak testing
* System-prompt protection
* Sensitive-data protection
* Input validation
* Output inspection
* Data Loss Prevention (DLP)
* Tool authorization
* Least-privilege tool access
* Security logging
* SIEM integration concepts
* Fail-closed security controls

## Trust Boundaries

The LLM is treated as an untrusted processing component.

It must not independently determine whether a user is authorized to:

* Access sensitive data
* Retrieve customer information
* Execute privileged tools
* Call protected APIs
* Reveal system instructions
* Override security controls

Authorization decisions must be enforced outside the model.

## Core Security Principle

Natural-language instructions are data, not authorization.

```text 
User Prompt
     ↓
Security Policy
     ↓
Authorization
     ↓
LLM Processing
     ↓
Output Inspection
     ↓
DLP
     ↓
Approved Response
```

The model may interpret the request. It must not grant the permission.
