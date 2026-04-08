from fastapi import FastAPI
from env import SmartFridgeEnv  # your environment class

app = FastAPI()
env = SmartFridgeEnv()

@app.post("/reset")
def reset_env():
    state = env.reset()  # must return JSON-serializable state
    return {"state": state, "status": "ok"}
