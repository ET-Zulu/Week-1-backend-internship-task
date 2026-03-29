import json
import os
from typing import List, Dict, Any

FILE_PATH = "tasks.json"


async def read_tasks() -> List[Dict[str, Any]]:
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r") as f:
            data = f.read()
            return json.loads(data) if data else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


async def write_tasks(tasks: List[Dict[str, Any]]) -> None:
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4)


async def get_next_id(tasks: List[Dict[str, Any]]) -> int:
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1
