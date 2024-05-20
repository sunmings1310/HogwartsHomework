from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, base_driver=None):
        if base_driver is None:
            options = Options()
            options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36")

            # 禁用 WebDriver 模式
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            # 设置为开发者模式
            options.add_argument("--disable-blink-features=AutomationControlled")

            self.driver = webdriver.Chrome(options=options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            # self.driver = webdriver.Remote(
            #     command_executor='http://127.0.0.1:4444/wd/hub',
            #     desired_capabilities=DesiredCapabilities)
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

    def util_find(self, by, locator=None, timeout=10):
        """
        等待元素出现在DOM中并且是可见的。
        :param by: 定位方式，可以是By的成员或者定位方式和表达式的元组
        :param locator: 元素的定位表达式
        :param timeout: 等待超时时间，默认为10秒
        :return: 返回定位到的元素
        """
        try:
            # 如果locator为None，说明by参数是一个元组
            if locator is None:
                print(f"等待元素的定位方式为{by[0]}， 元素的定位表达式为{by[1]}")
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located(by)
                )
            else:
                # 如果locator不为None，说明by和locator分别表示定位方式和表达式
                print(f"等待元素的定位方式为{by}， 元素的定位表达式为{locator}")
                element = WebDriverWait(self.driver, timeout).until(
                    EC.visibility_of_element_located((by, locator))
                )
            return element
        except TimeoutException:
            print("在指定的时间内未能找到元素。")
            return None