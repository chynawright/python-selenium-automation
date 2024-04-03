from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target page')
def open_page(context):
    context.driver.get('https://www.target.com/')

@when('Click sign in')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[aria-label='Account, sign in']").click()


@when('Click sign in on navigation menu')
def click_sign_in_nav(context):
    context.driver .find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(5)
@then('Verify sign in form is opened')
def verify_sign_in_opened(context):
    text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    assert 'Sign into your Target account' in text.text, f'Error! Text Sign into your Target account not in {text}.'