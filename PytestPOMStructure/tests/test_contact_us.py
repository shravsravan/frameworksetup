import logging

def test_contact_us(setup):
    driver, home_page, _, contact_us_page = setup

    home_page.click_contact_us_tab()
    contact_us_page.fill_contact_form("John Doe", "john@example.com", "Need assistance.")
    contact_us_page.submit_form()
    logging.info("Contact form submitted successfully.")
