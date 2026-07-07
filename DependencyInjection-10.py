from fastapi import FastAPI ,Depends ,Header ,HTTPException

app = FastAPI()

def verfity_token(token :str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401 ,
            detail="Unauthorized"
        )
    return{
        "user":"Authorized user"
    }

@app.get("/secure-data")
def secure_data(user = Depends(verfity_token)):
    return{
        "message":"Secure data accessed",
        "user":user
    }