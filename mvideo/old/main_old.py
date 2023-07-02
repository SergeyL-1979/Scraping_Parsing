import requests
import json


def get_data():

    cookies = {
        '__lhash_': '543f5f42b781baf4c58a01d5b39c5894',
        'CACHE_INDICATOR': 'false',
        'COMPARISON_INDICATOR': 'false',
        'HINTS_FIO_COOKIE_NAME': '2',
        'JSESSIONID': 'pNLXvvKLVLJzVHyLSQyWhxTzQQd22pFz4L6nJxZSL9FvJnTG5TdT!1482377436',
        'MAIN_PAGE_VARIATION_1': '3',
        'MVID_2_exp_in_1': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var2',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CATALOG_STATE': '1',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GIFT_KIT': 'true',
        'MVID_GUEST_ID': '20907703901',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_LP_SOLD_VARIANTS': '0',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_LK': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_LOGIN': 'true',
        'MVID_NEW_LK_MENU_BUTTON': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_SUGGESTIONS': 'true',
        'MVID_PDP_MAP_DEFAULT': 'true',
        'MVID_PROMO_CATALOG_ON': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_WEBP_ENABLED': 'true',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'bIPs': '-314595793',
        'flacktory': 'no',
        'searchType2': '2',
        'ADRUM_BT': 'R:78|g:978feb89-3ed7-49b8-8cbe-3e337b8af4f823817289',
        'MVID_ENVCLOUD': 'primary',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0',
        'Accept': 'application/json',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'x-set-application-id': 'bc1cc797-b9a4-4e76-8c04-10a7f10e7a5e',
        'Connection': 'keep-alive',
        'Referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '__lhash_=543f5f42b781baf4c58a01d5b39c5894; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; JSESSIONID=pNLXvvKLVLJzVHyLSQyWhxTzQQd22pFz4L6nJxZSL9FvJnTG5TdT!1482377436; MAIN_PAGE_VARIATION_1=3; MVID_2_exp_in_1=1; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20907703901; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=0; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PDP_MAP_DEFAULT=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; bIPs=-314595793; flacktory=no; searchType2=2; ADRUM_BT=R:78|g:978feb89-3ed7-49b8-8cbe-3e337b8af4f823817289; MVID_ENVCLOUD=primary',
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
        'limit': '0',
        'filterParams': 'WyLQotC+0LLQsNGA0Ysg0YHQviDRgdC60LjQtNC60L7QuSIsIi04Iiwi0JHQvtC70LXQtSA1JSJd',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers)
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

