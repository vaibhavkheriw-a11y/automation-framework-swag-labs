import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.read_config import ReadConfig
from utilities.read_test_data import ReadTestData

@pytest.mark.regression
def test_logout_returns_to_login_page(driver):
    url = ReadConfig.get_config_value("app", "base_url")
    login_data = ReadTestData.get_login_data()

    driver.go(url)
    login_page = LoginPage(driver)
    login_page.login(login_data["username"], login_data["password"])

    products_page = ProductsPage(driver)
    products_page.open_menu()
    products_page.click_logout()

    assert driver.visibility_of_element_located((By.ID, "login-button"))
    assert driver.get_text_of_element((By.CLASS_NAME, "login_logo")) == "Swag Labs"
