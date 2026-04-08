from fastapi import FastAPI
from env import SmartFridgeEnv  # your environment class

app = FastAPI()  # <-- this must be exactly named "app"
env = SmartFridgeEnv()

@app.post("/reset")
def reset_env():
    state = env.reset()
    return {"state": state, "status": "ok"}

@app.post("/step")
def step_env(action: dict):
    result = env.step(action)
    return result

@app.get("/state")
def get_state():
    return {"state": env.state}
