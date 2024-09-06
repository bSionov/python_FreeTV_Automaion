import time

import allure
import pytest
from pages.utilities.page_factory import PageFactory


@pytest.mark.usefixtures()
class TestCatchupPages:

    def setup_method(self):
        # Initialize the PageFactory and pages
        self.page_factory = PageFactory(self.driver)
        self.page_factory.init_pages()
        # Expose web_flows directly
        self.web_flows = self.page_factory.web_flows
        self.main_page = self.page_factory.main_page
        self.catchup_page = self.page_factory.catchup_page
        self.number_of_channel = 52

    # @allure.description("Test 01 - Test")
    # def test_with_no_fail_assertion(self, setup, capsys):
    #     step = 1
    #     self.web_flows.perform_login()
    #     time.sleep(1)
    #     self.main_page.press_on_menu()
    #     # channel_name = self.catchup_page.get_channel_name()
    #     for xxx in range(self.number_of_channel):
    #         with allure.step(f"Step {step}"):
    #             step += 1
    #             self.catchup_page.open_channels(self.number_of_channel)
    #             self.catchup_page.check_number_of_days(capsys)
    #             self.number_of_channel -= 1
    #             if self.number_of_channel == 45:
    #                 break

    @allure.description("Test 01 - This test is verify that the catchup pages has 14 rails")
    def test_open_53_14_hearing(self, setup, capsys):
        self.web_flows.perform_login()
        time.sleep(1)
        self.main_page.press_on_menu()
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_52_13_hearing(self, setup, capsys):
        self.number_of_channel = 51
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_51_12_hearing(self, setup, capsys):
        self.number_of_channel = 50
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_50_11_hearing(self, setup, capsys):
        self.number_of_channel = 49
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_49_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 48
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_48_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 47
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_47_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 46
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_46_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 45
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_45_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 44
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_44_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 43
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_43_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 42
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_42_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 41
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_41_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 40
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_40_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 39
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_39_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 38
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_38_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 37
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_37_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 36
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_36_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 35
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_35_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 34
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_34_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 33
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_33_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 32
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_32_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 31
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_31_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 30
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_30_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 29
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_29_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 28
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_28_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 27
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_27_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 26
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_26_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 25
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_25_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 24
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_24_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 23
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_23_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 22
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_22_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 21
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_21_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 20
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_20_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 19
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_19_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 18
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_18_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 17
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_17_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 16
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_16_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 15
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_15_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 14
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_14_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 13
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_13_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 12
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_12_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 1
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_11_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 10
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_10_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 9
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_9_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 8
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_8_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 7
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_7_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 6
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_6_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 5
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_5_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 4
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_4_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 3
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_3_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 2
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_2_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 1
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_1_channel(self, setup, capsys):
        time.sleep(1)
        self.number_of_channel = 0
        self.catchup_page.open_channels(self.number_of_channel)
        self.catchup_page.check_number_of_days(capsys)

    # Sports channels
    def test_open_sports_channel_1(self, setup, capsys):
        self.web_flows.perform_login()
        time.sleep(1)
        self.main_page.press_on_menu()
        number_of_sport_channel = 1
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_sports_channel_2(self, setup, capsys):
        number_of_sport_channel = 2
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_sports_channel_3(self, setup, capsys):
        number_of_sport_channel = 3
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_sports_channel_4(self, setup, capsys):
        number_of_sport_channel = 4
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_sports_channel_5(self, setup, capsys):
        number_of_sport_channel = 5
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_sports_channel_6(self, setup, capsys):
        number_of_sport_channel = 6
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_sports_channel_7(self, setup, capsys):
        number_of_sport_channel = 7
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_sports_channel_8(self, setup, capsys):
        number_of_sport_channel = 8
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_sports_channel_9(self, setup, capsys):
        number_of_sport_channel = 9
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

    def test_open_sports_channel_10(self, setup, capsys):
        number_of_sport_channel = 10
        self.catchup_page.open_sports_channel(number_of_sport_channel)
        self.catchup_page.check_number_of_days(capsys)

