import time
from selenium.webdriver.chrome.webdriver import WebDriver
from pages.page_objects.onboarding_freetv_page import LoginPage
from pages.utilities.base_page import BasePage
from pages.page_objects.main_page import MainPage


class WebFlows(BasePage):

    def __init__(self, login_page: LoginPage, main_page: MainPage, driver: WebDriver):
        super().__init__(driver)
        # self.main_page = main_page
        self.login_page = login_page
        self.main_page = main_page

    def perform_login(self):
        self.login_page.press_on_login()
        self.login_page.enter_phone_number()
        time.sleep(3)

    def perform_logout(self):
        self.main_page.logout()
