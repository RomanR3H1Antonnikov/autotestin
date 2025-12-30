from dbm import error

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from sqlalchemy import values
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from websocket import warning

# Импорт используемых библиотек

# Настройка драйвера
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--headless") # Добавляем опцию для открытия браузера в тестовом режиме

driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
base_url = "https://www.saucedemo.com/" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

# Заполнение полей с помощью метода send_keys с поиском полей по ID
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("visual_user")
print("Input Login") #сообщение в консоль об успешном вводе логина
user_password = driver.find_element(By.ID, "Incorrect_password")
user_password.send_keys("secret_sauce")
print("Input Password") #сообщение в консоль об успешном вводе пароля (неправильного)
button_login = driver.find_element(By.ID, 'login-button')
button_login.click() # Используем метод .click() для авторизации на сайте
print("Click Login Button") #сообщение в консоль об успешном нажатии на кнопку логина
warning_text = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warning_text = warning_text.text
assert  value_warning_text == "Epic sadface: Username and password do not match any user in this service" # берём строго текст с помощью DevTools
print("Сообщение корректно")
error_button = driver.find_element(By.XPATH, "//button[@button='error-button']") # находим крестик с помощью кастомного локатора класса
error_button.click()
print("Click Error Button") #сообщение в консоль об успешном нажатии на кнопку закрытия сообщения об ошибке
