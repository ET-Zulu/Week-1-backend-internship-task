# Project: Async Task Manager API

## Project Overview

You are required to build a **Task Management REST API** using FastAPI.  
This project is designed to help you practice and strengthen your skills in:

- **Git:** Branching, pull requests, and merge conflicts.
- **REST API Design:** Proper methods and status codes.
- **Python Type Hints:** Writing type-safe code.
- **Async Programming:** Using `asyncio`.
- **Data Validation:** Using Pydantic v2.
- **FastAPI Fundamentals:** Routing and dependency injection.

---

## Objective

By completing this project, you will:

- Build a fully functional REST API.
- Work collaboratively using Git.
- Write clean, structured, and typed Python code.

---

## Project Requirements

### 1. Task Model

Each task must have the following fields:

- `id: int` (auto-generated)
- `title: str`
- `description: str`
- `completed: bool` (default: `False`)
- `created_at: datetime`

> **Note:** Use **Pydantic v2** for validation.

---

### 2. API Endpoints

You must implement the following endpoints:

| Method     | Endpoint               | Description            |
| :--------- | :--------------------- | :--------------------- |
| **POST**   | `/tasks`               | Create a new task      |
| **GET**    | `/tasks`               | Get all tasks          |
| **GET**    | `/tasks/{id}`          | Get a single task      |
| **PUT**    | `/tasks/{id}`          | Update a task          |
| **DELETE** | `/tasks/{id}`          | Delete a task          |
| **PATCH**  | `/tasks/{id}/complete` | Mark task as completed |

---

### 3. Storage

Use **simple storage only** (no database). Choose one:

- In-memory dictionary: `tasks: dict[int, Task] = {}`
- JSON file: `tasks.json`

### 4. Async Requirement

All endpoints must be asynchronous. Simulate async behavior where needed:

```python
async def create_task(...):
    # logic here
```

### 5. Validation Rules

- `title` must not be empty.
- `description` must be at least 5 characters.
- `id` must **NOT** be provided by the user in the request body.
- `completed` defaults to `False`.

### 6. Type Hints

All functions must include proper type hints:

```python
async def get_task(task_id: int) -> Task:
```

### 7. Pydantic Usage (v2)

- Use Pydantic models for request and response validation.
- Separate input and output schemas if needed (e.g., `TaskCreate` vs `Task`).
- Use `model_config` where appropriate.

### 8. REST API Best Practices

Return appropriate HTTP status codes:

- **200** for success
- **201** for created
- **404** for not found
- **400** for bad request

### 9. Error Handling

Handle errors properly using FastAPI's built-in exceptions:

```python
raise HTTPException(status_code=404, detail="Task not found")
```

### 10. Code Organization

Split code into multiple files to keep logic clean and reusable:

- `models.py`
- `routes/`
- `storage.py`
- `main.py`

---

## 👥 Git Workflow (MANDATORY)

### 1. Branching

Each intern must create their own branch using the naming convention: `feature/<your-name>`

- _Examples:_ `feature/john`, `feature/sara`

### 2. Development Rule

- Work **only** on your branch.
- Do **NOT** commit directly to `main`.

### 3. Pull Requests (PR)

When you finish:

- Create a Pull Request to `main`.
- Add a clear description of what you implemented and challenges you faced.

---

## Suggested Project Structure

```text
app/
 ├── main.py
 ├── models.py
 ├── storage.py
 └── routes/
```

---

## Coding Standards

- **Naming:** Use `snake_case` for variables/functions and `PascalCase` for classes.
- **Code Quality:** Keep functions small and clear. Avoid code duplication.
- **Type Safety:** Use type hints everywhere.

---

## Bonus Features (Optional)

If you finish early, try adding:

- **Filtering:** `GET /tasks?completed=true`
- **Pagination:** `GET /tasks?page=1&limit=10`
- **Search:** `GET /tasks?search=keyword`

---

## Acceptance Criteria

Your project will be accepted if:

1.  All endpoints work correctly.
2.  Async functions are used.
3.  Pydantic models are implemented properly.
4.  Type hints are used everywhere.
5.  Errors are handled correctly.
6.  Git workflow rules are followed.

---

## Example Request

**Create Task**
`POST /tasks`

```json
{
  "title": "Learn FastAPI",
  "description": "Study async APIs"
}
```

## Final Notes

Focus on learning, not perfection. Try solving problems before asking for help

**Happy coding!**

---
