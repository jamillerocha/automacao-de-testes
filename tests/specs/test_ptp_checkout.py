from guara.application import Application
from selenium import webdriver
from guara import it

from tests.transactions.login_transaction import LoginTransaction
from tests.transactions.add_to_cart_transaction import AddToCartTransaction
from tests.transactions.checkout_transaction import CheckoutTransaction
from tests.transactions.finish_order_transaction import FinishOrderTransaction


def test_checkout():

    app = Application(webdriver.Chrome())

    app.given(
        LoginTransaction,
        url="https://www.saucedemo.com",
        user="standard_user",
        password="secret_sauce",
    ).then(it.Contains, "inventory")

    app.when(AddToCartTransaction).asserts(it.Contains, "cart")

    app.when(CheckoutTransaction, name="Douglas", last="Teste", zip_code="12345").asserts(
        it.Contains, "checkout-step-two"
    )

    app.when(FinishOrderTransaction).asserts(it.Contains, "Thank you")
