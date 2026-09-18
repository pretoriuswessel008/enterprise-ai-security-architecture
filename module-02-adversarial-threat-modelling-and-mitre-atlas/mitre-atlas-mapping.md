# MITRE ATLAS Threat Mapping

## Purpose

MITRE ATLAS provides a knowledge base for adversarial techniques targeting AI and machine-learning systems.

This mapping connects the threats identified in the enterprise AI threat model to relevant adversarial behaviours and defensive controls.

---

## Threat Mapping Matrix

| Threat | ATLAS-Relevant Adversarial Behaviour | Security Objective |
|---|---|---|
| Model Poisoning | Poison training data or manipulate ML artifacts | Protect training and model integrity |
| Prompt Injection | Manipulate generative AI instructions and context | Prevent attacker-controlled model behaviour |
| Sensitive Data Leakage | Extract sensitive or proprietary information | Prevent unauthorized information disclosure |
| API Abuse | Repeatedly query exposed AI/ML services | Restrict unauthorized and automated usage |
| Adversarial Input | Craft inputs designed to cause incorrect predictions | Improve model robustness and input validation |
| Model Theft | Query models to infer or reproduce their functionality | Protect model confidentiality and intellectual property |

---

# 1. Model Poisoning

## Adversary Objective

Influence model behaviour by compromising data or artifacts used during the ML lifecycle.

## Attack Path

Attacker  
↓  
Training Data / ML Pipeline  
↓  
Poisoned Dataset  
↓  
Model Training  
↓  
Compromised Model

## Defensive Controls

- Dataset provenance
- Cryptographic integrity verification
- Restricted write permissions
- Dataset validation
- Model signing
- Approval gates
- Version control

## Detection Opportunities

- Unexpected dataset changes
- Hash mismatches
- Label-distribution anomalies
- Model-performance degradation
- Unauthorized pipeline modifications

---

# 2. Prompt Injection

## Adversary Objective

Manipulate an LLM into following attacker-controlled instructions.

## Attack Path

Attacker  
↓  
Malicious Prompt  
↓  
AI Gateway  
↓  
LLM  
↓  
Unauthorized Behaviour

## Defensive Controls

- Input validation
- Prompt-injection detection
- Context isolation
- Independent authorization
- Tool allowlists
- Least privilege
- Output filtering

## Detection Opportunities

- Instruction-override patterns
- System-prompt extraction attempts
- Repeated jailbreak attempts
- Unauthorized tool requests

---

# 3. Sensitive Data Leakage

## Adversary Objective

Extract confidential information through model responses or retrieval systems.

## Potential Targets

- Customer information
- Credentials
- Internal documents
- System prompts
- Proprietary datasets
- API secrets

## Defensive Controls

- DLP
- Data classification
- Retrieval authorization
- Output filtering
- Context restrictions
- Secrets isolation

## Detection Opportunities

- Sensitive-data patterns in generated output
- Unusual retrieval queries
- Repeated extraction attempts
- Unauthorized document access

---

# 4. API Abuse

## Adversary Objective

Exploit exposed AI interfaces through automated or unauthorized interaction.

## Defensive Controls

- Strong authentication
- Authorization
- API Gateway
- Rate limiting
- Request quotas
- Network segmentation
- Security logging

## Detection Opportunities

- Request-rate spikes
- Endpoint enumeration
- Authentication failures
- Repetitive automated queries
- Abnormal API usage

---

# 5. Adversarial Input

## Adversary Objective

Manipulate input features so an ML system produces an attacker-desired prediction.

## Attack Path

Original Input  
↓  
Feature Manipulation  
↓  
Adversarial Input  
↓  
ML Model  
↓  
Incorrect Classification

## Defensive Controls

- Feature validation
- Input sanitization
- Range enforcement
- Adversarial testing
- Robustness testing
- Prediction monitoring

## Detection Opportunities

- Out-of-range features
- Suspicious feature combinations
- Prediction instability
- Repeated decision-boundary probing

---

# 6. Model Theft

## Adversary Objective

Infer, approximate, or reproduce proprietary model behaviour through systematic interaction.

## Attack Path

Attacker  
↓  
Repeated Queries  
↓  
Model API  
↓  
Collected Predictions  
↓  
Behavioural Approximation

## Defensive Controls

- Authentication
- Least-privilege API access
- Rate limiting
- Query monitoring
- Response minimization
- Usage quotas

## Detection Opportunities

- High-volume structured querying
- Systematic feature variation
- Boundary-probing patterns
- Abnormal query distributions

---

# Detection Engineering Integration

ATLAS-informed threat modelling should feed directly into operational monitoring.

```text
Threat Model
     ↓
Security Controls
     ↓
Telemetry
     ↓
Detection Rules
     ↓
SIEM
     ↓
SOC Investigation
     ↓
Incident Response
