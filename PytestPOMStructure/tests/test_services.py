import logging

def test_services(setup):
    driver, home_page, services_page, _ = setup

    home_page.click_services_tab()
    services_page.select_core_services()
    logging.info("Verified Services Page navigation.")
