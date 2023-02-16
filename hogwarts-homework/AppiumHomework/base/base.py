from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
<<<<<<< HEAD
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page.black_handle import black_wrapper

=======
from selenium.webdriver.support.wait import WebDriverWait

>>>>>>> 167506cbb999944c6e9d1441e1644071279c853b

class Base:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
<<<<<<< HEAD
        # 参考：黑名单类
        self.black_list = [By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']"]

    # 设计模式：代理模式，装饰器模式
    # 装饰器
    @black_wrapper
=======

>>>>>>> 167506cbb999944c6e9d1441e1644071279c853b
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def find_click(self, by, locator):
        # 找到之后完成点击操作
        self.find(by, locator).click()

    def find_send_keys(self, by, locator, text):
        # 找到之后完成点击操作
        self.find(by, locator).send_keys(text)

    def _swipe_func(self, func, by, locator, num=3):
        # 滑动查找元素
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                if func == "find":
                    element = self.find(by, locator)
                    return element
                elif func == "finds":
                    elements = self.finds(by, locator)
                    return elements
                elif func == "find_click":
                    self.find_click(by, locator)
                    break
                elif func == "find_send_keys":
                    self.find_send_keys(by, locator)
                    break
                self.driver.implicitly_wait(5)
            except:
                print("未找到")
                size = self.driver.get_window_size()
                # 'width', 'height'
                width = size.get("width")
                height = size.get("height")
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)

            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"找了{num}次，未找到")

    def swipe_find(self, by, locator, num=3):
        self._swipe_func("find", by, locator)

    def swipe_finds(self, by, locator, num=3):
        self._swipe_func("finds", by, locator)

    def swipe_find_click(self, by, locator, num=3):
        self._swipe_func("find_click", by, locator)

    def swipe_find_send_keys(self, by, locator, num=3):
        self._swipe_func("find_send_keys", by, locator)

    def wait_for_ele(self, by, locator):
        try:
            WebDriverWait(self.driver, 5). \
                until(lambda x: x.find_element(by, locator))
            return True
        except:
            return False