from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    SERVICES_TAB = (By.XPATH, "/html/body/header/div[1]/nav/ul/li[3]/a")
    CONTACT_US_TAB = (By.XPATH, '//*[@id="menuitem5"]/a')

    def click_services_tab(self):
        self.click_element(self.SERVICES_TAB)

    def click_contact_us_tab(self):
        self.click_element(self.CONTACT_US_TAB)
