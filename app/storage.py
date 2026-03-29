import asyncio
from typing import Dict, List, Optional
from datetime import datetime
from .models import Task, TaskCreate, TaskUpdate

class Storage:
    def __init__(self):
        self.tasks: Dict[int, Task] = {}
        self._next_id = 1

    async def get_all_tasks(
        self, 
        completed: Optional[bool] = None, 
        search: Optional[str] = None, 
        page: int = 1, 
        limit: int = 10
    ) -> List[Task]:
        tasks = list(self.tasks.values())
        
        # Filtering
        if completed is not None:
            tasks = [t for t in tasks if t.completed == completed]
            
        # Searching
        if search:
            search = search.lower()
            tasks = [t for t in tasks if search in t.title.lower() or search in t.description.lower()]
            
        # Pagination
        start = (page - 1) * limit
        end = start + limit
        return tasks[start:end]

    async def get_task(self, task_id: int) -> Optional[Task]: 
        return self.tasks.get(task_id)

    async def create_task(self, task_data: TaskCreate) -> Task:
        task_id = self._next_id # auto increment the Id
        self._next_id += 1
        
        new_task = Task(
            id=task_id,
            title=task_data.title,
            description=task_data.description,
            completed=False,
            created_at=datetime.now()
        )
        self.tasks[task_id] = new_task
        return new_task

    async def update_task(self, task_id: int, task_data: TaskUpdate) -> Optional[Task]:
        if task_id not in self.tasks:
            return None
        
        current_task = self.tasks[task_id]
        update_data = task_data.model_dump(exclude_unset=True)
        
        # Create a new Task instance with updated fields
        updated_task = current_task.model_copy(update=update_data)
        # replace the old task with the updated task
        self.tasks[task_id] = updated_task
        return updated_task

    async def delete_task(self, task_id: int) -> bool:
        if task_id in self.tasks:
            del self.tasks[task_id]
            return True
        return False

    async def mark_complete(self, task_id: int) -> Optional[Task]:
        if task_id not in self.tasks:
            return None
        
        current_task = self.tasks[task_id]
        updated_task = current_task.model_copy(update={"completed": True})
        self.tasks[task_id] = updated_task
        return updated_task

# Singleton instance for simple storage
storage = Storage()
