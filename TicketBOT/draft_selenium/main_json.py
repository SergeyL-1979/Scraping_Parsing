import requests
import json

from config import headers


def get_json():
    json_data = {
        'query': '\n  query GetMarketsAndCountries($locales: [String!]!) {\n    market_change_dialog_v1 {\n      markets {\n        code\n      }\n      countries {\n        iata\n        translations(filters: { locales: $locales })\n      }\n    }\n  }\n',
        'variables': {
            'locales': [
                'ru',
            ],
        },
        'operation_name': 'market_and_countries',
    }

    response = requests.post('https://ariadne.aviasales.ru/api/gql', headers=headers, json=json_data)
    src = response.json()

    with open('data/info.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)


def get_content():
    json_data = {
        'query': '\n  query MainContentQuery($brand: Brand!, $locales: [String!], $input: MainPageBlocksV1Input!) {\n    main_page_blocks_v1(input: $input, brand: $brand) {\n      blocks {\n        __typename\n\n        ... on ContentlessBlock {\n          type\n        }\n      \n        ... on CityPOIsBlock {\n          city {\n            ...locationMainPageFields\n          }\n          pois {\n            ...locationMainPageFields\n          }\n        }\n\n        ... on CityPOIBlock {\n          city {\n            ...locationMainPageFields\n          }\n          poi {\n            ...locationMainPageFields\n          }\n        }\n\n        ... on POICompilationBlock {\n          ark_id\n          title \n          pois {\n            location {\n              ...locationMainPageFields\n            }\n            poi {\n              ...locationMainPageFields\n            }\n          }\n        }\n\n        ... on CityPOICollectionBlock {\n          city {\n            ...locationMainPageFields\n          }\n          pois {\n            ...locationMainPageFields\n          }\n        }\n\n        ... on NationalParksCollectionBlock {\n          parks {\n            ...locationMainPageFields\n          }\n        }\n\n        ... on NationalParkPOIBlock {\n          park {\n            ...locationMainPageFields\n          }\n          poi {\n            ...locationMainPageFields\n          }\n        }\n\n        ... on LocationsCompilationBlock {\n          title\n          tag\n          locations {\n            ...locationMainPageFields\n          } \n        }\n\n        ... on HotTicketsBlock {\n          offers {\n            price {\n              ...priceFields\n            }\n            old_price {\n              value\n            }\n          }\n          cities {\n            ...citiesFields\n          }\n          airlines {\n            ...airlinesFields\n          }\n          airports {\n            ...airportsFields\n          }\n        }\n\n        ... on PromoKorocheBlock {\n          guide {\n            ark_id\n            city_iata\n            title \n            image_url\n            depart_date\n            badge {\n              text\n              style {\n                background_color\n                text_color\n                is_promo\n              }\n              icon {\n                svg\n                pdf\n              }\n            }\n          }\n        }\n\n        ... on WeekendsBlock {\n          weekend_prices {\n            price {\n              ...priceFields\n            }\n          }\n          places {\n            cities {\n              image_url\n              ...citiesFields\n            }\n            airports {\n              ...airportsFields\n            }\n          }\n        }\n        \n        ... on CityVideoBlock {\n          image_url\n          video_url\n          text\n          action_type\n          city_info {\n            ...citiesFields\n            city {\n              ark_id\n            }\n          }\n          min_price {\n            value\n            currency\n          }\n        }\n        \n        ... on PopularDestinationsBlock {\n          origin_city {\n            iata\n            translations(filters: {locales: $locales})\n          }\n          directions {\n            country_iata\n            image_url\n            min_price {\n              value\n              currency\n            }\n          }\n          places {\n            countries {\n              ...countriesFields\n            }\n          }\n        }\n      }\n    }\n  }\n\n  \nfragment locationMainPageFields on LocationMainPageV2 {\n  main_tag(filters: {locales: $locales})\n  min_price {\n    value\n    currency\n  }\n  entity {\n    iata\n    name(filters: {locales: $locales})\n    type\n    ark_id\n    slug\n  }\n  content {\n    __typename\n    ... on POIContent {\n      ark_id\n      poi_id\n      tabs_entities {\n        id\n      }\n      description(filters: {locales: $locales})\n      images {\n        image_url\n      }\n    }\n    ... on NationalParkContent {\n      ark_id\n      description(filters: {locales: $locales})\n      images_urls\n    }\n    ... on CityContent {\n      ark_id\n      images_urls\n    }\n    ... on IslandContent {\n      ark_id\n      images_urls\n    }\n    ... on RegionContent {\n      ark_id\n      images_urls\n    }\n    ... on CountryContent {\n      ark_id\n      images_urls\n    }\n  }\n}\n  \nfragment priceFields on Price {\n  depart_date\n  return_date\n  value\n  cashback\n  found_at\n  signature\n  ticket_link\n  currency\n  convenient\n  provider\n  segments {\n    transfers {\n      duration_seconds\n      country_code\n      visa_required\n      night_transfer\n      at\n      to\n      tags\n    }\n    flight_legs {\n      origin\n      destination\n      local_depart_date\n      local_depart_time\n      local_arrival_date\n      local_arrival_time\n      flight_number\n      operating_carrier\n      aircraft_code\n      technical_stops\n      equipment_type\n      duration_seconds\n    }\n  }\n}\n\n  \nfragment airlinesFields on Airline {\n  iata\n  translations(filters: {locales: $locales})\n}\n  \nfragment citiesFields on CityInfo {\n  city{\n    iata\n    translations(filters: {locales: $locales})\n  }\n}\n  \nfragment airportsFields on Airport {\n  iata\n  translations(filters: {locales: $locales})\n  city {\n    iata\n    translations(filters: {locales: $locales})\n  }\n}\n  \nfragment countriesFields on Country {\n  iata\n  translations(filters: {locales: $locales})\n}\n',
        'variables': {
            'brand': 'AS',
            'locales': [
                'ru',
            ],
            'input': {
                'auid': 'Ty1rd2UgaUhvVGdJdEwzAg==',
                'market': 'ru',
                'origin': 'MOW',
                'currency': 'rub',
                'trip_class': 'Y',
                'passport_country': 'RU',
                'language': 'ru',
                'application': 'selene',
                'poi_compilation_limit': 28,
                'countries_limit': 30,
                'weekends_params': {
                    'dates': {},
                    'add_extra_days': False,
                },
            },
        },
        'operation_name': 'main_page_blocks_v1',
    }

    response = requests.post('https://ariadne.aviasales.ru/api/gql', headers=headers, json=json_data)
    src = response.json()

    with open('data/country.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)



def main():
    # get_json()
    get_content()


if __name__ == '__main__':
    main()
