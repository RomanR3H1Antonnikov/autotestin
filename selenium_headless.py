from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from sqlalchemy import values
from webdriver_manager.microsoft import EdgeChromiumDriverManager
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
user_password = driver.find_element(By.ID, "password")
user_password.send_keys("secret_sauce")
print("Input Password") #сообщение в консоль об успешном вводе пароля
button_login = driver.find_element(By.ID, 'login-button')
button_login.click() # Используем метод .click() для авторизации на сайте
print("Click Login Button") #сообщение в консоль об успешном нажатии на кнопку логина
print(driver.current_url)
get_url = driver.current_url #сохраняем URL-адрес сайта, на котором мы оказались после нажатия на кнопку
url = 'https://www.saucedemo.com/inventory.html'
assert url == get_url # проверка открытой после нажатия страницы
print("URL корректен") #сообщение в консоль об корректности URL-адреса
text_products = driver.find_element(By.XPATH, "//span[@class='title']") #поиск локатора класса с помощью кастомного XPATH
print(text_products.text)
value_text_products = text_products.text # Берём только текст в отдельную переменную
assert value_text_products == "Products" # проверка соответствия текста
print("Заголовок корректен")