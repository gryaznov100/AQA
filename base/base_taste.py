import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage
from pages.admin_page import AdminPage
from pages.leave_page  import LeavePage


class BaseTest:

    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage
    admin_page: AdminPage
    leave_page: LeavePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)
        request.cls.admin_page = AdminPage(driver)
        request.cls.leave_page = LeavePage(driver)

