from pages.add_customer_page import AddCustomerPage

def test_enter_first_name(Setup):
    driver = Setup

    driver.get("https://devsite.testometer.co.in/v2.php/admin/customers")

    customer = AddCustomerPage(driver)

    customer.click_add_customer()

    customer.enter_first_name("Sushant")

    actual_value = driver.find_element(*customer.FIRST_NAME).get_attribute("value")

    assert actual_value == "Sushant"


