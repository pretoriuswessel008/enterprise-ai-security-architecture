# AI Threat Detection & SOC Response Playbook

## Purpose

This playbook translates AI threat-model findings into actionable detection and incident-response procedures.

---

## Detection & Response Matrix

| Threat | Detection Signal | Severity | SOC Response |
|---|---|---|---|
| Model Poisoning | Dataset hash mismatch or unauthorized dataset modification | Critical | Stop training/deployment, isolate artifact, preserve evidence |
| Prompt Injection | Instruction override or system-prompt extraction attempt | High | Block request, log session, correlate repeated attempts |
| Sensitive Data Leakage | Restricted information detected in model output | Critical | Block response, preserve logs, investigate data access |
| API Abuse | Abnormal request volume or repeated authentication failures | Medium–High | Rate limit/block source, investigate identity and activity |
| Adversarial Input | Repeated feature manipulation or boundary probing | High | Block suspicious input, preserve samples, investigate source |
| Model Theft | Systematic high-volume model queries | High | Restrict API access, investigate account, preserve query history |

---

# Incident Workflow

```text
AI Security Event
       ↓
Telemetry Generated
       ↓
SIEM Ingestion
       ↓
Detection Rule Triggered
       ↓
Risk / Severity Assessment
       ↓
SOC Investigation
       ↓
Containment
       ↓
Evidence Preservation
       ↓
Recovery
       ↓
Post-Incident Review
```

Playbook 1 – Model Poisoning
Trigger
Dataset hash mismatch
Unauthorized dataset modification
Unexpected provenance change
Significant training-data anomaly
Immediate Actions
Stop the affected training or deployment pipeline.
Prevent the suspicious dataset or model artifact from progressing.
Preserve the affected artifact in read-only evidence storage.
Record cryptographic hashes.
Identify the account or process responsible for the modification.
Compare against the last trusted dataset version.
Recovery

Restore the last verified dataset or model artifact and repeat security validation before deployment.

Playbook 2 – Prompt Injection
Trigger

Detection of instructions attempting to:

Override system instructions
Extract system prompts
Bypass security controls
Invoke unauthorized tools
Access restricted information
Immediate Actions
Block the malicious request.
Record user identity and session information.
Preserve the submitted prompt.
Correlate the event with previous requests.
Check for attempted tool or API execution.
Escalate repeated or successful attempts.
Recovery

No model recovery is required if deterministic gateway controls successfully contained the request.

Playbook 3 – Sensitive Data Leakage
Trigger

DLP detects restricted information in model output.

Immediate Actions
Block the response before delivery.
Preserve the generated output securely.
Identify the data source.
Review retrieval and authorization logs.
Determine whether protected information was exposed elsewhere.
Escalate confirmed disclosure according to incident-response procedures.
Recovery

Correct authorization, retrieval, context, or DLP controls before restoring affected functionality.

Playbook 4 – API Abuse
Trigger
Request-rate anomaly
Authentication failures
Endpoint enumeration
Automated repetitive queries
Excessive resource consumption
Immediate Actions
Apply rate limiting.
Identify the originating account, token, or source.
Revoke compromised credentials where justified.
Preserve API logs.
Investigate related endpoints.
Block confirmed malicious activity.
Playbook 5 – Adversarial Input
Trigger

Repeated feature manipulation or suspicious attempts to cross model decision boundaries.

Immediate Actions
Preserve adversarial samples.
Identify the requesting identity.
Block malformed or prohibited feature values.
Compare predictions against expected behaviour.
Determine whether exploitation succeeded.
Feed samples into future robustness testing.
Playbook 6 – Model Theft
Trigger

Systematic querying indicates possible behavioural extraction.

Immediate Actions
Apply stricter rate limits.
Review account authorization.
Preserve query and response history.
Identify systematic feature variation.
Restrict or suspend confirmed malicious access.
Determine whether proprietary model behaviour may have been exposed.
Evidence Requirements

For significant AI-security incidents, preserve:

Timestamp
User or service identity
Session identifier
Source information
Requested resource
Prompt or model input
Model output where permitted
Authorization decision
Security-control decision
Tool/API activity
Relevant hashes
Detection rule
Incident severity

Evidence must be handled according to organizational retention, privacy, and chain-of-custody requirements.
