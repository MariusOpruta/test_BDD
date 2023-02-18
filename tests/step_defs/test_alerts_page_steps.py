from pytest_bdd import scenarios, given, then, when

from pages.alerts_page import AlertsPage

scenarios('../features/test_alerts_page.feature')
@given("open login page")
def load_page(browser):
    load_page=AlertsPage(browser)
    load_page.load_page()

@when("the user click JS Alert button")
def click_Alert(browser):
    load_page = AlertsPage(browser)
    load_page.open_alert()

@when("the user click JS Confirm button")
def click_confirm(browser):
    load_page = AlertsPage(browser)
    load_page.load_page()
    load_page.open_confirm()

@when("the user click JS Prompt")
def click_prompt(browser):
    load_page = AlertsPage(browser)
    load_page.load_page()
    load_page.open_promt()




