from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket(browser):
    browser.get(link)
    time.sleep(10)
    browser.find_element(By.XPATH, '//*[@id="add_to_basket_form"]/button')
    assert test_basket, f'Страница товара на сайте {link} не содержит кнопки добавления в корзину'
