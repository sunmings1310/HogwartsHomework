from appium.webdriver.common.mobileby import MobileBy

from base.wework_app import WeworkApp
from page.add_member_page import AddMemberPage
from page.search_member_page import SearchMemberPage


class ContactPage(WeworkApp):
    _ADD_MEMBER_ELEMENT = (MobileBy.XPATH, "//*[@text='添加成员']")
    _SEARCH_MEMBER_ELEMENT = (MobileBy.XPATH, "//*[@text='Hogwarts']/../../../following-sibling::*/*[1]")

    def click_search_member(self):
        # 点击查找成员
        self.find_click(*self._SEARCH_MEMBER_ELEMENT)
        return SearchMemberPage(self.driver)

    def click_add_member(self):
        # click 添加成员
        self.swipe_find_click(*self._ADD_MEMBER_ELEMENT)
        return AddMemberPage(self.driver)