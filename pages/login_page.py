from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    URL = "https://devsite.testometer.co.in/login"

    USERNAME = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    CHECKBOX1 = (By.ID, "is_instructor")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.visibility_of_element_located(self.USERNAME))

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        field.clear()
        field.send_keys(password)

    def select_login_as_instructor(self):
        checkbox = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX1))
        if not checkbox.is_selected():
            checkbox.click()

    def is_instructor_selected(self):
        return self.wait.until(
            EC.presence_of_element_located(self.CHECKBOX1)
        ).is_selected()

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, username, password, instructor=False):
        self.enter_username(username)
        self.enter_password(password)
        if instructor:
            self.select_login_as_instructor()
        self.click_login()

    def is_login_form_displayed(self):
        return all(
            self.driver.find_elements(*locator)
            for locator in (self.USERNAME, self.PASSWORD, self.LOGIN_BUTTON)
        )

    def get_username_validation_message(self):
        return self.driver.find_element(*self.USERNAME).get_attribute(
            "validationMessage"
        )

    def get_password_validation_message(self):
        return self.driver.find_element(*self.PASSWORD).get_attribute(
            "validationMessage"
        )

    def is_password_masked(self):
        return (
            self.driver.find_element(*self.PASSWORD).get_attribute("type")
            == "password"
        )