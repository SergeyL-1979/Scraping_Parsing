import json
from datetime import datetime
from bs4 import BeautifulSoup


def filters_data():
    t_date = datetime.now().strftime('%d_%m_%Y')

    # with open("info_27_09_2022_1.json", 'r', encoding='utf-8') as file:
    #     data = json.load(file)
    # fragments = data['fragments']['containerBreadcrumb']

    with open("info_27_09_2022.html", 'r', encoding='utf-8') as file:
        data = file.read()

    # soul = BeautifulSoup(fragments, "lxml")
    soul = BeautifulSoup(data, "lxml")
    items_divs = soul.find_all("a")

    list_urls = []
    for d in items_divs:
        item_url = d.get("href")
        list_urls.append(item_url)

    with open(f"url_filters_{t_date}.txt", "w", encoding="utf-8", newline="") as file:
        for url in list_urls:
            file.write(f'https://www.zingat.com{url}\n')

    return list_urls

