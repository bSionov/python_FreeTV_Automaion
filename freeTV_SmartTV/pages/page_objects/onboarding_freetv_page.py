import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.utilities.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):

    # Text
    # enter_nuber = (By.CSS_SELECTOR, ".view-login__input-container")

    # Buttons
    # login_btn = (By.CSS_SELECTOR, ".view-login__buttons > div:nth-child(2)")

    def press_on_login(self):
        time.sleep(5)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.LEFT).perform()
        actions.send_keys(Keys.ENTER).perform()

    def enter_phone_number(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.NUMPAD4).perform()
        actions.send_keys(Keys.NUMPAD8).perform()
        actions.send_keys(Keys.NUMPAD1).perform()
        actions.send_keys(Keys.NUMPAD2).perform()
        actions.send_keys(Keys.NUMPAD3).perform()
        actions.send_keys(Keys.NUMPAD4).perform()
        actions.send_keys(Keys.NUMPAD5).perform()
        actions.send_keys(Keys.NUMPAD6).perform()
        actions.send_keys(Keys.NUMPAD7).perform()
        actions.send_keys(Keys.NUMPAD8).perform()
        actions.send_keys(Keys.NUMPAD9).perform()
        actions.send_keys(Keys.ENTER).perform()
