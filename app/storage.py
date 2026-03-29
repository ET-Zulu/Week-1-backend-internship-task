"""
This file handles storing and retrieving tasks.
For now, we use memory (a dictionary). Later we can switch to a real database.
"""

# Dictionary to store tasks: { task_id: task_data }
# This is our "database" for now
tasks_db = {}

# Counter to generate unique IDs for new tasks
# Starts at 1, increases each time we add a task
current_id = 1

def get_all_tasks():
    """
    Returns all tasks as a list
    Example: [{id: 1, title: "Buy milk"}, {id: 2, title: "Learn FastAPI"}]
    """
    return list(tasks_db.values())

def get_task_by_id(task_id: int):
    """
    Find a task by its ID
    Returns the task if found, None if not found
    """
    return tasks_db.get(task_id)

def create_task(task_data: dict):
    """
    Save a new task to storage
    task_data should contain: title, description, completed, created_at
    """
    global current_id
    
    # Add the ID to the task data
    task_data["id"] = current_id
    
    # Save to our dictionary
    tasks_db[current_id] = task_data
    
    # Increase ID counter for next task
    current_id += 1
    
    return task_data

def update_task(task_id: int, updated_data: dict):
    """
    Update an existing task
    Returns the updated task if found, None if not found
    """
    if task_id not in tasks_db:
        return None
    
    # Get existing task
    task = tasks_db[task_id]
    
    # Update only the fields provided
    for key, value in updated_data.items():
        if value is not None:  # Only update if value is provided
            task[key] = value
    
    # Save back to storage
    tasks_db[task_id] = task
    return task

def delete_task(task_id: int):
    """
    Remove a task from storage
    Returns True if deleted, False if not found
    """
    if task_id not in tasks_db:
        return False
    
    del tasks_db[task_id]
    return True