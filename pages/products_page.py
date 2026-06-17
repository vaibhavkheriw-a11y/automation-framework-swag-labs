import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class ProductsPage:

    products_title = (By.CLASS_NAME, "title")
    backpack_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
    backpack_remove_button = (By.ID, "remove-sauce-labs-backpack")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    cart_link = (By.CLASS_NAME, "shopping_cart_link")
    filter_dropdown = (By.CLASS_NAME, "product_sort_container")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_link = (By.ID, "logout_sidebar_link")

    def __init__(self, my_page_driver):
        self.my_page_driver = my_page_driver

    @allure.step("Get products title")
    def get_products_title(self):
        return self.my_page_driver.get_text_of_element(self.products_title)

    @allure.step("Add backpack to cart")
    def add_backpack_to_cart(self):
        self.my_page_driver.click_on_element(self.backpack_add_to_cart_button)

    @allure.step("Remove backpack from cart")
    def remove_backpack_from_cart(self):
        self.my_page_driver.click_on_element(self.backpack_remove_button)

    @allure.step("Get cart badge text")
    def get_cart_badge_text(self):
        return self.my_page_driver.get_text_of_element(self.cart_badge)

    @allure.step("Get backpack button text")
    def get_backpack_button_text(self):
        return self.my_page_driver.get_text_of_element(self.backpack_add_to_cart_button)

    @allure.step("Open cart")
    def open_cart(self):
        self.my_page_driver.click_on_element(self.cart_link)

    @allure.step("Select sort filter: {visible_text}")
    def select_sort_filter(self, visible_text):
        select = Select(self.my_page_driver.find_element(*self.filter_dropdown))
        select.select_by_visible_text(visible_text)

    @allure.step("Get selected sort option")
    def get_selected_sort_option(self):
        select = Select(self.my_page_driver.find_element(*self.filter_dropdown))
        return select.first_selected_option.text

    @allure.step("Open menu")
    def open_menu(self):
        self.my_page_driver.click_on_element(self.menu_button)

    @allure.step("Click logout")
    def click_logout(self):
        self.my_page_driver.click_on_element(self.logout_link)
