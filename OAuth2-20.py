from fastapi import FastAPI , Depends , HTTPException
from jose import jwt
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from datetime import datetime , timedelta , timezone
from passlib.context import CryptContext

app = FastAPI()

# JWT config 
SECRET_KEY = "mysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

# Password hashing setup 
pwd_context = CryptContext(schemes=["bcrypt"] , deprecated="auto")

# Oauth setup 
oauth2_schema = OAuth2PasswordBearer(token_url = "login")

# Dummy user DB 
fake_user = {
    "admin" : {
        "username":"admin",
        "hashed_password":pwd_context.hash("1234")
    }
}
