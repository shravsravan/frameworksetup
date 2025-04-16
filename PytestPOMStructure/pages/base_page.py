import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        logging.info(f"Clicking element: {locator}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        logging.info(f"Entering text '{text}' into {locator}")
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def scroll_to_element(self, locator):
        logging.info(f"Scrolling to element: {locator}")
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
