import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class RecruitmentPage(BasePage):

    PAGE_URL = Links.RECRUITMENT_PAGE

    ARROW_BUTTON = ("xpath", "//i[@class='oxd-icon bi-caret-up-fill']")
    JOB_TITLE = ("xpath", "//label[text()='Job Title']")
    SEARCH_BUTTON = ("xpath", "//button[text()=' Search ']")


    def click_arrow_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ARROW_BUTTON)).click()
        time.sleep(3)

    def filter_is_not_displayed(self):
        self.wait.until(EC.invisibility_of_element_located(self.JOB_TITLE))
        print("Фильтр свернулся, проверка по 'Job Title'")