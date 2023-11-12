import os
import requests
import json
import math
from config import cookies, headers
from bs4 import BeautifulSoup

if not os.path.exists('data'):
    os.mkdir('data')


def get_params():
    params = {
        # 'sort': '-percent_discount',
        'limit': '12',
        # 'city_ids[0]': '3',
        'radius': '0',
    }

    s = requests.Session()
    response = s.get(
        'https://api.autospot.ru/rest/filter/cars-with-parallel-import/',
        params=params,
        cookies=cookies,
        headers=headers,
    ).json()

    total_items = response.get("meta").get("totalOffers")

    if total_items is None:
        return '[!] No items :('

    page_count = math.ceil(total_items / 11)
    print(f'[INFO] Total position {total_items} | Total pages {page_count}')

    car_items = {}
    for i in range(page_count):
        limit = f'{i * 11}'

        params = {
            'sort': '-percent_discount',
            'limit': limit,
            # 'page': '2',
            # 'city_ids[0]': '3',
            'radius': '0',
        }

        res = s.get(
            'https://api.autospot.ru/rest/filter/cars-with-parallel-import/',
            params=params,
            cookies=cookies,
            headers=headers,
        ).json()

        car_list = res.get("items")
        car_items[i] = car_list

        print(f'[+] Finished {i + 1} of the {page_count} pages')

    with open('data/test_items1.json', 'w', encoding='utf-8') as file:
        json.dump(car_items, file, indent=4, ensure_ascii=False)
    # with open('data/test.json', 'w', encoding='utf-8') as file:
    #     json.dump(response, file, indent=4, ensure_ascii=False)


def get_html():
    s = requests.Session()
    response = s.get('https://autospot.ru/filters/').text
    # print(response.content)
    # with open('avtospot.html', 'w', encoding='utf-8') as file:
    #     file.write(response)
    with open('avtospot.html', 'r', encoding='utf-8') as file:
        data = file.read()

    # soul = BeautifulSoup(fragments, "lxml")
    soul = BeautifulSoup(data, "lxml")
    items_divs = soul.find_all('div', class_='filter-grid__col ng-star-inserted')
    print(items_divs)


def main():
    # get_params()
    get_html()



if __name__ == '__main__':
    main()
