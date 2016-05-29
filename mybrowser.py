from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def initBrowser():
    browser = webdriver.Chrome()
    # browser = webdriver.Firefox()
    # browser.wait = WebDriverWait(browser, 3)
    browser.set_window_size(800, 1000)
    browser.set_window_position(0, 0)

    # esperar si elements no available immediatament
    browser.implicitly_wait(1)

    return browser
