from pathlib import Path

from fastapi import FastAPI
import uvicorn

app = FastAPI()

from routes.create_task import router as create_task_router
from routes.get_all_task import router as get_all_task_router
from routes.get_single_task import router as get_single_task_router
from routes.update_task import router as update_task_router
from routes.delete_task import router as delete_task_router
from routes.mark_task import router as mark_task_router

app.include_router(create_task_router)
app.include_router(get_all_task_router)
app.include_router(get_single_task_router)
app.include_router(update_task_router)
app.include_router(delete_task_router)
app.include_router(mark_task_router)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        app_dir=str(Path(__file__).parent),
    )
