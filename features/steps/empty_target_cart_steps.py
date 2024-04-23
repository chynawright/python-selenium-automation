from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")


@given('Open main Target page')
def open_page(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()

@when('Click on cart icon')
def click_on_icon(context):
    context.wait.until(EC.element_to_be_clickable(CART_ICON),
                       message='The cart icon is not clickable'
                       )
    context.driver.find_element(*CART_ICON).click()
    sleep(6)

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_is_empty(context):
    text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading-sc']")
    assert 'Your cart is empty' in text.text, f'Error! Text Your cart is empty not in {text}.'
