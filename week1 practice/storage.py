# in memory storage
from typing import Dict

from model import Task


tasks: Dict[int, Task] = {
    1: Task(
        id=1,
        title="Sample Task",
        description="This is a sample task",
        completed=False,
        created_at="2024-06-01T12:00:00Z",
    ),
    2: Task(
        id=2,
        title="Another Task",
        description="This is another sample task",
        completed=True,
        created_at="2024-06-02T12:00:00Z",
    ),
}


current_id: int = tasks.__len__() - 1
