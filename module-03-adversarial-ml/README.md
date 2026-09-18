# Module 03 – Adversarial ML Exploit & Sanitization Laboratory

## Overview

This module demonstrates how machine-learning systems can be manipulated through adversarial input and poisoned data, and how deterministic security controls can reduce those risks.

A Decision Tree classifier is used as the laboratory model.

The objective is not simply to measure model accuracy, but to investigate how an attacker can manipulate inputs to influence model predictions.

---

## Security Objectives

This laboratory demonstrates:

- ML model training and validation
- Data poisoning concepts
- Feature manipulation
- Decision-boundary evasion
- Adversarial input generation
- Automated regression testing
- Input sanitization
- Feature-range enforcement
- Security telemetry

---

## Attack Flow

```text
Normal Input
     ↓
Feature Manipulation
     ↓
Adversarial Input
     ↓
ML Model
     ↓
Prediction
     ↓
Attacker adjusts features
     ↓
Decision-Boundary Evasion
```

## Defensive Flow

```text
Incoming ML Input
       ↓
Input Sanitization
       ↓
Feature Validation
       ↓
Range Enforcement
       ↓
ML Model
       ↓
Prediction Monitoring
       ↓
Security Logging
```

Laboratory Scenario

The model classifies activity as:
* BENIGN
* MALICIOUS

An attacker attempts to modify observable features while preserving malicious intent in order to cross the model's learned decision boundary.

The laboratory then introduces validation and sanitization controls designed to detect or reject manipulated inputs.

Key Security Principle
A high model-accuracy score does not prove that a machine-learning system is secure.

Security testing must evaluate how the model behaves when inputs are deliberately manipulated by an adversary.

Accuracy measures normal performance. Adversarial testing measures resilience.
