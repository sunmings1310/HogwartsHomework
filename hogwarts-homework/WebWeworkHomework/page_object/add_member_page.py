from selenium.webdriver.common.by import By

from page_object.contact_page import ContactPage
from page_object.wework_page import WeworkPage


class AddMemberPage(WeworkPage):
    _USERNAME = (By.ID, "username")
    _MEMACCTID = (By.ID, "memberAdd_acctid")
    _MEMPHONE = (By.ID, "memberAdd_phone")
    _BTNSAVE = (By.CLASS_NAME, "js_btn_save")

    def add_member(self, username, accid, phone):
        """
        添加成员功能
        ，添加成功后返回通讯录页面
        """
        self.find(self._USERNAME).send_keys(username)
        self.find(self._MEMACCTID).send_keys(accid)
        self.find(self._MEMPHONE).send_keys(phone)
        self.find(self._BTNSAVE).click()

        return ContactPage(self.driver)