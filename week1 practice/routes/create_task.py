import asyncio
from fastapi import APIRouter, HTTPException
from model import Task, TaskCreated
from storage import tasks, current_id


router = APIRouter()


@router.post("/task", response_model=Task, status_code=201)
async def create_task(value: TaskCreated) -> Task:

    global current_id

    current_id += 1

    id = current_id

    if id in tasks:
        raise HTTPException(status_code=400, detail="Task with this ID already exists")

    tasks[id] = Task(id=id, title=value.title, description=value.description)

    await asyncio.sleep(1)

    return tasks[id]
