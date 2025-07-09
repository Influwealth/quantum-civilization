# agent_logic.py

import random
from datetime import datetime

class QuantumAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.logs = []

    def perform_task(self, task, confidence=0.95):
        entropy = round(random.uniform(0, 1 - confidence), 4)
        output = f"[{self.name}] executed task: {task} | entropy={entropy}"
        self.logs.append({
            "task": task,
            "entropy": entropy,
            "timestamp": datetime.utcnow().isoformat()
        })
        return output

# Define your crew
agents = {
    "Nova": QuantumAgent("Nova", "Mesh Commander"),
    "CreditBuilder": QuantumAgent("CreditBuilder", "Financial Uplift Protocol"),
    "QuantumCritic": QuantumAgent("QuantumCritic", "Skeptical Analysis Unit"),
    "EchoSyn": QuantumAgent("EchoSyn", "Sentiment Resonance Model"),
    "BusinessBuilder": QuantumAgent("BusinessBuilder", "Entrepreneurship Engine")
}

def get_agent_logs(agent_name):
    if agent_name in agents:
        return agents[agent_name].logs
    else:
        return {"error": f"Agent '{agent_name}' not found"}

