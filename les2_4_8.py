import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

link = "http://suninjuly.github.io/explicit_wait2.html"


def funct(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


with webdriver.Chrome() as browser:
    browser.get(link)

    cost = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element(By.ID, "book").click()
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(funct(x))
    submit = WebDriverWait(browser,5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    submit.click()
    alert = browser.switch_to.alert
    print(alert.text)






