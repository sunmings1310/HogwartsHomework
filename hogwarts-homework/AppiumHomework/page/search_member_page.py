import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from base.wework_app import WeworkApp



class SearchMemberPage(WeworkApp):
    _SEARCH_ELEMENT = (MobileBy.XPATH, "//*[@text='搜索']")
    _SEARCH_BY_NAME_ELEMENT = (MobileBy.XPATH, "//*[@text='联系人']/../following-sibling::*[1]")
    _MEMBER_ELEMENTS = (MobileBy.XPATH,  "//*[@text='联系人']/../following-sibling::*")

    def search_member_by_name(self, name):
        self.find_send_keys(*self._SEARCH_ELEMENT, name)
        return self

    def get_member_nums(self):
        exists = self.get_search_member_rst()
        if not exists:
            return 0
        else:
            return len(self.finds(*self._MEMBER_ELEMENTS))

    def get_search_member_rst(self):
        # # 搜索结果分两种情况
        # # 第一种情况 ： 无结点
        # if "无搜索结果" in self.driver.page_source:
        #     pytest.xfail(reason=f"无搜索结果：{searchkey}")
        # print("有搜索结果")
        time.sleep(2)
        exists = self.wait_for_ele(*self._SEARCH_BY_NAME_ELEMENT)
        return exists

    def goto_personal_information_pgae_by_name(self, name):
        exists = self.get_search_member_rst()
        if not exists:
            raise NoSuchElementException(f"无搜索结果：{name}")
        else:
            self.find_click(*self._SEARCH_BY_NAME_ELEMENT)

            from page.personal_infomation_page import PersonalInformationPage
            return PersonalInformationPage(self.driver)