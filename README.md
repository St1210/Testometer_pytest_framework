Selenium SDET Automation Practice

A Python + Selenium + PyTest automation project for practicing web UI automation and building SDET fundamentals.

Tech Stack

Python

Selenium WebDriver

PyTest

Google Chrome

Page Object Model (POM)

Git / GitHub

Project Structure

selenium-sdet-practice/
│
├── pages/
│   ├── login_page.py
│   └── add_customer_page.py
│
├── tests/
│   ├── test_login.py
│   └── test_add_customer.py
│
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md

Current Practice Coverage

Element locating with ID and XPath

Text boxes and send_keys()

Buttons and click()

Radio buttons

Checkboxes

Native HTML dropdowns with Selenium Select

Assertions

get_attribute("value")

first_selected_option

Conditional logic with if/elif

Python f-strings

Page Object Model basics

Same-page Bootstrap offcanvas/modal handling

Custom JavaScript/Chosen dropdown analysis

Application Under Test

Current practice application:

https://devsite.testometer.co.in/v2.php/admin/customers

Additional practice application:

https://testautomationpractice.blogspot.com/

Use test/demo accounts and test data only. Do not commit real credentials, tokens, or customer information.

Setup

1. Clone the repository

git clone <your-github-repository-url>
cd selenium-sdet-practice

2. Create a virtual environment

Windows:

python -m venv .venv
.venv\Scripts\activate

macOS/Linux:

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Verify the installation

pytest --version
python --version

Running Tests

Run the complete suite:

pytest -v

Each test run also generates these reports:

- Machine-readable JUnit XML report: `reports/test-report.xml`
- Visual HTML report: run `powershell -ExecutionPolicy Bypass -File scripts\generate_report.ps1`
- Failure screenshots: `reports/screenshots/`

## CI/CD

GitHub Actions runs the UI tests on pushes to `main` or `master`, pull requests,
and manual workflow dispatches. Add `TESTOMETER_USERNAME` and
`TESTOMETER_PASSWORD` as repository secrets to enable valid-login tests in CI.
Every run uploads the HTML, JUnit XML, and failure screenshots as a downloadable
artifact named `test-reports-<run-number>`.

Run a specific test file:

pytest tests/test_add_customer.py -v

Run one test:

pytest tests/test_add_customer.py::test_select_gender -v

Page Object Model

Page classes contain:

Locators

UI actions

Reusable page-level behavior

Tests contain:

Test scenarios

Test data

Assertions

Example:

customer.select_gender("Male")

dropdown = Select(
    driver.find_element(*customer.SELECT_GENDER)
)

actual_gender = dropdown.first_selected_option.text

assert actual_gender == "Male"

The test describes what the user wants to do, while the Page Object hides the Selenium implementation details.

Current setup Fixture

conftest.py creates a fresh Chrome browser for each test and closes it after the test finishes.

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

Planned Automation Topics

Explicit waits and Expected Conditions

Custom/Chosen dropdowns

Keyboard actions

Mouse actions and ActionChains

Alerts

Frames / iframes

Multiple windows and tabs

File upload and download

Date pickers

Web tables

Dynamic elements and XPath

JavaScript execution

Screenshots

Selenium exceptions

Data-driven testing

PyTest parameterization

Logging

Test reports

Better fixtures and reusable utilities

CI/CD with GitHub Actions

Git Workflow

Check changes:

git status

Stage:

git add .

Commit:

git commit -m "Add customer form automation tests"

Push:

git push

Good Commit Examples

Initial project setup
Add login page object
Add customer page object
Add dropdown tests
Add textbox validation tests
Add keyboard action practice
Add explicit wait utilities
Add reporting

Notes

This repository is intentionally built incrementally as a learning project. Individual exercises may start simple and later be refactored into a more production-style SDET framework.