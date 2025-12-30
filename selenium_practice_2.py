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

# Заполнение полей с помощью метода send_keys с поиском полей по ID
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("visual_user")
user_password = driver.find_element(By.ID, "password")
user_password.send_keys("secret_sauce")
button_login = driver.find_element(By.ID, 'login-button')
button_login.click() # Используем метод .click() для авторизации на сайте