import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    a = browser.find_element(By.CSS_SELECTOR, "span#num1.nowrap").text
    b = browser.find_element(By.CSS_SELECTOR, "span#num2.nowrap").text
    c = int(a) + int(b)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(c))
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(20)
    browser.quit()


