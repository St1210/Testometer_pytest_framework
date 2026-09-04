from pages.add_customer_page import AddCustomerPage
from selenium.webdriver.support.ui import Select

def test_select_ttle(Setup):
    driver = Setup 

    driver.get("https://devsite.testometer.co.in/v2.php/admin/customers")

    customer = AddCustomerPage(driver)

    customer.click_add_customer()
    customer.select_title("Mr.")

    dropdown = Select(driver.find_element(*customer.TITLE_DROPDOWN))

    assert dropdown.first_selected_option == "Mr." 