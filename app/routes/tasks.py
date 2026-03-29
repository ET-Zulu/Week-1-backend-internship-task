"""
This file contains all task-related API endpoints.
Each endpoint handles a specific operation on tasks.
"""

from fastapi import APIRouter, HTTPException, status
from datetime import datetime
from app.models import Task, TaskCreate, TaskUpdate
from app.storage import (
    get_all_tasks, get_task_by_id, create_task,
    update_task, delete_task
)

# Create a router to group all task endpoints
router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=list[Task])
async def get_tasks():
    """
    Get all tasks
    Returns a list of all tasks in the system
    """
    tasks = get_all_tasks()
    return tasks

@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """
    Get a single task by its ID
    Returns 404 if task not found
    """
    task = get_task_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    return task

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_new_task(task: TaskCreate):
    """
    Create a new task
    Title and description are required
    ID and created_at are auto-generated
    """
    # Convert Pydantic model to dictionary
    task_data = task.model_dump()
    
    # Add created_at timestamp
    task_data["created_at"] = datetime.now()
    
    # Add completed default (False)
    task_data["completed"] = False
    
    # Save to storage
    new_task = create_task(task_data)
    
    return new_task

@router.put("/{task_id}", response_model=Task)
async def update_existing_task(task_id: int, task: TaskUpdate):
    """
    Update an existing task
    All fields are optional - update only what's provided
    """
    # Check if task exists
    existing = get_task_by_id(task_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    
    # Get only fields that were provided (not None)
    update_data = {k: v for k, v in task.model_dump().items() if v is not None}
    
    # Update the task
    updated = update_task(task_id, update_data)
    
    return updated

@router.patch("/{task_id}/complete", response_model=Task)
async def mark_task_complete(task_id: int):
    """
    Mark a task as completed
    This is a shortcut for updating just the completed field
    """
    # Check if task exists
    existing = get_task_by_id(task_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    
    # Update only the completed field to True
    updated = update_task(task_id, {"completed": True})
    
    return updated

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_existing_task(task_id: int):
    """
    Delete a task by its ID
    Returns 204 No Content on success
    """
    deleted = delete_task(task_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with id {task_id} not found"
        )
    # No return value for 204 status