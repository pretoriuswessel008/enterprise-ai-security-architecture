# Module 04 – Secure MLOps Test Results

## Test Environment

The Secure MLOps pipeline was executed locally using Python and scikit-learn.

**Process exit code: 0**

---

## Dataset Validation

```text
Dataset samples: 150
Features: 4
Classes: 3

Dataset validation passed.

Result: PASS ✅
```

The dataset passed structural and invalid-value validation before entering the training pipeline.

## Training and Model Testing
```text
Training samples: 120
Testing samples: 30

Model training completed.
Model accuracy: 0.9333

Result: PASS ✅
```

The trained Logistic Regression model achieved an accuracy of approximately 93.33% on the laboratory test set.

## Model Registry
```text
Model saved to: model_artifact.joblib

Model registered successfully:
model_registry\iris_model_v1.joblib

Result: PASS ✅
```

The trained model artifact was successfully stored in the local model registry.

## Model Integrity Baseline

A SHA-256 hash was generated for the trusted model artifact before the simulated attack.

```text
Trusted SHA-256:
6e2890c687f6b1e854cfff6e79a413dc408306afb3149d4cffe254e4aabd75b4
```

This hash represents the trusted integrity baseline.

## Simulated Model Tampering

The registered model artifact was deliberately modified after the trusted hash had been generated.
```text
WARNING: Model artifact has been modified!
```
This simulates unauthorized modification of a model stored inside the registry.

## Integrity Verification

The deployment candidate was hashed again before deployment.

```text
Expected hash:
6e2890c687f6b1e854cfff6e79a413dc408306afb3149d4cffe254e4aabd75b4

Current hash:
fda2a932be625b824c32af78f512e856671e5d851d60d08e703ad7387c1079a5

SECURITY ALERT: Model integrity verification FAILED!
Possible model tampering detected.

Result: PASS ✅ — Tampering successfully detected
```

The hash mismatch correctly identified that the registered artifact was no longer identical to the trusted model.

## Deployment Security Gate

Because integrity verification failed, the deployment security gate rejected the artifact.

```text
DEPLOYMENT BLOCKED.
Reason: Model failed integrity verification.

SYSTEM STATUS: No model deployed.

Result: PASS ✅
```

The compromised model was prevented from reaching deployment.

## Monitoring Behaviour
```text
Monitoring skipped because deployment was blocked.

MONITORING STATUS: Alert / Not Active
```

This is expected behaviour.

Runtime model monitoring was not started because the artifact failed the security gate and was never deployed.

## Final Security Assessment
```text
Dataset Validation: PASSED
Model Security Testing: PASSED
Model Registry: CREATED
Model Integrity: FAILED
Deployment: BLOCKED
Monitoring: NOT ACTIVE / ALERT

=== PRACTICAL 4 COMPLETE ===

Process finished with exit code 0
```

## Interpretation

Model Integrity: FAILED represents a successful security detection, not a failure of the practical.

The deliberately modified model failed SHA-256 integrity verification and was therefore prevented from entering production.

The tested control flow was:

```text

Trusted Model
     ↓
SHA-256 Baseline
     ↓
Model Registry
     ↓
Artifact Tampering
     ↓
Integrity Verification
     ↓
Hash Mismatch Detected
     ↓
Deployment BLOCKED
```

## Security Conclusion

The laboratory demonstrates that a model registry must not automatically be considered a trusted source.

Model artifacts should be cryptographically verified before deployment, and failed integrity validation should prevent execution.

The practical successfully demonstrated:

* Dataset validation
* Model training and testing
* Model artifact registration
* SHA-256 integrity baselining
* Unauthorized artifact modification
* Tampering detection
* Fail-closed deployment controls

Trust the approved hash, not merely the location of the model artifact.
