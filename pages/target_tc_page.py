from selenium.webdriver.common.by import By

from pages.base_page import Page


class TargetTC(Page):

    page_title = (By.CSS_SELECTOR, "[data-test*='page-title']")

    def tc_page_is_open(self):
        self.verify_partial_text('Terms & Conditions', *self.page_title)
