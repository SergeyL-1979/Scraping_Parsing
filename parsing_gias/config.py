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
import math

text = 'Всего 809 записей'
count = text[5:9:1]


# page = 809
limit = 40
result = math.ceil(int(count) / limit)
print(result)
