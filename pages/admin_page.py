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
    CHECK_BOX_BUTTON = ("xpath", "(// div[@class ='oxd-checkbox-wrapper'])[1]")
    DELETE_SELECTED_BUTTON = ("xpath", "//button[contains(@class, 'oxd-button oxd-button--medium oxd-button--label-danger')]")



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

