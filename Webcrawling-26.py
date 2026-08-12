# import requests 
# from bs4 import BeautifulSoup

# url = "http://example.com"

# response = requests.get(url)

# soup = BeautifulSoup(requests.text , "html.parser")
# print(soup.title.text)

from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

# Getting news 
@app.get("/news")
def get_news():
    url = "https://www.hindustantimes.com/"

    response = requests.get(url)
    soup = BeautifulSoup(response.text , "html.parser")

    