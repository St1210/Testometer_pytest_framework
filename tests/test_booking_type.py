from pages.add_customer_page import AddCustomerPage
from selenium.webdriver.support.ui import Select


def test_select_booking_type(Setup):

    driver = Setup

    driver.get(
        "https://devsite.testometer.co.in/v2.php/admin/customers"
    )

    customer = AddCustomerPage(driver)

    customer.click_add_customer()

    booking_type = "New Booking"

    customer.select_booking_type(booking_type)

    dropdown = Select(driver.find_element(*customer.SELECT_BOOKING_TYPE))

    actual_booking_type = dropdown.first_selected_option.text

    print("User selected:", booking_type)
    print("Application selected:", actual_booking_type)

    assert actual_booking_type == "booking_type"