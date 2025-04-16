from pages.navigation_page import NavigationPage
from utils.logger import setup_logger

logger = setup_logger(__name__)

def test_navigation(browser):
    logger.info("Starting Navigation Test")
    nav_page = NavigationPage(browser)
    nav_page.open_page("https://example.com")
    assert nav_page.is_navigation_visible()
    logger.info("Navigation Test Completed")
