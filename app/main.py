# Import FastAPI - this is our main tool for building the API
from fastapi import FastAPI
from app.routes import tasks
# Create the FastAPI application
# This is like creating a new server instance
app = FastAPI(
    title="Task Manager API",  # Name of our API
    description="A simple task management system",  # What it does
    version="1.0.0"  # Version number
)

# This is a "route" - it handles requests to the root URL "/"

app.include_router(tasks.router)

# @app.get means this handles GET requests

@app.get("/")
async def root():
    """
    Welcome endpoint
    When someone visits http://localhost:8000/
    They'll see this message
    """
    return {
        "message": "Welcome to Task Manager API",
        "status": "running"
    }

# Health check endpoint - good practice to have this
@app.get("/health")
async def health_check():
    """
    Check if API is alive
    Other services can ping this to see if we're working
    """
    return {
        "status": "healthy",
        "message": "API is running"
    }
