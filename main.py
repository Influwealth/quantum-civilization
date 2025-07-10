from fastapi import FastAPI

app = FastAPI()


# ✅ Health check — confirms cockpit is running
@app.get("/healthz")
def health_check():
    return {"status": "OK"}


# 📡 Overlay output — Firebase & stream HUD
@app.get("/overlay/latest/text")
def overlay_text():
    return {"text": "DeepSight cockpit live"}


# 🧠 InfraAgent Endpoint — Diagnose Build / Routing
@app.post("/agents/infraagent/diagnose")
async def diagnose_build():
    return {
        "status": "Build under review",
        "actions": [
            "Check Dockerfile flags",
            "Inspect render.yaml startCommand",
            "Validate port exposure",
            "Trigger redeploy"
        ]
    }


