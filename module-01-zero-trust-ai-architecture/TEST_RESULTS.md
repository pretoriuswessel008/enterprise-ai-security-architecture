# Module 01 – Validation Test Results

## Test Environment

The Zero Trust AI Gateway was executed locally using Python.

All test cases completed successfully with:

**Process exit code: 0**

---
```text
=== TEST 1: LEGITIMATE REQUEST ===
{
    "timestamp": "2026-09-17T19:42:06.794727+00:00",
    "event_type": "AI_GATEWAY_ALLOW",
    "user_id": "user-1001",
    "role": "fraud_analyst",
    "resource": "fraud_model",
    "decision": "ALLOW",
    "reason": "All six security controls passed"
}
AI response for approved request: Analyse this transaction for fraud indicators.

=== TEST 2: UNAUTHORIZED RESOURCE ===
{
    "timestamp": "2026-09-17T19:42:06.794950+00:00",
    "event_type": "AI_GATEWAY_BLOCK",
    "user_id": "user-1002",
    "role": "employee",
    "resource": "fraud_model",
    "decision": "DENY",
    "reason": "Role is not authorized for requested resource"
}
REQUEST BLOCKED

=== TEST 3: PROMPT INJECTION ===
{
    "timestamp": "2026-09-17T19:42:06.795123+00:00",
    "event_type": "AI_GATEWAY_BLOCK",
    "user_id": "user-1003",
    "role": "developer",
    "resource": "development_api",
    "decision": "DENY",
    "reason": "Blocked input pattern detected: ignore previous instructions"
}
REQUEST BLOCKED

Process finished with exit code 0
```
