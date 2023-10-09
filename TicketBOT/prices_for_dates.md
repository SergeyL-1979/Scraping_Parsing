## ==== Cамые дешевые авиабилеты на определённые даты ====
    def get_prices_for_dates()
### Поля ответа

* success — результат запроса.
* data — полученные данные:
    - origin — пункт отправления.
    - destination — пункт назначения.
    - origin_airport — IATA-код аэропорта отправления.
    - destination_airport — IATA-код аэропорта прибытия.
    - price — стоимость билета.
    - airline — IATA-код авиакомпании.
    - flight_number — номер рейса.
    - departure_at — дата отправления.
    - return_at — дата возвращения.
    - transfers — количество пересадок на пути «туда».
    - return_transfers — количество пересадок на пути «обратно».
    - duration — общая продолжительность перелёта туда-обратно в минутах.
    - duration_to — продолжительность перелёта до места назначения в минутах.
    - duration_back — продолжительность перелёта обратно в минутах.
    - link — ссылка на билет. Добавьте этот код к адресу https://www.aviasales.ru/, 
      чтобы открыть результаты поиска по данному направлению на сайте Авиасейлс. 
      Чтобы сделать из ссылки партнёрскую, используйте форму создания ссылок.
    - currency — валюта, в которой отображается цена на билеты.

### Как можно заменить старые запросы

    /v1/prices/cheap — выставить параметры direct=false и sorting=price.
    /v1/prices/direct — выставить параметры direct=true и sorting=price.
    /v1/city-directions — выставить параметры sorting=route и unique=true. Передавать только origin.


        f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin={ORIGIN}"
        f"&destination={DESTINATION}&departure_at={DEPARTURE}&return_at={RETURN}&unique=false&sorting=price"
        f"&direct=false&cy=rub&limit=30&page=1&one_way=true&token={TOKEN}"