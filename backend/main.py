from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Libera CORS pro frontend Angular
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em prod, restringe isso
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock de tarefas
tasks = [
    {"id": 1, "title": "Tarefa A", "column": "todo"},
    {"id": 2, "title": "Tarefa B", "column": "doing"},
    {"id": 3, "title": "Tarefa C", "column": "done"},
]

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks/move")
def move_task(task_id: int, new_column: str):
    for task in tasks:
        if task["id"] == task_id:
            task["column"] = new_column
            return {"status": "ok"}
    return {"error": "Task not found"}
