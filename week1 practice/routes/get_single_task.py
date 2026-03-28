import asyncio
from fastapi import APIRouter, HTTPException
from model import Task
from storage import tasks


router = APIRouter()


@router.get("/task/{task_id}", response_model=Task, status_code=200)
async def get_single_task(task_id: int) -> Task:
    await asyncio.sleep(1)
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]
