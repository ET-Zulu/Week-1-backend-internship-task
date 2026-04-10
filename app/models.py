from pydantic import BaseModel, Field
from datetime import datetime


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=5)


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    completed: bool = False
    created_at: datetime


class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1)
    description: str | None = Field(None, min_length=5)
    completed: bool | None = None