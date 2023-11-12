from selenium import webdriver
from selenium_stealth import stealth
import time
from fake_useragent import UserAgent

ua = UserAgent()

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# options.add_argument("--headless")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options, )

# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )
stealth(driver,
        user_agent=ua.random,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=False,
        run_on_insecure_origins=False,
        )

url = "https://www.zingat.com/en/for-sale"
driver.get(url)
time.sleep(30)
driver.quit()

# import os
# import time
# from platform import system
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
#
# # Как видите, здесь также импортируется класс Options, а значит, мы будем передавать в браузер параметры.
# # В данном случае передадим параметр для отключения автоматизации. Однако, на всякий случай на канале представлены
# # еще два дополнительных параметра, которые можно отключить при необходимости.
# # Python:
# options = Options()
# # options.add_argument("--headless")
# # options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # options.add_experimental_option('useAutomationExtension', False)
# options.add_argument("--disable-blink-features=AutomationControlled")
#
# # Указываем путь к драйверу и передаем опции и путь в объект браузера.
# # Python:
# exec_path = os.path.join(os.getcwd(), 'driver', 'chromedriver.exe') if system() == "Windows" else \
#     os.path.join(os.getcwd(), 'driver', 'chromedriver')
#
# driver = webdriver.Chrome(options=options, service=Service(log_path=os.devnull, ))
#
# # Теперь необходимо выполнить скрипт для удаления параметров, о которых мы говорили выше из текущего сеанса.
# # Для этого выполняем скрипт:
# # Python:
# driver.execute_cdp_cmd(
#     "Page.addScriptToEvaluateOnNewDocument", {
#         'source': '''
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
#         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
#   '''
#     })
#
# # Попытка обхода защиты
# driver.get('https://nowsecure.nl')
# time.sleep(30)
# driver.close()
# driver.quit()
#
