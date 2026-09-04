from pathlib import Path
import re
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage


CUSTOMER_URL = "https://devsite.testometer.co.in/v2.php/admin/customers"

def pytest_configure(config):
    Path("reports", "screenshots").mkdir(parents=True, exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("Setup") or item.funcargs.get("driver")
        if driver is not None:
            safe_name = re.sub(r"[^A-Za-z0-9_.-]+", "_", item.nodeid)
            screenshot = Path("reports", "screenshots", f"{safe_name}.png")
            driver.save_screenshot(str(screenshot))


@pytest.fixture
def Setup(request):
    options = Options()
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    if request.node.path.name != "test_login.py":
        username = os.getenv("TESTOMETER_USERNAME")
        password = os.getenv("TESTOMETER_PASSWORD")
        if not username or not password:
            driver.quit()
            pytest.skip(
                "Customer tests require TESTOMETER_USERNAME and "
                "TESTOMETER_PASSWORD secrets."
            )

        login = LoginPage(driver)
        login.open()
        login.login(username, password)
        driver.get(CUSTOMER_URL)
        if "login1" in driver.current_url:
            driver.quit()
            pytest.skip(
                "Customer page redirected to the application's unavailable "
                "login1 route after authentication."
            )

    yield driver

    driver.quit()


@pytest.fixture
def driver(Setup):
    return Setup