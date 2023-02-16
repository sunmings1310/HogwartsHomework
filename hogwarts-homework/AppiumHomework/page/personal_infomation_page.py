from appium.webdriver.common.mobileby import MobileBy

from base.wework_app import WeworkApp
from page.edit_member_page import EditMemberPage


class PersonalInformationPage(WeworkApp):
    _PERSONAL_INFORMATION_SETTING_ELEMENT = (MobileBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::*[1]")
    _EDIT_MEMBER_ELEMENT = (MobileBy.XPATH, "//*[@text='编辑成员']")


    def goto_edit_member_page(self):
        self.find_click(*self._PERSONAL_INFORMATION_SETTING_ELEMENT)
        self.find_click(*self._EDIT_MEMBER_ELEMENT)
        return EditMemberPage(self.driver)