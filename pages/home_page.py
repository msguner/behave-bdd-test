from enum import Enum

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePageConstants(Enum):
    LOG_IN_BTN = (By.XPATH, "//li[@class='login-text']/a")


class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def open_login_page(self):
        self.wait_and_find_element(*HomePageConstants.LOG_IN_BTN.value, seconds=5).click()
