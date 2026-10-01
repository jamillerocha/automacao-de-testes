from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):

    CHECKOUT = (By.ID, "checkout")

    def start_checkout(self):
        self.click(*self.CHECKOUT)
