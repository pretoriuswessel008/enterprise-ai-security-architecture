import hashlib
from pathlib import Path

import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# --------------------------------------------------
# STEP 1: SECURE MLOPS - BASIC ML PIPELINE
# --------------------------------------------------

print("=== Secure MLOps Pipeline ===")
print()

# --------------------------------------------------
# 1. DATASET
# --------------------------------------------------

print("[1] Loading dataset...")

data = load_iris()

X = data.data
y = data.target

print(f"Dataset samples: {len(X)}")
print(f"Features: {X.shape[1]}")
print(f"Classes: {len(set(y))}")
print()

# --------------------------------------------------
# 2. VALIDATION
# --------------------------------------------------

print("[2] Validating dataset...")

if len(X) == 0:
    raise ValueError("Dataset is empty.")

if len(X) != len(y):
    raise ValueError("Feature and label counts do not match.")

if not all(map(lambda row: all(value == value for value in row), X)):
    raise ValueError("Dataset contains invalid values.")

print("Dataset validation passed.")
print()

# --------------------------------------------------
# 3. TRAIN / TEST SPLIT
# --------------------------------------------------

print("[3] Splitting dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
print()

# --------------------------------------------------
# 4. PRE-PROCESSING + TRAINING
# --------------------------------------------------

print("[4] Pre-processing and training...")

model = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", LogisticRegression(max_iter=200))
])

model.fit(X_train, y_train)

print("Model training completed.")
print()

# --------------------------------------------------
# 5. SECURITY TESTING
# --------------------------------------------------

print("[5] Testing model...")

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Model accuracy: {accuracy:.4f}")
print()

# --------------------------------------------------
# 6. SAVE MODEL ARTIFACT
# --------------------------------------------------

print("[6] Saving model artifact...")

model_path = Path("model_artifact.joblib")

joblib.dump(model, model_path)

print(f"Model saved to: {model_path}")
print()

# --------------------------------------------------
# 7. MODEL REGISTRY
# --------------------------------------------------

print("[7] Registering model...")

registry_path = Path("model_registry")
registry_path.mkdir(exist_ok=True)

registered_model = registry_path / "iris_model_v1.joblib"

joblib.dump(model, registered_model)

print(f"Model registered successfully: {registered_model}")
print()

# --------------------------------------------------
# 8. MODEL INTEGRITY BASELINE
# --------------------------------------------------

print("[8] Creating model integrity baseline...")


def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as model_file:
        while chunk := model_file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


trusted_hash = calculate_hash(registered_model)

print(f"Trusted SHA-256: {trusted_hash}")
print()


def verify_model_integrity(artifact_path, expected_hash):
    current_hash = calculate_hash(artifact_path)

    print(f"Expected hash: {expected_hash}")
    print(f"Current hash:  {current_hash}")

    if current_hash != expected_hash:
        print()
        print("SECURITY ALERT: Model integrity verification FAILED!")
        print("Possible model tampering detected.")
        return False

    print()
    print("Model integrity verified successfully.")
    return True


def deploy_model(artifact_path, integrity_status):
    print("[11] Deployment security gate...")

    if not integrity_status:
        print("DEPLOYMENT BLOCKED.")
        print("Reason: Model failed integrity verification.")
        return False

    print("Model passed security gate.")
    print(f"Deploying model: {artifact_path}")
    print("Deployment completed successfully.")
    return True


def monitor_model(model_predictions):
    print("[12] Monitoring model behaviour...")

    if len(model_predictions) == 0:
        print("MONITORING ALERT: No predictions received.")
        return False

    unique_predictions = set(model_predictions)

    print(f"Predictions observed: {len(model_predictions)}")

    if len(unique_predictions) < 2:
        print("MONITORING ALERT: Suspicious prediction behaviour detected.")
        return False

    print("Model behaviour appears normal.")
    return True

# --------------------------------------------------
# 9. SIMULATE MODEL TAMPERING
# --------------------------------------------------

print("[9] Simulating malicious model modification...")

with open(registered_model, "ab") as file:
    file.write(b"MALICIOUS_DATA")

print("WARNING: Model artifact has been modified!")
print()

# --------------------------------------------------
# 10. MODEL INTEGRITY VERIFICATION
# --------------------------------------------------

print("[10] Running model integrity verification...")

model_is_trusted = verify_model_integrity(
    registered_model,
    trusted_hash
)

print()

if not model_is_trusted:
    print("DEPLOYMENT BLOCKED.")
else:
    print("DEPLOYMENT APPROVED.")

print()

# --------------------------------------------------
# 11. DEPLOYMENT SECURITY GATE
# --------------------------------------------------

deployment_status = deploy_model(
    registered_model,
    model_is_trusted
)

print()

if deployment_status:
    print("SYSTEM STATUS: Model deployed.")
else:
    print("SYSTEM STATUS: No model deployed.")

print()

# --------------------------------------------------
# 12. MODEL MONITORING
# --------------------------------------------------

if deployment_status:
    monitoring_status = monitor_model(predictions)
else:
    monitoring_status = False
    print("[12] Monitoring skipped because deployment was blocked.")

print()

if monitoring_status:
    print("MONITORING STATUS: Normal")
else:
    print("MONITORING STATUS: Alert / Not Active")

print()

# --------------------------------------------------
# 13. FINAL SECURITY SUMMARY
# --------------------------------------------------

print("[13] Final Secure MLOps Security Summary")
print("----------------------------------------")

print("Dataset Validation: PASSED")
print("Model Security Testing: PASSED")
print("Model Registry: CREATED")

if model_is_trusted:
    print("Model Integrity: PASSED")
else:
    print("Model Integrity: FAILED")

if deployment_status:
    print("Deployment: ALLOWED")
else:
    print("Deployment: BLOCKED")

if monitoring_status:
    print("Monitoring: ACTIVE")
else:
    print("Monitoring: NOT ACTIVE / ALERT")

print()
print("=== PRACTICAL 4 COMPLETE ===")