from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import time

app = FastAPI()

# Cache Storage
cache_data =[]
last_fetch = 0


# Getting news 
@app.get("/news")
def get_news(page : int=1 , limit : int=5):
    url = "https://news.ycombinator.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")

    title = []

    for item in soup.find_all("span", class_="titleline"):
        title.append(item.text)

    return{
        "data":title[:5]
    }