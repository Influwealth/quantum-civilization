# agent_logic.py

from datetime import datetime
import random

# Simple Agent class
class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.logs = []

    def process(self, task):
        timestamp = datetime.utcnow().isoformat()
        response = f"[{self.name}] ({self.role}) received task: '{task}' at {timestamp}"
        self.logs.append(response)
        return f"{self.name} processed task: {task}"

# Commander
Nova = Agent("Nova", "Mesh Commander")

# Core mission logic
def run_mission(task: str):
    entropy = random.random()

    Nova.logs.append(f"Incoming task: {task}")
    if entropy > 0.2:
        result = Nova.process(task)
    else:
        result = "Entropy too low — fallback agent activated (QuantumOps)"
        Nova.logs.append(result)

    return result

