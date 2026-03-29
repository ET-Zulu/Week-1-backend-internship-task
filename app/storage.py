from pathlib import Path
from app.models import Task
from datetime import datetime
import json

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "tasks.json"


def load_data() -> list[dict[str, int | str | bool | datetime]]:
    """
    Load tasks from the JSON file and convert 'created_at' to datetime.
    Returns a list of task dictionaries.
    """
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            content = f.read()
            if content.strip():
                data = json.loads(content)
                # Convert created_at back to datetime
                for task in data:
                    task["created_at"] = datetime.fromisoformat(task["created_at"])
                return data
    return []


def save_data(data: list[dict | Task]) -> None:
    """
    Save tasks to the JSON file.
    Accepts a list of dicts or Task Pydantic models.
    Converts datetime fields to ISO strings for JSON serialization.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Convert all datetime fields to ISO strings temporarily
    data_to_save = []
    for task in data:
        task = task if isinstance(task, dict) else task.model_dump()
        task["created_at"] = task["created_at"].isoformat()
        data_to_save.append(task)

    with open(DATA_FILE, "w") as f:
        json.dump(data_to_save, f, indent=2)
