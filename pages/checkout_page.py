from selenium.webdriver.common.by import By

class CheckoutPage:
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    finish_button = (By.ID, "finish")
    complete_header = (By.CLASS_NAME, "complete-header")

    def __init__(self, my_page_driver):
        self.my_page_driver = my_page_driver

    def enter_checkout_information(self, first_name, last_name, postal_code):
        self.my_page_driver.fill_data(self.first_name, first_name)
        self.my_page_driver.fill_data(self.last_name, last_name)
        self.my_page_driver.fill_data(self.postal_code, postal_code)
        self.my_page_driver.click_on_element(self.continue_button)

    def finish_checkout(self):
        self.my_page_driver.click_on_element(self.finish_button)

    def get_complete_header(self):
        return self.my_page_driver.get_text_of_element(self.complete_header)
