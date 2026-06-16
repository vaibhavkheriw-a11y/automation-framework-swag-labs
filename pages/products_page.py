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

    def get_products_title(self):
        return self.my_page_driver.get_text_of_element(self.products_title)

    def add_backpack_to_cart(self):
        self.my_page_driver.click_on_element(self.backpack_add_to_cart_button)

    def remove_backpack_from_cart(self):
        self.my_page_driver.click_on_element(self.backpack_remove_button)

    def get_cart_badge_text(self):
        return self.my_page_driver.get_text_of_element(self.cart_badge)

    def get_backpack_button_text(self):
        return self.my_page_driver.get_text_of_element(self.backpack_add_to_cart_button)

    def open_cart(self):
        self.my_page_driver.click_on_element(self.cart_link)

    def select_sort_filter(self, visible_text):
        select = Select(self.my_page_driver.find_element(*self.filter_dropdown))
        select.select_by_visible_text(visible_text)

    def get_selected_sort_option(self):
        select = Select(self.my_page_driver.find_element(*self.filter_dropdown))
        return select.first_selected_option.text

    def open_menu(self):
        self.my_page_driver.click_on_element(self.menu_button)

    def click_logout(self):
        self.my_page_driver.click_on_element(self.logout_link)
