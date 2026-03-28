# in memory storage
from typing import Dict

from model import Task


tasks: Dict[int, Task] = {}

current_id:int = 0
