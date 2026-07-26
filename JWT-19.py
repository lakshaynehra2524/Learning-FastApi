from fastapi import FastAPI , HTTPException , Depends , Header
from jose import jwt 
from datetime import datetime , timedelta , timezone

app = FastAPI()

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"

