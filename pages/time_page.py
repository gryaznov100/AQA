from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TimePage(BasePage):
    PAGE_URL = Links.TIME_PAGE

    ATTENDANCE_SELECT_BUTTON = ("xpath", "//span[text()='Attendance ']")
    PUNCH_IN_OUT_BUTTON = ("xpath", "//a[text()='Punch In/Out']")
    CALENDAR_BUTTON = ("xpath", "//i[@class='oxd-icon bi-calendar oxd-date-input-icon']")
    RIGHT_SCROLL_CALENDAR_BUTTON = ("xpath", "//i[@class='oxd-icon bi-chevron-right']")
    DATE_CALENDAR_BUTTON = ("xpath", "//div[text()='14']")
    TIME_CHANGE_BUTTON = ("xpath", "//i[@class='oxd-icon bi-clock oxd-time-input--clock']")
    HOUR_INPUT = ("xpath", "//input[@class='oxd-input oxd-input--active oxd-time-hour-input-text']")
    IN_OUT_BUTTON = ("xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
    IN_BUTTON = ("xpath", "//button[text()=' In ']")
    OUT_BUTTON = ("xpath", "//button[text()=' Out ']")

    def click_attendance_select_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ATTENDANCE_SELECT_BUTTON)).click()

    def click_punch_in_out_button(self):
        self.wait.until(EC.element_to_be_clickable(self.PUNCH_IN_OUT_BUTTON)).click()

    def click_calendar_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CALENDAR_BUTTON)).click()

    def click_right_scroll_calendar_button(self):
        self.wait.until(EC.element_to_be_clickable(self.RIGHT_SCROLL_CALENDAR_BUTTON)).click()

    def click_date_calendar(self):
        self.wait.until(EC.element_to_be_clickable(self.DATE_CALENDAR_BUTTON)).click()

    def click_time_change_button(self):
        self.wait.until(EC.element_to_be_clickable(self.TIME_CHANGE_BUTTON)).click()

    def input_hour(self):
        hour = self.wait.until(EC.element_to_be_clickable(self.HOUR_INPUT))
        hour.send_keys(Keys.COMMAND, "a")
        hour.send_keys(Keys.DELETE)
        # time.sleep(5)
        hour.send_keys("10")

    def click_in_button(self):
        if self.wait.until(EC.visibility_of_element_located(self.IN_BUTTON)).is_displayed():
            self.wait.until(EC.element_to_be_clickable(self.IN_BUTTON)).click()
        else:
            self.wait.until(EC.element_to_be_clickable(self.OUT_BUTTON)).click()

        # self.wait.until(EC.element_to_be_clickable(self.IN_OUT_BUTTON)).click()
        # time.sleep(2)
