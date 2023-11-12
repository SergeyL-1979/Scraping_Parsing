from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

# options = webdriver.ChromeOptions()
options = Options()
options.add_argument('--disable-blink-features=AutomationControlled')

url = "https://www.zingat.com/en/for-sale"
# url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"

# service = Service(executable_path="/home/fpw/PycharmProjects/Parsing/Frilans/chromedriver/chromedriver")
driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    driver.get(url=url)
    time.sleep(10)

    items_url = driver.find_elements(By.LINK_TEXT, "href")
    items_url[0].click()


except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

