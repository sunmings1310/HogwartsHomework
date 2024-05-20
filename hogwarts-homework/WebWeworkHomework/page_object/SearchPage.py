from selenium.webdriver.common.by import By

from page_object.meituan_page import MeituanPage


class SearchPage(MeituanPage):
    _SHOP_LIST = (By.CLASS_NAME, "shopCard_Ra8mF5")
    _INPUT_NAME = (By.XPATH, "//input[@placeholder='请输入商家或商品名称']")
    _SEARCH_BUTTON = (By.CLASS_NAME, "searchText_agXaiD")

    # 跳转添加成员功能
    def input_name(self, name):
        self.find(self._INPUT_NAME).send_keys(name)
        self.find(self._SEARCH_BUTTON).click()
        return self

    def get_shop_list(self):
        """
        获取商店列表
        :return:
        """
        ele_list = self.finds(self._SHOP_LIST)
        shop_list = [ele.text for ele in ele_list]

        return shop_list
