from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support  import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:

    def __init__ (self, driver, timeout=10):

        self.driver = driver
        self.wait = WebDriverWait

        #==============================
        # BASIC ELEMENTS ACTION
        #==============================

        def click(self,locator):
            self.wait.until(EC.element_to_be_clickable(locator)).click()

        def find(self,locator):
            return self.wait.until(EC.presence_of_element_located(locator))

        def find_visible(self,locator):
            return self.wait.until(EC.visibility_of_element_located(locator))

        def enter_text(self,locator,text):
            element = self.find_visible(locator)
            element.clear()
            element.send_keys(text)


        #==============================
        # GET and VERIFY
        #==============================

        def get_value(self,locator):
            return self.find(locator).get_attribute("value")

        def get_text(self,locator):
            return self.findd_visible(locator).text

        def is_visible(self,locator):
            return self.find_visible(locator).is_displayed() 

        #==============================
        # DROPDOWNS
        #==============================

        def select_by_text(self,locator,text):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            Select(element).select_by_visible_text(text)


        def select_by_value(self,locator,value):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            Select(element).select_by_value(value)


        def select_by_index(self,locator,index):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            Select(element).select_by_index(index)


        def get_selected_option(self,locator):
            element = self.find_visible(locator)

            dropdown = Select(element)
            return dropdown.first_selected_option.text


    # =========================
    # KEYBOARD
    # =========================

    def press_key(self, locator, key):
        element = self.find_visible(locator)
        element.send_keys(key)