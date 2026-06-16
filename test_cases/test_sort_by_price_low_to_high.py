import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.read_config import ReadConfig
from utilities.read_test_data import ReadTestData
    
@pytest.mark.regression
def test_sort_by_price_low_to_high(driver):
    url = ReadConfig.get_config_value("app", "base_url")
    login_data = ReadTestData.get_login_data()

    driver.go(url)
    login_page = LoginPage(driver)
    login_page.login(login_data["username"], login_data["password"])

    products_page = ProductsPage(driver)
    products_page.select_sort_filter("Price (low to high)")

    assert products_page.get_selected_sort_option() == "Price (low to high)"
