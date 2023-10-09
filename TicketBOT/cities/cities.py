import requests
import json

"""
Параметры ответа

    code — IATA-код города.
    name — название города.
    coordinates — координаты города.
    time_zone — часовой пояс относительно гринвича.
    name_translations — название города на разных языках.
    country_code — IATA-код страны, в которой находится город.
"""


def get_cities():
    response = requests.get("http://api.travelpayouts.com/data/ru/cities.json")
    src = response.json()

    with open('cities.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)

    # return src


get_cities()
