import time

import yaml

from page_object.base_page import BasePage


class MeituanPage(BasePage):
    _BASE_URL = "https://h5.waimai.meituan.com/waimai/mindex/home"

    def login(self):
        self.driver.get(self._BASE_URL)
        cookies = yaml.safe_load(open('../data/cookie.yaml', 'r'))
        # 循环遍历cookie_data，为每个cookie调用add_cookie方法
        for cookie in cookies:
            cookie.pop('sameSite', None)
            cookie.pop('storeId', None)
            if 'expirationDate' in cookie:
                cookie['expiry'] = int(cookie['expirationDate'])
                cookie.pop('expirationDate', None)
            if 'session' in cookie and cookie['session']:
                cookie.pop('expiry', None)
            cookie.pop('session', None)

            self.driver.add_cookie(cookie)
    def back_start_page(self):
        self.driver.get(self._BASE_URL)