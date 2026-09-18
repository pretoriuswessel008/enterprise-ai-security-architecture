# AI Threat Model – Enterprise AI Platform

## Scope

This threat model evaluates security risks affecting an enterprise AI/ML platform containing:

- Large Language Models (LLMs)
- Machine Learning models
- Training datasets
- RAG knowledge sources
- AI APIs
- Model registries
- Enterprise data
- AI Gateway services

The assessment follows a Zero Trust approach: AI models, users, datasets, APIs, and automated agents are not implicitly trusted.

---

## Threat Matrix

| Threat | Attack Scenario | Primary Security Controls | Detection |
|---|---|---|---|
| Model Poisoning | Malicious or manipulated data enters the training pipeline | Dataset integrity validation, provenance, hashing, approval gates | Dataset drift and integrity alerts |
| Prompt Injection | Attacker submits instructions designed to override intended model behaviour | AI Gateway, input validation, context isolation, tool authorization | Prompt-injection telemetry |
| Sensitive Data Leakage | Model exposes confidential enterprise or customer information | Data classification, least privilege, DLP, output filtering | DLP and sensitive-data alerts |
| API Abuse | Automated or unauthorized requests abuse AI endpoints | Authentication, authorization, rate limiting, API gateway | Abnormal request-rate detection |
| Adversarial Input | Manipulated features cause an ML model to misclassify input | Input sanitization, validation, adversarial testing | Prediction and feature anomaly detection |
| Model Theft | Attacker repeatedly queries a model to reconstruct its behaviour | Rate limiting, access control, query monitoring, response restrictions | Extraction-pattern and query-volume alerts |

---

# Threat 1 – Model Poisoning

## Attack

An attacker manipulates training data so that the resulting model learns malicious, biased, or attacker-controlled behaviour.

## Controls

- Dataset provenance
- Cryptographic hashing
- Dataset validation
- Approval gates
- Restricted write access
- Training-data versioning

## Detection

Changes in dataset integrity, distribution, labels, or provenance should generate security telemetry for investigation.

---

# Threat 2 – Prompt Injection

## Attack

An attacker provides malicious natural-language instructions intended to override system behaviour or manipulate model actions.

## Controls

- AI Gateway
- Input validation
- Context isolation
- Least-privilege tool access
- Independent authorization
- Output filtering

## Detection

Prompt-injection indicators should generate security events before requests reach privileged tools or protected resources.

---

# Threat 3 – Sensitive Data Leakage

## Attack

A user attempts to obtain confidential information through model responses, RAG retrieval, excessive context exposure, or unauthorized queries.

## Controls

- Data classification
- RBAC / ABAC
- DLP
- Output filtering
- Context restrictions
- Retrieval authorization

## Detection

Responses containing restricted data patterns or unauthorized classifications should generate DLP alerts and be blocked.

---

# Threat 4 – API Abuse

## Attack

An attacker repeatedly or automatically queries AI services to exhaust resources, enumerate functionality, bypass controls, or facilitate other attacks.

## Controls

- Authentication
- API authorization
- Rate limiting
- Request quotas
- Input validation
- Network controls

## Detection

Unusual request frequency, authentication failures, endpoint enumeration, or abnormal API behaviour should generate SOC telemetry.

---

# Threat 5 – Adversarial Input

## Attack

An attacker manipulates input features to move a malicious sample across the model's learned decision boundary.

## Controls

- Input validation
- Feature-range enforcement
- Data sanitization
- Adversarial testing
- Model robustness testing

## Detection

Unexpected feature combinations, abnormal prediction changes, and repeated boundary-testing behaviour should be monitored.

---

# Threat 6 – Model Theft

## Attack

An attacker systematically queries an AI/ML model to approximate its behaviour, decision boundaries, or proprietary functionality.

## Controls

- Strong authentication
- Least-privilege API access
- Rate limiting
- Query restrictions
- Response minimization
- Usage monitoring

## Detection

High-volume structured queries, systematic feature variation, or repeated attempts to map model behaviour should generate extraction alerts.

---

# Defensive Principle

AI security requires controls across the complete system rather than relying on the model to defend itself.

Security enforcement must exist around:

User → Identity → AI Gateway → Model → Data → APIs → Monitoring → SIEM → SOC

The objective is not merely to detect malicious prompts, but to prevent compromised or manipulated AI components from obtaining unauthorized authority over enterprise systems.
