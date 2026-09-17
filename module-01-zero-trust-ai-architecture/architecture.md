# Zero Trust AI Security Architecture

## Scenario

ApexBank is deploying an internal Generative AI platform used by:

- Employees
- Customer-service teams
- Fraud analysts
- Developers
- Risk analysts

The platform provides access to:

- Internal LLM services
- ML fraud-detection models
- Customer-data analysis
- Internal knowledge/RAG
- AI-powered APIs

AI workloads operate across cloud and enterprise environments. Sensitive systems and data remain protected behind explicit security boundaries.

## Architecture

```text
Users
  │
  ▼
Firewall / Network Security
  │
  ▼
Identity & Access Management
MFA + RBAC/ABAC
  │
  ▼
AI Gateway / Policy Enforcement Point
  │
  ├── Authentication Validation
  ├── Authorization Validation
  ├── Input Security
  ├── Rate Limiting
  ├── Context / Session Controls
  └── DLP Policy Enforcement
  │
  ▼
LLM / ML Platform
  │
  ├── Internal LLM
  ├── Fraud Detection Models
  ├── RAG / Knowledge Services
  └── AI APIs
  │
  ▼
Protected Data & Services
  │
  ├── Data Classification
  ├── Encryption
  ├── Secrets Management
  └── Least-Privilege Access
  │
  ▼
Logging & Monitoring
  │
  ▼
SIEM
  │
  ▼
SOC / Incident Response
