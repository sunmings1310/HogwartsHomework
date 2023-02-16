from appium.webdriver.common.mobileby import MobileBy

from base.wework_app import WeworkApp


class AddMemberPage(WeworkApp):
    _ADD_MEMBER_BY_MENUAL_ELEMENT = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    _ADD_MEMBER_BY_MENUAL_FOR_NAME_ELEMENT = (MobileBy.XPATH, '//*[contains(@text, "姓名")]/../*[@text="必填"]')
    _ADD_MEMBER_BY_MENUAL_FOR_phone_number_ELEMENT = (MobileBy.XPATH, '//*[contains(@text, "手机")]/..//*[@text="必填"]')
    _ADD_MEMBER_BY_MENUAL_FOR_SAVE_ELEMENT = (MobileBy.XPATH, "//*[@text='保存']")
    _ADD_MEMBER_BY_MENUAL_FOR_SAVE_SUCCESS = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def click_add_member_by_menual(self):
        self.find_click(*self._ADD_MEMBER_BY_MENUAL_ELEMENT)
        return self

    def quick_input_member_information(self, name, phone_num):
        self.find_send_keys(*self._ADD_MEMBER_BY_MENUAL_FOR_NAME_ELEMENT, name)
        self.find_send_keys(*self._ADD_MEMBER_BY_MENUAL_FOR_phone_number_ELEMENT, phone_num)
        self.find_click(*self._ADD_MEMBER_BY_MENUAL_FOR_SAVE_ELEMENT)
        return self

    def get_add_member_rst(self):
        ele_toast = self.find(*self._ADD_MEMBER_BY_MENUAL_FOR_SAVE_SUCCESS)
        rst = ele_toast.get_attribute('text')
        return rst