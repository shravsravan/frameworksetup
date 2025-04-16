import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


class Pivot:
    def __init__(self):
        self.driver = None

    def open_browser(self, browser_path, url):
        service = Service(executable_path=browser_path)
        self.driver = webdriver.Edge(service=service)
        self.driver.maximize_window()
        time.sleep(3)
        self.driver.get(url)
        print("Link is working")
        time.sleep(5)

    def link_click(self, xpath_button, print_det):
        clickable_path = self.driver.find_element(By.XPATH, xpath_button)
        clickable_path.click()
        print(print_det)
        time.sleep(5)

    def link_click_class(self, xpath_button, print_det):
        clickable_path = self.driver.find_element(By.CLASS_NAME, xpath_button)
        clickable_path.click()
        print(print_det)
        time.sleep(5)

    def main_nav(self):
        self.link_click('/html/body/div[1]/div[2]/div[2]/div/div/div[4]/section/article/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/nav/div/ul/li[4]/a', 'Delivery and Sales Tool Dropdown Selected!!!')
        self.link_click('/html/body/div[1]/div[2]/div[2]/div/div/div[4]/section/article/div/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div/div/div/div/div[1]/div/div/div/div/div[1]/div[3]/nav/div/ul/li[4]/div/div/div/li[11]/a', 'Pivot Link Selected!!!')
        self.link_click('/html/body/div[1]/div[2]/div[2]/div/div/div[4]/section/article/div/div/div/div[1]/div[1]/div/div/div/div/div/div[1]/div[5]/div/div/div[2]/div/div/div/div/div/div/div/div/div/button', 'Search Filter Selected!!!')
        time.sleep(5)
        self.link_click_class("linkPanelLayout__filterPanel__body__headerIcon_1fa0925c",'Document type selected!!!')

    def close_browser(self):
        if self.driver:
            self.driver.quit()
