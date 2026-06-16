import pytest
from pages.login_page import LoginPage
from utilities.read_config import ReadConfig
from utilities.read_test_data import ReadTestData

@pytest.mark.smoke
@pytest.mark.sanity
@pytest.mark.regression
def test_login_success(driver):
    url = ReadConfig.get_config_value("app", "base_url")
    login_data = ReadTestData.get_login_data()

    driver.go(url)
    login_page = LoginPage(driver)
    login_page.login(login_data["username"], login_data["password"])

    assert login_page.get_app_logo_text() == "Swag Labs"
