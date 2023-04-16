import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)
    req_elements = browser.find_elements(By.CSS_SELECTOR, "input:required")
    for element in req_elements:
        element.send_keys("blablabla")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)
    return browser.find_element(By.TAG_NAME, "h1").text


class TestStep1(unittest.TestCase):
    def test_page1(self):
        self.assertEqual(fill_form("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!",
                         "registration is failed")

    def test_page2(self):
        self.assertEqual(fill_form("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!",
                         "registration is failed")


if __name__ == "__main__":
    unittest.main()
