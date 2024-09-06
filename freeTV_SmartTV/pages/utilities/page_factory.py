from pages.page_objects.catchup_page import CatchupPage
from pages.page_objects.main_page import MainPage
from pages.page_objects.onboarding_freetv_page import LoginPage
from pages.webFlows.web_flows import WebFlows


class PageFactory:
    def __init__(self, driver):
        self.driver = driver
        self.onboarding_freetv_page = None
        self.main_page = None
        self.catchup_page = None
        self.web_flows = None

    def init_pages(self):
        # Initialize pages here
        self.onboarding_freetv_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.catchup_page = CatchupPage(self.driver)
        self.web_flows = WebFlows(self.onboarding_freetv_page, self.main_page, self.driver)

        return self

    # Optionally, add methods to get pages by name
    def get_page(self, page_name):
        return getattr(self, page_name, None)
