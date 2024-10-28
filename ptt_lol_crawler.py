import requests
from bs4 import BeautifulSoup
import json

url = "https://www.ptt.cc/bbs/LoL/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}
request = requests.get(url, headers=headers)
response = request.text
soup = BeautifulSoup(response, "html.parser")
acticles = soup.find_all("div", class_="r-ent")
data_list = []

for a in acticles:
    data = {}
    title = a.find("div", class_="title")
    if title and title.a:
        title = title.a.text
    else:
        title = "No title"
    data["標題"] = title
    popular = a.find("div", class_="nrec")
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = "N/A"
    data["人氣"] = popular

    date = a.find("div", class_="date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["日期"] = date
    data_list.append(data)
with open("ptt_lol.json", "w", encoding="utf-8") as file:
    json.dump(data_list, file, ensure_ascii=False, indent=4)
print("已儲存為Json")
