import requests
import os
import csv
import json
from datetime import datetime
from filters import filters_data

from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# ua = UserAgent()


def collect_data():
    for i in range(1, 10):
        headers = {
            'authority': 'www.zingat.com',
            'accept': 'application/json',
            'accept-language': 'ru-RU,ru;q=0.9,en;q=0.8',
            'content-type': 'application/json',
            'dnt': '1',
            'referer': 'https://www.zingat.com/en/for-sale',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'page': f'{i}',
            'page_size': '21',
            'noLocation': 'true',
            'responseType': 'json',
            '_': '1664198801208',
        }

        response = requests.get('https://www.zingat.com/en/for-sale', params=params, headers=headers)

        t_date = datetime.now().strftime('%d_%m_%Y')

        res = requests.get('https://www.zingat.com/en/for-sale')
        with open(f'info.html', 'w', encoding='utf-8') as file:
            file.write(res.text)

        # with open(f"info_{t_date}_{i}.json", 'w') as file:
        #     json.dump(response.json(), file, indent=4, ensure_ascii=False)

        listings = response.json()['listings']
        result = []

        for l in listings:
            l_phone = l.get('owner')['zinglinePhone']
            l_link = l.get('slug')
            l_id = l.get('id')
            l_price = l.get('price')['amount']
            l_room = l.get('property')['roomSlug']
            l_size = l.get('property')['size']
            l_city = l.get('property')['location']['city']['name']
            l_county = l.get('property')['location']['county']['name']
            l_location = l.get('property')['location']['name']
            l_contact = l.get('owner')['contact']['nameSurname']
            l_status = l.get('owner')['status']['label']
            l_description = l.get('description')
            l_create = l.get('publishedOn')[:-6:]
            # print(l_create.replace("T", " "))

            result.append(
                [l_contact, l_phone, l_price, l_room, f'{l_size}m2', l_location, l_county, l_city, l_description, l_create.replace("T", " "), l_status, f'https://www.zingat.com/en/{l_link}-{l_id}i']
            )

        with open(f'result_{t_date}_{i}.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=";")

            writer.writerow(
                (
                    "Contact",
                    "Phone",
                    "Price",
                    "Rooms",
                    "Size",
                    "Location",
                    "County",
                    "City",
                    "Description",
                    "Create Date",
                    "Status",
                    "URL",
                )
            )

            writer.writerows(
                result
            )


def main():
    collect_data()
    filters_data('info.html')


if __name__ == '__main__':
    main()
