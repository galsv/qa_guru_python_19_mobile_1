from appium.webdriver.common.appiumby import AppiumBy
from selene.support.shared import browser
from selene import have
from allure import step


def test_search():
    with step('Search for content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("BrowserStack")

    with step('Check result search'):
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.size_greater_than(0))


def test_open_settings():
    with step('Click settings'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/menu_overflow_button")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/explore_overflow_settings")).click()

    with step('Check window settings'):
        browser.element((AppiumBy.CLASS_NAME, "android.widget.TextView")).should(have.text('Settings'))
