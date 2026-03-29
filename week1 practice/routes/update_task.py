import asyncio
from fastapi import APIRouter, HTTPException
from model import Task, TaskUpdated
from storage import tasks

router = APIRouter()


@router.put("/task/{task_id}", response_model=Task, status_code=200)
async def update_task(task_id: int, value: TaskUpdated) -> Task:

    await asyncio.sleep(1)

    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    existing_task = tasks[task_id]

    updated_task = {}

    if value.title is not None:
        updated_task["title"] = value.title
    if value.description is not None:
        updated_task["description"] = value.description
    if value.completed is not None:
        updated_task["completed"] = value.completed

    tasks[task_id] = existing_task.model_copy(update=updated_task)

    return tasks[task_id]
