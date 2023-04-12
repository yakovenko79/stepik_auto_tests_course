import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

LINK = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(LINK)

treasure = browser.find_element(By.ID, "treasure")
treasure_value = treasure.get_attribute("valuex")


def calc(w):
    return math.log(abs(12 * math.sin(int(w))))


try:
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(calc(treasure_value))
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
