from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ContactUsPage(BasePage):
    FIRST_NAME = (By.NAME, 'first-name')
    EMAIL = (By.NAME, 'your-email')
    MESSAGE = (By.NAME, 'textarea')
    SUBMIT_BUTTON = (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div/form/div[2]/p[3]/button')

    def fill_contact_form(self, first_name, email, message):
        self.input_text(self.FIRST_NAME, first_name)
        self.input_text(self.EMAIL, email)
        self.input_text(self.MESSAGE, message)

    def submit_form(self):
        self.click_element(self.SUBMIT_BUTTON)
