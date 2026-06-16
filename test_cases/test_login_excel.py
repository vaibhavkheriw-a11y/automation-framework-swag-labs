import os
import time
import pytest
from pages.login_page import LoginPage
from utilities.read_config import ReadConfig
from utilities.read_test_data_excel import getRowCount, readData

@pytest.mark.sanity
def test_login_excel(driver):

    driver = driver

    path = os.path.join(os.getcwd(), "test_data", "login_data.xlsx")

    rows = getRowCount(path, "Sheet1")

    for r in range(2, rows):

        username = readData(path, "Sheet1", r, 1)
        password = readData(path, "Sheet1", r, 2)
        expected = readData(path, "Sheet1", r, 3)

        if (username is None) and (password is None) and (expected is None):
            print(f"Skipping row {r} due to missing data.")
            continue

        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Expected: {expected}")

        url = ReadConfig.get_config_value("app", "base_url")

        driver.go(url)
        login_page = LoginPage(driver)
        login_page.login(username, password)

        time.sleep(5)

        if expected == "Pass":
            assert login_page.get_app_logo_text() == "Swag Labs"
        elif expected == "Fail":
            error_message = login_page.get_error_message()
            assert "Username and password do not match" in error_message