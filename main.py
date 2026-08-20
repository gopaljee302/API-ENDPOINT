from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Task API", version="1.0")


class TaskCreate(BaseModel):
    title: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


tasks: list[dict] = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Finish FL-01 assignment", "done": True},
    {"id": 3, "title": "Walk the dog", "done": False},
]
next_id = 4


@app.get("/", summary="API info")
def read_root():
    """Basic info about this API and its main endpoint."""
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"],
    }


@app.get("/health", summary="Health check")
def health_check():
    """Returns ok if the server is alive."""
    return {"status": "ok"}


@app.get("/tasks", summary="List tasks (with optional filters)")
def list_tasks(done: Optional[bool] = None, search: Optional[str] = None):
    """Returns tasks, optionally filtered by done status or a title search term."""
    result = tasks
    if done is not None:
        result = [t for t in result if t["done"] == done]
    if search is not None:
        result = [t for t in result if search.lower() in t["title"].lower()]
    return result


@app.get("/tasks/{task_id}", summary="Get one task")
def get_task(task_id: int):
    """Returns a single task by id, or 404 if it doesn't exist."""
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.post("/tasks", status_code=201, summary="Create a task")
def create_task(payload: TaskCreate):
    """Creates a new task. title is required and cannot be empty."""
    global next_id
    if not payload.title or not payload.title.strip():
        raise HTTPException(status_code=400, detail="title is required and cannot be empty")
    new_task = {"id": next_id, "title": payload.title, "done": False}
    tasks.append(new_task)
    next_id += 1
    return new_task


@app.put("/tasks/{task_id}", summary="Update a task")
def update_task(task_id: int, payload: TaskUpdate):
    """Updates a task's title and/or done status. 404 if the id doesn't exist."""
    for t in tasks:
        if t["id"] == task_id:
            if payload.title is not None:
                if not payload.title.strip():
                    raise HTTPException(status_code=400, detail="title cannot be empty")
                t["title"] = payload.title
            if payload.done is not None:
                t["done"] = payload.done
            return t
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.delete("/tasks/{task_id}", status_code=204, summary="Delete a task")
def delete_task(task_id: int):
    """Deletes a task by id. 404 if it doesn't exist."""
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail=f"Task {task_id} not found")


@app.get("/stats", summary="Task stats")
def get_stats():
    """Returns total, done, and open task counts."""
    total = len(tasks)
    done_count = sum(1 for t in tasks if t["done"])
    return {"total": total, "done": done_count, "open": total - done_count}


@app.post("/reset", summary="Reset to seed data")
def reset_tasks():
    """Restores the 3 example tasks. Handy for demos."""
    global tasks, next_id
    tasks = [
        {"id": 1, "title": "Buy milk", "done": False},
        {"id": 2, "title": "Finish FL-01 assignment", "done": True},
        {"id": 3, "title": "Walk the dog", "done": False},
    ]
    next_id = 4
    return {"status": "reset"}
