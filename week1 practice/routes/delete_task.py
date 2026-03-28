import asyncio
from fastapi import APIRouter, HTTPException
from model import Task
from storage import tasks


router = APIRouter()


@router.delete("/task/{task_id}", response_model=str, status_code=200)
async def delete_task(task_id: int) -> str:
    await asyncio.sleep(1)
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    del tasks[task_id]
    
    return 'Task with id {} deleted successfully'.format(task_id)
