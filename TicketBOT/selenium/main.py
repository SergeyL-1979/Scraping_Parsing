import time
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


useragent = UserAgent()
# url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"


def get_data_with_selenium(url):
    service = Service(executable_path='geckodriver')
    ops = webdriver.FirefoxOptions()
    ops.set_preference("general.useragent.override", useragent.random)
    ops.set_preference("dom.webdriver.enabled", False)
    # ops.set_preference('dom.webnotifications.enabled', False)
    ops.set_preference('useAutomationExtension', False)

    driver = webdriver.Firefox(service=service, options=ops)

    try:
        driver.get(url=url)
        time.sleep(10)

        # items_url = driver.find_elements(By.LINK_TEXT, "href")
        # items_url[0].click()

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    # get_data_with_selenium("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    get_data_with_selenium("https://bot.sannysoft.com/")


if __name__ == '__main__':
    main()
