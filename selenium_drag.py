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
user_name.send_keys('standard_user')
print("input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']") # используем кастомный XPATH для поиска локатора поля
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']") # используем кастомный XPATH для поиска локатора кнопки
button_login.click() # Используем метод .click() для авторизации на сайте
print("Login Button Clicked")

#с помощью кастомного локатора XPATH добавляем все товары в корзину
button_add_backpack = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-backpack']").click()
button_add_bike_light = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']").click()
button_add_t_shirt = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
button_add_jacket = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']").click()
button_add_onesie = driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-onesie']").click()
button_add_red_t_shirt = driver.find_element(By.XPATH, "//*[@id='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
button_cart_link = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click() # переходим в корзину

actions = ActionChains(driver) # создаём экземпляр класса, с помощью которого мы будем перемещаться по странице
element = driver.find_element(By.ID, "item_3_title_link") # выбираем элемент с помощью ID
actions.move_to_element(element).perform() # с помощью move_to_element и perform перемещаемся к выбранному элементу и отмечаем/выделяем его невидимым курсором