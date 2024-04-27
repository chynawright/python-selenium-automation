from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResultsPage
from pages.side_nav_page import SideNavPage
from pages.sign_in_page import SignInPage
from pages.target_tc_page import TargetTC
from pages.base_page import Page


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.side_nav_page = SideNavPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.target_tc_page = TargetTC(driver)
        self.base_page = Page(driver)