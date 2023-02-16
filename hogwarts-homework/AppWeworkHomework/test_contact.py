from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By


class TestWeworkTest:
    def setup(self):
        desired_cap = {}
        desired_cap["platformName"] = "Android"
        # desired_cap["platformVersion"] = "6.0"
        desired_cap["deviceName"] = "127.0.0.1:62001"
        desired_cap["appPackage"] = "com.tencent.wework"
        desired_cap["appActivity"] = ".launch.WwMainActivity"
        desired_cap["noReset"] = True
        desired_cap["skipServerInstallation"] = True  # 跳过uiautomarot2安装
        desired_cap["skipDeviceInitialization"] = True  # 跳过设备初始化
        # desired_cap["unicodeKeyBoard"] = 'true'
        # desired_cap["restKeyBoard"] = 'true'
        desired_cap["settings[waitForIdleTimeout]"] = 0  # 等待页面完全加载完成的时间
        self.drive = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.drive.implicitly_wait(5)

    def teardown(self):
        self.drive.quit()

    def swipe_find(self, by_method, ele, num=3):
        # 滑动查找元素
        for i in range(num):
            try:
                ele = self.drive.find_element(by_method, ele)
                return ele
            except:
                print(f'第{i}次滑动')
                windows_size = self.drive.get_window_size()
                width = windows_size.get('width')
                height = windows_size.get('height')

                start_width = width / 2
                start_height = height * 0.8
                end_width = width / 2
                end_height = height * 0.3

                self.drive.swipe(start_width, start_height, end_width, end_height)

    def test_add_member(self):
        self.drive.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.swipe_find(MobileBy.XPATH, "//*[@text='添加成员']").click()
        # self.drive.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.drive.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        # self.drive.find_element(By.XPATH, "//*[@text='必填']")
        self.drive.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../*[@text="必填"]').send_keys('石页1223')
        self.drive.find_element(MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="必填"]').send_keys('18719384326')
        # self.drive.find_element(By.ID, 'com.tencent.wework:id/b0_').send_keys('石页')
        # self.drive.find_element(By.ID, 'com.tencent.wework:id/f85').send_keys('18729384716')
        self.drive.find_element(By.XPATH, "//*[@text='保存']").click()

        ele_toast = self.drive.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        rst = ele_toast.get_attribute('text')
        assert '添加成功' == rst

        # while True:
        #     current_xml = self.drive.page_source
        #     if "添加成功" in current_xml:
        #         print(current_xml)
        #         break
