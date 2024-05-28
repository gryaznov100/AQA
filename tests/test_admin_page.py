import random
import allure
import pytest
from base.base_taste import BaseTest


# @allure.feature("Profile Functionality")
class TestProfileFeature2(BaseTest):

    # @allure.title("Change profile name")
    # @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name2(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.admin_page.click_admin_link()
        self.admin_page.click_job_select()
        self.admin_page.click_job_title()
        self.admin_page.click_check_box()
        self.admin_page.delete_selected_is_clickable()
        self.admin_page.logout()


class TestAddUser(BaseTest):
    @pytest.mark.smoke
    def test_add_user(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.admin_page.click_admin_link()
        self.admin_page.click_add_button()
        self.admin_page.enter_user_role()
        self.admin_page.enter_employee_name()
        self.admin_page.enter_status()
        self.admin_page.enter_username()
        self.admin_page.enter_password()
        self.admin_page.click_save()