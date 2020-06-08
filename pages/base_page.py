import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    __TIMEOUT = 20

    def __init__(self, driver):
        self._driver = driver
        self._driver_wait = WebDriverWait(driver, BasePage.__TIMEOUT)

    """
    def __init__(self, driver):
        super(BasePage, self).__init__()
        self._driver_wait = WebDriverWait(driver, BasePage.__TIMEOUT)
        self._driver = driver
    """

    def wait_for_element(self, *locator, seconds):
        try:
            return WebDriverWait(self._driver, seconds).until(EC.presence_of_element_located(locator))
        except NoSuchElementException as err:
            raise AssertionError("Element could not be found.")

    def find_element(self, *locator):
        return self._driver.find_element(locator)

    def find_elements(self, *locator):
        return self._driver.find_elements(*locator)

    def is_exist(self, *locator, seconds):
        try:
            WebDriverWait(self._driver, seconds).until(EC.presence_of_element_located(locator))
        except NoSuchElementException:
            return False
        return True

    def go_url(self, url):
        self._driver.get(url)

    def wait_seconds(self, seconds):
        time.sleep(seconds)

    def hover(self, element):
        ActionChains(self._driver).move_to_element(element).perform()
        self.wait_seconds(5)  # hoverda gerekıyor

    def close_tab(self):
        self._driver.close()
        self._driver.switch_to_window(self._driver.window_handles[0])

    def browser_clear(self):
        self._driver.delete_all_cookies()
        self._driver.execute_script('window.localStorage.clear()')
        self._driver.execute_script('window.sessionStorage.clear()')
        self._driver.refresh()
