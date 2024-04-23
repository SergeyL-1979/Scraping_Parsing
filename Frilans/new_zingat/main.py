import time

import requests
import json
import requests_cache
from bs4 import BeautifulSoup

from config import cookies, headers


def get_data(total_page):
    response = requests.get('https://www.zingat.com/en/for-sale',
                            cookies=cookies, headers=headers)

    # soup = BeautifulSoup(response.text, 'lxml')

    # total_page = soup.find('nav', attrs={'data-total': True}).get('data-total')
    # print(total_page)

    # TODO получить все объявления по одной странице.
    page_num = 0
    while page_num <= int(total_page):
        response = requests.get(f'https://www.zingat.com/en/for-sale?page={page_num}',
                                cookies=cookies, headers=headers)
        # soup = BeautifulSoup(response.text, 'lxml')
        #
        # ads = soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-4 col-lg-4')
        # for ad in ads:
        #     title = ad.find('h3', class_='title').text.strip()
        #     price = ad.find('span', class_='price').text.strip()
        #     link = ad.find('a')['href']
        #     print(f'{title} {price} {link}')

        page_num += 1
        print(f'Страница {page_num} из {total_page}')
        time.sleep(15)

        with open(f'pages/info_{page_num}.html', 'w', encoding='utf-8') as file:
            file.write(response.text)


def get_ad():
    with open('info.html', 'r', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')

    total_page = soup.find('nav', attrs={'data-total': True}).get('data-total')
    print(total_page)
    return total_page


def main():
    get_data(get_ad())
    get_ad()


if __name__ == '__main__':
    main()
