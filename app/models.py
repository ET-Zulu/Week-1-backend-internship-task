from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional
from datetime import timezone

class TaskBase(BaseModel):
   
    title: str = Field(..., min_length=1, description="The title of the task")
    description: str = Field(..., min_length=5, description="The description must be at least 5 characters")
class TaskCreate(TaskBase):
    pass
class TaskUpdate(BaseModel):
   
    title: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = Field(None, min_length=5)

class Task(TaskBase):
    
    id: int
    completed: bool = False
    created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
    model_config = ConfigDict(from_attributes=True)