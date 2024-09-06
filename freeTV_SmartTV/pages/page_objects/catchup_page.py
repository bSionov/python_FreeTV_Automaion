import time
import uuid
import allure
from selenium.webdriver.common.by import By
from pages.utilities.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class CatchupPage(BasePage):

    # Class constructor to initialize instance attributes
    def __init__(self, driver):
        super().__init__(driver)
        # self.number_of_channels: int = 52

    # Text
    enter_number = (By.CSS_SELECTOR, ".view-login__input-container")
    channel_name_txt = (By.CSS_SELECTOR, ".metadata__channel-name")

    # Buttons
    catchup_menu_btn = (By.CSS_SELECTOR, ".menu.menu--opened > ul:nth-child(2) > li:nth-child(4) > div")
    menu_btn = (By.CSS_SELECTOR, ".menu")
    # rails = (By.CSS_SELECTOR, ".section--size-M > div > h1")
    rails2 = (By.CSS_SELECTOR, ".section__container > .section__headline")
    channels = (By.CSS_SELECTOR, "#app > div.view.view--catalog > div > div.sections > "
                                 "div.section.one-line.is-visible.is-current.section--1x1.section--size-XS > div > "
                                 "div.section__layout--one-line.section__layout > div > div")

    def press_on_menu(self):
        self.press(self.menu_btn)
        self.press(self.catchup_menu_btn)

    def get_channel_name(self):
        self.get_text(self.channel_name_txt)

    def check_number_of_days(self, capsys):
        x = 1
        print(f"Texted channel is: '{self.get_text(self.channel_name_txt)}'")

        # # Save screenshot
        # screenshot_path = f"/Users/borissionov/IdeaProjects/freeTV_SmartTV/tests/allure-results/{uuid.uuid4()}.png"
        # self.driver.save_screenshot(screenshot_path)
        # allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)

        for y in range(7):
            rail_elements = self.get_texts(self.rails2)
            for rail in rail_elements:
                if not rail.text == "":
                    print(f"{x} - {rail.text}")
                    x += 1
            self.actions.send_keys(Keys.DOWN).perform()
            time.sleep(1)
            self.actions.send_keys(Keys.DOWN).perform()
            time.sleep(1)

        # Capture printed output using capsys
        captured = capsys.readouterr()
        random_filename = f"{uuid.uuid4()}.txt"
        allure.attach(captured.out, name=random_filename, attachment_type=allure.attachment_type.TEXT)
        x -= 1
        assert x == 14, f"Expected rails: '{14}' but got '{x}"

    def open_channels(self, number_of_channels):
        # time.sleep(2)
        if number_of_channels == 1:
            self.actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            self.actions.send_keys(Keys.ENTER).perform()

        elif 1 < number_of_channels < 10:
            self.actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            self.actions.send_keys(Keys.LEFT).perform()
            time.sleep(0.2)
            time.sleep(1)
            self.actions.send_keys(Keys.ENTER).perform()

        elif 10 < number_of_channels < 52:
            self.actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(1)
            for y in range(number_of_channels):
                self.actions.send_keys(Keys.LEFT).perform()
                time.sleep(0.2)
            time.sleep(1)
            self.actions.send_keys(Keys.ENTER).perform()

        elif number_of_channels == 52:
            for y in range(number_of_channels):
                self.actions.send_keys(Keys.LEFT).perform()
                time.sleep(0.2)
            time.sleep(1)
            self.actions.send_keys(Keys.ENTER).perform()

    def open_sports_channel(self, number_of_sport_channel):
        if number_of_sport_channel >= 9:
            time.sleep(1)
            self.actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(2)
            for y in range(number_of_sport_channel):
                self.actions.send_keys(Keys.LEFT).perform()
                time.sleep(0.2)
            time.sleep(1)
            self.actions.send_keys(Keys.ENTER).perform()
        elif number_of_sport_channel == 1:
            time.sleep(1)
            self.actions.send_keys(Keys.DOWN).perform()
            time.sleep(1)
            self.actions.send_keys(Keys.ENTER).perform()
        elif 1 < number_of_sport_channel < 9:
            time.sleep(1)
            self.actions.send_keys(Keys.ESCAPE).perform()
            time.sleep(2)
            self.actions.send_keys(Keys.LEFT).perform()
            time.sleep(1)
            self.actions.send_keys(Keys.ENTER).perform()
