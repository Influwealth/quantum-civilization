from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, firestore

# 🔐 Initialize Firebase
cred = credentials.Certificate("firebase_creds.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = FastAPI()

# ✅ Health check — confirms cockpit status
@app.get("/healthz")
def health_check():
    return {"status": "OK"}

# 📡 Overlay output — writes to Firestore HUD
@app.get("/overlay/latest/text")
def overlay_text():
    hud_text = "DeepSight cockpit live"
    db.collection("overlay").document("latest").set({"text": hud_text})
    return {"text": hud_text}

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

# 🧠 Nova sync route confirmed — forcing rebuild



