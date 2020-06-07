from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers.singleton import Singleton
from helpers.utils import Utils


class Driver(metaclass=Singleton):

    def __init__(self):
        self.driver = self._create_driver()

    @staticmethod
    def _create_driver():
        driver_path = Utils.get_full_path('drivers', 'chromedriver.exe')
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-proxy-server')
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")

        try:
            driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
            driver.set_page_load_timeout(time_to_wait=200)
            return driver
        except ValueError as err:
            print('Driver could not be created.', err)
