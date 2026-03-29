# Async Task Manager API

A simple **Task Management REST API** built with **FastAPI**, featuring async endpoints, filtering, pagination, and search.

---

## Features

- Create, read, update, and delete tasks
- Mark tasks as completed
- Filter tasks by completion status
- Search tasks by keyword
- Pagination support
- Async endpoints using `async/await`
- Data validation with Pydantic v2

---

## Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/ET-Zulu/Week-1-backend-internship-task.git
cd async-task-manager
```
### 2. Install dependencies using Pipenv
```bash
pipenv install
```

### 3. Activate virtual environment
```bash
pipenv shell
```

### 4. Run the server
```bash
uvicorn app.main:app --reload
```