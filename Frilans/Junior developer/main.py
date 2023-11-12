import time
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
# options.page_load_strategy = 'none'
options.add_argument('--disable-blink-features=AutomationControlled')

# service = Service(log_path=log_path)
# service = Service(service_args=['--log-level=INFO'], log_path='log_path.log')
# service = Service(service_args=['--append-log', '--readable-timestamp'], log_path='log_path.log')
ua = UserAgent()

driver = webdriver.Chrome(options=options)
# url = "https://www.zingat.com/en/for-sale"


try:
    # driver.implicitly_wait(5)
    # driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    driver.get(url="https://www.zingat.com/en/for-sale")
    time.sleep(60)
    # driver.implicitly_wait(60)



except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
