from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ADD_TO_CART = By.CSS_SELECTOR, "[data-test='chooseOptionsButton']"
ADD_TO_CART_SIDE = By.CSS_SELECTOR, "[data-test='orderPickupButton']"
CART_CHECKOUT = By.CSS_SELECTOR, "a[href='/cart']"
ITEM_TEXT_IN_CART = By.XPATH, "//a[@data-test='cartItem-linked-title']"
CART_ICON = By.CSS_SELECTOR, "[data-test='@web/CartLink']"
ADD_TO_CART_BUTTON = By.CSS_SELECTOR, "[aria-label*='Add']"


@then('Add item to cart')
def add_item(context):
    # context.driver.find_element(*ADD_TO_CART).click()
    context.app.cart_page.add_item()


@then('Add item to cart in side view')
def add_item_side(context):
    # context.driver.find_element(*add_to_cart_side).click()
    context.app.side_nav_page.add_item_side()
    sleep(4)


@then('View cart and checkout')
def view_cart_checkout(context):
    # context.driver.find_element(*CART_CHECKOUT).click()
    context.app.side_nav_page.view_cart_checkout()
    sleep(4)


@then("Assert '{verified_item}' in cart")
def view_item(context, verified_item):
    # actual_text = context.driver.find_element(*ITEM_TEXT_IN_CART).text
    # assert verified_item in actual_text, f'Error! Text {verified_item} not in {actual_text}'
    context.app.cart_page.view_item(verified_item)
