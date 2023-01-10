import csv
import time
import json
import random
import datetime
from os import system 

# Created module - созданный модуль
from core.config import URL, HEADERS, DOMEN

# Downloaded libraries - скачанная библиотека 
import requests
from bs4 import BeautifulSoup
# название, описание статьи, когда было создано, фотографии
# tn-news-author-list-title tn-announce tn-data-list tn-image-container

count_site = int(input("Сколько страниц спарсить: "))
for count in range(1, count_site + 1):
    response = requests.get(url = URL, headers = HEADERS, params={"page": f"page-{count}"})

    with open("core/html/index.html", "a", encoding = "UTF-8") as file: 
        file.write(response.text) 




for count in range(1, count_site + 1):
    with open("core/html/index.html", "r") as file: 
        src = file.read()

    soup = BeautifulSoup(src, "html.parser").find_all("div", class_ = "tn-news-author-section")

    with open("core/html/index.html", "w") as file:
        file.write(str(soup))




with open("core/html/index.html", "r") as file:
    src = file.read()

soup = BeautifulSoup(src, "html.parser").find_all("a") 

news_info = []

for item in soup: 
    url_product = DOMEN + item.get("href")
    news_image = item.get("tn-image-container")
    description = item.get("data-category").replace("/", " ")
    news_url = str(item.find("span", class_ = "tn-image-container").text).strip()

    information = {
    "url": url_product,
    "name": news_image,
    "category": description,
    "new_price": news_url
    }

    news_info.append(information)

with open("core/json/asd.json", "w") as file:
    json.dump(news_info, file, indent = 4, ensure_ascii = False)
