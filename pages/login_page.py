import allure
from selenium.webdriver.common.by import By

class LoginPage():

    username_textbox = (By.ID, "user-name")
    password_textbox = (By.ID, "password")
    login_button = (By.ID, "login-button")
    app_logo = (By.CLASS_NAME, "app_logo")
    error_element = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, my_page_driver):
        self.my_page_driver = my_page_driver

    @allure.step("Enter username: {username}")
    def enter_username(self, username):
        self.my_page_driver.fill_data(self.username_textbox, username)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.my_page_driver.fill_data(self.password_textbox, password)

    @allure.step("Click login button")
    def click_login_button(self):
        self.my_page_driver.click_on_element(self.login_button)

    @allure.step("Login with username: {username}")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Get app logo text")
    def get_app_logo_text(self):
        return self.my_page_driver.get_text_of_element(self.app_logo)

    @allure.step("Get error message")
    def get_error_message(self):
        return self.my_page_driver.get_text_of_element(self.error_element)
