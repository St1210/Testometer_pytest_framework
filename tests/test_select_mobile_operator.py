from pages.add_customer_page import AddCustomerPage
from selenium.webdriver.support.ui import Select

def test_select_mobile_operator(Setup):
    driver = Setup

    driver.get("https://devsite.testometer.co.in/v2.php/admin/customers")

    customer = AddCustomerPage(driver)

    customer.click_add_customer()

    customer.select_mobile_operator("india")

    dropdown = Select(driver.find_element(*customer.MOB_OPERATOR_DROPDOWN))

    actual_value = dropdown.first_selected_option.text

    assert actual_value == "India"