# Module 07 – AI Incident Response & Digital Forensics

## Overview

This module demonstrates an incident-response and digital-forensics workflow designed for AI/ML security incidents.

It extends the detection capabilities developed in Module 06 by processing confirmed security incidents through evidence preservation, investigation, containment, eradication, recovery, and post-incident validation.

The objective is to demonstrate the complete lifecycle from AI security detection to defensible incident response.

---

## Incident Response Architecture

```text
AI Security Event
        ↓
Detection & Correlation
        ↓
Confirmed Incident
        ↓
Incident Triage
        ↓
Evidence Preservation
        ↓
Digital Forensics
        ↓
Containment
        ↓
Eradication
        ↓
Recovery
        ↓
Security Validation
        ↓
Post-Incident Review
```

---

## Security Objectives

This laboratory demonstrates:

- Incident triage
- Evidence acquisition
- Evidence integrity verification
- SHA-256 hashing
- Chain-of-custody concepts
- Timeline reconstruction
- Attack-path analysis
- Incident containment
- Threat eradication
- Recovery validation
- Security-control retesting
- Post-incident review
- Lessons learned

---

## AI/ML Forensic Evidence

AI security investigations can require evidence beyond traditional operating-system and network logs.

Relevant evidence can include:

- AI Gateway logs
- User prompts
- Model responses
- Authentication records
- API requests
- Tool execution records
- DLP events
- Model-access logs
- Dataset hashes
- Model artifact hashes
- Model registry activity
- MLOps pipeline logs
- SIEM alerts
- Correlated incident records

---

## Evidence Integrity

Collected evidence must be protected against unauthorized modification.

```text
Evidence
   ↓
Acquisition
   ↓
SHA-256 Hash
   ↓
Evidence Record
   ↓
Protected Storage
   ↓
Integrity Verification
```

If evidence changes after acquisition, its cryptographic hash will no longer match the trusted value.

---

## Chain of Custody

Forensic evidence should maintain a record of:

- Evidence identifier
- Collection timestamp
- Evidence source
- Collector
- Cryptographic hash
- Storage location
- Evidence status
- Authorized handling activity

This provides traceability throughout the investigation.

---

## Incident Investigation

The investigation process reconstructs attacker behaviour from available telemetry.

Example:

```text
Prompt Injection
       ↓
Sensitive-Data Request
       ↓
AI Gateway Detection
       ↓
SIEM Events
       ↓
Event Correlation
       ↓
Confirmed Incident
       ↓
Evidence Preservation
       ↓
Forensic Investigation
```

---

## Containment

Containment actions can include:

- Blocking malicious requests
- Suspending compromised identities
- Revoking API credentials
- Restricting model access
- Disabling unauthorized tools
- Isolating affected AI services
- Quarantining suspicious datasets
- Preventing compromised model deployment

Containment should reduce immediate risk while preserving evidence required for investigation.

---

## Eradication

After containment, the underlying cause must be removed.

Examples include:

- Removing malicious training data
- Rotating compromised credentials
- Removing unauthorized model artifacts
- Correcting excessive permissions
- Fixing insecure tool integrations
- Strengthening AI Gateway controls
- Updating detection rules

---

## Recovery

Systems should not return to normal operation until their integrity and security controls have been validated.

```text
Containment
     ↓
Eradication
     ↓
Restore Trusted State
     ↓
Integrity Verification
     ↓
Security Testing
     ↓
Controlled Recovery
     ↓
Monitoring
```

---

## Post-Incident Validation

Recovery alone does not prove that the vulnerability has been removed.

Security controls should be retested using the original attack path.

For example:

```text
Original Attack
      ↓
Remediation
      ↓
Repeat Attack
      ↓
Control Blocks Attack
      ↓
Remediation Validated
```

This converts remediation from an assumption into a testable security outcome.

---

## Post-Incident Review

The final investigation should document:

- What happened
- How the incident was detected
- Which controls succeeded
- Which controls failed
- What evidence was collected
- How the incident was contained
- What was changed
- Whether remediation was validated
- What monitoring improvements are required

---

## Security Principle

Incident response does not end when the attacker is blocked.

Evidence must be preserved, the attack path understood, the root cause addressed, and the remediation independently validated.

> **Detect the attack. Preserve the evidence. Remove the cause. Prove the fix.**
