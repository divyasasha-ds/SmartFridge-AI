import os
import requests

API_BASE_URL = os.environ.get("API_BASE_URL", "http://127.0.0.1:8000")
MODEL_NAME = os.environ.get("MODEL_NAME", "dummy_model")
HF_TOKEN = os.environ.get("HF_TOKEN", "")

def run_agent():
    # Reset environment
    r = requests.get(f"{API_BASE_URL}/reset")
    state = r.json()['state']

    # Example action
    action = "consume_milk"
    r = requests.post(f"{API_BASE_URL}/step", json={"action": action})
    result = r.json()

    print("START")
    print("STEP 1:", result)
    print("END")

if __name__ == "__main__":
    run_agent()
