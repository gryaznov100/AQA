import random
import allure
import pytest
from base.base_taste import BaseTest

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        # self.personal_page.is_opend()
        self.personal_page.click_my_info_link()
        self.personal_page.is_opend()
        self.personal_page.change_name(f"Test{random.randint(1,100)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("Success")




@allure.feature("Profile Functionality")
class TestProfileFeature2(BaseTest):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.admin_page.click_admin_link()
        self.admin_page.click_job_select()
        self.admin_page.click_job_title()
        self.admin_page.click_check_box()
        self.admin_page.delete_selected_is_clickable()
