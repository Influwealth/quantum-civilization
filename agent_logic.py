# mission_router.py
from fastapi import FastAPI
from agent_logic import run_mission, Nova

app = FastAPI()

@app.get("/healthz")
def health_check():
    return {
        "status": "DeepSight Quantum Mesh Online",
        "commander": Nova.name
    }

@app.post("/send-mission")
def send_mission(task: str):
    results = run_mission(task)
    return {
        "mission": task,
        "results": results
    }

@app.get("/logs")
def get_logs():
    return Nova.logs  # Optional: extend to all agent logs later
