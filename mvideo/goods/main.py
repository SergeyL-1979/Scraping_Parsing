import requests
import json


def get_data():

    cookies = {
        # '__hash_': '6534b44051d190414758cb7e6996e0fc',
        # '__lhash_': '36ae6966bf103c5ccbadcd172f4ba5be',
        'MVID_AB_TOP_SERVICES': '1',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CATALOG_STATE': '1',
        'MVID_CHECKOUT_STORE_SORTING': 'true',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_GLP_GLC': '2',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINDBOX_DYNAMICALLY': 'true',
        'MVID_MINI_PDP': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_RECOMENDATION': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod2',
        'cfidsgib-w-mvideo': 'V36bPryZg5A+/4oMGRUaIiEv7Mb1prsGyJt+T2jHkhDrwDkgSb7Z0mvn7Oa3EazvPr7HjSpogtfTcHCkJQEH4TNoCI+a7LH2qTaPVHirC6LQB9cV5x790fjSt7Fp7h6QpsU/hi7EdjYSBqrC5OV6Kz30juMWh7yxcEXR',
        'fgsscgib-w-mvideo': 'UkFm194d18bfb804d8dd925a6aef75593903ea6f',
        'fgsscgib-w-mvideo': 'UkFm194d18bfb804d8dd925a6aef75593903ea6f',
        'gssc218': '',
        'gsscgib-w-mvideo': 'avDqxmxG2V5kyZRIUCj+pOdGneU7OgK+dXya507xI9L+ykrO9sufZ3437H2AgvyQFMtrHEAqB93kUJLBukJpj8PArhLI11fmqcfRo6kAHOa6aYn75GoJn48unnGhamiBb1FkUPTjOZ/k/EHv+DC/mvh37JiW6rJ1A1FEYW5+q5ptWMUxaU7D9djoqzxtWCpisUgYFjQQQss/jG5IBYL+z8a+K9XqR39bggKVi99IOVmxFFZWJEKavKd65VSVeg==',
        'gsscgib-w-mvideo': 'avDqxmxG2V5kyZRIUCj+pOdGneU7OgK+dXya507xI9L+ykrO9sufZ3437H2AgvyQFMtrHEAqB93kUJLBukJpj8PArhLI11fmqcfRo6kAHOa6aYn75GoJn48unnGhamiBb1FkUPTjOZ/k/EHv+DC/mvh37JiW6rJ1A1FEYW5+q5ptWMUxaU7D9djoqzxtWCpisUgYFjQQQss/jG5IBYL+z8a+K9XqR39bggKVi99IOVmxFFZWJEKavKd65VSVeg==',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'application/json',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'x-set-application-id': '01a52091-d520-4c4f-bae2-38fc282fd176',
        'X-GIB-GSSCgib-w-mvideo': 'avDqxmxG2V5kyZRIUCj+pOdGneU7OgK+dXya507xI9L+ykrO9sufZ3437H2AgvyQFMtrHEAqB93kUJLBukJpj8PArhLI11fmqcfRo6kAHOa6aYn75GoJn48unnGhamiBb1FkUPTjOZ/k/EHv+DC/mvh37JiW6rJ1A1FEYW5+q5ptWMUxaU7D9djoqzxtWCpisUgYFjQQQss/jG5IBYL+z8a+K9XqR39bggKVi99IOVmxFFZWJEKavKd65VSVeg==',
        'X-GIB-FGSSCgib-w-mvideo': '7tVff0407ef651bd764c955a11e94067907189c9',
        'sentry-trace': '4f4a501d4b84435682e532498c24954f-9fe92bdc6008d4e7-1',
        'baggage': 'sentry-environment=production,sentry-transaction=%2F**%2F,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=4f4a501d4b84435682e532498c24954f,sentry-sample_rate=0.5',
        'Connection': 'keep-alive',
        'Referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195',
        # 'Cookie': '__hash_=6534b44051d190414758cb7e6996e0fc; __lhash_=36ae6966bf103c5ccbadcd172f4ba5be; MVID_AB_TOP_SERVICES=1; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; cfidsgib-w-mvideo=V36bPryZg5A+/4oMGRUaIiEv7Mb1prsGyJt+T2jHkhDrwDkgSb7Z0mvn7Oa3EazvPr7HjSpogtfTcHCkJQEH4TNoCI+a7LH2qTaPVHirC6LQB9cV5x790fjSt7Fp7h6QpsU/hi7EdjYSBqrC5OV6Kz30juMWh7yxcEXR; fgsscgib-w-mvideo=UkFm194d18bfb804d8dd925a6aef75593903ea6f; fgsscgib-w-mvideo=UkFm194d18bfb804d8dd925a6aef75593903ea6f; gssc218=; gsscgib-w-mvideo=avDqxmxG2V5kyZRIUCj+pOdGneU7OgK+dXya507xI9L+ykrO9sufZ3437H2AgvyQFMtrHEAqB93kUJLBukJpj8PArhLI11fmqcfRo6kAHOa6aYn75GoJn48unnGhamiBb1FkUPTjOZ/k/EHv+DC/mvh37JiW6rJ1A1FEYW5+q5ptWMUxaU7D9djoqzxtWCpisUgYFjQQQss/jG5IBYL+z8a+K9XqR39bggKVi99IOVmxFFZWJEKavKd65VSVeg==; gsscgib-w-mvideo=avDqxmxG2V5kyZRIUCj+pOdGneU7OgK+dXya507xI9L+ykrO9sufZ3437H2AgvyQFMtrHEAqB93kUJLBukJpj8PArhLI11fmqcfRo6kAHOa6aYn75GoJn48unnGhamiBb1FkUPTjOZ/k/EHv+DC/mvh37JiW6rJ1A1FEYW5+q5ptWMUxaU7D9djoqzxtWCpisUgYFjQQQss/jG5IBYL+z8a+K9XqR39bggKVi99IOVmxFFZWJEKavKd65VSVeg==',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'DNT': '1',
        'Sec-GPC': '1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    params = {
        'categoryId': '195',
        'offset': '0',
        'limit': '24',
        'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    # print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_price.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_price = {}

    material_price = response.get('body').get('materialPrices')
    for item in material_price:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_price[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus,
        }

    with open('4_items_price.json', 'w') as file:
        json.dump(items_price, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_price.json') as file:
        products_price = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_price:
            prices = products_price[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
