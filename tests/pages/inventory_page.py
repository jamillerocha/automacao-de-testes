from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage


class InventoryPage(BasePage):

    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART = (By.CLASS_NAME, "shopping_cart_link")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")

    def add_product(self):
        self.click(*self.ADD_BACKPACK)

    def go_to_cart(self):
        self.click(*self.CART)

    def is_loaded(self, timeout=10):
        driver = getattr(self, "driver", None) or getattr(self, "_driver")
        try:
            WebDriverWait(driver, timeout).until(EC.url_contains("inventory.html"))
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(self.INVENTORY_LIST)
            )
            return True
        except TimeoutException:
            return False