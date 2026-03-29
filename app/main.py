from fastapi import FastAPI
from app.routes import router as task_router

app=FastAPI(
    title="Task Management API",
    description="A REST API for managing tasks using FastAPI and Pydantic v2",
    version="1.0.0"
)
app.include_router(task_router)

@app.get("/", tags=["Root"])
async def root():
    
    return {
        "message": "Task Management API is online",
        "docs": "/docs"
    }