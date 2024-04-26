from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):
    SIGN_IN_ELEMENT_1 = (By.CSS_SELECTOR, "a[aria-label='Account, sign in']")
    def open_main_page(self):
        self.driver.get('https://www.target.com/')

    def click_sign_in(self):
        self.driver.find_element(*self.SIGN_IN_ELEMENT_1).click()
