import time

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

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys('standard_user')
print("input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']") #находим с помощью составления кастомного локатора id
button_login.click() # нажимаем на кнопку с помощью метода click()
print("Click Login Button")

menu = driver.find_element(By.XPATH, "//*[@id='react-burger-menu-btn']").click()
time.sleep(1) # ждём, пока закончится анимация открытия окна
logout_button = driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click() # совершаем логаут по кнопке в скрытом меню

get_url = driver.current_url # получаем текущий url для проверки логаута
url = 'https://www.saucedemo.com/'
assert url == get_url, f"Ошибка логаута! Мы ожидали {url}, а получили {get_url}"
print("URL корректен и совпадает, выход из аккаунта прошёл успешно")