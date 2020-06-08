from enum import Enum

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePageConstants(Enum):
    LOG_IN_BTN = (By.XPATH, "//li[@class='login-text']/a")
    USER_NAME = (By.XPATH, "//li[@class='username-area']/a")


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)


