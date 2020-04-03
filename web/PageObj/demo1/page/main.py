import json
import time

from web.PageObj.demo1.page.index import IndexPage
from web.PageObj.demo1.page.base import BasePage


class MainPage(BasePage):

    _base_url = 'https://work.weixin.qq.com/'

    def goto_login(self):
        pass

    def login_by_cookie(self):
        # time.sleep(5)
        # with open('../page/work_wx.txt','r') as f:
        #     cookies = json.load(f)
        #     for cookie in cookies:
        #         if 'expiry' in cookie:
        #             cookie.pop('expiry')
        #         self.driver.add_cookie(cookie)
        return IndexPage(self.driver)