import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


'''
使用复用浏览器技术获取企业微信的cookie，点击添加成员
'''
class TestWorkWX:
    def setup(self):
        #浏览器复用
        option = webdriver.ChromeOptions()
        option.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=option)

    def teardown(self):
        time.sleep(5)
        # self.driver.quit()

    def test_add_mem(self):
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx')
        self.driver.implicitly_wait(5)
        time.sleep(10)
        #获取cookie
        cookies:list(dict) = self.driver.get_cookies()
        for cookie in cookies:
            with open('work_wx.txt','a') as f:
                json.dump(cookie,f)
        wait = WebDriverWait(self.driver,10)
        # #index页的添加成员
        # wait.until(lambda driver: driver.find_element(By.XPATH,'//*[@class="index_service_cnt_item"]')).click()
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#menu_contacts')).click()
        # 通讯录页的添加成员
        wait.until(lambda driver: driver.find_element(By.XPATH, '//*[@class="ww_operationBar"]//a[text()="添加成员"]')).click()
