from pathlib import Path
import re

import pytest
from selenium import webdriver


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
    driver = webdriver.Chrome()

    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def driver(Setup):
    return Setup