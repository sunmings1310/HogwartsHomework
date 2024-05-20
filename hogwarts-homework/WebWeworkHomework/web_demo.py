from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote(command_executor='http://127.0.0.1:9515',desired_capabilities=DesiredCapabilities.CHROME)
webdriver.Chrome()