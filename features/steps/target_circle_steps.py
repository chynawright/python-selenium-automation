from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

benefit_box_link = (By.CSS_SELECTOR, "[class*='styles__CellBlock-sc-3f68hg-4 gDUgop']")
target_circle = 'https://www.target.com/l/target-circle/-/N-pzno9'


@given('Open the Target Circle page')
def open_page(context):
    context.driver.get(target_circle)
    sleep(6)


@then('Verify there are {number} benefit boxes')
def verify_boxes(context, number):
    number = int(number)
    boxes = context.driver.find_elements(*benefit_box_link)
    print(boxes)
    assert len(boxes) == number, f'Error! Expected {number} links but got {len(boxes)}.'


