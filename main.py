from fastapi import FastAPI
import os
import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# 🚀 FastAPI cockpit app
app = FastAPI()

# ✅ Health check
@app.get("/healthz")
def health_check():
    return {"status": "OK"}

# 📡 HUD overlay sync via Firestore REST API
@app.get("/overlay/latest/text")
def overlay_text():
    try:
        # Load service account from environment
        firebase_creds = json.loads(os.environ["FIREBASE_CREDS"])

        # Generate access token
        creds = service_account.Credentials.from_service_account_info(
            firebase_creds,
            scopes=["https://www.googleapis.com/auth/datastore"]
        )
        creds.refresh(Request())
        access_token = creds.token

        # REST API PATCH request to Firestore
        url = f"https://firestore.googleapis.com/v1/projects/{firebase_creds['project_id']}/databases/(default)/documents/overlay/latest"
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "fields": {
                "text": { "stringValue": "DeepSight cockpit live" }
            }
        }

        response = requests.patch(url, json=payload, headers=headers)
        if response.status_code in [200, 201]:
            return { "text": "DeepSight cockpit live" }
        else:
            return { "error": f"Firestore failed: {response.text}" }

    except Exception as e:
        return { "error": f"Overlay sync failed: {str(e)}" }

# 🧠 InfraAgent route
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

# 🔁 Nova sync route
@app.post("/agents/nova/sync-overlay")
async def sync_overlay():
    return {
        "status": "Overlay sync triggered",
        "routes": [
            "/overlay/latest/text",
            "/healthz",
            "/agents/infraagent/diagnose"
        ],
        "output": "REST HUD injection live"
    }

# 🔥 Uvicorn boot
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080)

# Final deploy patch
