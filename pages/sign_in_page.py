from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class SignInPage(Page):

    TC_LINK = (By.CSS_SELECTOR, "a[aria-label*='terms & conditions - opens in a new window']")

    def open_sign_in_page(self):
        self.open('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')
        sleep(4)
    def click_terms_conditions(self):
        self.find_element(*self.TC_LINK).click()







