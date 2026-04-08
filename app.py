from fastapi import FastAPI
from env import SmartFridgeEnv

app = FastAPI()
env = SmartFridgeEnv()

@app.post("/reset")
def reset_env():
    state = env.reset()
    return {"state": state, "status": "ok"}

@app.post("/step")
def step_env(payload: dict):
    result = env.step(payload)
    return result

@app.get("/state")
def state_env():
    return {"state": env.state}
