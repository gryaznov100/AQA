
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class LeavePage(BasePage):

    PAGE_URL = Links.LEAVE_PAGE

    FROM_DATE_CALENDAR = ("xpath", "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]")
    CLEAR_CALENDAR_BUTTON = ("xpath", "//div[@class='oxd-date-input-link --clear']")
    REQUIRED = ("xpath", "//span[text()='Required']")

    def click_from_date_calendar(self):
        self.wait.until(EC.element_to_be_clickable(self.FROM_DATE_CALENDAR)).click()

    def click_clear_of_calendar(self):
        self.wait.until(EC.element_to_be_clickable(self.CLEAR_CALENDAR_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.REQUIRED))
        print("!!!!!!!!Проверка пустого календаря сработала!!!!!!!!")


