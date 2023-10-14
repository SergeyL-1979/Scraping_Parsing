import json
from pathlib import Path
from typing import TypeVar, Iterable

from pydantic import BaseModel, ValidationError

TItem = TypeVar('TItem', bound='Item')

BASE_DIR = Path().cwd()
ITEMS_PATH = BASE_DIR.joinpath('waldberris.json')
COLLECT_DATA_PATH = BASE_DIR.joinpath('data', 'collect_data')


class Item(BaseModel):
    id: int
    parent: int | None = None
    name: str
    seo: str | None = None
    url: str
    shard: str | None = None
    query: str | None = None
    landing: bool | None = None
    childs: list[TItem] = []


def get_items() -> Iterable[Item]:
    try:
        with open(ITEMS_PATH, encoding='utf-8') as file:
            return map(Item.model_validate, json.load(file))
    except FileNotFoundError:
        print('File not found')
    except ValidationError:
        print('Validation error')

    return []


ITEMS_DICT: dict[int, list[Item]] = {}


def parse_items(items: Iterable[Item], level: int = 0) -> None:
    for item in items:
        if item.childs:
            parse_items(item.childs, level + 1)

        if level not in ITEMS_DICT:
            ITEMS_DICT[level] = [item]
        else:
            ITEMS_DICT[level].append(item)


def get_collect_all_the_childs():
    items = get_items()

    parse_items(items)

    for level, items_list in ITEMS_DICT.items():
        DIR = COLLECT_DATA_PATH.joinpath(str(level))
        DIR.mkdir(exist_ok=True)

        # TODO: Ну этим можно не заниматься
        data = []
        for i in items_list:
            i = i.model_dump()
            i.pop('childs', None)
            data.append(i)

        with open(DIR.joinpath('items.json'), 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    COLLECT_DATA_PATH.mkdir(parents=True, exist_ok=True)

    get_collect_all_the_childs()


if __name__ == '__main__':
    main()
