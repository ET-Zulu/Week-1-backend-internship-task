import datetime

from pydantic import BaseModel, ConfigDict, Field, validator


def validate_title(value: str) -> str:
    if not value.strip():
        raise ValueError("Title must not be empty")
    return value


def validate_description(value: str) -> str:
    if not value.strip():
        raise ValueError("Description must not be empty")

    if len(value) < 5:
        raise ValueError("Description must be at least 5 characters long")
    return value


class Task(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.now)

    @validator("title")
    def title_must_not_be_empty(cls, value) -> str:
        return validate_title(value)

    @validator("description")
    def description_validation(cls, value) -> str:
        return validate_description(value)
           

class TaskCreated(BaseModel):
    title: str
    description: str

    @validator("title")
    def title_must_not_be_empty(cls, value) -> str:
        return validate_title(value)

    @validator("description")
    def description_validation(cls, value) -> str:
        return validate_description(value)

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)


class TaskUpdated(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
  
    @validator("title")
    def title_must_not_be_empty(cls, value: str | None) -> str | None:
        if value is None:
            return value
        return validate_title(value)

    @validator("description")
    def description_validation(cls, value: str | None) -> str | None:
        if value is None:
            return value
        return validate_description(value)

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)
