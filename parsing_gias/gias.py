import csv
import time
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium_stealth import stealth

from fake_useragent import UserAgent

from parsing_gias.model import Result

ua = UserAgent()

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')

# run in headless mode = фоновый режим запуска браузера
# options.add_argument("--headless")
# disable the AutomationControlled feature of Blink rendering engine
options.add_argument('--disable-blink-features=AutomationControlled')
# disable pop-up blocking
options.add_argument('--disable-popup-blocking')
# start the browser window in maximized mode
options.add_argument('--start-maximized')
# disable extensions
options.add_argument('--disable-extensions')
# disable sandbox mode
options.add_argument('--no-sandbox')
# disable shared memory usage
options.add_argument('--disable-dev-shm-usage')
# options.add_argument(f'user-agent={ua.random}')

driver = webdriver.Chrome(options=options, )
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": ua.random})

stealth(driver,
        user_agent=ua.random,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


def get_data_selenium():
    try:
        create_csv()
        # driver.implicitly_wait(5)
        print("Вызов URL")
        driver.get(url="https://gias.by/gias/#/purchase/current?extended")
        # time.sleep(5)
        # driver.implicitly_wait(60)
        # driver.find_element(By.XPATH,
        #                     '//*[@id="root"]/div/section/section/main/div/div/div/div/div/div[1]/div/a[2]/span').click()
        time.sleep(5)

        print("Запрос в поисковике")
        search = driver.find_element(
            By.XPATH, '//*[@id="contextTextSearch"]')
        # TODO ==== сделать универсальную возможность ввода текста в поиск
        search.send_keys('ультразвуковой')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div['
                                      '1]/div/div/span/span/span/span/button').click()
        # driver.implicitly_wait(10)
        time.sleep(5)

        # ================================= ВЫБОР ОТРАСЛИ И ЕЕ ВИДЫ ===================================================
        # TODO === сделать возможность выбора отрасли и ее видов
        # 1 !!!!!!!выбрать Виды отрасли
        clickable = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div['
                                        '3]/div[6]/div/div[2]/div/span/span/span/ul')
        ActionChains(driver).click(clickable).perform()
        time.sleep(5)
        # driver.implicitly_wait(10)

        # 2 !!!!!!!выбрать отрасль МЕДИЦИНА
        industry_selection = driver.find_element(By.XPATH, '//*[@id="rc-tree-select-list_1"]/ul/li[19]/span[1]')
        ActionChains(driver).click(industry_selection).perform()
        time.sleep(5)
        # driver.implicitly_wait(10)

        # 3 !!!!!!!выбрать Медицинский инструмент
        medical_instrument = driver.find_element(By.XPATH,
                                                 '//*[@id="rc-tree-select-list_1"]/ul/li[19]/ul/li[5]/span[2]')
        ActionChains(driver).click(medical_instrument).perform()
        time.sleep(5)
        # driver.implicitly_wait(15)

        # 4 !!!!!!!выбрать Медицинское оборудование / комплектующие
        medical_equipment = driver.find_element(By.XPATH,
                                                '//*[@id="rc-tree-select-list_1"]/ul/li[19]/ul/li[6]/span[2]/span')
        ActionChains(driver).click(medical_equipment).perform()
        time.sleep(5)
        # driver.implicitly_wait(15)

        # 5 !!!!!!!выбрать Расходные материалы
        consumables = driver.find_element(By.XPATH,
                                          '//*[@id="rc-tree-select-list_1"]/ul/li[19]/ul/li[7]/span[2]/span')
        ActionChains(driver).click(consumables).perform()
        time.sleep(5)
        # driver.implicitly_wait(15)
        # =============================================================================================================

        # ================= ВЫБОР. В поле «Статус закупки (лота)» выбрать статус «Договор подписан» ===================
        # TODO === сделать возможность выбора из поля «Статус закупки (лота)»
        procurement_status = driver.find_element(By.XPATH, '//*[@id="purchaseState"]/div/div')
        ActionChains(driver).click(procurement_status).perform()
        time.sleep(5)

        contract_is_signed = driver.find_element(By.XPATH, '//span[text()="Договор подписан"]')
        ActionChains(driver).click(contract_is_signed).perform()
        time.sleep(5)
        # =============================================================================================================

        print("Выбор количества записей на страницу")
        # =========================================== ПАГИНАЦИЯ ========================================================
        page = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div['
                                             '2]/div/div/ul/li[11]/div[1]/div/div/div')
        ActionChains(driver).click(page).perform()
        time.sleep(5)

        posts_per_page = driver.find_element(By.XPATH, '//li[text()="40 / стр."]')
        ActionChains(driver).click(posts_per_page).perform()
        time.sleep(5)
        # =============================================================================================================

        print("Начинаем сбор данных со страниц")
        # ============================ СБОР ДАННЫХ СО СТРАНИЦ ЗАПИСЬ ДАННЫХ В ФАЙЛ CSV ================================
        # TODO ==== сделать цикл и условие при котором будет окончен сбор данных при разном количестве страниц
        list_data_result = []
        for i in range(1, 22):
            html = driver.page_source
            soup = BeautifulSoup(html, 'lxml')

            data_html_pages = []
            tbody = soup.find_all('tbody', class_='ant-table-tbody')
            for tb in tbody:
                rows = tb.find_all('tr')
                for row in rows:
                    row_data = []
                    cols = row.find_all('td')
                    for col in cols:
                        row_data.append(col.text.strip())
                    data_html_pages.append(row_data)

            data_rows = []
            for i in data_html_pages:
                data_rows.append(Result(subject_of_purchase=i[0],
                                        customer_name=i[1],
                                        location=i[2],
                                        item=i[3],
                                        estimated_cost=i[4],
                                        closing_date_for_proposals=i[5],
                                        region=i[2]))

            list_data_result.extend(data_rows)
            # ========================================================================================================

            # =========== Реализовать сбор данный со страниц. Так же определить их количество ========================
            page_next = driver.find_element(
                By.CSS_SELECTOR, 'li[title="Вперед"]'
            )
            ActionChains(driver).click(page_next).perform()
            time.sleep(10)

        print(list_data_result)
        write_csv(list_data_result)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
        print("Сбор закончен")


def create_csv():
    t_date = datetime.now().strftime('%d_%m_%Y')

    with open(f'result_{t_date}.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=";")

        writer.writerow(
            (
                "Предмет закупки",
                "Наименование заказчика/организатора",
                "Место нахождения",
                "Номер",
                "Ориентировочная стоимость",
                "Дата окончания приема предложений",
                "Регион",
            )
        )


def write_csv(result: list[Result]):
    t_date = datetime.now().strftime('%d_%m_%Y')

    with open(f'result_{t_date}.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=";")
        for res in result:
            writer.writerow([
                res.subject_of_purchase,
                res.customer_name,
                res.location,
                res.item,
                res.estimated_cost,
                res.closing_date_for_proposals,
                res.region
            ])


def main():
    get_data_selenium()


if __name__ == '__main__':
    main()
