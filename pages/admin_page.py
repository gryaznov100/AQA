import time
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class AdminPage(BasePage):
    PAGE_URL = Links.ADMIN_PAGE

    JOB_BUTTON = ("xpath", "//span[text()='Job ']")
    JOB_TITLE_BUTTON = ("xpath", "//a[text()='Job Titles']")
    # JOB_BUTTON = ("xpath", "//span[text()='Puesto de Trabajo ']")
    # JOB_TITLE_BUTTON = ("xpath", "//a[text()='Títulos de los Puestos']")
    CHECK_BOX_BUTTON = ("xpath", "(//div[@class ='oxd-checkbox-wrapper'])[1]")
    DELETE_SELECTED_BUTTON = (
        "xpath", "//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--label-danger')]")
    ADD_BUTTON = ("xpath", "//button[text()=' Add ']")
    ADD_USER_TITLE = ("xpath", "//h6[text()='Add User']")
    USER_ROLE_SELECT = ("xpath", "(//div[@class='oxd-select-wrapper'])[1]")
    EMPLOYEE_NAME_INPUT = ("xpath", "//input[@placeholder='Type for hints...']")
    STATUS_SELECT = ("xpath", "(//div[@class='oxd-select-wrapper'])[2]")
    USERNAME_INPUT = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[2]")
    PASSWORD_INPUT = ("xpath", "//input[@type='password']")
    CONFIRM_PASSWORD_INPUT = ("xpath", "(//input[@type='password'])[2]")
    SAVE_BUTTON = ("xpath", "//button[text()=' Save ']")
    CANCEL_BUTTON = ("xpath", "//button[text()=' Cancel ']")
    ADMIN_ROLE = ("xpath", "//*[contains(text(), 'Admin')]")
    NAME = ("xpath", "//*[contains(text(), 'Nalim  R P')]")
    STATUS = ("xpath", "//*[contains(text(), 'Enabled')]")

    def click_job_select(self):
        self.wait.until(EC.element_to_be_clickable(self.JOB_BUTTON)).click()

    def click_job_title(self):
        self.wait.until(EC.element_to_be_clickable(self.JOB_TITLE_BUTTON)).click()
        time.sleep(2)

    def click_check_box(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECK_BOX_BUTTON)).click()
        time.sleep(2)

    def delete_selected_is_clickable(self):
        self.wait.until(EC.visibility_of_element_located(self.DELETE_SELECTED_BUTTON))
        print('Все окей')

    def click_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.ADD_USER_TITLE))

    def enter_user_role(self):
        self.wait.until(EC.element_to_be_clickable(self.USER_ROLE_SELECT)).click()
        self.wait.until(EC.element_to_be_clickable(self.ADMIN_ROLE)).click()

    def enter_employee_name(self):
        self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_NAME_INPUT)).send_keys("Nalim R P")
        # time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.NAME)).click()
        time.sleep(3)

    def enter_status(self):
        self.wait.until(EC.element_to_be_clickable(self.STATUS_SELECT)).click()
        self.wait.until(EC.element_to_be_clickable(self.STATUS)).click()
        time.sleep(3)

    def enter_username(self):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT)).send_keys("kirill")
        time.sleep(3)

    def enter_password(self):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys("kirill123")
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable(self.CONFIRM_PASSWORD_INPUT)).send_keys("kirill123")

    def click_save(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        time.sleep(3)
