import time
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    _base_url = ''

    def __init__(self,driver:WebDriver=None):
        self.driver = ''
        if driver is None:
            option = webdriver.ChromeOptions()
            option.debugger_address = '127.0.0.1:9999'
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver = driver
        if self._base_url != '':
            time.sleep(5)
            self.driver.get(self._base_url)
            self.driver.implicitly_wait(10)
