from appium import webdriver

from base.base import Base


class WeworkApp(Base):
    def start(self):
        if self.driver == None:
            print("driver == None")
            desired_cap = {}
            desired_cap["platformName"] = "Android"
            desired_cap["deviceName"] = "127.0.0.1:62001"
            desired_cap["appPackage"] = "com.tencent.wework"
            desired_cap["appActivity"] = ".launch.WwMainActivity"
            desired_cap["noReset"] = True
            desired_cap["skipServerInstallation"] = True  # 跳过uiautomarot2安装
            desired_cap["skipDeviceInitialization"] = True  # 跳过设备初始化
            desired_cap["settings[waitForIdleTimeout]"] = 0  # 等待页面完全加载完成的时间
            desired_cap["unicodeKeyBoard"] = 'true'
            desired_cap["restKeyBoard"] = 'true'
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
            self.driver.implicitly_wait(5)
        else:
            print("driver != None")
            # 启动desire里面设置的activity   热启动
            # launch 没有杀应用的操作，只是启动
            if self.driver.current_activity != "com.tencent.wework.launch.WwMainActivity":
                self.driver.launch_app()
            # 启动 给定的activity
            # self.driver.start_activity(packagename, activityname)
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.launch_app()

    def back(self, num=3):
        # 封装返回方法
        for i in range(num):
            self.driver.back()

    def goto_main(self):
        from page.main_page import MainPage
        return MainPage(self.driver)