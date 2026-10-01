from selenium.webdriver.common.by import By  # noqa: F401
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def _wait(self):
        return WebDriverWait(self.driver, self.TIMEOUT)

    def find(self, by, value):
        return self._wait().until(EC.visibility_of_element_located((by, value)))

    def click(self, by, value):
        self._wait().until(EC.element_to_be_clickable((by, value))).click()

    def type(self, by, value, text):
        self.find(by, value).send_keys(text)

    def get_text(self, by, value):
        return self.find(by, value).text