import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.read_config import ReadConfig
from utilities.read_test_data import ReadTestData

@pytest.mark.sanity
@pytest.mark.regression
def test_add_to_cart_updates_cart_badge(driver):
    url = ReadConfig.get_config_value("app", "base_url")
    login_data = ReadTestData.get_login_data()

    driver.go(url)
    login_page = LoginPage(driver)
    login_page.login(login_data["username"], login_data["password"])

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()

    assert products_page.get_cart_badge_text() == "1"
