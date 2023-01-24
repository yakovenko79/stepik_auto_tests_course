import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStep1(unittest.TestCase):
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()

    def test_page1(self):
        self.browser.get(self.link1)
        self.browser.find_element(By.CSS_SELECTOR, "input.first:required").send_keys("Ivan")
        self.browser.find_element(By.CSS_SELECTOR, "input.second:required").send_keys("Ivanoff")
        self.browser.find_element(By.CSS_SELECTOR, "input.third:required").send_keys("aaa@aaa.aa")
        self.browser.find_element(By.CSS_SELECTOR, "button.btn").click()


    def test_page(self):
        self.browser.get(self.link2)
        self.browser.
