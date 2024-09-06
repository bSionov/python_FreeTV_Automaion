import time

from dotenv import load_dotenv
import os
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class BasePage:

    # Init base page with driver, action-chains, timeout and wait
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.actions = ActionChains(driver)
        self.timeout = int(os.getenv("TIMEOUT"))
        self.wait = WebDriverWait(driver, self.timeout)

    # # Fluent wait method that waits for an element to be located based on the provided locator
    # def fluent_wait(self, locator, timeout=None, poll_frequency=1):
    #     # poll_frequency is to every second if the element appears during the timeout given
    #     timeout = timeout or self.timeout
    #     try:
    #         return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
    #                              ignored_exceptions=[NoSuchElementException, TimeoutException]).until(
    #             EC.visibility_of_element_located(locator)
    #         )
    #     except TimeoutException as e:
    #         print(f"TimeoutException: Element with locator {locator} not found after {timeout} seconds.")
    #         raise TimeoutException(f"TimeoutException: "
    #                                f"Element with locator {locator} not found after {timeout} seconds.") from e

    # Actions - like press, hover, fill in text etc...
    def press(self, locator) -> None:
        # Wait for the element to be clickable
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        time.sleep(1)

    def fill_text(self, locator, txt: str) -> None:
        # Wait for the element to be visible
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(txt)

    def hover_with_mouse(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.actions.move_to_element(element).perform()

    def key_left(self):
        self.actions.send_keys(Keys.ARROW_LEFT)

    def update_drop_down(self, locator, value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        drop_down = Select(element)
        drop_down.select_by_value(value)

    # Verifications - like check if text is correct, get text from element etc...

    # This function is to get a text
    def get_text(self, locator):
        # Wait for the element to be visible
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def get_texts(self, locator: tuple) -> List[WebElement]:
        elements = self.driver.find_elements(*locator)
        if not elements:
            print(f"No elements found with locator: {locator}")
        return elements

    def verify_text_in_element(self, locator, expected_text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        actual_text = element.text
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but got: '{actual_text}'"
