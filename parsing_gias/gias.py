import requests
import requests_cache
import csv
import json
from datetime import datetime
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium_stealth import stealth
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent

from parsing.model import Result

ua = UserAgent()

options = webdriver.ChromeOptions()
# options = Options()
# options.add_argument("start-maximized")
# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
# options.add_argument('--disable-blink-features=AutomationControlled')

# run in headless mode
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
# stealth(driver,
#         user_agent=ua.random,
#         languages=["en-US", "en"],
#         # vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=False,
#         run_on_insecure_origins=False,
#         )
stealth(driver,
        user_agent=ua.random,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )


def get_data_json():
    try:
        # driver.implicitly_wait(5)
        driver.get(url="https://gias.by/gias/#/purchase/current?extended")
        # time.sleep(5)
        # # driver.implicitly_wait(60)
        # driver.find_element(By.XPATH,
        #                     '//*[@id="root"]/div/section/section/main/div/div/div/div/div/div[1]/div/a[2]/span').click()
        time.sleep(5)

        search = driver.find_element(
            By.XPATH, '//*[@id="contextTextSearch"]')
        search.send_keys('ультразвуковой')
        driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div['
                                      '1]/div/div/span/span/span/span/button').click()
        # driver.implicitly_wait(10)
        time.sleep(5)

        # ================================= ВЫБОР ОТРАСЛИ И ЕЕ ВИДЫ ===================================================
        # 1 выбрать Виды отрасли
        clickable = driver.find_element(By.XPATH,
                                        '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/form/div['
                                        '3]/div[6]/div/div[2]/div/span/span/span/ul')
        ActionChains(driver).click(clickable).perform()
        time.sleep(5)
        # driver.implicitly_wait(10)

        # 2 выбрать отрасль МЕДИЦИНА
        industry_selection = driver.find_element(By.XPATH, '//*[@id="rc-tree-select-list_1"]/ul/li[19]/span[1]')
        ActionChains(driver).click(industry_selection).perform()
        time.sleep(5)
        # driver.implicitly_wait(10)

        # 3 выбрать Медицинский инструмент
        medical_instrument = driver.find_element(By.XPATH,
                                                 '//*[@id="rc-tree-select-list_1"]/ul/li[19]/ul/li[5]/span[2]')
        ActionChains(driver).click(medical_instrument).perform()
        time.sleep(5)
        # driver.implicitly_wait(15)

        # 4 выбрать Медицинское оборудование / комплектующие
        medical_equipment = driver.find_element(By.XPATH,
                                                '//*[@id="rc-tree-select-list_1"]/ul/li[19]/ul/li[6]/span[2]/span')
        ActionChains(driver).click(medical_equipment).perform()
        time.sleep(5)
        # driver.implicitly_wait(15)

        # 5 выбрать Расходные материалы
        сonsumables = driver.find_element(By.XPATH,
                                          '//*[@id="rc-tree-select-list_1"]/ul/li[19]/ul/li[7]/span[2]/span')
        ActionChains(driver).click(сonsumables).perform()
        time.sleep(5)
        # driver.implicitly_wait(15)
        # =============================================================================================================

        # ================= ВЫБОР. В поле «Статус закупки (лота)» выбрать статус «Договор подписан» ===================
        procurement_status = driver.find_element(By.XPATH, '//*[@id="purchaseState"]/div/div')
        ActionChains(driver).click(procurement_status).perform()
        time.sleep(5)

        contract_is_signed = driver.find_element(By.XPATH, '//span[text()="Договор подписан"]')
        # contract_is_signed.send_keys('Договор подписан')
        ActionChains(driver).click(contract_is_signed).perform()
        time.sleep(5)
        # =============================================================================================================

        # =========================================== ПАГИНАЦИЯ ========================================================
        page = driver.find_element(By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div['
                                             '2]/div/div/ul/li[11]/div[1]/div/div/div')
        # page = driver.find_element(By.XPATH, '//*[@id="b23b68aa-e0db-41fd-b4c2-3de0957d8c4b"]/ul/li[4]')
        ActionChains(driver).click(page).perform()
        time.sleep(5)

        page_count = driver.find_element(By.XPATH, '//li[text()="40 / стр."]')
        ActionChains(driver).click(page_count).perform()
        time.sleep(5)
        # =============================================================================================================

        # ============= НАЙТИ КОЛИЧЕСТВО ЗАПИСЕЙ =================
        # count_pages = driver.page_source
        # soup = BeautifulSoup(count_pages, 'lxml')

        # page_item = soup.find(class_='ant-pagination-total-text').text
        page_item = driver.find_element(
            By.XPATH,
            '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/ul/li[1]/span'
        ).text[5:9:1]

        print(page_item)

        # ============================================== СБОР ДАННЫХ ==================================================
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        with open('page_1.html', 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        # =============================================================================================================

        # ======================================= СБОР ДАННЫХ СО СТРАНИЦ ==============================================
        page_next = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/section/section/main/div/div[2]/div/div/div/div[2]/div/div/ul/li[10]'
        )
        ActionChains(driver).click(page_next).perform()
        time.sleep(15)

        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        with open('page_2.html', 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        # =============================================================================================================




    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def create_csv():
    t_date = datetime.now().strftime('%d_%m_%Y')

    with open(f'result_{t_date}.csv', 'a', encoding='utf-8', newline='') as file:
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
    get_data_json()
    # get_csv()


if __name__ == '__main__':
    main()

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
