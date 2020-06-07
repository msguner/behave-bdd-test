from enum import Enum

from selenium.webdriver.common.by import By


class Locator:
    def __init__(self, by: By, value: str, description: str = ""):
        self.by = by
        self.value = value
        self.description = description

    def get_by(self):
        return self.by

    def get_value(self):
        return self.value

    def get_description(self):
        return self.description
