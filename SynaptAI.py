import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


class SynaptAI:
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

    def navigation_bar(self):
        self.link_click('//*[@id="navbarNavDropdown"]/ul/li[2]/a', 'Experience Synapt Selected!!!')
        self.link_click("//a[@class='nav-link' and @aria-current='page' and @href='#target7']",
                        'Synapt Ecosystem Selected!!!')
        self.link_click('//*[@id="navbarDropdownMenuLink"]','Why Prodapt dropdown Selected!!!')
        self.link_click("//a[@class='dropdown-item thin-text' and @href='#target8']", 'Prodpat Edge Selected!!!')
        self.link_click("//a[@class='dropdown-item thin-text' and @href='https://career-portal.prodapt.com/']",
                        'Redirection Link to Career Portal Selected!!!')
        self.driver.back()
        self.link_click('//*[@id="navbarNavDropdown"]/ul/li[5]/a', 'Redirection Link to Contact US Selected!!!')
        self.driver.back()
        self.link_click('//*[@id="navbarNavDropdown"]/ul/li[1]/a/img','Synapt AI Selected!!!')
        self.link_click('//*[@id="target1"]/div/div/div/a/div/div/h5','Experience the Synapt advantage button Selected!!!')
        self.driver.back()
        self.link_click('//*[@id="target6"]/div/div[1]/div/div[2]/div/div/h5/a','Free Pilot Button Selected')
        self.driver.back()

    def close_browser(self):
        if self.driver:
            self.driver.quit()
