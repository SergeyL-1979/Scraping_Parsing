import requests
import json

"""
Описание ответа
    code — IATA-код страны.
    name — название страны.
    currency — валюта страны.
    name_translations — название страны на различных языках.
"""


def get_countries():
    response = requests.get("https://api.travelpayouts.com/data/ru/countries.json")
    src = response.json()

    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)

        currency_list = {}
        new_dict = dict()
        for country in src:
            new_dict[country["name"]] = country['code']
            currency_list[country["name"]] = country["currency"]

    with open('new_countries.json', 'w', encoding='utf-8') as file:
        json.dump(new_dict, file, indent=4, ensure_ascii=False)

    with open('currency.json', 'w', encoding='utf-8') as file:
        json.dump(currency_list, file, indent=4, ensure_ascii=False)

    # return src


get_countries()
