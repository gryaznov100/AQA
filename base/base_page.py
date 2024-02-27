import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")
    ADMIN_BUTTON = ("xpath", "//span[text()='Admin']")
    PIM_BUTTON = ("xpath", "//span[text()='PIM']")
    LEAVE_BUTTON = ("xpath", "//span[text()='Leave']")
    TIME_BUTTON = ("xpath", "//span[text()='Time']")
    RECRUITMENT_BUTTON = ("xpath", "//span[text()='Recruitment']")
    PERFORMANCE_BUTTON = ("xpath", "//span[text()='Performance']")
    DASHBOARD_BUTTON = ("xpath", "//span[text()='Dashboard']")
    DIRECTORY_BUTTON = ("xpath", "//span[text()='Directory']")
    MAINTENANCE_BUTTON = ("xpath", "//span[text()='Maintenance']")
    CLAIM_BUTTON = ("xpath", "//span[text()='Claim']")
    BUZZ_BUTTON = ("xpath", "//span[text()='Buzz']")
    SEARCH_INPUT = ("xpath", "//input[@placeholder='Search']")
    SEARCH_BUTTON = ("xpath", "//input[@placeholder='Search']")
    USER_SELECT_BUTTON = ("xpath", "//span[@class='oxd-userdropdown-tab']")
    ABOUT_SELECT_BUTTON = ("xpath", "//a[text()='About']")
    SUPPORT_SELECT_BUTTON = ("xpath", "//a[text()='Support']")
    CHANGE_PASSWORD_SELECT_BUTTON = ("xpath", "//a[text()='Change Password']")
    LOGOUT_SELECT_BUTTON = ("xpath", "//a[text()='Logout']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)


    def is_opend(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))


    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def click_my_info_link(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()


    def click_admin_link(self):
        self.wait.until(EC.element_to_be_clickable(self.ADMIN_BUTTON)).click()

    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_SELECT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_SELECT_BUTTON)).click()





