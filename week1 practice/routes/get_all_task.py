import asyncio
from typing import Dict
from fastapi import APIRouter
from model import Task
from storage import tasks


router = APIRouter()


@router.get("/task", response_model=Dict[str, list[Task]], status_code=200)
async def get_all_tasks() -> Dict[str, list[Task]]:
    await asyncio.sleep(1)
    return {"data": list(tasks.values())}
