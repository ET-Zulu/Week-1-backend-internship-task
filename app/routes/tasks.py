from fastapi import APIRouter, HTTPException, status
from typing import List, Dict, Any
from datetime import datetime, timezone

# Relative imports based on your app structure
from ..models import Task, TaskCreate
from ..storage import read_tasks, write_tasks, get_next_id

router: APIRouter = APIRouter(prefix="/tasks", tags=["Tasks"])


def to_task(data: Dict[str, Any]) -> Task:
    return Task(**data)


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task_in: TaskCreate) -> Task:
    tasks = await read_tasks()

    new_task = Task(
        id=await get_next_id(tasks),
        title=task_in.title,
        description=task_in.description,
        completed=False,
        created_at=datetime.now(timezone.utc),
    )

    # Use model_dump(mode="json") so datetime becomes a string for JSON
    tasks.append(new_task.model_dump(mode="json"))
    await write_tasks(tasks)
    return new_task


@router.get("/", response_model=List[Task])
async def get_tasks() -> List[Task]:
    tasks = await read_tasks()
    return [to_task(task) for task in tasks]


@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int) -> Task:
    tasks = await read_tasks()
    task = next((t for t in tasks if t.get("id") == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return to_task(task)


@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, updated: TaskCreate) -> Task:
    tasks = await read_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["title"] = updated.title
            task["description"] = updated.description
            await write_tasks(tasks)
            return to_task(task)
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int) -> None:
    tasks = await read_tasks()
    new_tasks = [t for t in tasks if t.get("id") != task_id]
    if len(tasks) == len(new_tasks):
        raise HTTPException(status_code=404, detail="Task not found")
    await write_tasks(new_tasks)


@router.patch("/{task_id}/complete", response_model=Task)
async def complete_task(task_id: int) -> Task:
    tasks = await read_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["completed"] = True
            await write_tasks(tasks)
            return to_task(task)
    raise HTTPException(status_code=404, detail="Task not found")
