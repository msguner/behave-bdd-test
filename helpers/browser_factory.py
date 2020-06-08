from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from helpers.utils import Utils


def create_driver(browser, headless=False):
    if browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-proxy-server')
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        if headless:
            chrome_options.add_argument("--headless")

        driver_path = Utils.get_full_path('drivers', 'chromedriver.exe')
        return webdriver.Chrome(options=chrome_options, executable_path=driver_path)

    elif browser == 'firefox':
        options = Options()
        options.add_argument('--start-maximized')
        if headless:
            options.add_argument('-headless')

        return webdriver.Firefox(options=options)

    elif browser == 'safari':
        pass

    elif browser == 'ie':
        pass

    elif browser == 'opera':
        pass

    elif browser == 'phantomjs':
        pass

    elif browser == 'chrome_mobile':
        mobile_emulation = {
            'deviceName': 'Nexus 5'
        }
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)

        return webdriver.Chrome(chrome_options=chrome_options)

    else:
        raise ValueError("Browser you entered:", browser, "is invalid value")
