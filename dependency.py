from storage import tasks
from fastapi import HTTPException, Depends


# Dependency to get storage
def get_storage():
    """Inject the tasks storage"""
    return tasks


# Dependency to validate task existence
def get_task_by_id(id: int, storage=Depends(get_storage)):
    task = storage.get(id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
