from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Task(BaseModel):
    id: Optional[int] = Field(default=None, exclude=True)
    title: str = Field(min_length=1)
    description: str = Field(min_length=5)
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
