from pages.add_customer_page import AddCustomerPage
from selenium.webdriver.support.ui import Select

def test_customer_type(Setup):
    driver = Setup 

    customer = AddCustomerPage(driver)

    customer.click_add_customer()

    customer.select_customer_type("B2C")

    dropdown = Select (driver.find_element(*customer.SELECT_DROPDOWN))

    assert dropdown.first_selected_option.text == "B2C"

