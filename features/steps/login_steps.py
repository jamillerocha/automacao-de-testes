from behave import given, when, then
from tests.pages.login_page import LoginPage
from tests.pages.inventory_page import InventoryPage


@given("que o usuário acessa a página de login")
def step_open_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when("ele realiza login com usuário válido")
def step_valid_login(context):
    context.login_page.login("standard_user", "secret_sauce")


@then("ele deve ser redirecionado para a página de inventário")
def step_validate_inventory(context):
    inventory_page = InventoryPage(context.driver)
    assert inventory_page.is_loaded()