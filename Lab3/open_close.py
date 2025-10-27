from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# создаём объект Service, так как выдаёт ошибку, что webdriver-manager нельзя просто так передавать путь в webdriver.Chrome()
service = Service(ChromeDriverManager().install())

# Запуск браузера
driver = webdriver.Chrome(service=service)

# Открытие страницы гугл
driver.get("https://www.google.com")

# Закрытие браузера
driver.quit()
