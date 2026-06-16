import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utilities.read_config import ReadConfig
from utilities.read_test_data import ReadTestData

@pytest.mark.sanity
@pytest.mark.regression
def test_checkout_can_finish_order(driver):
    url = ReadConfig.get_config_value("app", "base_url")
    login_data = ReadTestData.get_login_data()

    driver.go(url)
    login_page = LoginPage(driver)
    login_page.login(login_data["username"], login_data["password"])

    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_information("Test", "User", "12345")
    checkout_page.finish_checkout()

    assert checkout_page.get_complete_header() == "Thank you for your order!"
