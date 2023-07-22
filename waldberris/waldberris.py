import os
import requests
import json

if not os.path.exists('data'):
    os.mkdir('data')


def get_catalogy_waldberris():
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

    response = requests.get('https://static-basket-01.wb.ru/vol0/data/main-menu-ru-ru-v2.json', headers=headers).json()

    # print(response)
    with open('waldberris.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)


def get_category():
    with open('waldberris.json', 'r', encoding='utf-8') as file:
        category_data = json.load(file)

        new_json = []
        for cat in category_data:
            id = cat.get("id")
            name = cat.get("name")
            url = cat.get("url")
            shard = cat.get("shard")
            query = cat.get("query")
            childs = cat.get("childs")

            new_json.append({
                "id": id,
                "name": name,
                "url": f'https://www.wildberries.ru{url}',
                "shard": shard,
                "query": query,
                "childs": childs
            })

    with open('data/category.json', 'w', encoding='utf-8') as file:
        json.dump(new_json, file, indent=4, ensure_ascii=False)

    childs_json = []
    for childs_cat in category_data:
        ch = childs_cat.get("childs")
        # childs_json.append({"ids": ch})
        childs_json.append(ch)

    with open('data/childs.json', 'w', encoding='utf-8') as file:
        json.dump(childs_json, file, indent=4, ensure_ascii=False)


def get_url_link():
    with open('data/childs.json', 'r', encoding='utf-8') as file:
        url_data = json.load(file)

    # TODO переделать в другой запрос или объединить с предыдущим
    for index, item in enumerate(url_data):
        with open(f'data/item{index}.json', 'w', encoding='utf-8') as file:
            json.dump(item, file, indent=4, ensure_ascii=False)



def main():
    # get_catalogy_waldberris()
    # get_category()
    get_url_link()


if __name__ == '__main__':
    main()
