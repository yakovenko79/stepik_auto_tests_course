import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestAut():

    def test_auth(self, browser):
        browser.get("https://stepik.org/lesson/236895/step/1")
        browser.implicitly_wait(10)
        button_auth = browser.find_element(By.CSS_SELECTOR, "nav a.navbar__auth_login")
        button_auth.click()
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("om")
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("")
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

