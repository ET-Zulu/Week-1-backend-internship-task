from app.models import Task
from datetime import datetime

tasks: dict[int, Task] = {}
task_id_counter = 1