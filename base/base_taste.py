import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.my_info_page import MyInfoPage
from pages.admin_page import AdminPage
from pages.leave_page import LeavePage
from pages.pim_page import PIMPage
from pages.time_page import TimePage


class BaseTest:
    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    my_info_page: MyInfoPage
    admin_page: AdminPage
    leave_page: LeavePage
    pim_page: PIMPage
    time_page: TimePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()

        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.my_info_page = MyInfoPage(driver)
        request.cls.admin_page = AdminPage(driver)
        request.cls.leave_page = LeavePage(driver)
        request.cls.pim_page = PIMPage(driver)
        request.cls.time_page = TimePage(driver)
