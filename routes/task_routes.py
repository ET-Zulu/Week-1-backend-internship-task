from fastapi import APIRouter, HTTPException, status
from storage import tasks
from models import Task
from datetime import datetime

# router
router = APIRouter(prefix="/tasks", tags=["Tasks"])


# get router
async def get_tasks():
    return list(tasks.values())


# get a single task
@router.get("/{id}")
async def get_single_task(id: int):
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[id]
