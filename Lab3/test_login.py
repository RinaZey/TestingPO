from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


def setup_browser():
    """Запуск браузера (чтобы не повторять код в каждом тесте)."""
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def test_login_success():
    """Ввод валидных credentials на странице логина и проверка успешного входа"""
    driver = setup_browser()
    driver.get("https://the-internet.herokuapp.com/login")

    # Ввод правильных данных
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(2)

    # Проверка наличия кнопки Logout
    assert "Logout" in driver.page_source

    driver.quit()


def test_login_fail():
    """Ввод невалидных credentials на странице логина и проверка вывода ошибки"""
    driver = setup_browser()
    driver.get("https://the-internet.herokuapp.com/login")

    # Ввод неправильных данных
    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(2)

    # Проверка наличия текста ошибки
    assert "Your username is invalid!" in driver.page_source

    driver.quit()
