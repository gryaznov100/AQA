import random

import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class PIMPage(BasePage):

    PAGE_URL = Links.PIM_PAGE

    CHECK_BOX = ("xpath", "(//div[@class='oxd-table-card-cell-checkbox'])[3]")
    DELETED_SELECTED = ("xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")

    def click_check_boxes(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECK_BOX)).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.DELETED_SELECTED))
        print("Кнопка удаления появилась :)")



