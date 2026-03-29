from pydantic import BaseModel, Field
from datetime import datetime


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=5)

    model_config = {"extra": "forbid"}


class Task(TaskCreate):
    id: int
    completed: bool = False
    created_at: datetime


class TaskUpdate(TaskCreate):
    pass
