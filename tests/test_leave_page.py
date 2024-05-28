import random
import allure
import pytest
from base.base_taste import BaseTest


class TestLeavePageClearCalendar(BaseTest):

    def test_leave_page_clear_calendar(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.leave_page.click_leave_link()
        self.leave_page.click_from_date_calendar()
        self.leave_page.click_clear_of_calendar()