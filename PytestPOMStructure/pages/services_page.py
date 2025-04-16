from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ServicesPage(BasePage):
    CORE_SERVICES = (By.XPATH, '//*[@id="featured"]/a')

    def select_core_services(self):
        self.click_element(self.CORE_SERVICES)
