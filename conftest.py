import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    print("\nSetup fixture executed")

    # Initialize WebDriver (Update path as per your setup)
    driver = webdriver.Edge()
    driver.get("https://yourwebsite.com")

    # Initialize page objects
    home_page = HomePage(driver)
    services_page = ServicesPage(driver)
    contact_us_page = ContactUsPage(driver)

    yield driver, home_page, services_page, contact_us_page  # Ensure you're returning these values

    print("\nTeardown after test")
    driver.quit()
