from fastapi import FastAPI , UploadFile , File , HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

#Step-1: Ensure uploads folder exist

UPLOAD_DIR = "uploads"
