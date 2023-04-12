# pytest --language=es test_items2.py
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


def test_product_page_has_add_to_cart_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    try:
        browser.find_element(By.CSS_SELECTOR, "[class='btn btn-lg btn-primary btn-add-to-basket']")
        button_presented = True
    except NoSuchElementException:
        button_presented = False
    assert button_presented, 'Element not found'
