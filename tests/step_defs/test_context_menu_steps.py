from pytest_bdd import scenarios, given, when, then

from pages.context_menu_page import ContextMenuPage
from tests.conftest import browser

scenarios('../features/test_context_menu_feature.feature')

@given("load page"):
    context_menu_page = ContextMenuPage(browser)
    context_menu_page.load_page()
@when("open menu"):

@then("accept alert:")

