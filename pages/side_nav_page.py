from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep


class SideNavPage(Page):
    SIGN_IN_ELEMENT_2 = (By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")
    ADD_TO_CART_SIDE = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    CART_CHECKOUT = (By.CSS_SELECTOR, "a[href='/cart']")

    def click_sign_in_nav(self):
        self.wait_until_clickable_click(*self.SIGN_IN_ELEMENT_2)
        # self.click(*self.SIGN_IN_ELEMENT_2)

    def add_item_side(self):
        self.click(*self.ADD_TO_CART_SIDE)

    def view_cart_checkout(self):
        self.click(*self.CART_CHECKOUT)
