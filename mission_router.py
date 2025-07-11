# mission_router.py

from fastapi import FastAPI
from pydantic import BaseModel
from agent_logic import agents, get_agent_logs

app = FastAPI()


# Define input structure for POST
class Mission(BaseModel):
    task: str
    agent_name: str = "Nova"  # default to Nova if not specified


@app.get("/healthz")
def health_check():
    return {
        "status": "DeepSight Quantum Mesh Online",
        "crew": list(agents.keys())
    }


@app.post("/send-mission")
def send_mission(mission: Mission):
    agent = agents.get(mission.agent_name)
    if not agent:
        return {"error": f"Agent '{mission.agent_name}' not found."}
    
    result = agent.perform_task(mission.task)
    return {
        "mission": mission.task,
        "agent": mission.agent_name,
        "result": result
    }


@app.get("/logs/{agent_name}")
def get_logs(agent_name: str):
    return get_agent_logs(agent_name)

