from pages.add_customer_page import AddCustomerPage

def test_enter_mobile_number1(Setup):
    driver = Setup

    driver.get("https://devsite.testometer.co.in/v2.php/admin/customers")

    customer = AddCustomerPage(driver)

    customer.click_add_customer()

    customer.enter_contact_number1("8952475621")

    actual_value = driver.find_element(*customer.CONTACT_NUMBER1).get_attribute("value")

    assert actual_value == "8952475621"