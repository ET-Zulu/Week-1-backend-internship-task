from fastapi import FastAPI, HTTPException, status
from storage import tasks
from models import Task
from datetime import datetime

app = FastAPI()


@app.get("/")
def greet():
    return "Welcome to the task management API"


@app.get("/tasks")
async def get_tasks():
    return list(tasks.values())


@app.get("/tasks/{id}")
async def get_single_task(id: int):
    try:
        task = tasks.get(id)
        if not task:
            raise KeyError
        return task
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks")
async def create_task(task: Task):
    new_id = len(tasks) + 1
    new_task = Task(
        id=new_id,
        title=task.title,
        description=task.description,
        completed=task.completed,
        created_at=datetime.now(),
    )
    tasks[new_id] = new_task
    return {
        "message": "task created successfully",
        "status_code": 201,
        "task": new_task,
    }


@app.put("/tasks/{id}")
async def update_task(id: int, task: Task):
    try:
        if id not in tasks:
            raise KeyError

        tasks[id] = task

        return {
            "message": "task updated successfully",
            "status_code": 200,
            "task": tasks[id],
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")
    except AttributeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid task data: {str(e)}")


@app.patch("/tasks/{id}/complete")
async def mark_complete(id: int):
    try:
        if id not in tasks:
            raise KeyError

        task = tasks[id]
        task.completed = not task.completed
        tasks[id] = task

        status_text = "completed" if task.completed else "marked incomplete"
        return {
            "message": f"Task {status_text} successfully",
            "status_code": 200,
            "task": task,
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{id}")
async def delete_task(id: int):
    try:
        if id not in tasks:
            raise KeyError

        deleted_task = tasks.pop(id)

        return {
            "message": "task removed successfully",
            "status_code": 200,
            "deleted_task": deleted_task,
        }
    except KeyError:
        raise HTTPException(status_code=404, detail="Task not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting task: {str(e)}")
