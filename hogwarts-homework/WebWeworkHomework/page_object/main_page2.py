from page_object.add_member_page import AddMemberPage
from page_object.SearchPage import SearchPage
from page_object.meituan_page import MeituanPage
from selenium.webdriver.common.by import By


class MainPage2(MeituanPage):
    _SEARCH_XPATH = (By.XPATH, "//input[@placeholder='请输入商家或商品名称']")
    _ADD_MEMBER_CLASS = (By.CLASS_NAME, 'index_service_cnt_item_title')

    def goto_search(self):
        """
        跳转查询也米娜
        :return:
        """
        # self.driver.find_element_by_css_selector(self._CONTACT_CLASS).click()
        self.util_find(self._SEARCH_XPATH).click()
        return SearchPage(self.driver)

    def goto_add_member(self):
        """
        跳转添加成员功能
        :return:
        """
        # self.driver.find_element_by_css_selector(self._ADD_MEMBER_CLASS).click()
        self.find(self._ADD_MEMBER_CLASS).click()
        return AddMemberPage(self.driver)
