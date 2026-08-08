from fastapi import FastAPI

app =FastAPI()

@app.get("/")
def get_home():
    return {
        "message":"Hello Lakshay"
    }

@app.get("/add")
def get_add(a:int , b:int):
    return {
        "Addition": a+b
    }
