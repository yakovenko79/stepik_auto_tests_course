import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

linx = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]


def tim():
    return str(math.log(int(time.time())))


@pytest.mark.parametrize('links', linx)
class TestAuth():

    def test_auth(self, browser, links):
        link = links
        browser.get(link)

        button_auth = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
        button_auth.click()

        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys("imresquer@gmail.com")
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("joy78963214")
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()

        browser.find_element(By.CSS_SELECTOR, "textarea.textarea").send_keys(tim())
        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))).click()
        answer = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "smart-hints__hint"))).text
        assert "Correct!" == answer, answer


if __name__ == "__main__":
    pytest.main()
