import os
import requests
import json
from pathlib import Path
from datetime import datetime

if not os.path.exists('data/collect_data'):
    os.mkdir('data/collect_data')

if not os.path.exists('data/collect_data/1'):
    os.mkdir('data/collect_data/1')

if not os.path.exists('data/collect_data/2'):
    os.mkdir('data/collect_data/2')

if not os.path.exists('data/collect_data/3'):
    os.mkdir('data/collect_data/3')

if not os.path.exists('data/collect_data/4'):
    os.mkdir('data/collect_data/4')


def get_collect_all_the_childs(path):

    with open(path, 'r', encoding='utf-8') as file:
        collect_data = json.load(file)

    new_json_1 = []
    new_json_2 = []
    new_json_3 = []
    new_json_4 = []
    for child_1 in collect_data:
        if 'childs' in child_1.keys():
            collect_1 = child_1["childs"]
            new_json_1.append(collect_1)

            for child_2 in collect_1:
                if 'childs' in child_2.keys():
                    collect_2 = child_2["childs"]
                    new_json_2.append(collect_2)

                    for child_3 in collect_2:
                        if 'childs' in child_3.keys():
                            collect_3 = child_3["childs"]
                            new_json_3.append(collect_3)

                            for child_4 in collect_3:
                                if 'childs' in child_4.keys():
                                    collect_4 = child_4["childs"]
                                    new_json_4.append(collect_4)

    for index, item in enumerate(new_json_1):
        with open(f'data/collect_data/1/item_collect_{index}.json', 'w', encoding='utf-8') as file:
            json.dump(item, file, indent=4, ensure_ascii=False)
    for index, item in enumerate(new_json_2):
        with open(f'data/collect_data/2/item_collect_{index}.json', 'w', encoding='utf-8') as file:
            json.dump(item, file, indent=4, ensure_ascii=False)
    for index, item in enumerate(new_json_3):
        with open(f'data/collect_data/3/item_collect_{index}.json', 'w', encoding='utf-8') as file:
            json.dump(item, file, indent=4, ensure_ascii=False)
    for index, item in enumerate(new_json_4):
        with open(f'data/collect_data/4/item_collect_{index}.json', 'w', encoding='utf-8') as file:
            json.dump(item, file, indent=4, ensure_ascii=False)


def main():
    get_collect_all_the_childs(path=r'D:\TEST_JUNIOR\Parser_Scraper\Scraping_Parsing\waldberris\waldberris.json')


if __name__ == '__main__':
    main()
