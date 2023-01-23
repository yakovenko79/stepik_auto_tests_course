import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    browser.find_element(By.CSS_SELECTOR, '[placeholder = "Enter first name"]').send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, '[placeholder = "Enter last name"]').send_keys("Ivanoff")
    browser.find_element(By.CSS_SELECTOR, '[placeholder = "Enter email"]').send_keys("Ivan@ivan.iv")
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element.send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    time.sleep(15)
    browser.quit()
