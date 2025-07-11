import random
from datetime import datetime

import firebase_admin
from firebase_admin import credentials, db

# 🔐 Initialize Firebase (edit URL below)
cred = credentials.Certificate("firebase-service-account.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://myappanalytics-a01b7-default-rtdb.firebaseio.com'  # 🔁 REPLACE with your Firebase DB URL
})


class QuantumAgent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.logs = []

    def perform_task(self, task, confidence=0.95):
        entropy = round(random.uniform(0, 1 - confidence), 4)
        timestamp = datetime.utcnow().isoformat()
        output = f"[{self.name}] executed task: {task} | entropy={entropy}"

        self.logs.append({
            "task": task,
            "entropy": entropy,
            "timestamp": timestamp
        })

        # 📡 Stream to Firebase overlay
        try:
            db.reference("/overlay/latest").update({ "text": output })
        except Exception as e:
            print("⚠️ Firebase overlay error:", e)

        return output


# 🧠 Define your agent crew
agents = {
    "Nova": QuantumAgent("Nova", "Mesh Commander"),
    "CreditBuilder": QuantumAgent("CreditBuilder", "Financial Uplift Protocol"),
    "QuantumCritic": QuantumAgent("QuantumCritic", "Skeptical Analysis Unit"),
    "EchoSyn": QuantumAgent("EchoSyn", "Sentiment Resonance Model"),
    "BusinessBuilder": QuantumAgent("BusinessBuilder", "Entrepreneurship Engine")
}


# 📜 Retrieve agent log history
def get_agent_logs(agent_name):
    if agent_name in agents:
        return agents[agent_name].logs
    else:
        return {"error": f"Agent '{agent_name}' not found"}


