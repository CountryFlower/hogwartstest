import time
from selenium.webdriver.common.by import By

from web.PageObj.demo1.page.add_mem import AddMem
from web.PageObj.demo1.page.base import BasePage



class IndexPage(BasePage):

    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_mem(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@class="index_service_cnt_item"]').click()
        return AddMem(self.driver)