import json
import requests

cookies = {
    '__utma': '55604128.138776428.1692213382.1692213382.1692213382.1',
    '__utmc': '55604128',
    '__utmz': '55604128.1692213382.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
    '__utmt': '1',
    '__utmb': '55604128.2.10.1692213382',
}

headers = {
    'authority': 'www.zingat.com',
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    # 'cookie': '__utma=55604128.138776428.1692213382.1692213382.1692213382.1; __utmc=55604128; __utmz=55604128.1692213382.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=55604128.2.10.1692213382',
    'dnt': '1',
    'pragma': 'no-cache',
    'referer': 'https://www.zingat.com/en/for-sale',
    'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

params = {
    'page_size': '21',
    'noLocation': 'true',
    'responseType': 'json',
    '_': '1692213408069',
}

response = requests.get('https://www.zingat.com/en/for-sale',
                        params=params, cookies=cookies, headers=headers).json()

with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(response, file, indent=4, ensure_ascii=False)

with open('listings.json', 'w', encoding='utf-8') as file:
    json.dump(response['listings'], file, indent=4, ensure_ascii=False)

with open('page.json', 'w', encoding='utf-8') as file:
    json.dump(response['pageMetaData'], file, indent=4, ensure_ascii=False)

# with open('data.json', 'r', encoding='utf-8') as file:
#     real_estate = json.load(file)
# d_list = []
# for i in response:
#     # res = dict()
#     print(i.get("status"))

#     res["pageMetaData"] = i.get("pageMetaData")
#
#     d_list.append({1: res})
