from pages.add_customer_page import AddCustomerPage

def test_open_add_customer(Setup):
    driver = Setup

    driver.get("https://devsite.testometer.co.in/v2.php/admin/customers")

    customer = AddCustomerPage(driver)

    customer.click_add_customer()

    assert customer.is_add_customer_page_displayed()


