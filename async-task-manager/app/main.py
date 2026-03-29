from fastapi import FastAPI
from app.routes import tasks

app = FastAPI(title="Async Task Manager API")

app.include_router(tasks.router)