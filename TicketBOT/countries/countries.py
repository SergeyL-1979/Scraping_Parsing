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
    response = requests.get("http://api.travelpayouts.com/data/ru/countries.json")
    src = response.json()

    with open('countries.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)


get_countries()
