import os
import requests

# -------------------------------
# Step C: OpenEnv Validator Format
# -------------------------------

# Must have [START] at the beginning
print("[START] inference.py")

# API URL from environment variable
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:7860")

# -------------------------------
# 1. RESET the environment
# -------------------------------
try:
    res = requests.post(f"{API_BASE_URL}/reset").json()
    print(f"[STEP] reset: {res}")
except Exception as e:
    print(f"[STEP] reset failed: {e}")

# -------------------------------
# 2. Perform sample actions
# -------------------------------

actions = ["consume_milk", "check_items", "add_item"]

for action in actions:
    try:
        payload = {"action": action}
        res = requests.post(f"{API_BASE_URL}/step", json=payload).json()
        print(f"[STEP] action '{action}': {res}")
    except Exception as e:
        print(f"[STEP] action '{action}' failed: {e}")

# -------------------------------
# Must have [END] at the end
# -------------------------------
print("[END] inference.py")
