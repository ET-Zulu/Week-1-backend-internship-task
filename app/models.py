"""
This file defines what a Task looks like in our system.
Think of it as a blueprint or form that all tasks must follow.
"""

# Import datetime for timestamps
from datetime import datetime
# Import Pydantic - this helps validate our data
from pydantic import BaseModel, Field, ConfigDict

# This is our Task model - defines the structure of a task
class Task(BaseModel):
    """
    This is what a complete Task looks like when we send it to the user.
    All fields are required when returning a task.
    """
    # ID is an integer that identifies this task uniquely
    id: int
    
    # Title cannot be empty - Field helps with validation
    title: str = Field(..., min_length=1, description="Task title")
    
    # Description must be at least 5 characters
    description: str = Field(..., min_length=5, description="Task description")
    
    # completed is a boolean (True/False), default is False
    completed: bool = False
    
    # created_at is automatically set to current time
    created_at: datetime = Field(default_factory=datetime.now)
    
    # This config tells Pydantic how to handle the model
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "Learn FastAPI",
                "description": "Study async APIs and build a task manager",
                "completed": False,
                "created_at": "2024-01-01T10:00:00"
            }
        }
    )


# This is for CREATING a new task - user doesn't provide id or created_at
class TaskCreate(BaseModel):
    """
    This is what the user sends when creating a task.
    Notice: no 'id' and no 'created_at' - the system will generate these!
    """
    title: str = Field(..., min_length=1, description="Task title")
    description: str = Field(..., min_length=5, description="Task description")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "title": "Learn FastAPI",
                "description": "Study async APIs and build a task manager"
            }
        }
    )


# This is for UPDATING a task - all fields are optional
class TaskUpdate(BaseModel):
    """
    This is what the user sends when updating a task.
    All fields are optional - they can update just what they want.
    """
    title: str | None = Field(None, min_length=1, description="Task title")
    description: str | None = Field(None, min_length=5, description="Task description")
    completed: bool | None = Field(None, description="Task completion status")