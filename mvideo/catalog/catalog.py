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

    collection_list_product = []
    for collection in collection_of_links:
        col_name = collection.get('name')
        col_url = collection.get('url')

        collection_list_product.append({'name': col_name, 'url': f"https://www.mvideo.ru{col_url}"})

    with open('data/4_links.json', 'w', encoding='utf-8') as file:
        json.dump(collection_list_product, file, indent=4, ensure_ascii=False)


def links_subcategory():
    with open('data/3_collection_of_links.json', encoding='utf-8') as file:
        subcategory_of_links = json.load(file)

    link_url_list = []
    for cat in subcategory_of_links:
        cat = cat.get('categories')
        for name_and_url in cat:
            link_url_list.append(name_and_url)

    with open('data/5_links_subcategory.json', 'w', encoding='utf-8') as file:
        json.dump(link_url_list, file, indent=4, ensure_ascii=False)

    collection_list_product = []
    output_data = [v for v in {inp['name']: inp for inp in link_url_list}.values()]
    for collection in output_data:
        col_name = collection.get('name')
        col_url = collection.get('url')

        collection_list_product.append({'name': col_name, 'url': f"https://www.mvideo.ru{col_url}"})

    with open('data/6_links_products.json', 'w', encoding='utf-8') as file:
        json.dump(collection_list_product, file, indent=4, ensure_ascii=False)


def get_following_link():
    s = requests.Session()

    with open('data/6_links_products.json', encoding='utf-8') as file:
        card_product = json.load(file)

    for i in card_product:
        url = i['url']
        # r = s.get(url=url, headers=headers, cookies=cookies)
        # print(r.text)
        # for count in range(1, 7):
        # with open(f'data/test.txt', 'w', encoding='utf-8', newline='') as file:
        #     file.write(f'{i}\n')
    for lin_url in card_product:
        print('[INFO]' f'{lin_url["url"]}')


def main():
    # get_catalog()
    # read_catalog_save_url_and_name()
    # read_catalog_product()
    # collection_of_links_to_sections()
    # links_subcategory()
    get_following_link()


if __name__ == '__main__':
    main()
