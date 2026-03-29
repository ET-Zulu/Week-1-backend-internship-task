import asyncio
from typing import Dict
from fastapi import APIRouter, Query
from model import Task
from storage import tasks


router = APIRouter()

@router.get("/tasks", response_model=Dict[str, list[Task]], status_code=200)
async def get_all_tasks(
    completed: bool | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=10, ge=1),
    search: str | None = Query(default=None),
) -> Dict[str, list[Task]]:
    await asyncio.sleep(1)

    filtered_tasks = list(tasks.values())

    if completed is not None:
        filtered_tasks = [task for task in filtered_tasks if task.completed == completed]

    if search:
        keyword = search.strip().lower()
        filtered_tasks = [
            task
            for task in filtered_tasks
            if keyword in task.title.lower() or keyword in task.description.lower()
        ]

    start = (page - 1) * limit
    end = start + limit
    paginated_tasks = filtered_tasks[start:end]

    return {"data": paginated_tasks}
