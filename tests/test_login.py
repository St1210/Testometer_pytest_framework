import os

import pytest
from selenium.webdriver.common.keys import Keys

from pages.login_page import LoginPage


LOGIN_URL = "https://devsite.testometer.co.in/login"
INVALID_USERNAME = "invalid-user@example.com"
INVALID_PASSWORD = "definitely-not-a-valid-password"


def open_login(driver):
    login = LoginPage(driver)
    login.open()
    return login


def valid_credentials():
    username = os.getenv("TESTOMETER_USERNAME")
    password = os.getenv("TESTOMETER_PASSWORD")
    if not username or not password:
        pytest.skip(
            "Set TESTOMETER_USERNAME and TESTOMETER_PASSWORD for valid-login tests."
        )
    return username, password


def test_login_page_loads_with_required_controls(Setup):
    login = open_login(Setup)

    assert Setup.current_url == LOGIN_URL
    assert login.is_login_form_displayed()


def test_password_field_masks_entered_value(Setup):
    login = open_login(Setup)
    login.enter_password("secret-value")

    assert login.is_password_masked()


def test_instructor_checkbox_is_unselected_by_default(Setup):
    login = open_login(Setup)

    assert login.is_instructor_selected() is False


def test_instructor_checkbox_can_be_selected_and_deselected(Setup):
    login = open_login(Setup)

    login.select_login_as_instructor()
    assert login.is_instructor_selected() is True

    Setup.find_element(*login.CHECKBOX1).click()
    assert login.is_instructor_selected() is False


@pytest.mark.parametrize(
    ("username", "password", "expected_field"),
    [
        ("", INVALID_PASSWORD, "username"),
        (INVALID_USERNAME, "", "password"),
        ("", "", "username"),
    ],
)
def test_login_requires_mandatory_fields(Setup, username, password, expected_field):
    login = open_login(Setup)
    login.enter_username(username)
    login.enter_password(password)
    login.click_login()

    assert Setup.current_url == LOGIN_URL
    if expected_field == "username":
        assert login.get_username_validation_message()
    else:
        assert login.get_password_validation_message()


@pytest.mark.parametrize(
    "username",
    ["not-an-email", "missing-at.example.com", "@missing-user.com"],
)
def test_login_rejects_invalid_email_format(Setup, username):
    login = open_login(Setup)
    login.enter_username(username)
    login.enter_password(INVALID_PASSWORD)
    login.click_login()

    assert Setup.current_url == LOGIN_URL
    assert login.is_login_form_displayed()


@pytest.mark.parametrize(
    ("username", "password"),
    [
        (INVALID_USERNAME, INVALID_PASSWORD),
        (INVALID_USERNAME, "wrong-password"),
    ],
)
def test_login_rejects_invalid_credentials(Setup, username, password):
    login = open_login(Setup)
    login.login(username, password)

    assert Setup.current_url == LOGIN_URL
    assert login.is_login_form_displayed()


def test_valid_user_can_log_in(Setup):
    username, password = valid_credentials()
    login = open_login(Setup)
    login.login(username, password)

    assert "/login" not in Setup.current_url


def test_valid_instructor_can_log_in(Setup):
    username, password = valid_credentials()
    login = open_login(Setup)
    login.login(username, password, instructor=True)

    assert "/login" not in Setup.current_url


def test_login_can_be_submitted_with_enter_key(Setup):
    username, password = valid_credentials()
    login = open_login(Setup)
    login.enter_username(username)
    password_field = Setup.find_element(*login.PASSWORD)
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

    assert "/login" not in Setup.current_url
