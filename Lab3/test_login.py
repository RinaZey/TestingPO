import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def setup_browser():
    """Универсальный запуск Chrome для локали и CI."""
    opts = Options()
    # Хедлесс и стабильные флаги для GitHub Actions
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=opts)

    # Локально можно разворачивать окно (в CI это ломается)
    if os.getenv("GITHUB_ACTIONS") != "true":
        try:
            driver.maximize_window()
        except Exception:
            pass

    return driver


def test_login_success():
    """Ввод валидных credentials на странице логина и проверка успешного входа"""
    driver = setup_browser()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(2)

    assert "Logout" in driver.page_source

    driver.quit()


def test_login_fail():
    """Ввод невалидных credentials на странице логина и проверка вывода ошибки"""
    driver = setup_browser()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("wronguser")
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(2)

    assert "Your username is invalid!" in driver.page_source

    driver.quit()
