from fastapi import FastAPI
from routes import task_routes

app = FastAPI()

app.include_router(task_routes.router)


@app.get("/")
def greet():
    return "Welcome to the task management API"
