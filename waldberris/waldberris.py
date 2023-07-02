import requests
import json


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
    with open('waldberris.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)



def main():
    get_catalogy_waldberris()


if __name__ == '__main__':
    main()

