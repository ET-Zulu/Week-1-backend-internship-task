import asyncio
from fastapi import APIRouter, HTTPException
from model import Task
from storage import tasks

router = APIRouter()


@router.put("/task/{task_id}/complete", response_model=Task, status_code=200)
async def mark_task(task_id: int) -> Task:
    await asyncio.sleep(1)
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    # Toggle the completed status of the task
    tasks[task_id].completed = not tasks[task_id].completed

    return tasks[task_id]
