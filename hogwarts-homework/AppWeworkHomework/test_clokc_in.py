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
        desired_cap["dontStopAppOnReset"] = True  # 等待页面完全加载完成的时间

        self.drive = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
        self.drive.implicitly_wait(5)

    def teardown(self):
        self.drive.quit()

    def swipe_find(self, by_method, ele, num=3):
        # 滑动查找元素
        for i in range(num):
            try:
                rst_ele = self.drive.find_element(by_method, ele)
                return rst_ele
            except:
                windows_size = self.drive.get_window_size()
                width = windows_size.get('width')
                height = windows_size.get('height')

                start_width = width / 2
                start_height = height * 0.8
                end_width = width / 2
                end_height = height * 0.3

                self.drive.swipe(start_width, start_height, end_width, end_height)

    def test_add_member(self):
        self.drive.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滑动查找打卡选项
        # self.drive.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                'scrollable(true).instance(0)).'
        #                                                f'scrollIntoView(new UiSelector().text("打卡")'
        #                                                ');').click()
        # self.drive.find_element(MobileBy.XPATH, "//*[@text='打卡']").click()
        self.swipe_find(MobileBy.XPATH, "//*[@text='打卡']").click()

        # self.drive.update_settings({"waitForIdleTimeout": 0})  # driver方法更新等待页面完全加载完成的时间
        self.drive.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.drive.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()

        self.drive.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")



        # while True:
        #     current_xml = self.drive.page_source
        #     if "添加成功" in current_xml:
        #         print(current_xml)
        #         break
