from fastapi import FastAPI ,status , HTTPException

app = FastAPI()

@app.post("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return{
        "message":"user created!"
    }

@app.get("/user")
def get_users():
    return{
        "status":"success",
        "message":"User fetched",
        "user":{
            "name":"Lakshay",
            "age":22
        }
    }

@app.get("/user/{user_id}")
def get_user(user_id:int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User Not Found"
        )
    return {
        "id":1,
        "name":"Lakshay"
    }