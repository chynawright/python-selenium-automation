from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open main Target page')
def open_page(context):
    context.driver.get('https://www.target.com/')

@when('Click on cart icon')
def click_on_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(6)

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_is_empty(context):
    text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading-sc']")
    assert 'Your cart is empty' in text.text, f'Error! Text Your cart is empty not in {text}.'
