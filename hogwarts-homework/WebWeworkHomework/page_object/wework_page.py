import time

import yaml

from page_object.base_page import BasePage


class WeworkPage(BasePage):
    _BASE_URL = "https://h5.waimai.meituan.com/waimai/mindex/home"

    def login(self):
        self.driver.get(self._BASE_URL)
        cookies = yaml.safe_load(open('../data/cookie.yaml', 'r'))
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get(self._BASE_URL)

    def back_start_page(self):
        self.driver.get(self._BASE_URL)