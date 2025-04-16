from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class NavigationPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def is_navigation_visible(self):
        return self.driver.find_element(By.ID, "nav-bar").is_displayed()
