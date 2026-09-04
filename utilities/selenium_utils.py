from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumUtils:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)

    def get_value(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.get_attribute("value")

    def get_text(self, locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )
        return element.text