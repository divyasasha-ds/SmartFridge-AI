import requests
import os

BASE_URL = os.getenv("API_BASE_URL")

print("[START]")

res = requests.get(f"{BASE_URL}/reset")
state = res.json()

for i in range(5):
    res = requests.post(f"{BASE_URL}/step", params={"action": "consume"})
    data = res.json()
    print("[STEP]", data)

print("[END]")
