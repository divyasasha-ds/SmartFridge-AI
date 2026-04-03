import random

class SmartFridgeEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        # fridge items with expiry days
        self.state = {
            "milk": random.randint(0, 3),
            "eggs": random.randint(0, 6),
            "apple": random.randint(0, 5),
            "expiry": {
                "milk": random.randint(1, 5),
                "eggs": random.randint(1, 5),
                "apple": random.randint(1, 5)
            }
        }
        self.steps = 0
        return self.state

    def step(self, action):
        reward = 0
        self.steps += 1

        # Reduce expiry every step
        for item in self.state["expiry"]:
            self.state["expiry"][item] -= 1

        # Action logic
        if action == "consume_milk" and self.state["milk"] > 0:
            self.state["milk"] -= 1
            reward += 1

        elif action == "consume_eggs" and self.state["eggs"] > 0:
            self.state["eggs"] -= 1
            reward += 1

        elif action == "consume_apple" and self.state["apple"] > 0:
            self.state["apple"] -= 1
            reward += 1

        else:
            reward -= 0.2  # invalid action penalty

        # Penalty for expired items
        for item, days in self.state["expiry"].items():
            if days <= 0 and self.state[item] > 0:
                reward -= 1

        # Done condition
        done = self.steps >= 10

        return self.state, reward, done

    def get_state(self):
        return self.state
