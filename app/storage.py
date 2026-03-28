from models import TaskResponse
from datetime import datetime
tasks: dict[int, TaskResponse] = {
    1: TaskResponse(
        id=1,
        title="Work with FastAPI",
        description="Build Task Manager app",
        completed=True,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
    2: TaskResponse(
        id=2,
        title="Learn SQLAlchemy",
        description="Practice ORM queries",
        completed=False,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
    3: TaskResponse(
        id=3,
        title="Docker Basics",
        description="Containerize FastAPI app",
        completed=True,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
    4: TaskResponse(
        id=4,
        title="Authentication Setup",
        description="Implement JWT auth",
        completed=False,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
    5: TaskResponse(
        id=5,
        title="API Documentation",
        description="Add Swagger UI docs",
        completed=True,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
    6: TaskResponse(
        id=6,
        title="Testing with Pytest",
        description="Write unit tests",
        completed=False,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
    7: TaskResponse(
        id=7,
        title="Frontend Integration",
        description="Connect React client",
        completed=True,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
    8: TaskResponse(
        id=8,
        title="Database Migration",
        description="Use Alembic for schema changes",
        completed=False,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
    9: TaskResponse(
        id=9,
        title="Deployment",
        description="Deploy app to Heroku",
        completed=True,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
    10: TaskResponse(
        id=10,
        title="CI/CD Pipeline",
        description="Set up GitHub Actions",
        completed=False,
        created_at=datetime.fromisoformat("2026-03-28T12:00:00")
    ),
}
