from app.models import Task, TaskCreate, TaskUpdate
from fastapi import HTTPException

class TaskStorage:
    def __init__(self):
        self.tasks: dict[int, Task] = {}
        self._id_counter: int = 1

    async def create_task(self, task_data: TaskCreate) -> Task:
        new_id = self._id_counter
        self._id_counter += 1
        
        new_task = Task(
            id=new_id,
            title=task_data.title,
            description=task_data.description,
            completed=False
        )
        
        self.tasks[new_id] = new_task
        return new_task

    async def get_all_tasks(self) -> list[Task]:
        return list(self.tasks.values())

    async def get_task_by_id(self, task_id: int) -> Task:
        if task_id not in self.tasks:
            raise HTTPException(status_code=404, detail="Task not found")
        return self.tasks[task_id]

    async def update_task(self, task_id: int, task_data: TaskUpdate) -> Task:
        task = await self.get_task_by_id(task_id)
        
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        
        self.tasks[task_id] = task
        return task

    async def complete_task(self, task_id: int) -> Task:
        task = await self.get_task_by_id(task_id)
        task.completed = True
        
        self.tasks[task_id] = task
        return task

    async def delete_task(self, task_id: int) -> None:
        if task_id not in self.tasks:
            raise HTTPException(status_code=404, detail="Task not found")
        del self.tasks[task_id]


storage = TaskStorage()