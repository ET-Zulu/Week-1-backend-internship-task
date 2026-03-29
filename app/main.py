from fastapi import FastAPI
from .routes.tasks import router as task_router

app = FastAPI(title="Todo App")

app.include_router(task_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Todo API"}
