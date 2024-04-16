from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

expanded_items_page = (By.CSS_SELECTOR, "[data-test*='product-title']")
COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage']")


@given('Open Target product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(6)


@then('Verify user can click through colors')
def click_through_colors(context):
    expected_colors = ['Blue', 'Lilac Purple', 'Tan', 'Teal Blue', 'White', 'Black - Out of Stock', 'Burgundy - Out '
                                                                                                    'of Stock',
                       'Olive Green - Out of Stock']
    #expected_colors_period = ['Black', 'Blue', 'Burgundy', 'Lilac Purple', 'Olive Green', 'Tan', 'Teal Blue', 'White']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match acutal {actual_colors}.'