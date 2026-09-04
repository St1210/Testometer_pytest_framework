from pathlib import Path
import re
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
def Setup():
    options = Options()
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def driver(Setup):
    return Setup