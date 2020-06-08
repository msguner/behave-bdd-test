from enum import Enum

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignUpConstants(Enum):
    SIGN_UP_BTN = (By.ID, "signUpButton")


class SignUpPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def is_initialize(self):
        return self.is_exist(*SignUpConstants.SIGN_UP_BTN.value, seconds=5)
