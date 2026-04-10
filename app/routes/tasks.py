from fastapi import APIRouter, HTTPException
from typing import List
from datetime import datetime

from app.models import Task, TaskCreate, TaskUpdate
from app.storage import tasks, task_id_counter

router = APIRouter()

@router.post("/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    global task_id_counter

    new_task = Task(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        completed=False,
        created_at=datetime.utcnow()
    )

    tasks[task_id_counter] = new_task
    task_id_counter += 1

    return new_task

@router.get("/tasks", response_model=List[Task])
async def get_tasks():
    return list(tasks.values())


@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]


@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    existing = tasks[task_id]

    updated = Task(
        id=task_id,
        title=updated_task.title,
        description=updated_task.description,
        completed=existing.completed,
        created_at=existing.created_at
    )

    tasks[task_id] = updated
    return updated


@router.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[task_id]
    return {"message": "Task deleted successfully"}


@router.patch("/tasks/{task_id}/complete", response_model=Task)
async def complete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    task.completed = True

    tasks[task_id] = task
    return task