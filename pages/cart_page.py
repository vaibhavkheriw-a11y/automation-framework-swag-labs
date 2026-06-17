import allure
from selenium.webdriver.common.by import By

class CartPage:
    cart_item_names = (By.CLASS_NAME, "inventory_item_name")
    checkout_button = (By.ID, "checkout")
    continue_shopping_button = (By.ID, "continue-shopping")

    def __init__(self, my_page_driver):
        self.my_page_driver = my_page_driver

    @allure.step("Get cart items")
    def get_cart_items(self):
        elements = self.my_page_driver.presence_of_all_elements_located(
            self.cart_item_names
        )
        return [element.text for element in elements]

    @allure.step("Click checkout")
    def click_checkout(self):
        self.my_page_driver.click_on_element(self.checkout_button)

    @allure.step("Click continue shopping")
    def click_continue_shopping(self):
        self.my_page_driver.click_on_element(self.continue_shopping_button)
