from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

add_to_cart = By.CSS_SELECTOR, "[data-test='chooseOptionsButton']"
add_to_cart_side = By.CSS_SELECTOR, "[data-test='orderPickupButton']"
cart_checkout = By.CSS_SELECTOR, "a[href='/cart']"
item_text_in_cart = By.XPATH, "//a[@data-test='cartItem-linked-title']"
cart_icon = By.CSS_SELECTOR, "[data-test='@web/CartLink']"
add_to_cart_button = By.CSS_SELECTOR, "[aria-label*='Add']"


@then('Add item to cart')
def add_item(context):
    context.driver.find_element(*add_to_cart).click()



@then('Add item to cart in side view')
def add_item_side(context):
    context.driver.find_element(*add_to_cart_side).click()
    sleep(4)


@then('View cart and checkout')
def view_cart_checkout(context):
    context.driver.find_element(*cart_checkout).click()
    sleep(4)


@then("Assert '{verified_item}' in cart")
def view_item(context, verified_item):
    actual_text = context.driver.find_element(*item_text_in_cart).text
    assert verified_item in actual_text, f'Error! Text {verified_item} not in {actual_text}'
