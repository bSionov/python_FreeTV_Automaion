import time

from selenium.webdriver.common.by import By
from pages.utilities.base_page import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):

    # Text
    enter_nuber = (By.CSS_SELECTOR, ".view-login__input-container")

    # Buttons
    catchup_menu_btn = (By.CSS_SELECTOR, ".menu.menu--opened > ul:nth-child(2) > li:nth-child(4) > div")
    menu_btn = (By.CSS_SELECTOR, ".menu")
    love_island_btn = (By.CSS_SELECTOR, ".tile.is-clickable.is-focused")
    kan_11_btn = (By.CSS_SELECTOR, ".section__layout > div > div:nth-child([53])")
    settings_btn = (By.CSS_SELECTOR, ".menu.menu--opened > ul:nth-child(3) > li:nth-child(1) > div > div")

    def press_on_menu(self):
        self.press(self.menu_btn)
        self.press(self.catchup_menu_btn)

    def open_settings(self):
        self.press(self.menu_btn)
        self.press(self.settings_btn)

    def logout(self):
        self.press(self.menu_btn)
        self.press(self.settings_btn)
        for x in range(3):
            self.actions.send_keys(Keys.LEFT).perform()
            time.sleep(1)
        self.actions.send_keys(Keys.ENTER).perform()
        time.sleep(1)
        self.actions.send_keys(Keys.RIGHT).perform()
        time.sleep(1)
        self.actions.send_keys(Keys.ENTER).perform()






