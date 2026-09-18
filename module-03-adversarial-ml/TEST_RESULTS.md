# Module 03 – Adversarial ML Test Results

## Test Environment

The adversarial ML laboratory was executed locally using Python and scikit-learn.

**Process exit code: 0**

---

## Baseline Model Performance

```text
Model Accuracy: 1.0

precision    recall    f1-score
0       1.00      1.00      1.00
1       1.00      1.00      1.00
```
The model achieved perfect accuracy on the small laboratory test set.

This baseline does not imply adversarial robustness.

## Normal Classification

```text
Normal Input Prediction:
BENIGN

Result: PASS ✅
```

## Malicious Classification

```text 
Original Malicious Input:
MALICIOUS

Result: PASS ✅
```

## Adversarial Feature Manipulation

```text
After attacker-controlled feature manipulation:

Adversarial Input:
BENIGN

Evasion demonstrated ⚠️

A malicious sample was successfully moved across the model's learned decision boundary.
```

## Request-Rate Evasion Test

```text
Request rate was progressively reduced while the remaining malicious features were preserved.

Request Rate: 120 -> MALICIOUS
...
Request Rate:   5 -> MALICIOUS

No request-rate-only evasion found.
Other malicious features maintained the classification.

Result: No single-feature request-rate evasion detected.
```

## Automated Decision-Boundary Testing

```text
The automated adversarial test modified individual features while monitoring model predictions.

Evasion found by modifying packet_size to 1010

Evasion demonstrated ⚠️

This shows that packet_size influenced a vulnerable decision boundary in the trained model.
```
This indicates that the Decision Tree split on a feature threshold below 1010, demonstrating how automated black-box fuzzing maps algorithmic blind spots.

## Training-Data Poisoning

```text
Initial poisoning:

Clean samples: 20
Poisoned samples: 23

Clean Model:
MALICIOUS

Poisoned Model:
MALICIOUS

The initial poisoned samples did not alter the target prediction.

A stronger poisoning attack was then performed.

Heavily Poisoned Model:
BENIGN

Poisoning impact demonstrated ⚠️

Repeated malicious samples intentionally mislabeled as benign successfully altered model behaviour.
```

## Dataset Integrity Validation

```text
SHA-256 hashes were calculated before and after simulated unauthorized dataset modification.

Original Dataset Hash:
4f7ff250e1f8db0a21cea66f39e586c1c108f37c5cc871f75fa4b0efb854f577

Modified Dataset Hash:
832f6a57baa9187c2f0f512aca0c3c34e0d7a12939109cbaceaf4d30c7b1fdad

WARNING: Dataset integrity check FAILED!
The dataset has been modified.

Result: PASS ✅
```

## Duplicate Detection

```text
15 duplicate rows detected.

Result: PASS ✅

The repeated poisoning samples were detected through duplicate analysis.
```

## Suspicious Label Detection

```text
3 suspicious label(s) detected.

The validation logic identified malicious-looking samples that had been labeled as benign.

Result: PASS ✅
```

## Security Assessment

```text
[PASS] Normal input classified as BENIGN
[PASS] Malicious input detected
[PASS] Suspicious labels detected
[PASS] Dataset modification detected
[PASS] Duplicate samples detected
[PASS] Poisoning successfully demonstrated

SECURITY ASSESSMENT COMPLETE

Overall security assessment: 6/6 checks passed.
```

## Security Conclusion

The laboratory demonstrates that conventional model accuracy and adversarial resilience are separate properties.

Despite achieving 1.0 accuracy on the laboratory test set, the model remained vulnerable to:

* Adversarial feature manipulation
* Decision-boundary evasion
* Training-data poisoning

Deterministic controls successfully detected:

* Dataset modification
* Duplicate poisoning samples
* Suspicious labels

The experiment demonstrates why production ML systems require security validation around both training and inference pipelines.

A model can be statistically accurate and still be insecure.
