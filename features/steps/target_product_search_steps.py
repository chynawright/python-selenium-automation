from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")


@when("Search for '{item}'")
def search_product(context, item):
    # context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    # context.wait.until(EC.visibility_of_element_located(SEARCH_INPUT),
                       # message="Search field not visible")
    # context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_product(item)


@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    # actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    # assert expected_item in actual_text, f'Error! Text {expected_item} not in {actual_text}'
    # sleep(4)
    context.app.search_results.verify_search_results(expected_item)

@then('Verify header in shown')
def verify_header_shown(context):
    context.driver.find_element(*HEADER)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == expected_amount, f'Error! Expected {expected_amount} links but got {len(links)}.'


