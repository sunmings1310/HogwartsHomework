from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, base_driver=None):
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
        else:
            self.driver: WebDriver = base_driver

    def find(self, by, locator=None):
        """
        有可能传入 的是一个元祖(a, b)
        也有可能是传入两个参数
        :param by:
        :param locator:
        :return:
        """
        if locator is None:
            print(f"元素的定位方式为{by[0]}， 元素的定位表达式为{by[1]}")
            # 如果传入元祖，那么给元祖做解包，分别传入到函数中
            return self.driver.find_element(*by)
        else:
            # 如果传入两个参数，则正常使用。
            print(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")
            return self.driver.find_element(by, locator)

    def finds(self, by, locator=None):
        """
        有可能传入 的是一个元祖(a, b)
        也有可能是传入两个参数
        :param by:
        :param locator:
        :return:
        """
        if locator is None:
            print(f"元素的定位方式为{by[0]}， 元素的定位表达式为{by[1]}")
            # 如果传入元祖，那么给元祖做解包，分别传入到函数中
            return self.driver.find_elements(*by)
        else:
            # 如果传入两个参数，则正常使用。
            print(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")
            return self.driver.find_elements(by, locator)