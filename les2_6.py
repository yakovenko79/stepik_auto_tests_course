import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


def funct(a):
    return str(math.log(abs(12 * math.sin(a))))


try:
    x = browser.find_element(By.ID, "input_value").text
    f = funct(int(x))
    field = browser.find_element(By.CSS_SELECTOR, "input#answer.form-control")
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    field.send_keys(f)
    browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "input#robotsRule").click()
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(10)
    browser.quit()




