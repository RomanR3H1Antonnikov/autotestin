from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

# Импорт используемых библиотек

# Настройка драйвера
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
base_url = "https://www.saucedemo.com/" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") # используем кастомный XPATH для поиска локатора поля
user_name.send_keys('standartt_use')
print("input Incorrect Login")

password = driver.find_element(By.XPATH, "//input[@id='password']") # используем кастомный XPATH для поиска локатора поля
password.send_keys("no_secret_sauce")
print("Input Incorrect Password")

user_name.send_keys(Keys.CONTROL + "a") # имитируем ввод с клавиатуры (сочетание Ctrl + A)
user_name.send_keys(Keys.DELETE)  # имитируем ввод с клавиатуры (кнопка Delete)
password.send_keys(Keys.CONTROL + "a") # имитируем ввод с клавиатуры (сочетание Ctrl + A)
password.send_keys(Keys.DELETE)  # имитируем ввод с клавиатуры (кнопка Delete)

user_name.send_keys('standard_user')
print("input correct Login")
password.send_keys("secret_sauce")
print("Input correct Password")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']") # используем кастомный XPATH для поиска локатора кнопки
button_login.click() # Используем метод .click() для авторизации на сайте
print("Login Button Clicked")
