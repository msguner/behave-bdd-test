from enum import Enum

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchConstants(Enum):
    pass


class SearchPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def open_main_category(self, category_name):
        CATEGORY = (By.XPATH, "//div[@class='category-top-level']/a[text()='%s']" % category_name)
        self.wait_for_element(*CATEGORY, seconds=5).click()
        self.wait_seconds(3)
