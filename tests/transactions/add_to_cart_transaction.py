from guara.transaction import AbstractTransaction
from tests.pages.inventory_page import InventoryPage


class AddToCartTransaction(AbstractTransaction):

    def do(self):
        page = InventoryPage(self._driver)
        page.add_product()
        page.go_to_cart()

        return self._driver.current_url
