import requests

from fastapi import FastAPI , HTTPException

app = FastAPI()

# GET all data 
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()


