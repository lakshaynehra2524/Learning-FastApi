from fastapi import FastAPI , UploadFile , File , HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

#Step-1: Ensure uploads folder exist

UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

#STEP-2:Static file set-up
#URL: HTTP://127.0.0.1:8080/FILES/<FILEnAME>
app.mount("/files",StaticFiles(directory=UPLOAD_DIR), name="files")