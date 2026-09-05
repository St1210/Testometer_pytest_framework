from pages.add_customer_page import AddCustomerPage

def test_manage_customer_page(Setup):
   driver = Setup

   driver.get("https://devsite.testometer.co.in/v2.php/admin/customers")

   customer = AddCustomerPage(driver)

   customer.click_manage_customers()

   assert customer.is_manage_customers_page_displayed() == True 
