from fastapi import FastAPI
from env import SmartFridgeEnv

app = FastAPI()
env = SmartFridgeEnv()

@app.get("/")
def home():
    return {"message": "Smart Fridge Environment Running"}

@app.get("/reset")
def reset():
    return {"state": env.reset()}

@app.get("/state")
def get_state():
    return {"state": env.get_state()}

@app.post("/step")
def step(action: str):
    state, reward, done = env.step(action)
    return {"state": state, "reward": reward, "done": done}
