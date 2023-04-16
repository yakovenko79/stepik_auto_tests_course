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


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', linx)


    def test_auth(self, browser, links):
        link = links
        browser.get(link)
        time.sleep(10)
        button_auth = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
        button_auth.click()
        browser.find_element(By.CSS_SELECTOR, "#id_login_email").send_keys(".com")
        browser.find_element(By.CSS_SELECTOR, "#id_login_password").send_keys("")
        browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn").click()
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "textarea.textarea").send_keys(str(math.log(int(time.time()))))
        time.sleep(5)
        browser.find_element(By.CSS_SELECTOR, "button.submit-submission").click()
        time.sleep(5)
        answer = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text

        assert answer == "Correct!", f"part of answer {answer}"


if __name__ == "__main__":
    pytest.main()
