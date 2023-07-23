import os
import requests
import json
from pathlib import Path
from collect_all import get_collect_all_the_childs

if not os.path.exists('data'):
    os.mkdir('data')


def get_catalogy_waldberris():
    """ Вытягиваем JSON для дальнейшей работы с данными """
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Origin': 'https://www.wildberries.ru',
        'Connection': 'keep-alive',
        'Referer': 'https://www.wildberries.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'DNT': '1',
        'Sec-GPC': '1',
    }

    response = requests.get('https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru-v2.json',
                            headers=headers).json()

    # print(response)
    with open('waldberris.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)


def get_category():
    """ Распарсиваем JSON. Разбиваем на категории и подкатегории """
    with open('waldberris.json', 'r', encoding='utf-8') as file:
        category_data = json.load(file)

        new_json = []
        for cat in category_data:
            ids = cat.get("id")
            name = cat.get("name")
            url = cat.get("url")
            shard = cat.get("shard")
            query = cat.get("query")
            childs = cat.get("childs")

            new_json.append({
                "id": ids,
                "name": name,
                "url": url,
                "shard": shard,
                "query": query,
                "childs": childs
            })

    with open('data/category.json', 'w', encoding='utf-8') as file:
        json.dump(new_json, file, indent=4, ensure_ascii=False)

    childs_json = []
    for childs_cat in category_data:
        if 'childs' in childs_cat.keys():
            ch = childs_cat.get("childs")
            childs_json.append(ch)

    # если нет папки, то создаем папку
    if not os.path.exists('data/childs'):
        os.mkdir('data/childs')

    for index, item in enumerate(childs_json):
        with open(f'data/childs/item{index}.json', 'w', encoding='utf-8') as file:
            json.dump(item, file, indent=4, ensure_ascii=False)


def get_url_link():
    """ Выбираем все подкатегории из файлов """
    count = 0
    p = Path("data/childs/")
    for x in p.rglob("*"):
        print(x)

        with open(f'{x}', 'r', encoding='utf-8') as file:
            url_data = json.load(file)
        # print(url_data)
        items_category = []
        for childs_cat in url_data:
            if 'childs' in childs_cat.keys():
                ch = childs_cat.get("childs")
                items_category.append(ch)
        # print(items_category)

        # если нет папки, то создаем папку
        if not os.path.exists('data/item'):
            os.mkdir('data/item')
        count += 1
        for index, item in enumerate(items_category):
            with open(f'data/item/child{index}_{count}.json', 'w', encoding='utf-8') as file:
                json.dump(item, file, indent=4, ensure_ascii=False)


def main():
    get_catalogy_waldberris()
    get_category()
    get_url_link()
    get_collect_all_the_childs(path=r'D:\TEST_JUNIOR\Parser_Scraper\Scraping_Parsing\waldberris\waldberris.json')


if __name__ == '__main__':
    main()
