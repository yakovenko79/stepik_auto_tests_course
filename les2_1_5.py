import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "https://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(LINK)

x = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap").text


def calc(w):
    return math.log(abs(12 * math.sin(int(w))))


try:
    browser.find_element(By.CSS_SELECTOR, "input#answer.form-control").send_keys(calc(x))
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule.form-check-input").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()


