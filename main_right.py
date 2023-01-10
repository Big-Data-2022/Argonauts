# описание
#название
#фотография
#когда была опубликована

import json
import csv
from bs4 import BeautifulSoup
import requests
from core.config import URL, DOMEN, HEADERS


# response = requests.get(url=URL, headers=HEADERS)
# print(response.status_code)
# src = response.text
# with open("core/html/index.html", "w") as file:
#     file.write(src)

with open("core/html/index.html", "r") as file:
    src = file.read()

soup = BeautifulSoup(src, "html.parser")

news = soup.find_all("div", class_="tn-news-author-list-item")
teg_img = soup.find_all('img')

news_info = []
for item in news:
    title = item.find("div", class_="tn-news-author-list-item-text").find("span", class_="tn-news-author-list-title")
    description = item.find("div", class_="tn-news-author-list-item-text").find("p", class_="tn-announce")
    date_time = item.find("div", class_="tn-news-author-list-item-text").find("li")
    news_url = DOMEN + item.find("a").get("href")
    
#     print(f"""
# {title.text} 
# {description.text}
# {date_time.text} 
# {news_url}\n""")
    for image in teg_img:
        src = image.get("src")
        if src:
            image = DOMEN + src
    
    information = {
        "title": title.text,
        "description": description.text,
        "date_time": date_time.text.strip(),
        "image": image,
        "url": news_url
    }
    
    news_info.append(information)

with open(f"core/json/tengrinews.json", "w", encoding="utf-8") as file:
    json.dump(news_info, file, indent=4, ensure_ascii=False)





