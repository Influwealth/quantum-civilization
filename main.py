from fastapi import FastAPI

app = FastAPI()

@app.get("/overlay/latest/text")
async def get_overlay_text():
    return { "text": "DeepSight cockpit live" }
