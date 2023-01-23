import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)

def funct(a):
    return str(math.log(abs(12 * math.sin(a))))


try:
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap").text)
    browser.find_element(By.CSS_SELECTOR, "#answer.form-control").send_keys(funct(x))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()

