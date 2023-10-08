import requests
import json
import time

from config import TOKEN

# =================== API ===================

# DEPARTURE = '2023-11-01'  # (в формате YYYY-MM или YYYY-MM-DD)
# RETURN = '2023-11-15'  # (в формате YYYY-MM или YYYY-MM-DD)
# ORIGIN = 'MOW'  # Москва
# DESTINATION = 'LED'  # Санкт-Петербург


def get_search_city(origin, destination):
    response = requests.get(
        f"https://www.travelpayouts.com/widgets_suggest_params?q=Из%20{origin}%20в%20{destination}"
    )
    src = response.json()
    ORIGIN = src['origin']['iata']
    DESTINATION = src['destination']['iata']

    # return {'ORIGIN': ORIGIN, 'DESTINATION': DESTINATION}
    return ORIGIN, DESTINATION


# ===== Сгруппированные дешевые авиабилеты ====
def get_grouped_cheap_flights(url):
    """
    :currency: — валюта цен на билеты. Значение по умолчанию — rub.
    :origin: — пункт отправления. IATA-код города или аэропорта. Длина не менее двух и не более трёх символов.
    :destination: — пункт назначения. IATA-код города или аэропорта. Длина не менее двух и не более трёх.
    :group_by: — параметр группировки:
        :departure_at: — по дате отправления (по умолчанию);
        :return_at: — по дате обратного вылета;
        :month: — по месяцам.
    :departure_at: — дата вылета из пункта отправления (в формате YYYY-MM или YYYY-MM-DD).
    :return_at: — дата возвращения. Чтобы получить билеты в один конец, оставьте это поле пустым.
    :market: — задаёт маркет источника данных (по умолчанию ru).
    :direct: — получить рейсы без пересадок. Принимает значения true или false. По умолчанию false.
    :trip_duration: — длительность путешествия.

    """
    # url = (f"https://api.travelpayouts.com/aviasales/v3/grouped_prices?origin={ORIGIN}"
    #        f"&destination={DESTINATION}&currency=usd&departure_at={DATE}&group_by=departure_at&token={TOKEN}")
    response = requests.get(url=url)
    src = response.json()

    with open('grouped_cheap_flights_1.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)


# ==== Cамые дешевые авиабилеты на определённые даты ====
def get_prices_for_dates(url):
    """
    :currency: — валюта цен на билеты. Значение по умолчанию — rub.
    :origin: — пункт отправления. IATA-код города или аэропорта. Длина не менее двух и не более трёх символов.
                Необходимо указать, если нет destination.
    :destination: — пункт назначения. IATA-код города или аэропорта. Длина не менее двух и не более трёх.
                    Необходимо указать, если нет origin.
    :departure_at: (необязательно)— дата вылета из пункта отправления (в формате YYYY-MM или YYYY-MM-DD).
    :return_at: (необязательно) — дата возвращения. Чтобы получить билеты в один конец, оставьте это поле пустым.
    :one_way: (необязательно) — билет в одну сторону. Принимает значения true или `false`. По умолчанию `true`.
                                При значении true возвращает 1 билет. Используйте значение false, чтобы получить больше предложений.
    :direct: — получить рейсы без пересадок. Принимает значения `true` или `false`. По умолчанию `false`.
    :market: — задаёт маркет источника данных (по умолчанию ru).
    :limit: — количество записей в ответе. Значение по умолчанию — 30. Не более 1000.
    :page: — номер страницы. Используется, чтобы пропустить первые записи.
             То есть, выдача будет отдавать билеты в диапазоне [(page — 1) * limit; page * limit].
             Таким образом, если мы хотим получить билеты с 100 по 150, то мы должны установить page=3, а limit=50.
    :sorting: — сортировка цен:
        :price: — по цене (значение по умолчанию).
        :route: — по популярности маршрута.
    :unique: — возвращает только уникальные направления, если был указан `:origin`, но не указан `:destination`.
               Позволяет собрать топ самых дешевых билетов из указанного города. Принимает значения `true` или `false`.
               По умолчанию `false`.

    """
    response = requests.get(url=url)
    src = response.json()

    with open('prices_for_dates.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)


def main():
    orig = input("Город отправления: ")
    destin = input("Город прибытия: ")
    departure_at = input("Дата выезда (в формате YYYY-MM или YYYY-MM-DD): ")
    return_at = input("Дата возвращения (в формате YYYY-MM или YYYY-MM-DD): ")

    origin_from, destination_at = get_search_city(origin=orig, destination=destin)
    # get_grouped_cheap_flights(
    #     f"https://api.travelpayouts.com/aviasales/v3/grouped_prices?origin={ORIGIN}"
    #     f"&destination={DESTINATION}&currency=usd&departure_at={DEPARTURE}&group_by=departure_at&token={TOKEN}"
    # )
    get_prices_for_dates(
        f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin={origin_from}"
        f"&destination={destination_at}&departure_at={departure_at}&return_at={return_at}&token={TOKEN}"
    )


if __name__ == '__main__':
    main()
