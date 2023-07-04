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

    with open('data/1_catalog_ids.json', encoding='utf-8') as file:
        url_link_product = json.load(file)

    with open('data/2_name_and_url_product.json', 'w', encoding='utf-8') as file:
        json.dump([cat for cat in url_link_product], file, indent=4, ensure_ascii=False)


def read_catalog_product():
    with open('data/2_name_and_url_product.json', encoding='utf-8') as file:
        product_catalog = json.load(file)

    link_url_list = []
    for cat in product_catalog:
        cat = cat.get('categories')
        for i in cat:
            link_url_list.append(i)

    with open('data/3_collection_of_links.json', 'w', encoding='utf-8') as file:
        json.dump(link_url_list, file, indent=4, ensure_ascii=False)


def collection_of_links_to_sections():
    with open('data/3_collection_of_links.json', encoding='utf-8') as file:
        collection_of_links = json.load(file)
        print(collection_of_links)


def main():
    # get_catalog()
    # read_catalog_save_url_and_name()
    # read_catalog_product()
    collection_of_links_to_sections()



if __name__ == '__main__':
    main()
