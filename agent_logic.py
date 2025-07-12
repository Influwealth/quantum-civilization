import os, json, requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

def get_access_token():
    creds = service_account.Credentials.from_service_account_info(
        json.loads(os.environ["FIREBASE_CREDS"]),
        scopes=["https://www.googleapis.com/auth/datastore"]
    )
    creds.refresh(Request())
    return creds.token

def patch_firestore(payload):
    token = get_access_token()
    url = "https://firestore.googleapis.com/v1/projects/myappanalytics-a01b7/databases/(default)/documents/overlay/latest"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return requests.patch(url, headers=headers, json=payload)

agents = ["Nova", "EchoSyn", "InfraAgent", "GeminiCLI"]

def get_agent_logs():
    return {agent: "Idle" for agent in agents}
