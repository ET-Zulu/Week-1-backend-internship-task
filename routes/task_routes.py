from fastapi import APIRouter, HTTPException, Depends
from datetime import datetime
from models import Task
from dependency import get_storage, get_task_by_id

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/")
async def get_tasks(storage: dict = Depends(get_storage)):
    return list(storage.values())


@router.get("/{id}")
async def get_single_task(task: dict = Depends(get_task_by_id)):
    return task


@router.post("/")
async def create_task(task: Task, storage: dict = Depends(get_storage)):
    new_id = len(storage) + 1
    new_task = Task(
        id=new_id,
        title=task.title,
        description=task.description,
        completed=task.completed,
        created_at=datetime.now(),
    )
    storage[new_id] = new_task
    return {
        "message": "Task created successfully",
        "status_code": 200,
        "task": new_task,
    }


@router.put("/{id}")
async def update_task(id: int, task: Task, storage: dict = Depends(get_storage)):
    if id not in storage:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    storage[id] = task

    return {
        "message": "Task updated successfully",
        "status_code": 200,
        "task": storage[id],
    }


@router.patch("/{id}/complete")
async def mark_complete(id: int, storage: dict = Depends(get_storage)):
    if id not in storage:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    task = storage[id]
    task.completed = not task.completed
    storage[id] = task

    status_text = "completed" if task.completed else "marked incomplete"

    return {
        "message": f"Task {status_text} successfully",
        "status_code": 200,
        "task": task,
    }


@router.delete("/{id}")
async def delete_task(id: int, storage: dict = Depends(get_storage)):
    if id not in storage:
        raise HTTPException(status_code=404, detail=f"Task with id {id} not found")

    deleted_task = storage.pop(id)

    return {
        "message": "Task removed successfully",
        "status_code": 200,
        "deleted_task": deleted_task,
    }
