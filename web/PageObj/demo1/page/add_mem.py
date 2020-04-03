from selenium.webdriver.common.by import By

from web.PageObj.demo1.page.base import BasePage
import time

class AddMem(BasePage):

    _base_url = ''

    def add_mem(self):
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,'#username').send_keys('test')
        self.driver.find_element(By.CSS_SELECTOR,'#memberAdd_acctid').send_keys('tester')
        self.driver.find_element(By.CSS_SELECTOR,'#memberAdd_mail').send_keys('awl18565151938@163.com')
        self.driver.execute_script('document.documentElement.scrollTop=0')
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//form[@class="js_member_editor_form"]/div[1]/a[2]').click()

    def get_new_mem(self):
        time.sleep(5)
        mems = self.driver.find_elements(By.CSS_SELECTOR,'#member_list tr')
        mem = ''
        for item in mems:
            if item.find_element(By.XPATH, './td[2]/span').text == '艾文龙':
                continue
            mem = item.find_element(By.XPATH, './td[2]/span')
        return mem

    def clean_environment(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//form[@class="js_member_editor_form"]/div[1]/a[3]').click()
        time.sleep(5)
        mems = self.driver.find_elements(By.CSS_SELECTOR, '#member_list tr')
        for mem in mems:
            if mem.find_element(By.XPATH, './td[2]/span').text == '艾文龙':
                continue
            mem.find_element(By.XPATH, './td[1]//input').click()
        self.driver.find_element(By.XPATH, '//div[@class="js_has_member"]/div[1]//a[text()="删除"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div[1]/div[3]/a[1]').click()
