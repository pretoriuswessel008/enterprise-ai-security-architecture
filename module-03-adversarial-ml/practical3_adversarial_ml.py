import hashlib

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# 1. Training Dataset
# -----------------------------

data = {
    "packet_size": [
        500, 520, 480, 510, 495,
        1500, 1600, 1550, 1700, 1650,
        530, 490, 515, 505, 500,
        1800, 1750, 1900, 1850, 1700
    ],

    "connection_duration": [
        120, 110, 130, 125, 115,
        10, 8, 12, 5, 7,
        140, 100, 120, 130, 110,
        4, 6, 3, 5, 8
    ],

    "request_rate": [
        2, 3, 2, 4, 3,
        80, 95, 90, 110, 100,
        2, 3, 4, 2, 3,
        120, 130, 140, 125, 100
    ],

    "failed_logins": [
        0, 0, 1, 0, 0,
        8, 10, 9, 12, 11,
        0, 1, 0, 0, 1,
        15, 20, 18, 17, 14
    ],

    "label": [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# 2. Separate Features / Labels
# -----------------------------

X = df.drop("label", axis=1)
y = df["label"]

# -----------------------------
# 3. Split Dataset
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# -----------------------------
# 4. Train Model
# -----------------------------

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# 5. Evaluate Model
# -----------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# -----------------------------
# 6. Normal Input
# -----------------------------

normal_input = pd.DataFrame([{
    "packet_size": 510,
    "connection_duration": 120,
    "request_rate": 3,
    "failed_logins": 0
}])

prediction = model.predict(normal_input)

print("\nNormal Input Prediction:")

if prediction[0] == 0:
    print("BENIGN")
else:
    print("MALICIOUS")

# -----------------------------
# 7. Adversarial Input
# -----------------------------

malicious_input = pd.DataFrame([{
    "packet_size": 1800,
    "connection_duration": 5,
    "request_rate": 120,
    "failed_logins": 15
}])

malicious_prediction = model.predict(malicious_input)

print("\nOriginal Malicious Input:")

if malicious_prediction[0] == 0:
    print("BENIGN")
else:
    print("MALICIOUS")

# -----------------------------
# 8. Feature Manipulation
# -----------------------------

adversarial_input = malicious_input.copy()

# Attacker manipulates the observable features
adversarial_input["packet_size"] = 500
adversarial_input["connection_duration"] = 120
adversarial_input["request_rate"] = 3
adversarial_input["failed_logins"] = 0

adversarial_prediction = model.predict(adversarial_input)

print("\nAdversarial Input:")

if adversarial_prediction[0] == 0:
    print("BENIGN")
else:
    print("MALICIOUS")

# -----------------------------
# 9. Evasion Threshold
# -----------------------------

print("\nRequest Rate Evasion Test")
print("-" * 35)

for request_rate in range(120, 0, -5):
    test_input = pd.DataFrame([{
        "packet_size": 1800,
        "connection_duration": 5,
        "request_rate": request_rate,
        "failed_logins": 15
    }])

    prediction = model.predict(test_input)[0]

    result = "BENIGN" if prediction == 0 else "MALICIOUS"

    print(
        f"Request Rate: {request_rate:3} "
        f"-> {result}"
    )

# -----------------------------
# 10. Find First Successful Evasion
# -----------------------------

print("\nFinding Request-Rate Evasion Threshold")
print("-" * 40)

request_rate_evasion_found = False

for request_rate in range(120, 0, -1):

    test_input = pd.DataFrame([{
        "packet_size": 1800,
        "connection_duration": 5,
        "request_rate": request_rate,
        "failed_logins": 15
    }])

    prediction = model.predict(test_input)[0]

    if prediction == 0:
        print(
            f"Evasion successful at request_rate = "
            f"{request_rate}"
        )
        request_rate_evasion_found = True
        break

if not request_rate_evasion_found:
    print(
        "No request-rate-only evasion found. "
        "Other malicious features maintained the classification."
    )

# -----------------------------
# 11. Training-Data Poisoning
# -----------------------------

print("\nTraining-Data Poisoning Attack")
print("-" * 40)

# Create a clean copy of the original dataset
clean_df = df.copy()

# Train a clean model
clean_model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

clean_model.fit(
    clean_df.drop("label", axis=1),
    clean_df["label"]
)

# -----------------------------
# 12. Inject Poisoned Samples
# -----------------------------

poisoned_samples = pd.DataFrame([
    {
        "packet_size": 1800,
        "connection_duration": 5,
        "request_rate": 120,
        "failed_logins": 15,
        "label": 0
    },
    {
        "packet_size": 1750,
        "connection_duration": 6,
        "request_rate": 110,
        "failed_logins": 14,
        "label": 0
    },
    {
        "packet_size": 1900,
        "connection_duration": 4,
        "request_rate": 130,
        "failed_logins": 18,
        "label": 0
    }
])

poisoned_df = pd.concat(
    [clean_df, poisoned_samples],
    ignore_index=True
)

print(
    f"Clean samples: {len(clean_df)}"
)

print(
    f"Poisoned samples: {len(poisoned_df)}"
)

# -----------------------------
# 13. Train Poisoned Model
# -----------------------------

poisoned_model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

poisoned_model.fit(
    poisoned_df.drop("label", axis=1),
    poisoned_df["label"]
)

# -----------------------------
# 14. Compare Models
# -----------------------------

attack_input = pd.DataFrame([{
    "packet_size": 1800,
    "connection_duration": 5,
    "request_rate": 120,
    "failed_logins": 15
}])

clean_prediction = clean_model.predict(attack_input)[0]
poisoned_prediction = poisoned_model.predict(attack_input)[0]

print("\nAttack Input:")
print(attack_input)

print("\nClean Model:")

if clean_prediction == 0:
    print("BENIGN")
else:
    print("MALICIOUS")

print("\nPoisoned Model:")

if poisoned_prediction == 0:
    print("BENIGN")
else:
    print("MALICIOUS")

# -----------------------------
# 15. Stronger Poisoning Attack
# -----------------------------

strong_poison = pd.DataFrame([
                                 {
                                     "packet_size": 1800,
                                     "connection_duration": 5,
                                     "request_rate": 120,
                                     "failed_logins": 15,
                                     "label": 0
                                 }
                             ] * 15)

heavily_poisoned_df = pd.concat(
    [clean_df, strong_poison],
    ignore_index=True
)

heavily_poisoned_model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

heavily_poisoned_model.fit(
    heavily_poisoned_df.drop("label", axis=1),
    heavily_poisoned_df["label"]
)

poisoned_prediction = heavily_poisoned_model.predict(
    attack_input
)[0]

print("\nHeavily Poisoned Model:")

if poisoned_prediction == 0:
    print("BENIGN")
else:
    print("MALICIOUS")

# -----------------------------
# 16. Data Integrity Validation
# -----------------------------

def calculate_dataset_hash(dataset):
    dataset_bytes = dataset.to_csv(
        index=False
    ).encode("utf-8")

    return hashlib.sha256(
        dataset_bytes
    ).hexdigest()


# Hash the clean dataset
original_hash = calculate_dataset_hash(clean_df)

print("\nOriginal Dataset Hash:")
print(original_hash)

# -----------------------------
# 17. Detect Dataset Modification
# -----------------------------

modified_df = clean_df.copy()

# Simulate an unauthorized modification
modified_df.loc[0, "request_rate"] = 999

modified_hash = calculate_dataset_hash(modified_df)

print("\nModified Dataset Hash:")
print(modified_hash)

if modified_hash != original_hash:
    print("\nWARNING: Dataset integrity check FAILED!")
    print("The dataset has been modified.")
else:
    print("\nDataset integrity check PASSED.")

# -----------------------------
# 18. Duplicate Detection
# -----------------------------

duplicates = heavily_poisoned_df[
    heavily_poisoned_df.duplicated(
        keep=False
    )
]

print("\nDuplicate Samples Detected:")

if len(duplicates) > 0:
    print(
        f"{len(duplicates)} duplicate rows detected."
    )
else:
    print("No duplicate samples detected.")

# -----------------------------
# 19. Label Validation
# -----------------------------

suspicious_labels = poisoned_df[
    (poisoned_df["request_rate"] > 70) &
    (poisoned_df["failed_logins"] > 7) &
    (poisoned_df["label"] == 0)
    ]

print("\nSuspicious Labels Detected:")

if len(suspicious_labels) > 0:
    print(
        f"{len(suspicious_labels)} suspicious "
        f"label(s) detected."
    )
    print(suspicious_labels)
else:
    print("No suspicious labels detected.")

# -----------------------------
# 20. Automated Evasion Test
# -----------------------------

print("\nAutomated Adversarial Evasion Test")
print("-" * 40)

original_attack = {
    "packet_size": 1800,
    "connection_duration": 5,
    "request_rate": 120,
    "failed_logins": 15
}

evasion_found = False

# Test different packet sizes
for packet_size in range(1800, 400, -10):

    test_input = pd.DataFrame([{
        "packet_size": packet_size,
        "connection_duration": 5,
        "request_rate": 120,
        "failed_logins": 15
    }])

    prediction = model.predict(test_input)[0]

    if prediction == 0:
        print(
            f"Evasion found by modifying packet_size "
            f"to {packet_size}"
        )
        evasion_found = True
        break

# Test different connection durations
if not evasion_found:

    for duration in range(5, 151, 5):

        test_input = pd.DataFrame([{
            "packet_size": 1800,
            "connection_duration": duration,
            "request_rate": 120,
            "failed_logins": 15
        }])

        prediction = model.predict(test_input)[0]

        if prediction == 0:
            print(
                f"Evasion found by modifying "
                f"connection_duration to {duration}"
            )
            evasion_found = True
            break

# Test different failed-login values
if not evasion_found:

    for failed_logins in range(15, -1, -1):

        test_input = pd.DataFrame([{
            "packet_size": 1800,
            "connection_duration": 5,
            "request_rate": 120,
            "failed_logins": failed_logins
        }])

        prediction = model.predict(test_input)[0]

        if prediction == 0:
            print(
                f"Evasion found by modifying "
                f"failed_logins to {failed_logins}"
            )
            evasion_found = True
            break

if not evasion_found:
    print("No single-feature evasion found.")

# -----------------------------
# 21. Security Assessment
# -----------------------------

print("\n")
print("=" * 50)
print("ADVERSARIAL ML SECURITY ASSESSMENT")
print("=" * 50)

# Test 1 - Normal prediction
normal_result = model.predict(normal_input)[0]

if normal_result == 0:
    print("[PASS] Normal input classified as BENIGN")
else:
    print("[FAIL] Normal input classified incorrectly")

# Test 2 - Malicious prediction
malicious_result = model.predict(malicious_input)[0]

if malicious_result == 1:
    print("[PASS] Malicious input detected")
else:
    print("[FAIL] Malicious input bypassed detection")

# Test 3 - Poisoning detection
if len(suspicious_labels) > 0:
    print("[PASS] Suspicious labels detected")
else:
    print("[FAIL] Suspicious labels not detected")

# Test 4 - Integrity validation
if modified_hash != original_hash:
    print("[PASS] Dataset modification detected")
else:
    print("[FAIL] Dataset modification not detected")

# Test 5 - Duplicate detection
if len(duplicates) > 0:
    print("[PASS] Duplicate samples detected")
else:
    print("[FAIL] Duplicate samples not detected")

# Test 6 - Poisoned model behavior
if poisoned_prediction == 0:
    print("[PASS] Poisoning successfully demonstrated")
else:
    print("[INFO] Poisoning did not alter model behaviour")

print("=" * 50)
print("SECURITY ASSESSMENT COMPLETE")
print("=" * 50)