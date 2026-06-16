import configparser
import os
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class BaseDriver:
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "config_files",
        "config.ini"
    )

    def __init__(self):
        browser_name = self.get_browser_name()
        try:
            if browser_name in ("chrome", "ch"):
                self.options = webdriver.ChromeOptions()
                self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
                self.options.add_argument("--disable-notifications")
                self.options.add_argument("--incognito")
                self.options.add_argument("--start-maximized")
                self.my_webdriver = webdriver.Chrome(options=self.options)
            elif browser_name in ("firefox", "ff"):
                self.my_webdriver = webdriver.Firefox()
            elif browser_name in ("edge", "me"):
                self.my_webdriver = webdriver.Edge()
            elif browser_name in ("safari", "sf"):
                self.my_webdriver = webdriver.Safari()
            else:
                print(f"{browser_name} browser is not in my knowledge, opening chrome.")
                self.my_webdriver = webdriver.Chrome()
        except Exception as e:
            assert False, f"Can not create webdriver for browser '{browser_name}'.\n{e}"

    def get_browser_name(self):
        config = configparser.ConfigParser()
        config.read(BaseDriver.config_path)
        if config.has_section("browser") and config.has_option("browser", "name"):
            return config.get("browser", "name").strip().lower()
        return "ch"

    def go(self, url):
        try:
            self.my_webdriver.get(url)
        except Exception as e:
            assert False, f"Can not navigate to {url}.\n{e}"

    def title_is(self, title):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.title_is(title)
            )
        except Exception as e:
            assert False, f"Title is not {title}.\n{e}"

    def title_contains(self, text):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.title_contains(text)
            )
        except Exception as e:
            assert False, f"Title does not contain {text}.\n{e}"

    def url_contains(self, text):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.url_contains(text)
            )
        except Exception as e:
            assert False, f"URL does not contain {text}.\n{e}"

    def url_to_be(self, url):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.url_to_be(url)
            )
        except Exception as e:
            assert False, f"URL is not {url}.\n{e}"

    def presence_of_element_located(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.presence_of_element_located(element_locator)
            )
        except Exception as e:
            assert False, f"Element not present in DOM: {element_locator}.\n{e}"

    def visibility_of_element_located(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.visibility_of_element_located(element_locator)
            )
        except Exception as e:
            assert False, f"Element not visible: {element_locator}.\n{e}"

    def visibility_of(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.visibility_of(
                    self.my_webdriver.find_element(*element_locator)
                )
            )
        except Exception as e:
            assert False, f"Element is not visible: {element_locator}.\n{e}"

    def presence_of_all_elements_located(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.presence_of_all_elements_located(element_locator)
            )
        except Exception as e:
            assert False, f"Elements not present: {element_locator}.\n{e}"

    def text_to_be_present_in_element(self, element_locator=(), text=""):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.text_to_be_present_in_element(element_locator, text)
            )
        except Exception as e:
            assert False, f"Text '{text}' not present in element {element_locator}.\n{e}"

    def text_to_be_present_in_element_value(self, element_locator=(), text=""):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.text_to_be_present_in_element_value(
                    element_locator, text
                )
            )
        except Exception as e:
            assert False, f"Text '{text}' not present in element value {element_locator}.\n{e}"

    def frame_to_be_available_and_switch_to_it(self, frame_locator=()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.frame_to_be_available_and_switch_to_it(frame_locator)
            )
        except Exception as e:
            assert False, f"Frame not available: {frame_locator}.\n{e}"

    def invisibility_of_element_located(self, element_locator=()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.invisibility_of_element_located(element_locator)
            )
        except Exception as e:
            assert False, f"Element is still visible: {element_locator}.\n{e}"

    def element_to_be_clickable(self, element_locator=()):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_to_be_clickable(element_locator)
            )
        except Exception as e:
            assert False, f"Element not clickable: {element_locator}.\n{e}"

    def staleness_of(self, element_locator=()):
        try:
            if isinstance(element_locator, tuple):
                element = self.my_webdriver.find_element(*element_locator)
            else:
                element = element_locator

            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.staleness_of(element)
            )
        except Exception as e:
            assert False, f"Element is not stale: {element_locator}.\n{e}"

    def element_to_be_selected(self, element_locator=()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_to_be_selected(
                    self.my_webdriver.find_element(*element_locator)
                )
            )
        except Exception as e:
            assert False, f"Element is not selected: {element_locator}.\n{e}"

    def element_located_to_be_selected(self, element_locator=()):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_located_to_be_selected(element_locator)
            )
        except Exception as e:
            assert False, f"Located element is not selected: {element_locator}.\n{e}"

    def element_selection_state_to_be(self, element_locator=(), state=True):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_selection_state_to_be(
                    self.my_webdriver.find_element(*element_locator), state
                )
            )
        except Exception as e:
            assert False, f"Element selection state is not {state}: {element_locator}.\n{e}"

    def element_located_selection_state_to_be(self, element_locator=(), state=True):
        try:
            WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.element_located_selection_state_to_be(
                    element_locator, state
                )
            )
        except Exception as e:
            assert False, f"Element selection state is not {state}: {element_locator}.\n{e}"

    def alert_is_present(self):
        try:
            return WebDriverWait(self.my_webdriver, 10).until(
                expected_conditions.alert_is_present()
            )
        except Exception as e:
            assert False, f"Alert is not present.\n{e}"

    def wait_for_element(self, element_locator=()):
        try:
            return self.visibility_of_element_located(element_locator)
        except Exception as e:
            assert False, f"Can not wait for {element_locator} element.\n{e}"

    def wait_for_element_clickable(self, element_locator=()):
        try:
            return self.element_to_be_clickable(element_locator)
        except Exception as e:
            assert False, f"Can not wait for clickable element {element_locator}.\n{e}"

    def click_on_element(self, element_locator=()):
        try:
            self.wait_for_element_clickable(element_locator).click()
        except Exception as e:
            assert False, f"Can not click on {element_locator}.\n{e}"

    def get_text_of_element(self, element_locator=()):
        try:
            # wait for visibility to ensure element is present and visible
            elem = self.visibility_of_element_located(element_locator)
            return elem.text
        except Exception as e:
            assert False, f"Can not get text of {element_locator} element.\n{e}"

    def wait_for_seconds(self, sec):
        time.sleep(sec)

    def switch_to_tab(self, tab_number):
        try:
            self.my_webdriver.switch_to.window(
                self.my_webdriver.window_handles[tab_number]
            )
        except Exception as e:
            assert False, f"Can not switch to tab {tab_number}.\n{e}"

    def fill_data(self, upload_locator=(), file_path=""):
        try:
            elem = self.visibility_of_element_located(upload_locator)
            elem.send_keys(file_path)
        except Exception as e:
            assert False, f"Can not fill data in {upload_locator}.\n{e}"

    def take_screenshot(self, file_name):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        screenshots_dir = os.path.join(base_dir, "screenshots")
        os.makedirs(screenshots_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshots_dir, file_name)
        self.my_webdriver.save_screenshot(screenshot_path)
        return screenshot_path

    def exit_webdriver(self):
        try:
            self.my_webdriver.quit()
        except Exception as e:
            assert False, f"Can not exit webdriver.\n{e}"

    # Convenience passthroughs so callers can use webdriver APIs when needed
    def find_element(self, by, value=None):
        try:
            # Allow both (by, value) and single tuple argument
            if value is None and isinstance(by, tuple):
                return self.my_webdriver.find_element(*by)
            return self.my_webdriver.find_element(by, value)
        except Exception as e:
            assert False, f"Can not find element {by, value}.\n{e}"

    def find_elements(self, by, value=None):
        try:
            if value is None and isinstance(by, tuple):
                return self.my_webdriver.find_elements(*by)
            return self.my_webdriver.find_elements(by, value)
        except Exception as e:
            assert False, f"Can not find elements {by, value}.\n{e}"