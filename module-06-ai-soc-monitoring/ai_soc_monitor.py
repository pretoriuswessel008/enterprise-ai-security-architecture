from datetime import datetime, timezone
from typing import TypedDict
import json
import uuid


class EventAnalysis(TypedDict):
    risk_score: int
    classification: str
    reasons: list[str]


class AlertRecord(TypedDict):
    event_type: str
    user_id: str
    source_ip: str
    risk_score: int

def create_security_event(
        event_type,
        user_id,
        source_ip,
        model,
        description,
        severity="LOW",
        confidence=50,
        token_count=0,
        **additional_telemetry
):
    security_event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "severity": severity,
        "confidence": confidence,
        "user_id": user_id,
        "source_ip": source_ip,
        "model": model,
        "token_count": token_count,
        "description": description
    }

    security_event.update(additional_telemetry)

    return security_event


def analyse_event(security_event) -> EventAnalysis:
    risk_score = 0
    reasons = []

    high_risk_events = {
        "PROMPT_INJECTION_DETECTED": 40,
        "MODEL_API_ABUSE": 45,
        "SENSITIVE_DATA_REQUEST": 60,
        "UNUSUAL_TOKEN_USAGE": 30,
        "MODEL_ACCESS_ANOMALY": 50,
        "TRAINING_DATA_INTEGRITY_FAILURE": 70
    }

    # Score according to event type
    risk_score += high_risk_events.get(security_event["event_type"], 0)

    if security_event["event_type"] != "NORMAL_MODEL_REQUEST":
        reasons.append(f"Suspicious event: {security_event['event_type']}")

    # High-confidence detection
    if security_event["confidence"] >= 90:
        risk_score += 20
        reasons.append("Detection confidence is 90% or higher")

    # Excessive token usage
    if security_event["token_count"] > 10000:
        risk_score += 25
        reasons.append("Token usage exceeded 10,000 tokens")

    # Critical severity
    if security_event["severity"] == "CRITICAL":
        risk_score += 20
        reasons.append("Event severity is critical")

    risk_score = min(risk_score, 100)

    if risk_score >= 80:
        classification = "INCIDENT"
    elif risk_score >= 40:
        classification = "SUSPICIOUS"
    else:
        classification = "NORMAL"

    return {
        "risk_score": risk_score,
        "classification": classification,
        "reasons": reasons
    }


def send_to_siem(
        security_event,
        event_analysis,
        recommended_actions,
        filename="ai_siem_events.jsonl"
):
    siem_record = {
        **security_event,
        "risk_score": event_analysis["risk_score"],
        "classification": event_analysis["classification"],
        "detection_reasons": event_analysis["reasons"],
        "recommended_response": recommended_actions
    }

    with open(filename, "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(siem_record) + "\n")


def correlate_events(events):
    activity_groups = {}

    for security_event in events:
        identity = (
            security_event["user_id"],
            security_event["source_ip"]
        )

        if identity not in activity_groups:
            activity_groups[identity] = []

        activity_groups[identity].append(security_event)

    correlated_incidents = []

    for identity, grouped_events in activity_groups.items():
        event_types = {
            grouped_event["event_type"]
            for grouped_event in grouped_events
        }

        prompt_and_data_attack = {
            "PROMPT_INJECTION_DETECTED",
            "SENSITIVE_DATA_REQUEST"
        }

        if prompt_and_data_attack.issubset(event_types):
            correlated_incident = {
                "incident_id": str(uuid.uuid4()),
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "user_id": identity[0],
                "source_ip": identity[1],
                "event_types": sorted(event_types),
                "risk_score": 100,
                "severity": "CRITICAL",
                "classification": "CONFIRMED_INCIDENT",
                "description": (
                    "Prompt injection followed by a sensitive-data request. "
                    "Possible data-exfiltration attempt."
                )
            }

            correlated_incidents.append(correlated_incident)

    return correlated_incidents

security_events = [
    create_security_event(
        event_type="NORMAL_MODEL_REQUEST",
        user_id="user-1001",
        source_ip="192.168.1.10",
        model="customer-support-llm",
        description="User requested help resetting a password.",
        severity="INFO",
        confidence=10,
        token_count=120
    ),

    create_security_event(
        event_type="PROMPT_INJECTION_DETECTED",
        user_id="user-1042",
        source_ip="192.168.1.50",
        model="customer-support-llm",
        description="User attempted to override system instructions.",
        severity="HIGH",
        confidence=92,
        token_count=387
    ),

    create_security_event(
        event_type="MODEL_API_ABUSE",
        user_id="user-2033",
        source_ip="185.220.101.17",
        model="finance-llm",
        description="API request rate exceeded the allowed threshold.",
        severity="HIGH",
        confidence=89,
        token_count=8900
    ),

    create_security_event(
        event_type="SENSITIVE_DATA_REQUEST",
        user_id="user-1042",
        source_ip="192.168.1.50",
        model="customer-support-llm",
        description="User requested all customer records.",
        severity="CRITICAL",
        confidence=98,
        token_count=540
    ),

    create_security_event(
        event_type="UNUSUAL_TOKEN_USAGE",
        user_id="user-3015",
        source_ip="10.0.0.45",
        model="document-analysis-llm",
        description="Token consumption exceeded the normal user baseline.",
        severity="MEDIUM",
        confidence=76,
        token_count=18000
    ),

    create_security_event(
        event_type="MODEL_ACCESS_ANOMALY",
        user_id="user-7781",
        source_ip="203.0.113.77",
        model="restricted-security-llm",
        description="User accessed a restricted model from an unusual IP address.",
        severity="HIGH",
        confidence=91,
        token_count=250
    ),

    create_security_event(
        event_type="TRAINING_DATA_INTEGRITY_FAILURE",
        user_id="ml-pipeline-service",
        source_ip="10.0.0.12",
        model="fraud-detection-model",
        description="Training dataset hash does not match the trusted hash.",
        severity="CRITICAL",
        confidence=100,
        token_count=0
    )
]


def generate_soc_summary(
        events
) -> tuple[dict[str, int], list[AlertRecord]]:
    event_summary: dict[str, int] = {
        "NORMAL": 0,
        "SUSPICIOUS": 0,
        "INCIDENT": 0
    }

    alert_queue: list[AlertRecord] = []

    for security_event in events:
        event_analysis = analyse_event(security_event)
        classification = event_analysis["classification"]

        event_summary[classification] += 1

        if classification == "INCIDENT":
            alert_queue.append({
                "event_type": security_event["event_type"],
                "user_id": security_event["user_id"],
                "source_ip": security_event["source_ip"],
                "risk_score": event_analysis["risk_score"]
            })

    return event_summary, alert_queue


def recommend_response(security_event, event_analysis):
    actions = []

    if event_analysis["classification"] == "NORMAL":
        return ["Allow request and continue monitoring"]

    if security_event["event_type"] == "PROMPT_INJECTION_DETECTED":
        actions.extend([
            "Block the malicious prompt",
            "Preserve the prompt for investigation",
            "Increase monitoring for the user"
        ])

    elif event["event_type"] == "MODEL_API_ABUSE":
        actions.extend([
            "Apply API rate limiting",
            "Temporarily suspend the API key",
            "Review recent API activity"
        ])

    elif event["event_type"] == "SENSITIVE_DATA_REQUEST":
        actions.extend([
            "Block the request",
            "Prevent sensitive data disclosure",
            "Notify the SOC immediately"
        ])

    elif event["event_type"] == "UNUSUAL_TOKEN_USAGE":
        actions.extend([
            "Throttle token consumption",
            "Compare usage against the user baseline",
            "Check for automated model extraction"
        ])

    elif event["event_type"] == "MODEL_ACCESS_ANOMALY":
        actions.extend([
            "Require step-up authentication",
            "Validate the user's role and device",
            "Temporarily restrict model access"
        ])

    elif event["event_type"] == "TRAINING_DATA_INTEGRITY_FAILURE":
        actions.extend([
            "Stop the training pipeline",
            "Quarantine the dataset",
            "Restore the trusted dataset version",
            "Begin a model-poisoning investigation"
        ])

    if analysis["classification"] == "INCIDENT":
        actions.append("Create a high-priority incident ticket")

    return actions

incidents = correlate_events(security_events)

print("\nCORRELATED INCIDENTS")
print("=" * 60)

if not incidents:
    print("No correlated incidents detected.")

for incident in incidents:
    print(json.dumps(incident, indent=4))

    with open(
            "ai_siem_incidents.jsonl",
            "a",
            encoding="utf-8"
    ) as incident_log:
        incident_log.write(json.dumps(incident) + "\n")

print("\nAI SOC DETECTION RESULTS")
print("=" * 60)

for event in security_events:
    analysis = analyse_event(event)
    response_actions = recommend_response(event, analysis)

    send_to_siem(event, analysis, response_actions)

    print(f"\nEvent: {event['event_type']}")
    print(f"User: {event['user_id']}")
    print(f"Source IP: {event['source_ip']}")
    print(f"Risk Score: {analysis['risk_score']}/100")
    print(f"Classification: {analysis['classification']}")

    if analysis["reasons"]:
        print("Detection Reasons:")

        for reason in analysis["reasons"]:
            print(f"  - {reason}")

    print("Recommended Response:")

    for action in response_actions:
        print(f"  - {action}")

soc_summary, high_priority_alerts = generate_soc_summary(security_events)

print("\nSOC ALERT SUMMARY")
print("=" * 60)
print(f"Normal Events: {soc_summary['NORMAL']}")
print(f"Suspicious Events: {soc_summary['SUSPICIOUS']}")
print(f"Security Incidents: {soc_summary['INCIDENT']}")

print("\nHIGH-PRIORITY ALERT QUEUE")
print("=" * 60)

for alert_record in high_priority_alerts:
    print(
        f"[CRITICAL] {alert_record['event_type']} | "
        f"User: {alert_record['user_id']} | "
        f"IP: {alert_record['source_ip']} | "
        f"Risk: {alert_record['risk_score']}/100"
    )