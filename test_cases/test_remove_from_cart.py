import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.read_config import ReadConfig
from utilities.read_test_data import ReadTestData

@pytest.mark.sanity
def test_remove_from_cart_returns_button_to_add(driver):
    url = ReadConfig.get_config_value("app", "base_url")
    login_data = ReadTestData.get_login_data()

    driver.go(url)
    login_page = LoginPage(driver)
    login_page.login(login_data["username"], login_data["password"])

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.remove_backpack_from_cart()

    assert products_page.get_backpack_button_text() == "Add to cart"
