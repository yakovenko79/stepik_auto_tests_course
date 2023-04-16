from selenium import webdriver
from selenium.webdriver.common.by import By



link = "https://stepik.org/lesson/236895/step/1"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



