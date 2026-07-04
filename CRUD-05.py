from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

todos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {
        "message":"Todo added !" ,
        "data":todo
    }

@app.get("/todos")
def get_todo():
    return{
        "All todos":todos
    }

@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {
        "error":f"No todo found with id no.{todo_id}"
    }

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int , updated_todo:Todo):
    for index , todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index]=updated_todo
            return {
                "message":f"Todo data updated for id no. {todo_id}",
                "data":updated_todo
            }
    return {
        "error":"Todo not found !"
    }
