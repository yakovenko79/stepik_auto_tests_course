import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

LINK = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(LINK)


def summa(a, b):
    return int(a) + int(b)


try:
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    sel = Select(browser.find_element(By.CSS_SELECTOR, "select#dropdown"))
    sel.select_by_visible_text(str(summa(num1, num2)))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()

