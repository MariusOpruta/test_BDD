# from pytest_bdd import scenarios, given, then, parsers, when
# from selenium.webdriver.common.by import By
#
# from pages.add_remove_elements_page import AddRemoveElementsPage
# from pages.login_page import LoginPage
#
# #Scenario
# scenarios('../features/test_add_remove_elements_page.feature')
#
# @given("open login page")
# def open_page(browser):
#     add_remove_page = AddRemoveElementsPage(browser)
#     add_remove_page.load_page()
#
#
# @when("title message is displayed")
# def title_message(browser):
#     add_remove_page = AddRemoveElementsPage(browser)
#     assert "Add/Remove Elements" in add_remove_page.getTitlePage
#
# @when("the user click AddButton 10 times")
# def click_addButon(browser):
#     add_remove_page = AddRemoveElementsPage(browser)
#     add_remove_page.clickAddButton()
#     for i in range(10):
#         click_addButon.click()
#
# @then("the user click Delete Button")
# def click_delete_buton(browser):
#     delete_button_list = browser.find_elements(By.CLASS_NAME, "added-manually")
#     #assert len(delete_button_list) == 10, "Not all delete button is displayed"
#     for i in range(10):
#         delete_button_list[0].click()
#         delete_button_list = browser.find_elements(By.CLASS_NAME, "added-manually")