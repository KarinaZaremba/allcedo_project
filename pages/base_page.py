from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _define_locator_type(self, locator):
        if "//" in locator:
            return By.XPATH

    def url_open(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def _find_element(self, locator, timeout=30):
        return self.wait_for_element_presence(locator, timeout)

    def _find_element_new(self, locator, timeout=30):
        return self.wait_new(locator, timeout)

    def wait_for_element_presence(self, locator, time=30):
        locator_type = self._define_locator_type(locator)
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable((locator_type, locator)))
        return element

    def wait_new(self, locator, time=30):
        locator_type = self._define_locator_type(locator)
        element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located((locator_type, locator)))
        return element

    def for_upload(self, locator):
        element = self._find_element_new(locator)
        one = element.send_keys(f"{os.getcwd()}\\adidas.jpg")
        print(os.getcwd())
        print(one)

    def click(self, locator):
        element = self._find_element(locator)
        element.click()

    def click_the_button_action(self, locator):
        element = self._find_element(locator)
        ActionChains(self.driver).move_to_element(element).click(element).perform()

    def get_element_text(self, locator):
        element = self._find_element(locator)
        return element.text

    def send_text(self, locator, text):
        element = self._find_element(locator)
        element.send_keys(text)

    def clear(self, locator):
        element = self._find_element(locator)
        element.clear()

    def refresh_page(self):
        self.driver.refresh()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_current_url(self):
        return self.driver.current_url

    def for_geo(self, locator, text):
        element = self._find_element_new(locator)
        element.send_keys(text)



