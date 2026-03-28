from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional
class TaskCreate(BaseModel):
    title:str= Field(... , min_length=1,description="Title must not be empty.")
    description:str =Field(... , min_length=5,description="Title must not be empty.")
    completed:Optional[bool]=False

class TaskResponse(TaskCreate):
    id: int
    created_at:datetime=Field(default_factory=datetime.utcnow)
class TaskUpdate(BaseModel):
    title:Optional[str]=None
    description:Optional[str]=None
    completed:Optional[bool]=None