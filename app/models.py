from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: str = Field(..., min_length=5)
    model_config = ConfigDict(extra="forbid")


class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime

    model_config = ConfigDict(extra="forbid")
