from fastapi import FastAPI
from mission_router import router

app = FastAPI()
app.include_router(router)
