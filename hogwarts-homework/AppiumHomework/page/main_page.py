from appium.webdriver.common.mobileby import MobileBy

from base.wework_app import WeworkApp
from page.contact_page import ContactPage


class MainPage(WeworkApp):
    _CONTACT_ELEMENT = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contact(self):
        # 点击通讯录
        self.find_click(*self._CONTACT_ELEMENT)
        return ContactPage(self.driver)