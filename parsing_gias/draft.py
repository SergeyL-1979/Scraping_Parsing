# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# driver = webdriver.Chrome()
# driver.get('https://gias.by/gias/')
#
# html = driver.page_source
# soup = BeautifulSoup(html, 'lxml')
#
# with open('page.html', 'w', encoding='utf-8') as file:
#     file.write(soup.prettify())
#
#
# driver.close()
# driver.quit()
# import math
#
# text = 'Всего 809 записей'
# count = text[5:9:1]
#
#
# # page = 809
# limit = 40
# result = math.ceil(int(count) / limit)
# print(result)


# def read_file():
#     with open(f'page_1.html', 'r', encoding='utf-8') as file:
#         data_html = file.read()
#     links = []
#     soup = BeautifulSoup(data_html, 'lxml')

    # for link in soup.find('tbody', class_='ant-table-tbody').find_all('a'):
    #     href = link.get('href')
    #     links.append({'href': href})
    # for t in links:
    #     print(f"https://gias.by/gias/{t['href']}")
# data_row_key = soup.find('tbody', class_='ant-table-tbody')
# data_row = [td.text.strip() for td in data_row_key.find_all('td')]
# print(data_row[0])
# print(data_row[1])
# print(data_row[2])
# print(data_row[3])
# print(data_row[4])
# print(data_row[5])
# for d in data_row:
#     data_rows.append({
#         'name': d[0],
#         'address': d[1],
#         'number': d[2],
#         'price': d[3],
#         'none': d[4]
#     })
# print(data_rows)

# block = soup.find_all('tr', class_='ant-table-row-level-0')
# print(len(block))
# for i in block:
#     try:
#         print(i.get('data-row-key'), i.text)
#     except Exception as e:
#         print(i, ':', 'Attr.: no data-row-key', '\r\n')

# for i in range(10):
#     print(i+1)
# def read_file(page_data):
#     with open(page_data, 'r', encoding='utf-8') as file:
#         data_html = file.read()
#     links = []
#     soup = BeautifulSoup(data_html, 'lxml')
#
#     for link in soup.find('tbody', class_='ant-table-tbody').find_all('a'):
#         href = link.get('href')
#         links.append({'href': href})
#
#     data = []
#     tbody = soup.find_all('tbody', class_='ant-table-tbody')
#     for tb in tbody:
#         rows = tb.find_all('tr')
#         for row in rows:
#             row_data = []
#             cols = row.find_all('td')
#             for col in cols:
#                 row_data.append(col.text.strip())
#             data.append(row_data)
#     print(data)
#
#     data_rows = []
#     for i in data:
#         data_rows.append(Result(subject_of_purchase=i[0],
#                                 customer_name=i[1],
#                                 location=i[2],
#                                 item=i[3],
#                                 estimated_cost=i[4],
#                                 closing_date_for_proposals=i[5],
#                                 region=i[2]))
#     print(data_rows)
#     write_csv(data_rows)

# data = []
# tbody = soup.find_all('tbody', class_='ant-table-tbody')
# for tb in tbody:
#     rows = tb.find_all('tr')
#     for row in rows:
#         row_data = []
#         cols = row.find_all('td')
#         for col in cols:
#             row_data.append(col.text.strip())
#         data.append(row_data)
#
# data_rows = []
# for i in data:
#     data_rows.append(Result(subject_of_purchase=i[0],
#                             customer_name=i[1],
#                             location=i[2],
#                             item=i[3],
#                             estimated_cost=i[4],
#                             closing_date_for_proposals=i[5],
#                             region=i[2]))
#
# write_csv(data_rows)
# =====================================================================================================================
# def read_file():
#     with open(f'page_1.html', 'r', encoding='utf-8') as file:
#         data_html = file.read()
#     links = []
#     soup = BeautifulSoup(data_html, 'lxml')
#
#     for link in soup.find('tbody', class_='ant-table-tbody').find_all('a'):
#         href = link.get('href')
#         links.append({'href': href})
#
#     data = []
#     tbody = soup.find_all('tbody', class_='ant-table-tbody')
#     for tb in tbody:
#         rows = tb.find_all('tr')
#         for row in rows:
#             row_data = []
#             cols = row.find_all('td')
#             for col in cols:
#                 row_data.append(col.text.strip())
#             data.append(row_data)
#     print(data)
#
#     data_rows = []
#     for i in data:
#         data_rows.append(Result(subject_of_purchase=i[0],
#                                 customer_name=i[1],
#                                 location=i[2],
#                                 item=i[3],
#                                 estimated_cost=i[4],
#                                 closing_date_for_proposals=i[5],
#                                 region=i[2]))
#     print(data_rows)
#     write_csv(data_rows)

# ============= НАЙТИ КОЛИЧЕСТВО ЗАПИСЕЙ =================
# count_pages = driver.page_source
# soup = BeautifulSoup(count_pages, 'lxml')

# page_item = soup.find(class_='ant-pagination-total-text').text
# page_item = driver.find_element(
#     By.XPATH,
#     '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/ul/li[1]/span'
# ).text[5:9:1]
#
# print(page_item)

# ============================================== СБОР ДАННЫХ ==================================================
# html = driver.page_source
# soup = BeautifulSoup(html, 'lxml')
#
# with open('page_1.html', 'w', encoding='utf-8') as file:
#     file.write(soup.prettify())
# =============================================================================================================
# result = []
# with open(f'result_1.csv', 'a', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file, delimiter=";")
#     writer.writerow(
#         (
#             "Предмет закупки",
#             "Наименование заказчика/организатора",
#             "Место нахождения",
#             "Номер",
#             "Ориентировочная стоимость",
#             "Дата окончания приема предложений",
#             "Регион",
#         )
#     )
#     writer.writerows(
#         result
#     )