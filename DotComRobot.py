import time
from encodings import search_function
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service


class DotComRobot:
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

    def link_click_ss(self,xpath_button, print_det):
        # Locate and click the dropdown
        dropdown = self.driver.find_element(By.CLASS_NAME, "insight-landing-filter-select")
        dropdown.click()
        # Locate and click the desired option
        option = self.driver.find_element(By.XPATH, xpath_button)
        option.click()
        time.sleep(5)
        print(print_det)

    def link_click_is(self, xpath_button, print_det):
        button = self.driver.find_element(By.XPATH, xpath_button)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        time.sleep(5)
        button.click()
        print(print_det)

    def input_details(self, input_ID, details):
        input_de = self.driver.find_element(By.NAME, input_ID)
        input_de.send_keys(details)
        time.sleep(5)

    def dropdown_click(self, drop_xpath, choice_click):
        select = self.driver.find_element(By.ID, drop_xpath)
        select.select_by_visible_text(choice_click)
        print(choice_click + " Selected!!!")
        time.sleep(5)

    def main_nav(self):
        self.link_click('/html/body/header/div[1]/nav/ul/li[3]/a', 'Services Selected!!!')
        self.link_click('//*[@id="menuitem1"]/a', 'Success Stories Selected!!!')
        self.link_click('//*[@id="menuitem3"]/a', 'Insights Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[6]/a', 'About us Selected!!!')
        self.link_click('//*[@id="menuitem5"]/a', 'Contact Us Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[9]/a', 'Search Selected!!!')

    def test_service_tab(self):
        self.link_click('/html/body/header/div[1]/nav/ul/li[3]/a', 'Services Selected!!!')
        self.link_click('//*[@id="featured"]/a', 'Core Services Selected!!!')
        self.link_click('//*[@id="menu-1"]/div[1]/div[1]/h3/a', 'Generative Enterprise Modernization (GEM) Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[3]/a', 'Services Selected!!!')
        self.link_click('//*[@id="menu-1"]/div[1]/div[2]/h3/a', 'Generative Digital Engineering (GDE) Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[3]/a', 'Services Selected!!!')
        self.link_click('/html/body/div[1]/section/div/div/div[1]/div[3]/h3/a',
                        'Data Modernization & AI (DM & AI) Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[3]/a', 'Services Selected!!!')
        self.link_click('/html/body/div[1]/section/div/div/div[1]/div[4]/h3/a',
                        'Autonomous Operations (AO) Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[3]/a', 'Services Selected!!!')
        self.link_click('//*[@id="featured"]/a', 'Featured services Selected!!!')
        self.link_click('//*[@id="menu-1"]/section[1]/div/div[1]/h3/a', 'ServiceNow Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[3]/a', 'Services Selected!!!')
        self.link_click('/html/body/div[1]/section/div/div/section[1]/div/div[2]/h3/a', 'Salesforce Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[3]/a', 'Services Selected!!!')
        self.link_click('//*[@id="menu-1"]/section[1]/div/div[3]/h3/a', 'Fiber Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[3]/a', 'Services Selected!!!')

    def success_story_tab(self):
        # Simulate interaction with dropdowns and buttons in the "Success Story" tab
        self.link_click('//*[@id="menuitem1"]/a', 'Success Stories Selected!!!')
        # Locate and click the dropdown
        self.link_click_ss("//option[@value='cloud-success']","Cloud services Selected!!!")
        self.link_click_ss("//option[@value='digital-success-suc-story']","Digital Customer Experience Selected!!!")
        self.link_click_ss("//option[@value='itagility']", "IT Agility Selected!!!")
        self.link_click_ss("//option[@value='operational-excellence-suc-story']", "Operational Excellence Selected!!!")
        self.link_click_ss("//option[@value='product-eng']", "Product Engineering Selected!!!")
        self.link_click_ss("//option[@value='success-sales']", "Salesforce Selected!!!")
        self.link_click_ss("//option[@value='software-networks']", "Software Intensive Networks Selected!!!")

    def insights_tab(self):
        self.link_click('//*[@id="menuitem3"]/a', 'Insights Selected!!!')
        self.link_click_ss("//option[@value='cloud']", "Cloud Selected!!!")
        self.link_click_ss("//option[@value='digital-customer-experience']", "Digital Customer Experience Selected!!!")
        self.link_click_ss("//option[@value='it-agility']", "IT Agility Selected!!!")
        self.link_click_ss("//option[@value='media-entertainment']", "Media &amp; Entertainment Selected!!!")
        self.link_click_ss("//option[@value='operational-excellence']", "Operational Excellence Selected!!!")
        self.link_click_ss("//option[@value='product-engineering']", "Product Engineering Selected!!!")
        self.link_click_ss("//option[@value='sales-force']", "Salesforce Selected!!!")
        self.link_click_ss("//option[@value='software-intensive-networks']", "Software Intensive Networks Selected!!!")

    def about_us(self):
        self.link_click('/html/body/header/div[1]/nav/ul/li[6]', 'About us Selected!!!')
        self.link_click('/html/body/header/div[2]/div/div/h2/a','About us page view Selected!!!')
        self.link_click('/html/body/header/div[1]/nav/ul/li[6]', 'About us Selected!!!')
        self.link_click('/html/body/header/div[2]/div/div/div/div[1]/h3/a','Prodapt Redbook in about us page Selected!!!')
        self.driver.back()
        self.link_click('/html/body/header/div[1]/nav/ul/li[6]','About us page view Selected!!!')
        self.link_click('/html/body/header/div[2]/div/div/div/div[2]/h3/a','Prodapt foundation in about us page Selected!!!')
        self.driver.back()
        self.link_click('/html/body/header/div[1]/nav/ul/li[6]', 'About us Selected!!!')
        self.link_click('/html/body/header/div[2]/div/div/div/div[3]/h3/a','Leadership team in about us page Selected!!!')
        self.driver.back()
        self.link_click('/html/body/header/div[1]/nav/ul/li[6]', 'About us Selected!!!')
        self.link_click('/html/body/header/div[2]/div/div/div/div[4]/h3/a','Diversity and Inclusion in about us page Selected!!!')
        self.driver.back()
        self.link_click('/html/body/header/div[1]/nav/ul/li[6]', 'About us Selected!!!')
        self.link_click('/html/body/header/div[2]/div/div/div/div[5]/h3/a', 'Massively distributed delivery Selected!!!')
        self.driver.back()
        self.link_click('/html/body/header/div[1]/nav/ul/li[6]', 'About us Selected!!!')
        self.link_click('/html/body/header/div[2]/div/div/div/div[6]/h3/a', 'Newsroom Selected!!!')
        self.driver.back()

    def contact_us_form(self):
        self.link_click('//*[@id="menuitem5"]/a', 'Contact Us Selected!!!')
        self.driver.execute_script("document.body.style.zoom='50%'")
        self.input_details('first-name','Test')
        self.input_details('last-name','Test')
        self.input_details('your-email','shravan.v@prodapt.com')
        self.input_details('orgde','prodapt')
        self.input_details('your-telephone','9444080419')
        self.input_details('textarea','I need help')
        self.input_details('city','Asia')
        self.link_click('/html/body/div[1]/div/div/div[2]/div/div/div/form/div[2]/p[3]/button', 'Contact form submitted')


    def close_browser(self):
        if self.driver:
            self.driver.quit()
