from selenium import webdriver


class WebDriver:
    class __WebDriver:
        def __init__(self):
            self.driver = webdriver.Chrome(r'C:\webdriver\chromedriver.exe')

    driver = None

    def __init__(self):
        if not self.driver:
            WebDriver.driver = WebDriver.__WebDriver().driver
