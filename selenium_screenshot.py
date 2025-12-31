import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Импорт используемых библиотек

# Настройка драйвера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://www.saucedemo.com/" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

user_name = driver.find_element(By.ID, "user-name") # поиск локатора поля ввода имени пользователя по ID
user_name.send_keys('standard_user')
print("input Login")

password = driver.find_element(By.ID, "password") # поиск локатора поля ввода пароля по ID
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.ID, "login-button") # поиск локатора кнопки по ID
button_login.click() # Используем метод .click() для авторизации на сайте
print("Login Button Clicked")

time.sleep(3) # ждём 3 секунды для подгрузки сайта

now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S") # получаем точное время в определённом формате, заключаем его в переменную now_date
name_screenshot = "screenshot" + now_date + ".png" # формируем название скриншота с помощью конкатенации строк и переменной now_date
driver.save_screenshot("D:\\Programming\\Selenium_1\\screen_directory\\" + name_screenshot) #помещаем скриншот в нужную директорию и добавляем сформированное название