from datetime import datetime
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=5)


class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime

    model_config = {
        "from_attributes": True
    }