from page_object.add_member_page import AddMemberPage
from page_object.contact_page import ContactPage
from page_object.meituan_page import MeituanPage
from selenium.webdriver.common.by import By


class MainPage(MeituanPage):
    _CONTACT_CLASS = (By.ID, 'menu_contacts')
    _ADD_MEMBER_CLASS = (By.CLASS_NAME, 'index_service_cnt_item_title')

    def goto_contact(self):
        """
        跳转通讯录功能
        :return:
        """
        # self.driver.find_element_by_css_selector(self._CONTACT_CLASS).click()
        self.find(self._CONTACT_CLASS).click()
        return ContactPage(self.driver)

    def goto_add_member(self):
        """
        跳转添加成员功能
        :return:
        """
        # self.driver.find_element_by_css_selector(self._ADD_MEMBER_CLASS).click()
        self.find(self._ADD_MEMBER_CLASS).click()
        return AddMemberPage(self.driver)
