import random
import allure
import pytest
from base.base_taste import BaseTest


# @allure.feature("Profile Functionality")
# class TestProfileFeature(BaseTest):
#
#     # @allure.title("Change profile name")
#     # @allure.severity("Critical")
#     # @pytest.mark.smoke
#     def test_change_profile_name(self):
#         self.login_page.open()
#         self.login_page.enter_login(self.data.LOGIN)
#         self.login_page.enter_password(self.data.PASSWORD)
#         self.login_page.click_submit_button()
#         # self.personal_page.is_opend()
#         self.personal_page.click_my_info_link()
#         self.personal_page.is_opend()
#         self.personal_page.change_name(f"Test{random.randint(1, 100)}")
#         self.personal_page.save_changes()
#         self.personal_page.is_changes_saved()
#         self.personal_page.make_screenshot("Success")
#
#
# # @allure.feature("Profile Functionality")
# class TestProfileFeature2(BaseTest):
#
#     # @allure.title("Change profile name")
#     # @allure.severity("Critical")
#     @pytest.mark.smoke
#     def test_change_profile_name2(self):
#         self.login_page.open()
#         self.login_page.enter_login(self.data.LOGIN)
#         self.login_page.enter_password(self.data.PASSWORD)
#         self.login_page.click_submit_button()
#         self.admin_page.click_admin_link()
#         self.admin_page.click_job_select()
#         self.admin_page.click_job_title()
#         self.admin_page.click_check_box()
#         self.admin_page.delete_selected_is_clickable()
#         self.admin_page.logout()
#
#
# class TestAddUser(BaseTest):
#     @pytest.mark.smoke
#     def test_add_user(self):
#         self.login_page.open()
#         self.login_page.enter_login(self.data.LOGIN)
#         self.login_page.enter_password(self.data.PASSWORD)
#         self.login_page.click_submit_button()
#         self.admin_page.click_admin_link()
#         self.admin_page.click_add_button()
#         self.admin_page.enter_user_role()
#         self.admin_page.enter_employee_name()
#         self.admin_page.enter_status()
#         self.admin_page.enter_username()
#         self.admin_page.enter_password()
#         self.admin_page.click_save()
#
#
# class TestLeavePageClearCalendar(BaseTest):
#
#     def test_leave_page_clear_calendar(self):
#         self.login_page.open()
#         self.login_page.enter_login(self.data.LOGIN)
#         self.login_page.enter_password(self.data.PASSWORD)
#         self.login_page.click_submit_button()
#         self.leave_page.click_leave_link()
#         self.leave_page.click_from_date_calendar()
#         self.leave_page.click_clear_of_calendar()


# class TestPIMPageClickCheckBox(BaseTest):
#
#     def test_pim_page_click_check_box(self):
#         self.login_page.open()
#         self.login_page.enter_login(self.data.LOGIN)
#         self.login_page.enter_password(self.data.PASSWORD)
#         self.login_page.click_submit_button()
#         self.pim_page.click_pim_link()
#         self.pim_page.click_check_boxes()

#
class TestTimePagePunch(BaseTest):

    def test_time_page_punch(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.time_page.click_time_link()
        self.time_page.click_Attendance_select_button()
        self.time_page.click_punch_in_out_button()
        self.time_page.click_calendar_button()
        self.time_page.click_left_scroll_calendar_button()
        self.time_page.click_date_calendar()
        self.time_page.click_time_change_button()
        self.time_page.input_hour()
        self.time_page.click_in_button()


# class TestPimPageAddEmployee(BaseTest):
#
#     def test_add_employee(self):
#         self.login_page.open()
#         self.login_page.enter_login(self.data.LOGIN)
#         self.login_page.enter_password(self.data.PASSWORD)
#         self.login_page.click_submit_button()
#         self.time_page.click_pim_link()
#         self.pim_page.click_add_employee()
#         self.pim_page.input_first_name()
#         self.pim_page.input_middle_name()
#         self.pim_page.input_last_name()
#         self.pim_page.input_employee_id()
#         self.pim_page.click_save_button()
