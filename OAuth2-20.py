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

def hash_password(password : str):
    return pwd_context.hash("1234")

def verify_password(plain_password , hashed_password):
    return pwd_context.verify(plain_password , hashed_password)

# Create token 
def create_token(data : dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({
        "exp":expire
    })
    token =jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)
    return token