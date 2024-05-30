import random
import allure
import pytest
from base.base_taste import BaseTest


class TestInvisibilityOfFilter(BaseTest):

    def test_invisibility_of_filter(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.time_page.click_recruitment_link()
        self.recruitment_page.click_arrow_button()
        self.recruitment_page.filter_is_not_displayed()