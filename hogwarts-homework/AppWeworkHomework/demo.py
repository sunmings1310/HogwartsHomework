from appium import webdriver
from selenium.webdriver.common.by import By


class WeworkTest:
    def __init__(self):
        desired_cap = {}
        desired_cap["platformName"] = "Android"
        # desired_cap["platformVersion"] = "6.0"
        desired_cap["deviceName"] = "127.0.0.1:62001"
        desired_cap["appPackage"] = "com.tencent.wework"
        desired_cap["appActivity"] = ".launch.WwMainActivity"
        desired_cap["noReset"] = True
        desired_cap["skipServerInstallation"] = True
        desired_cap["unicodeKeyBoard"] = 'true'
        desired_cap["restKeyBoard"] = 'true'
        self.drive = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.drive.implicitly_wait(5)

    def add_member(self):
        self.drive.find_element(By.XPATH, "//*[@text='通讯录']").click()
        self.drive.find_element(By.XPATH, "//*[@text='添加成员']").click()
        self.drive.find_element(By.XPATH, "//*[@text='手动输入添加']").click()
        self.drive.find_element(By.ID, 'com.tencent.wework:id/b0_').send_keys('石页')
        self.drive.find_element(By.ID, 'com.tencent.wework:id/f85').send_keys('18729384716')
        self.drive.find_element(By.XPATH, "//*[@text='保存']").click()

if __name__ == '__main__':
    ww = WeworkTest()
    ww.add_member()