from selenium.webdriver.common.by import By

class LoginPage:

    USERNAME = (By.XPATH, "//input[@placeholder='Email'] ")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    CHECKBOX1 = (By.ID, "is_instructor")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    DASHBOARD = (By.XPATH, "//span[contains(text(),'Dashboard')]")
     
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element(*self.USERNAME).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)

    def select_login_as_instructor(self):
        self.driver.find_element(*self.CHECKBOX1).click()

    def is_instructor_selected(self):
        return self.driver.find_element(*self.CHECKBOX1).is_selected()

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
 
        
    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

        print("Current URL:", self.driver.current_url)
    

    def click_dashboard(self):
            self.driver.find_element(*self.DASHBOARD).click()
    
    def is_dashboard_page_displayed(self):
            return "/dashboard" in self.driver.current_url