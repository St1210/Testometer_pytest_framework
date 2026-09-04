from pages.add_customer_page import AddCustomerPage

def test_enter_email(Setup):
    driver = Setup

    driver.get("https://devsite.testometer.co.in/v2.php/admin/customers")

    customer = AddCustomerPage(driver)

    customer.click_add_customer()

    customer.enter_email("sushant@gmail.com")

    actual_value = driver.find_element(*customer.EMAIL).get_attribute("value")

    assert actual_value == "sushant@gmail.com"