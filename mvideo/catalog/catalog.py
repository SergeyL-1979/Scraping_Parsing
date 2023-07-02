import requests
import json


def get_catalog():
    cookies = {
        # '__hash_': '6534b44051db504a8758cb7e6996e0fc',
        # '__lhash_': '36ae6966bf103c5ccbadcd172f4ba5be',
        'MVID_ENVCLOUD': 'prod2',
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
        'cfidsgib-w-mvideo': 'HIn6PN3dqAonSHoeEOnpS5PLVB6RrjLKtgr9Wyco/q+S93Rw/mDaSgJXId3Q83dWW0IvQQNOzyWln6ZWyd1KZfEfGXYohQAYibVoVi6PZ5KMz+Ropsnj3dS7K5w7j6W2Lb+2adGDIgScbt9s3c2qnqf+4iotDiymMjY8Cg==',
        'fgsscgib-w-mvideo': 'oDtu47411675549a607572aaf23d854de1c72a86',
        'fgsscgib-w-mvideo': 'oDtu47411675549a607572aaf23d854de1c72a86',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '2483346442.20480.0000',
        'bIPs': '2105588670',
        'Old_Browser_Accept_the_Risk_and_Continue': '1',
        'MVID_GUEST_ID': '22691347404',
        'MVID_VIEWED_PRODUCTS': '',
        'wurfl_device_id': 'generic_web_browser',
        'JSESSIONID': 'CH2RkgRJgYqRsfg7ccFLxbpXtPxdNnyRjYp7FrdnhpQxGSpvvFvP!17797630',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_YANDEX_WIDGET': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'HINTS_FIO_COOKIE_NAME': '2',
        'searchType2': '1',
        'COMPARISON_INDICATOR': 'false',
        'CACHE_INDICATOR': 'true',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'BIGipServeratg-ps-prod_tcp80_clone': '2483346442.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'deviceType': 'desktop',
        'gssc218': '',
        'gsscgib-w-mvideo': 'qUvRdzwLIxLoPMpj2ILs7nKffAn1nmXReGsafwd1A6kRm45H1tjxgxHBGe83L3Yi5nfq8A21I7z+0ZH+J6YjQO897Mi41GmH4OCXVszLQVqyQ7Tat/xjiCy7Xz/5zQFBJTpUt0I7LQjlQotEyBxX5j01wPk3AkBBOfZMVPTG1Ngmnsd5ExhDDAHRxpR6PI48W7KYPPbR8RpQoNyUecn/jGAxqRTcGn+eJtphhFGTg4Ir0XUlILNc4XPfXo75PQ==',
        'gsscgib-w-mvideo': 'qUvRdzwLIxLoPMpj2ILs7nKffAn1nmXReGsafwd1A6kRm45H1tjxgxHBGe83L3Yi5nfq8A21I7z+0ZH+J6YjQO897Mi41GmH4OCXVszLQVqyQ7Tat/xjiCy7Xz/5zQFBJTpUt0I7LQjlQotEyBxX5j01wPk3AkBBOfZMVPTG1Ngmnsd5ExhDDAHRxpR6PI48W7KYPPbR8RpQoNyUecn/jGAxqRTcGn+eJtphhFGTg4Ir0XUlILNc4XPfXo75PQ==',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.mvideo.ru/',
        'Connection': 'keep-alive',
        # 'Cookie': '__hash_=6534b44051db504a8758cb7e6996e0fc; __lhash_=36ae6966bf103c5ccbadcd172f4ba5be; MVID_ENVCLOUD=prod2; MVID_AB_TOP_SERVICES=1; MVID_ALFA_PODELI_NEW=true; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CATALOG_STATE=1; MVID_CHECKOUT_STORE_SORTING=true; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GIFT_KIT=true; MVID_GLP_GLC=2; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_MINI_PDP=true; MVID_NEW_ACCESSORY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_RECOMENDATION=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; cfidsgib-w-mvideo=HIn6PN3dqAonSHoeEOnpS5PLVB6RrjLKtgr9Wyco/q+S93Rw/mDaSgJXId3Q83dWW0IvQQNOzyWln6ZWyd1KZfEfGXYohQAYibVoVi6PZ5KMz+Ropsnj3dS7K5w7j6W2Lb+2adGDIgScbt9s3c2qnqf+4iotDiymMjY8Cg==; fgsscgib-w-mvideo=oDtu47411675549a607572aaf23d854de1c72a86; fgsscgib-w-mvideo=oDtu47411675549a607572aaf23d854de1c72a86; flacktory=no; BIGipServeratg-ps-prod_tcp80=2483346442.20480.0000; bIPs=2105588670; Old_Browser_Accept_the_Risk_and_Continue=1; MVID_GUEST_ID=22691347404; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; JSESSIONID=CH2RkgRJgYqRsfg7ccFLxbpXtPxdNnyRjYp7FrdnhpQxGSpvvFvP!17797630; MVID_CALC_BONUS_RUBLES_PROFIT=false; NEED_REQUIRE_APPLY_DISCOUNT=true; MVID_CART_MULTI_DELETE=false; MVID_YANDEX_WIDGET=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; HINTS_FIO_COOKIE_NAME=2; searchType2=1; COMPARISON_INDICATOR=false; CACHE_INDICATOR=true; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=2483346442.20480.0000; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; gssc218=; gsscgib-w-mvideo=qUvRdzwLIxLoPMpj2ILs7nKffAn1nmXReGsafwd1A6kRm45H1tjxgxHBGe83L3Yi5nfq8A21I7z+0ZH+J6YjQO897Mi41GmH4OCXVszLQVqyQ7Tat/xjiCy7Xz/5zQFBJTpUt0I7LQjlQotEyBxX5j01wPk3AkBBOfZMVPTG1Ngmnsd5ExhDDAHRxpR6PI48W7KYPPbR8RpQoNyUecn/jGAxqRTcGn+eJtphhFGTg4Ir0XUlILNc4XPfXo75PQ==; gsscgib-w-mvideo=qUvRdzwLIxLoPMpj2ILs7nKffAn1nmXReGsafwd1A6kRm45H1tjxgxHBGe83L3Yi5nfq8A21I7z+0ZH+J6YjQO897Mi41GmH4OCXVszLQVqyQ7Tat/xjiCy7Xz/5zQFBJTpUt0I7LQjlQotEyBxX5j01wPk3AkBBOfZMVPTG1Ngmnsd5ExhDDAHRxpR6PI48W7KYPPbR8RpQoNyUecn/jGAxqRTcGn+eJtphhFGTg4Ir0XUlILNc4XPfXo75PQ==',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'DNT': '1',
        'Sec-GPC': '1',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    response = requests.get('https://www.mvideo.ru/bff/settings/catalog', cookies=cookies,
                            headers=headers).json()
    # print(response)

    catalog_ids = response.get('body').get('categories')
    # print(catalog_ids)

    with open('1_categories_ids.json', 'w') as file:
        json.dump(catalog_ids, file, indent=4, ensure_ascii=False)


def read_catalog_save_url_name():
    with open('1_categories_ids.json') as file:
        catalog_ids = json.load(file)

    link_url = []
    for cat in catalog_ids:
        cat['categories'] = cat.get('name')
        cat['categories'] = cat.get('url')
        link_url.append({'name': cat['name'], 'url': 'https://www.mvideo.ru' + cat['url']})

    with open('2_categories_ids.json', 'w') as file:
        json.dump(link_url, file, indent=4, ensure_ascii=False)


def reader_url_product():
    with open('2_categories_ids.json') as file:
        url_link_product = json.load(file)

    for link_product in url_link_product:
        print(link_product.get('url'))


def main():
    # get_catalog()
    # read_catalog_save_url_name()
    reader_url_product()


if __name__ == '__main__':
    main()
