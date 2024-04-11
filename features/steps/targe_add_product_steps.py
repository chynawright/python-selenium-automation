from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Add item to cart')
def add_item(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()
    sleep(4)


@then('Add item to cart in side view')
def add_item_side(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='orderPickupButton']").click()
    sleep(4)


@then('View cart and checkout')
def view_cart_checkout(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
    sleep(4)


@then("Assert '{verified_item}' in cart")
def view_item(context, verified_item):
    actual_text = context.driver.find_element(By.XPATH, "//a[@data-test='cartItem-linked-title']").text
    assert verified_item in actual_text, f'Error! Text {verified_item} not in {actual_text}'



