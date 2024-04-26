from selenium.webdriver.common.by import By

from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")
    ADD_TO_CART = By.CSS_SELECTOR, "[data-test='chooseOptionsButton']"
    ITEM_TEXT_IN_CART = (By.XPATH, "//a[@data-test='cartItem-linked-title']")

    def verify_cart_is_empty(self):
        # actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        # expected_text = 'Your cart is empty'
        # assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def add_item(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART)


    def view_item(self, verified_item):
        actual_text = self.find_element(*self.ITEM_TEXT_IN_CART).text
        assert verified_item in actual_text, f'Error! Text {verified_item} not in {actual_text}'


