import jmespath
import json

with open("info_25_09_2022_1.json", 'r', encoding='utf-8') as file:
    data = json.load(file)

res = jmespath.search("listings[*].property.location.city.name", data)
print(res)
