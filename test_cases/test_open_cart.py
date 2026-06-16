import pytest
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.read_config import ReadConfig
from utilities.read_test_data import ReadTestData
    
@pytest.mark.regression
def test_open_cart_shows_added_item(driver):
    url = ReadConfig.get_config_value("app", "base_url")
    login_data = ReadTestData.get_login_data()

    driver.go(url)
    login_page = LoginPage(driver)
    login_page.login(login_data["username"], login_data["password"])

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    assert "Sauce Labs Backpack" in cart_page.get_cart_items()
