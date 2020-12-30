from typing import Optional
from fastapi import FastAPI, Request
import requests
import re
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

base_url = 'https://www.popdaily.com.tw/'

@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    url_japan_new = 'http://localhost:8000/popdaily/japan/new'
    url_travel_new = 'http://localhost:8000/popdaily/travel/new'
    url_food_new = 'http://localhost:8000/popdaily/food/new'
    url_life_new = 'http://localhost:8000/popdaily/life/new'
    url_press_new = 'http://localhost:8000/popdaily/press/new'
    return_dict = {
        "request": request,
        "btn_japan": url_japan_new,
        "btn_travel": url_travel_new,
        "btn_food": url_food_new,
        "btn_life": url_life_new,
        "btn_press": url_press_new
    }
    return templates.TemplateResponse("home.html", return_dict)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/popdaily/{article_type}/new", response_class=HTMLResponse)
def popdaily_latest_urls(article_type: str, request: Request):
    page_url = base_url + article_type
    resp = requests.get(page_url)
    pattern = r'(?<=,\"url\":\")https://www.popdaily.com.tw/{}/\d+'.format(article_type)
    if resp.status_code == 200:
        urls = re.findall(pattern , resp.text)
    return templates.TemplateResponse("item.html", {"request": request, "urls": urls})
