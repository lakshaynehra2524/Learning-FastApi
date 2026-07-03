from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

# class User(BaseModel):
#     name:str
#     age:int
#     email:str

# @app.post("/Createuser")
# def create_user(user:User):
#     return {
#         "message":"User created !",
#         "data":user
#     }

class Address(BaseModel):
    city:str
    pincode:str

class User(BaseModel):
    name:str
    age:int
    address:Address

@app.post("/Createuser")
def create_user(user:User):
    return user