from enum import Enum

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginConstants(Enum):
    USERNAME = (By.ID, 'username')
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "userLoginSubmitButton")

    USERNAME_HB = (By.ID, 'txtUserName')
    PASSWORD_HB = (By.ID, "txtPassword")
    LOGIN_BTN_HB = (By.ID, "btnLogin")


class LoginPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def enter_username(self, username):
        self.wait_for_element(*LoginConstants.USERNAME.value, seconds=5).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(*LoginConstants.PASSWORD.value, seconds=5).send_keys(password)

    def click_login(self):
        self.wait_for_element(*LoginConstants.LOGIN_BTN.value, seconds=5).click()
