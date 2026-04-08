# SmartFridge-AI

**SmartFridge-AI** is an AI-driven simulation of a smart fridge environment. It tracks fridge contents, their expiry dates, and allows simple actions like consuming items while updating the fridge state. The project uses FastAPI as a backend for API endpoints and includes a basic agent script to interact with the environment.

---

## 🚀 Features

- 🧊 Fridge simulation environment (`env.py`) with items and expiry logic.
- ⚡ FastAPI server (`app.py`) exposing API endpoints:
  - `GET /` — Health check
  - `GET /reset` — Reset fridge state
  - `GET /state` — Get current fridge state
  - `POST /step` — Step the environment with an action
- 🤖 Sample agent script (`inference.py`) demonstrating how to interact with the fridge environment.

---

## 📁 Repository Structure

```
├── Dockerfile
├── app.py
├── env.py
├── inference.py
├── openenv.yaml
└── requirements.txt
```

---

## 🧠 How It Works

### Environment (`env.py`)

The `SmartFridgeEnv` class is the core:

- Tracks food items like `milk`, `eggs`, `apple`, with expiry counters.
- Manages steps taken in the environment.
- Computes rewards:
  - +1 for consuming valid items
  - −0.2 for invalid actions
  - −1 for expired items remaining

Each `step` simulates a time unit passing and decreases expiry days. The environment ends after a maximum number of steps.

---

## 🚀 API Endpoints (FastAPI)

| Endpoint  | Method | Description                        |
|-----------|--------|------------------------------------|
| `/`       | GET    | Check server status                |
| `/reset`  | GET    | Reset the fridge to a random state |
| `/state`  | GET    | Get current fridge state           |
| `/step`   | POST   | Perform an action (e.g., consume milk) |

**Example request for `/step`:**

```json
{
  "action": "consume_milk"
}

```
🤖 Running the Agent

inference.py demonstrates a simple agent:

Reset the environment.
Perform an action, e.g., "consume_milk".
Print updated state and reward.

You can adapt this to more advanced agents or integrate AI models.

---

🛠 Installation & Setup

1 Clone the repository:
```
bash
git clone https://github.com/divyasasha-ds/SmartFridge-AI.git
cd SmartFridge-AI

```
2 Install dependencies:

```
pip install -r requirements.txt

```

3 Start FastAPI server:

```
uvicorn app:app --reload
```

4 Run inference.py or your own scripts to interact with the API.

---

💡 Future Extensions

```
Connect with real sensors for fridge items.
Integrate object detection or image recognition.
Implement reinforcement learning agents.
Build a frontend dashboard for visualization.

```

---

## ✅ Conclusion

SmartFridge-AI provides a simple, extendable simulation of a smart fridge environment. You can experiment with AI agents, track item expiry, and explore integrations like object detection or reinforcement learning. It’s a great starting point for building more advanced smart kitchen applications.

---

## 👩‍💻 Author

**Divya Sasha**  
- GitHub: [https://github.com/divyasasha-ds](https://github.com/divyasasha-ds)  
- Email: divyasasha.ds@gmail.com
