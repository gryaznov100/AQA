import random
import allure
import pytest
from base.base_taste import BaseTest


@allure.feature("Profile Functionality")
class TestMyInfoFeature(BaseTest):

    # @allure.title("Change profile name")
    # @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        # self.personal_page.is_opend()
        self.my_info_page.click_my_info_link()
        self.my_info_page.is_opend()
        self.my_info_page.change_name(f"Test{random.randint(1, 100)}")
        self.my_info_page.save_changes()
        self.my_info_page.is_changes_saved()
        self.my_info_page.make_screenshot("Success")

class TestClickSwitch(BaseTest):
    def test_click_switch(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.my_info_page.click_my_info_link()
        self.my_info_page.click_job()
        self.my_info_page.click_switch()
