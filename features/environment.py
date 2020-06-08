import os
import shutil
import time

from helpers.browser_factory import create_driver

BEHAVE_DEBUG_ON_ERROR = False


def before_all(context):
    setup_debug_on_error(context.config.userdata)


def before_scenario(context, scenario):
    print("*** User data:", context.config.userdata)

    # behave -D BROWSER=chrome
    if 'BROWSER' in context.config.userdata.keys():
        if context.config.userdata['BROWSER'] is None:
            browser = 'chrome'
        else:
            browser = context.config.userdata['BROWSER']
    else:
        browser = 'chrome'

    context.driver = create_driver(browser, False)
    context.driver.implicitly_wait(30)
    context.driver.set_page_load_timeout(30)
    context.driver.maximize_window()


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
                "screenshots")
            # os.rmdir("screenshots")


def setup_debug_on_error(userdata):
    global BEHAVE_DEBUG_ON_ERROR
    BEHAVE_DEBUG_ON_ERROR = userdata.getbool("BEHAVE_DEBUG_ON_ERROR")
