from fastapi import FastAPI

app = FastAPI()


# ✅ Health check — confirms cockpit status
@app.get("/healthz")
def health_check():
    return {"status": "OK"}


# 📡 Overlay output — Firebase stream HUD
@app.get("/overlay/latest/text")
def overlay_text():
    return {"text": "DeepSight cockpit live"}


# 🧠 InfraAgent — Diagnose build & routing issues
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


# 🧠 Nova — Sync overlay & HUD visuals
@app.post("/agents/nova/sync-overlay")
async def sync_overlay():
    return {
        "status": "Overlay sync triggered",
        "routes": [
            "/overlay/latest/text",
            "/healthz",
            "/agents/infraagent/diagnose"
        ],
        "output": "Firebase HUD injection + OBS layout prep initialized"
    }


