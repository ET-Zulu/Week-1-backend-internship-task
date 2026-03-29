from fastapi import APIRouter,HTTPException, status
from app.storage import storage
from app.models import Task, TaskCreate,TaskUpdate

router = APIRouter(
    prefix= "/tasks",
    tags= ["tasks"]
)

@router.post('/', response_model=Task, status_code=status.HTTP_201_CREATED)

async def create_task(task_data: TaskCreate):
    return await storage.create_task(task_data)

@router.get('/',response_model=list[Task])

async def get_all_tasks():

    return await storage.get_all_tasks()

@router.get('/{task_id}', response_model=Task)

async def get_task(task_id: int):
    return await storage.get_task_by_id(task_id)

@router.put('/{task_id}',response_model=Task)

async def update_task(task_data:TaskUpdate, task_id:int):
    return await storage.update_task(task_id,task_data)



@router.patch('/{task_id}/complete', response_model=Task)
async def complete_task(task_id:int):
    return await storage.complete_task(task_id)

@router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_task( task_id:int):
    await storage.delete_task(task_id)
    return None