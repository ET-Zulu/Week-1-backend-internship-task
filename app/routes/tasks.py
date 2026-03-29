from fastapi import APIRouter, HTTPException, status
from typing import List, Optional
from ..models import Task, TaskCreate, TaskUpdate
from ..storage import storage

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task_data: TaskCreate) -> Task:
    return await storage.create_task(task_data)

@router.get("/", response_model=List[Task])
async def get_tasks(
    completed: Optional[bool] = None, 
    search: Optional[str] = None, 
    page: int = 1, 
    limit: int = 10
) -> List[Task]:
    return await storage.get_all_tasks(completed=completed, search=search, page=page, limit=limit)

@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int) -> Task:
    task = await storage.get_task(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_data: TaskUpdate) -> Task:
    task = await storage.update_task(task_id, task_data)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    success = await storage.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return {"message": "Task deleted successfully"}

@router.patch("/{task_id}/complete", response_model=Task)
async def mark_task_complete(task_id: int) -> Task:
    task = await storage.mark_complete(task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task
