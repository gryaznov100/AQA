import random
import allure
import pytest
from base.base_taste import BaseTest


class TestLogin(BaseTest):

    def test_time_page_punch(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opend()


class TestInvalidLogin(BaseTest):

    def test_invalid_login(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.INVALID_LOGIN)
        self.login_page.enter_password(self.data.INVALID_PASSWORD)
        self.login_page.click_submit_button()
        self.login_page.invalid_credentials()

