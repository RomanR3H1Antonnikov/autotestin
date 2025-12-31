import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Импорт используемых библиотек

# Настройка драйвера
options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))
base_url = "https://www.saucedemo.com/" #Тестовый сайт для Selenium
driver.get(base_url)
driver.set_window_size(1920, 1080) # Настройка разрешения монитора

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys('standard_use')
print("input Login")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys("secret_sauce")
print("Input Password")

button_login = driver.find_element(By.XPATH, "//input[@id='login-button']") #находим с помощью составления кастомного локатора id
button_login.click() # нажимаем на кнопку с помощью метода click()
print("Click Login Button")

time.sleep(5) #задержка выполнения кода на 5 секунд
driver.refresh() #обновление страницы