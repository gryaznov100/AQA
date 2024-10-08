import random
import allure
import pytest
from base.base_taste import BaseTest


class TestTimePagePunch(BaseTest):
    @pytest.mark
    def test_time_page_punch(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.time_page.click_time_link()
        self.time_page.click_attendance_select_button()
        self.time_page.click_punch_in_out_button()
        self.time_page.click_calendar_button()
        self.time_page.click_right_scroll_calendar_button()
        self.time_page.click_date_calendar()
        self.time_page.click_time_change_button()
        self.time_page.input_hour()
        self.time_page.click_in_button()



