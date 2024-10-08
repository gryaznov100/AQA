import time
import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys


class MyInfoPage(BasePage):

    PAGE_URL = Links.MY_INFO_PAGE

    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")
    JOB_BUTTON = ("xpath", "//a[text()='Job']")
    Include_Employment_Contract_Details_SWITCH = ("xpath", "//div[@class='oxd-switch-wrapper']")
    CONTRACT_START_DATE_INPUT = ("xpath", "(//input[@class='oxd-input oxd-input--active'])[3]")

    # @allure.step("Change name")
    def change_name(self, new_name):
        with allure.step("Change name on '{new_name}'"):
            first_name_field = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.COMMAND + "A")
            first_name_field.send_keys(Keys.BACKSPACE)
            # assert first_name_field.get_attribute("value") == "", "There is text"
            first_name_field.send_keys(new_name)
            self.name = new_name

    # @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    # @allure.step("Changes has been caved suсcessfuly")
    def is_changes_saved(self):
        self.wait.until(EC.invisibility_of_element_located(self.SPINNER))
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(self.FIRST_NAME_FIELD, self.name))


    def click_job(self):
        self.wait.until(EC.element_to_be_clickable(self.JOB_BUTTON)).click()


    def click_switch(self):
        self.wait.until(EC.element_to_be_clickable(self.Include_Employment_Contract_Details_SWITCH)).click()
        self.wait.until(EC.visibility_of_element_located(self.CONTRACT_START_DATE_INPUT))
        print('Свитч нажался, элемент отображется!')

