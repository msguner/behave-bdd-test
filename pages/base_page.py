import time
import traceback

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30

    def wait_and_find_element(self, *locator, seconds):
        try:
            return WebDriverWait(self.driver, seconds).until(EC.presence_of_element_located(locator))
        except StaleElementReferenceException:
            raise AssertionError("Element could not be found.")

    def find_element(self, *locator):
        return self.driver.find_element(locator)

    def visit(self, url):
        self.browser.get(url)

    def hover(self, element):
        ActionChains(self.browser).move_to_element(element).perform()
        time.sleep(5)  # hoverda gerekıyor

    def browser_clear(self):
        self.driver.delete_all_cookies()
        self.driver.execute_script('window.localStorage.clear()')
        self.driver.execute_script('window.sessionStorage.clear()')
        self.driver.refresh()

    def __getattr__(self, what):
        try:
            if what in self.locator_dictionary.keys():
                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.presence_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()

                try:
                    element = WebDriverWait(self.browser, self.timeout).until(
                        EC.visibility_of_element_located(self.locator_dictionary[what])
                    )
                except(TimeoutException, StaleElementReferenceException):
                    traceback.print_exc()
                # I could have returned element, however because of lazy loading, I am seeking the element before return
                return self.find_element(*self.locator_dictionary[what])
        except AttributeError:
            super(BasePage, self).__getattribute__("method_missing")(what)

    def method_missing(self, what):
        print("No %s here!" % what)
