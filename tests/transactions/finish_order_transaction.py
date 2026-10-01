from guara.transaction import AbstractTransaction
from tests.pages.checkout_page import CheckoutPage


class FinishOrderTransaction(AbstractTransaction):

    def do(self):
        checkout = CheckoutPage(self._driver)
        checkout.finish()

        return checkout.get_success_message()
