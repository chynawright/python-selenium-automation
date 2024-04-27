from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep





@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@when('Click on Target terms and conditions link')
def click_terms_conditions(context):
    context.app.sign_in_page.click_terms_conditions()


@when('Switch to the newly opened window')
def switch_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then('Verify Terms and Conditions page is opened')
def tc_page_is_open(context):
    context.app.target_tc_page.tc_page_is_open()


@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.app.sign_in_page.close()
    context.app.sign_in_page.switch_window_by_id(context.original_window)
