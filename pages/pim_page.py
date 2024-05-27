import random

import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class PIMPage(BasePage):

    PAGE_URL = Links.PIM_PAGE

    CHECK_BOX = ("xpath", "(//div[@class='oxd-table-card-cell-checkbox'])[3]")
    DELETED_SELECTED_BUTTON = ("xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-horizontal-margin']")
    ADD_EMPLOYEE_BUTTON = ("xpath", "//a[text()='Add Employee']")
    INPUT_FIRST_NAME = ("xpath", "//input[@placeholder='First Name']")
    INPUT_MIDDLE_NAME = ("xpath", "//input[@placeholder='Middle Name']")
    INPUT_LAST_NAME = ("xpath", "//input[@placeholder='Last Name']")
    INPUT_EMPLOYEE_ID = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    SAVE_BUTTON = ("xpath", "//button[text()=' Save ']")

    def click_check_boxes(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECK_BOX)).click()
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.DELETED_SELECTED_BUTTON))
        print("Кнопка удаления появилась :)")

    def click_add_employee(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_EMPLOYEE_BUTTON)).click()

    def input_first_name(self):
        self.wait.until(EC.element_to_be_clickable(self.INPUT_FIRST_NAME)).send_keys('Кирилл')

    def input_middle_name(self):
        self.wait.until(EC.element_to_be_clickable(self.INPUT_MIDDLE_NAME)).send_keys('Александрович')

    def input_last_name(self):
        self.wait.until(EC.element_to_be_clickable(self.INPUT_LAST_NAME)).send_keys('Грязнов')

    def input_employee_id(self):
        emp_id = self.wait.until(EC.element_to_be_clickable(self.INPUT_EMPLOYEE_ID))
        emp_id.send_keys(Keys.COMMAND, "a")
        emp_id.send_keys(Keys.DELETE)
        emp_id.send_keys('1999')
        time.sleep(5)


    def click_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()


