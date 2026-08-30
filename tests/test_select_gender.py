from pages.add_customer_page import AddCustomerPage
from selenium.webdriver.support.ui import Select

def test_select_gender(Setup):
    driver = Setup

    driver.get("https://devsite.testometer.co.in/v2.php/admin/customers")

    customer = AddCustomerPage(driver)

    customer.click_add_customer()

    user_gender = "Male"

    customer.select_gender(user_gender)

    dropdown = Select(driver.find_element(*customer.SELECT_GENDER))

    actual_gender = dropdown.first_selected_option.text

    # assert actual_value == "Male"   

    if user_gender == "Male":
        assert actual_gender == "Male"

    elif user_gender == "Female":
        assert actual_gender == "Female"

    else: 
        assert False, f"Unexpected gender: {user_gender}"
    
