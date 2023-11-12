import requests
import json


def get_airports():
    response = requests.get("https://api.travelpayouts.com/data/ru/airports.json")
    src = response.json()

    with open('airports.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)


get_airports()
