# Module 02 – Adversarial Threat Modelling & MITRE ATLAS

## Objective

Identify AI-specific attack paths and translate them into preventative controls, detection opportunities, and SOC response procedures.

## Threats Analysed

- Model poisoning
- Prompt injection
- Sensitive-data leakage
- API abuse
- Adversarial input
- Model theft

## Security Engineering Approach

Each threat was evaluated using the following lifecycle:

```text
Asset
  ↓
Threat
  ↓
Attack Path
  ↓
Preventative Control
  ↓
Detection Signal
  ↓
SOC Response
  ↓
Security Improvement
```
Deliverables
Enterprise AI Threat Model

Documents attack scenarios, affected AI components, preventative controls, and detection opportunities.

MITRE ATLAS Mapping

Relates identified threats to adversarial behaviours described by the MITRE ATLAS knowledge base and connects those behaviours to defensive engineering controls.

SOC Response Playbook

Converts threat-model findings into operational procedures covering:

* Detection
* Triage
* Containment
* Evidence preservation
* Recovery
* Post-incident improvement

Key Findings

1. AI Models Must Not Enforce Their Own Security

Authorization, access control, DLP, tool permissions, and other critical controls must remain external to the model.

2. AI Security Extends Beyond Prompt Injection

The attack surface includes training data, model artifacts, APIs, retrieval systems, inference inputs, credentials, tools, and monitoring infrastructure.

3. Threat Modelling Must Produce Telemetry

A documented threat without a corresponding detection opportunity creates an operational visibility gap.

4. Detection Must Lead to Response

Security telemetry becomes useful when connected to defined SOC investigation and containment procedures.

Outcome

Module 02 establishes the threat intelligence foundation used by later modules for adversarial ML testing, secure MLOps, LLM security, SOC monitoring, and digital forensics.

The resulting defensive lifecycle is:

Threat Modelling → Prevention → Detection → Response → Improvement
