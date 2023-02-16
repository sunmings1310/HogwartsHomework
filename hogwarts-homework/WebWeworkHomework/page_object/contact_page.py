from selenium.webdriver.common.by import By

from page_object.wework_page import WeworkPage


class ContactPage(WeworkPage):
    _MEMLIST = (By.CSS_SELECTOR, ".member_colRight_memberTable_tr td:nth-child(2)")

    # 跳转添加成员功能
    def goto_add_member(self):
        pass

    def get_member_list(self):
        """
        获取成员列表
        :return:
        """
        ele_list = self.finds(self._MEMLIST)
        member_list = [ele.text for ele in ele_list]

        return member_list