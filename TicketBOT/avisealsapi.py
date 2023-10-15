import requests

from config import TOKEN

url = 'https://api.travelpayouts.com/aviasales/v3/prices_for_dates'


def get_flight_info(origin, destination, departure_date):
    r = requests.get(
        url,
        params={
            'origin': origin,
            'destination': destination,
            'unique': 'false',
            'sorting': 'price',
            'departure_at': departure_date,
            'direct': 'true',
            'currency': 'rub',
            'limit': 5,
            'page': 1,
            'one_way': 'true',
            'token': TOKEN,
        }
    )
    print(r.json()['data'])
    return r.json()['data']


if __name__ == '__main__':
    get_flight_info(origin='IST', destination='UFA', departure_date='2023-11-10')
