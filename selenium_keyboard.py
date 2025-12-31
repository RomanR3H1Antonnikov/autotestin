from selenium.webdriver.common.keys import Keys

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

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']") # используем кастомный XPATH для поиска локатора поля
user_name.send_keys('standard_user')
print("input Login")
user_name.send_keys(Keys.CONTROL + "a") # имитируем ввод с клавиатуры (сочетание Ctrl + A)
user_name.send_keys(Keys.DELETE)  # имитируем ввод с клавиатуры (кнопка Delete)
print("Login deleted")

password = driver.find_element(By.XPATH, "//input[@id='password']") # используем кастомный XPATH для поиска локатора поля
password.send_keys("secret_sauce")
print("Input Password")
password.send_keys(Keys.CONTROL + "a") # имитируем ввод с клавиатуры (сочетание Ctrl + A)
password.send_keys(Keys.DELETE)  # имитируем ввод с клавиатуры (кнопка Delete)
print("Password deleted")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']") # используем кастомный XPATH для поиска локатора кнопки
button_login.click() # Используем метод .click() для авторизации на сайте
print("Login Button Clicked")