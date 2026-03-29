from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from typing import Optional
from app.models import Task, TaskCreate, TaskUpdate
from app.storage import load_data, save_data


def generate_id(tasks: list[dict]) -> int:
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


router = APIRouter(prefix="/api/v1/tasks", tags=["Tasks"])


@router.get("/", response_model=list[Task])
async def get_tasks(
    completed: Optional[bool] = None,
    search: Optional[str] = None,
    page: int = 1,
    limit: int = 5,
) -> list[Task]:
    """
    Get all tasks with optional filtering, search, and pagination.
    """
    tasks = load_data()

    # Filter by completion status
    if completed is not None:
        tasks = [task for task in tasks if task["completed"] == completed]

    # Filter by completion status
    if search:
        search_lower = search.lower()
        tasks = [
            task
            for task in tasks
            if search_lower in task["title"].lower()
            or search_lower in task["description"].lower()
        ]

    # Pagination
    start = (page - 1) * limit
    end = start + limit
    return tasks[start:end]


@router.get("/{id}", response_model=Task)
async def get_task(id: int) -> Task:
    """Get a task with its id"""
    tasks = load_data()

    for task in tasks:
        if task["id"] == id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(payload: TaskCreate) -> Task:
    """Create a task"""
    tasks = load_data()

    new_id = generate_id(tasks)
    new_task = Task(
        id=new_id,
        title=payload.title,
        description=payload.description,
        completed=False,
        created_at=datetime.now(),
    )

    tasks.append(new_task.model_dump())
    save_data(tasks)
    return new_task


@router.put("/{id}", response_model=Task)
async def update_task(id: int, payload: TaskUpdate) -> Task:
    """Update task by id"""
    tasks = load_data()

    for i, task in enumerate(tasks):
        if task["id"] == id:
            updated_task = Task(
                id=id,
                title=payload.title,
                description=payload.description,
                completed=tasks[i]["completed"],
                created_at=tasks[i]["created_at"],
            )

            tasks[i] = updated_task.model_dump()
            save_data(tasks)
            return updated_task

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@router.patch("/{id}/complete", response_model=Task)
async def mark_task_completed(id: int) -> Task:
    """Mark task as completed"""
    tasks = load_data()

    for task in tasks:
        if task["id"] == id:
            task["completed"] = True
            save_data(tasks)
            return Task(**task)

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@router.delete("/{id}")
async def delete_task(id: int) -> None:
    """Delete a task by id"""
    tasks = load_data()

    for i, task in enumerate(tasks):
        if task["id"] == id:
            tasks.pop(i)
            save_data(tasks)
            return

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
