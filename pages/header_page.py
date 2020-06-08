from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class HeaderPageConstants(Enum):
    LOG_IN = (By.XPATH, "//li[@class='login-text']/a")
    SIGN_UP = (By.XPATH, "//li[@class='register-text']/a")
    USER_MENU = (By.ID, "usernameArea")
    SEARCH_BOX = (By.ID, "searchText")


class HeaderPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def open_login_page(self):
        self.wait_for_element(*HeaderPageConstants.LOG_IN.value, seconds=5).click()

    def get_user_name(self):
        return self.wait_for_element(*HeaderPageConstants.USER_MENU.value, seconds=10).text

    def open_user_menu(self):
        my_account_el = self.wait_for_element(*HeaderPageConstants.USER_MENU.value, seconds=10)
        return self.hover(my_account_el)

    def open_sign_up_page(self):
        self.wait_for_element(*HeaderPageConstants.SIGN_UP.value, seconds=5).click()

    def search(self, text):
        search_box = self.wait_for_element(*HeaderPageConstants.SEARCH_BOX.value, seconds=10)
        search_box.send_keys(text)
        search_box.send_keys(Keys.ENTER)
        self.wait_seconds(5)
