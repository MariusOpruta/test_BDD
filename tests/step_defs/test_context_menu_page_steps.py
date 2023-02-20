from pytest_bdd import scenarios, given, when, then
from pages.context_menu_page import ContextMenuPage
from tests.conftest import browser

scenarios('../features/test_context_menu_page.feature')

@given("load page")
def load_page(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()
@when("open menu")
def open_page(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.open_menu()

@then("accept alert")
def accept_alert(browser):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.accept_alert()



