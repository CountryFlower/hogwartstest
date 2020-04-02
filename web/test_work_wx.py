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
        time.sleep(5)
        #获取cookie
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        time.sleep(10)
        self.driver.implicitly_wait(10)

        cookies:list(dict) = self.driver.get_cookies()
        with open('work_wx.txt','w') as f:
           json.dump(cookies,f)

        with open('work_wx.txt','r') as f:
            cookies = json.load(f)
            for cookie in cookies:
                if 'expiry' in cookie:
                    cookie.pop('expiry')
                self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        wait = WebDriverWait(self.driver,30)
        # #index页的添加成员
        # wait.until(lambda driver: driver.find_element(By.XPATH,'//*[@class="index_service_cnt_item"]')).click()
        wait.until(lambda driver: driver.find_element(By.CSS_SELECTOR, '#menu_contacts')).click()
        # 通讯录页的添加成员
        add_mem = self.driver.find_element(By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
        add_mem.click()