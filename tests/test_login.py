from pages.login_page import LoginPage

def test_valid_login(driver):


    driver.get("https://devsite.testometer.co.in/login")

    login = LoginPage(driver)
    login.login("sushanttawade30@gmail.com","test@123")

    assert "https://devsite.testometer.co.in" in driver.current_url

    