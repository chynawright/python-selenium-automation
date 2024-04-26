from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SIGN_IN_ELEMENT_1 = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")
SIGN_IN_ELEMENT_2 = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")


@when('Click sign in')
def click_sign_in(context):
    # context.driver.find_element(*SIGN_IN_ELEMENT_1).click()
    context.app.main_page.click_sign_in()


@when('Click sign in on navigation menu')
def click_sign_in_nav(context):
    # context.wait.until(
    # EC.visibility_of_element_located(SIGN_IN_ELEMENT_2),
    # message="Sign in element is invisible"
    # )
    # context.driver.find_element(*SIGN_IN_ELEMENT_2).click()
    context.app.side_nav_page.click_sign_in_nav()


@then('Verify sign in form is opened')
def verify_sign_in_opened(context):
    text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    assert 'Sign into your Target account' in text.text, f'Error! Text Sign into your Target account not in {text}.'
