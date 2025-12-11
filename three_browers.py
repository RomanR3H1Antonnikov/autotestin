import time
from webbrowser import Chrome

from selenium import webdriver
# Импорты библиотек для браузера Microsoft Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# Импорт используемых библиотек для браузера Google Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
# Импорт библиотек для браузера Mozilla Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# открытие в браузере Edge
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
base_url = "https://www.saucedemo.com/" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настойка разрешения монитора
time.sleep(10)
driver.close()

# открытие в браузере Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://www.saucedemo.com/" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настойка разрешения монитора
time.sleep(10)
driver.close()

# открытие в браузере Firefox
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
base_url = "https://www.saucedemo.com/" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настойка разрешения монитора
time.sleep(10)
driver.close()