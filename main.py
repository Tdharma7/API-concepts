
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
app = FastAPI()




class NewTask(BaseModel):
    title: str
    completed: bool = False


# Temporary storage inside your running Python program.
tasks = []


@app.post("/tasks", status_code=201)
def create_task(task: NewTask):
    task_data = task.model_dump()

    task_data["id"]=len(tasks)+1

    tasks.append(task_data)

    return {
        "message": "Task stored",
        "task": task_data
    }



@app.get("/tasks/{task_id}")
def get_one_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )