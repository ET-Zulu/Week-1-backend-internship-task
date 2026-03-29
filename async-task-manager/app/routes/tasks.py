from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from typing import List

from app.models import Task, TaskCreate
from app.storage import tasks, task_id_counter

router = APIRouter()


@router.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate) -> Task:
    global task_id_counter

    task = Task(
        id=task_id_counter,
        title=task_data.title,
        description=task_data.description,
        completed=False,
        created_at=datetime.utcnow()
    )

    tasks[task_id_counter] = task
    task_id_counter += 1

    return task


@router.get("/tasks", response_model=List[Task])
async def get_tasks() -> List[Task]:
    return list(tasks.values())


@router.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]


@router.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_data: TaskCreate) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    existing_task = tasks[task_id]

    updated_task = existing_task.model_copy(update={
        "title": task_data.title,
        "description": task_data.description
    })

    tasks[task_id] = updated_task
    return updated_task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def delete_task(task_id: int) -> dict:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[task_id]
    return {"message": "Task deleted successfully"}


@router.patch("/tasks/{task_id}/complete", response_model=Task)
async def complete_task(task_id: int) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    updated_task = task.model_copy(update={"completed": True})

    tasks[task_id] = updated_task
    return updated_task