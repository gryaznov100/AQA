import random
import allure
import pytest
from base.base_taste import BaseTest


class TestPIMPageClickCheckBox(BaseTest):

    def test_pim_page_click_check_box(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.pim_page.click_pim_link()
        self.pim_page.click_check_boxes()


class TestPimPageAddEmployee(BaseTest):

    def test_add_employee(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.time_page.click_pim_link()
        self.pim_page.click_add_employee()
        self.pim_page.input_first_name()
        self.pim_page.input_middle_name()
        self.pim_page.input_last_name()
        self.pim_page.input_employee_id()
        self.pim_page.click_save_button()