from fastapi import FastAPI
from .routes.tasks import router as tasks_router

app = FastAPI(
    title="Async Task Manager API",
    description="A simple REST API for managing tasks asynchronously.",
)

# Include the task router
app.include_router(tasks_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Async Task Manager API"}
