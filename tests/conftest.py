import os
import pytest
from dotenv import load_dotenv
from utils import attach
from selene.support.shared import browser
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope='session', autouse=True)
def app_management():
    load_dotenv()
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": f"bs://{os.environ('APP_ID')}",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": f"{os.environ('USER_NAME')}",
            "accessKey": f"{os.environ('ACCESS_KEY')}"
        }
    })

    browser.config.driver = webdriver.Remote(
        "http://hub.browserstack.com/wd/hub",
        options=options)

    yield

    attach.add_video(browser)
    browser.quit()
