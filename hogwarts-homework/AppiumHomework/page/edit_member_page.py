from appium.webdriver.common.mobileby import MobileBy

from base.wework_app import WeworkApp




class EditMemberPage(WeworkApp):
    _DEL_MEMBER_ELEMENT = (MobileBy.XPATH, "//*[@text='删除成员']")
    _MAKE_SURE_FOR_DEL_MEMBER_ELEMENT = (MobileBy.XPATH, "//*[@text='确定']")

    def del_member_by_search(self):
        self.swipe_find_click(*self._DEL_MEMBER_ELEMENT)
        self.find_click(*self._MAKE_SURE_FOR_DEL_MEMBER_ELEMENT)

        from page.search_member_page import SearchMemberPage
        return SearchMemberPage(self.driver)

    def del_member_by_contacts(self):
        self.swipe_find_click(*self._DEL_MEMBER_ELEMENT)
        self.find_click(*self._MAKE_SURE_FOR_DEL_MEMBER_ELEMENT)

        from page.contact_page import ContactPage
        return ContactPage(self.driver)
