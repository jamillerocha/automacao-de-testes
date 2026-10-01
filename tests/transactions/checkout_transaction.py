from guara.transaction import AbstractTransaction
from tests.pages.cart_page import CartPage
from tests.pages.checkout_page import CheckoutPage


class CheckoutTransaction(AbstractTransaction):

    def do(self, name, last, zip_code):
        cart = CartPage(self._driver)
        cart.start_checkout()

        checkout = CheckoutPage(self._driver)
        checkout.fill_form(name, last, zip_code)
        checkout.continue_checkout()

        return self._driver.current_url
