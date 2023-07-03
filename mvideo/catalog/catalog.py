import os
import requests
import json

from config import cookies, headers


def get_catalog():
    if not os.path.exists('data'):
        os.mkdir('data')

    s = requests.Session()
    response = s.get('https://www.mvideo.ru/bff/settings/catalog', cookies=cookies, headers=headers).json()

    catalog_ids = response.get('body').get('categories')

    with open('data/1_catalog_ids.json', 'w', encoding='utf-8') as file:
        json.dump(catalog_ids, file, indent=4, ensure_ascii=False)


def read_catalog_save_url_and_name():
    # with open('data/1_catalog_ids.json', encoding='utf-8') as file:
    #     catalog_ids = json.load(file)
    #
    # link_url = []
    # for cat in catalog_ids:
    #     cat['categories'] = cat.get('name')
    #     cat['categories'] = cat.get('url')
    #     link_url.append({'name': cat['name'], 'url': 'https://www.mvideo.ru' + cat['url']})
    #
    # with open('data/2_categories_ids.json', 'w', encoding='utf-8') as file:
    #     json.dump(link_url, file, indent=4, ensure_ascii=False)

    with open('data/1_catalog_ids.json', encoding='utf-8') as file:
        url_link_product = json.load(file)

    link_url = []
    for cat in url_link_product:
        cat = cat.get('categories')
        link_url.append(cat)

    with open('data/2_name_and_url_product.json', 'w', encoding='utf-8') as file:
        json.dump(link_url, file, indent=4, ensure_ascii=False)


def main():
    get_catalog()
    read_catalog_save_url_and_name()

if __name__ == '__main__':
    main()
