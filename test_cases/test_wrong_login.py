import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utilities.read_config import ReadConfig

@pytest.mark.sanity
def test_login_with_wrong_credentials_shows_error(driver):
    url = ReadConfig.get_config_value("app", "base_url")

    driver.go(url)
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "wrong_pass")

    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message
