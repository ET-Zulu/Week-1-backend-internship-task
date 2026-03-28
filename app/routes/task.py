from fastapi import FastAPI,HTTPException, status
from models import TaskCreate,TaskResponse,TaskUpdate
from typing import List, Optional
from datetime import datetime
from storage import tasks
import asyncio
app=FastAPI()

@app.post('/tasks',status_code=status.HTTP_201_CREATED)
async def create_new_task(task:TaskCreate)->TaskResponse:
    new_id=len(tasks)+1
    new_task=TaskResponse(
        id=new_id,
        title=task.title,
        description=task.description,
        completed=task.completed,
    )
    tasks[new_id]=new_task.dict()
    return new_task

@app.get('/tasks',response_model=List[TaskResponse],status_code=status.HTTP_200_OK)
async def get_all_tasks(completed :Optional[bool]=None ,page :int=1,limit:int=5 ,search:Optional[str]=None):
    all_tasks=list(tasks.values())  
    if search is not None:
       all_tasks = [task for task  in all_tasks if search.lower() in task.title.lower()]
    if completed is not None:
       all_tasks= [task for  task in all_tasks if task.completed ==completed]
    
    start_at=(page-1 )*limit
    end_at=start_at+limit
    return all_tasks[start_at:end_at]

@app.get('/tasks/{id}',status_code=status.HTTP_200_OK)
async def get_task(id :int)->TaskResponse:
  if id not in tasks:
    raise HTTPException(status_code=404,detail="Task not found")
  return tasks.get(id)

@app.put('/tasks/{id}',status_code=status.HTTP_200_OK)
async def update_task(id:int,task:TaskCreate)->TaskResponse:
   if id not in tasks:
      raise HTTPException(status_code=404,detail="The task is not found")
   target_task= tasks.get(id)
   updated_task=TaskResponse(
    id=target_task.id,
    title=task.title,
    description=task.description,
    completed=task.completed,
    created_at=target_task.created_at
    )
   tasks[id]=updated_task.dict()
   return updated_task

@app.delete('/tasks/{id}',status_code=status.HTTP_200_OK)
async def remove_task(id :int )->TaskResponse:
   if id not in tasks:
      raise HTTPException(status_code=404,detail="The task is already not in the list")
   removed_task=tasks.pop(id)
   return removed_task
  
@app.patch('/tasks/{id}',status_code=status.HTTP_200_OK)
def update_task(id:int,task:TaskUpdate)->TaskResponse:
   if id not in tasks:
      raise HTTPException(status_code=404,detail="Task not found.")
   tasks[id] = tasks[id].copy(
      update=task.dict(exclude_unset=True)
    )
   return tasks[id]