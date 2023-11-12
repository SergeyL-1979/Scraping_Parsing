import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Origin': 'https://www.wildberries.ru',
    'Connection': 'keep-alive',
    'Referer': 'https://www.wildberries.ru/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'DNT': '1',
    'Sec-GPC': '1',
}

response = requests.get(
    'https://catalog.wb.ru/brands/m/filters?TestGroup=control&TestID=331&appType=1&brand=27445&curr=rub&dest=-1257786&filters=xsubject&regions=80,83,38,4,64,33,68,70,30,40,86,75,69,1,66,110,22,48,31,71,112,114&spp=29',
    headers=headers,
)