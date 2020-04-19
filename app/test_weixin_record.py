import yaml
from appium import webdriver
import pytest
import time


desire_caps = {
  "platformName": "android",
  "deviceName": "111",
  "appPackage": "com.tencent.wework",
  "appActivity": ".launch.WwMainActivity",
  "noReset": "true",
  "skipDeviceInitialization": "true",
  "dontStopAppOnReset":"true",
  "unicodeKeyboard":"true"
}


class TestWX:
    def setup_class(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desire_caps)
        self.driver.implicitly_wait(50)

    #还可以将参数配置在yaml文件中，    yaml.safe_load(open('文件路径'))
    @pytest.mark.parametrize('name',['狄青','test','灰太狼'])
    def test_search(self,name):
        self.driver.find_element_by_id("com.tencent.wework:id/gq_").click()
        self.driver.find_element_by_id("com.tencent.wework:id/ffq").send_keys(name)
        self.driver.keyevent(66)
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="%s"]'%name).click()
        self.driver.find_element_by_id("com.tencent.wework:id/azc").send_keys('测试code')
        self.driver.find_element_by_id('com.tencent.wework:id/dtr').click()
        self.driver.back()
        self.driver.back()
        time.sleep(10)

    def teardown_class(self):
        print('结束')


if __name__ == '__main__':
    pytest.main()