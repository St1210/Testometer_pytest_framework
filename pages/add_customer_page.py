from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomerPage:

    # =========================
    # CUSTOMER MENU
    # =========================

    CUSTOMER = (
        By.XPATH,
        "//span[@key='t-tasks' and text()='Customer']"
    )

    MANAGE_CUSTOMER = (
        By.XPATH,
        "//a[@key='t-task-list' and text()='Manage Customer']"
    )

    MANAGE_BATCH = (
        By.XPATH,
        "//a[@key='t-task-list' and text()='Manage Batch']"
    )

    ARCHIVE_BATCH = (
        By.XPATH,
        "//a[@key='t-task-list' and text()='Archive Batch']"
    )

    SOLD_CERTIFICATE = (
        By.XPATH,
        "//a[@key='t-task-list' and text()='Sold Certificate']"
    )

    SOLD_COURSES = (
        By.XPATH,
        "//a[@key='t-task-list' and text()='Sold Courses']"
    )

    PAYMENT_HISTORY = (
        By.XPATH,
        "//a[@key='t-task-list' and text()='Payments History']"
    )

    # =========================
    # PAGE HEADERS
    # =========================

    MANAGE_CUSTOMER_PAGE = (
        By.XPATH,
        "//h4[contains(text(),'Manage customers')]"
    )

    MANAGE_BATCH_PAGE = (
        By.XPATH,
        "//h4[contains(text(),'Manage Batch')]"
    )

    ARCHIVE_BATCH_PAGE = (
        By.XPATH,
        "//h4[contains(text(),'Manage Batch')]"
    )

    # =========================
    # ADD CUSTOMER
    # =========================

    ADD_CUSTOMER_BUTTON = (
        By.ID,
        "add-customer"
    )

    ADD_NEW_CUSTOMER_PAGE = (
        By.ID,
        "canvasNewCustomerLabel"
    )

    # =========================
    # CUSTOMER TYPE
    # =========================

    SELECT_DROPDOWN = (
        By.ID,
        "customer_type"
    )

    # =========================
    # PERSONAL INFORMATION
    # =========================

    TITLE_DROPDOWN = (
        By.XPATH,
        "//select[@name='title']"
    )

    FIRST_NAME = (
        By.XPATH,
        "//input[@name='fname']"
    )

    LAST_NAME = (
        By.XPATH,
        "//input[@name='lname']"
    )

    # =========================
    # MOBILE
    # =========================

    MOB_OPERATOR_DROPDOWN = (
        By.XPATH,
        "//select[@name='phonecode']"
    )

    CONTACT_NUMBER = (
        By.XPATH,
        "//input[@name='contactNumber']"
    )

    MOB_OPERATOR_DROPDOWN1 = (
        By.XPATH,
        "//select[@name='phonecode1']"
    )

    CONTACT_NUMBER1 = (
        By.XPATH,
        "//input[@name='contactNumber1']"
    )

    # =========================
    # EMAIL
    # =========================

    EMAIL = (
        By.XPATH,
        "//input[@name='email']"
    )

    # =========================
    # GENDER
    # =========================

    SELECT_GENDER = (
        By.XPATH,
        "//select[@name='gender']"
    )

    # =========================
    # COMPANY
    # =========================

    SELECT_COMPANY = (
        By.XPATH,
        '//*[@id="companySearch_chosen"]/a/span'
    )

    SELECT_REFERENCE_COMPANY = (
        By.XPATH,
        '//*[@id="referenceCompanySearch_chosen"]/a/span'
    )

    # =========================
    # BOOKING TYPE
    # =========================

    SELECT_BOOKING_TYPE = (
        By.XPATH,
        "//select[@name='bookingType']"
    )

    # =========================
    # CONSTRUCTOR
    # =========================

    def __init__(self, driver):
        self.driver = driver

    # =========================
    # MENU ACTIONS
    # =========================

    def click_manage_customers(self):
        self.driver.find_element(
            *self.MANAGE_CUSTOMER
        ).click()

    def is_manage_customers_page_displayed(self):
        return self.driver.find_element(
            *self.MANAGE_CUSTOMER_PAGE
        ).is_displayed()

    # =========================
    # ADD CUSTOMER
    # =========================

    def click_add_customer(self):
        self.driver.find_element(
            *self.ADD_CUSTOMER_BUTTON
        ).click()

    def is_add_customer_page_displayed(self):
        return self.driver.find_element(
            *self.ADD_NEW_CUSTOMER_PAGE
        ).is_displayed()

    # =========================
    # CUSTOMER TYPE
    # =========================

    def select_customer_type(self, customer_type):
        dropdown = Select(
            self.driver.find_element(
                *self.SELECT_DROPDOWN
            )
        )

        dropdown.select_by_visible_text(customer_type)

    # =========================
    # TITLE
    # =========================

    def select_title(self, title):
        dropdown = Select(
            self.driver.find_element(
                *self.TITLE_DROPDOWN
            )
        )

        dropdown.select_by_visible_text(title)

    # =========================
    # FIRST NAME
    # =========================

    def enter_first_name(self, first_name):
        self.driver.find_element(
            *self.FIRST_NAME
        ).send_keys(first_name)

    # =========================
    # LAST NAME
    # =========================

    def enter_last_name(self, last_name):
        self.driver.find_element(
            *self.LAST_NAME
        ).send_keys(last_name)

    # =========================
    # MOBILE OPERATOR
    # =========================

    def select_mobile_operator(self, operator):
        dropdown = Select(
            self.driver.find_element(
                *self.MOB_OPERATOR_DROPDOWN
            )
        )

        dropdown.select_by_visible_text(operator)

    # =========================
    # CONTACT NUMBER
    # =========================

    def enter_contact_number(self, contact_number):
        self.driver.find_element(
            *self.CONTACT_NUMBER
        ).send_keys(contact_number)

    # =========================
    # SECOND MOBILE OPERATOR
    # =========================

    def select_mobile_operator1(self, operator):
        dropdown = Select(
            self.driver.find_element(
                *self.MOB_OPERATOR_DROPDOWN1
            )
        )

        dropdown.select_by_visible_text(operator)

    # =========================
    # SECOND CONTACT NUMBER
    # =========================

    def enter_contact_number1(self, contact_number):
        self.driver.find_element(
            *self.CONTACT_NUMBER1
        ).send_keys(contact_number)

    # =========================
    # EMAIL
    # =========================

    def enter_email(self, email):
        self.driver.find_element(
            *self.EMAIL
        ).send_keys(email)

    # =========================
    # GENDER
    # =========================

    def select_gender(self, gender):
        dropdown = Select(
            self.driver.find_element(
                *self.SELECT_GENDER
            )
        )

        dropdown.select_by_visible_text(gender)

    # =========================
    # BOOKING TYPE
    # =========================

    def select_booking_type(self, booking_type):
        dropdown = Select(
            self.driver.find_element(
                *self.SELECT_BOOKING_TYPE
            )
        )

        dropdown.select_by_visible_text(booking_type)