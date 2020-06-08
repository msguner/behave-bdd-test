import os
import shutil
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from helpers.driver import Driver
from helpers.utils import Utils

BEHAVE_DEBUG_ON_ERROR = False


def before_all(context):
    setup_debug_on_error(context.config.userdata)


def before_scenario(context, scenario):
    print("*** User data:", context.config.userdata)
    set_driver(context)

    context.driver.maximize_window()
    context.driver.implicitly_wait(15)
    context.driver.get("https://www.sahibinden.com/")
    #context.driver.get("https://www.dekopasaj.com/")



def after_scenario(context, scenario):
    print("Scenario status", scenario.status)
    if scenario.status == "failed":
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        os.chdir("screenshots")
        context.driver.save_screenshot(scenario.name + "_failed.png")

    context.driver.close()
    context.driver.quit()


def after_all(context):
    # behave -D ARCHIVE=Yes
    if 'ARCHIVE' in context.config.userdata.keys():
        if os.path.exists("screenshots"):
            os.rmdir("screenshots")
            os.makedirs("screenshots")

        if context.config.userdata['ARCHIVE'] == "Yes":
            shutil.make_archive(
                time.strftime("%d_%m_%Y"),
                'zip',
                "failed_scenarios_screenshots")
            # os.rmdir("screenshots")


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")


# TODO cross browser ayarları yapılacak.
def set_driver(context):
    # behave -D BROWSER=chrome
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            browser = 'chrome'
        else:
            browser = context.config.userdata['BROWSER']
    else:
        browser = 'chrome'

    # create driver
    if browser == 'chrome':
        # context.driver = Driver().driver  # Burası dinamik olacak. belki parametre alabılır. araştırılacak
        driver_path = Utils.get_full_path('drivers', 'chromedriver.exe')
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument('--no-proxy-server')
        chrome_options.add_argument("--proxy-server='direct://'")
        chrome_options.add_argument("--proxy-bypass-list=*")
        driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path)
        context.driver = driver

    # elif browser == 'firefox':
    #     context.driver = webdriver.Firefox()
    # elif browser == 'safari':
    #     context.driver = webdriver.Safari()
    # elif browser == 'ie':
    #     context.driver = webdriver.Ie()
    # elif browser == 'opera':
    #     context.driver = webdriver.Opera()
    # elif browser == 'phantomjs':
    #     context.driver = webdriver.PhantomJS()
    else:
        raise ValueError("Browser you entered:", browser, "is invalid value")
