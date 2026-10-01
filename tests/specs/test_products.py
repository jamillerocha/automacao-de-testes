from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver  # noqa: F401


def _wait(driver, timeout=10):
    return WebDriverWait(driver, timeout)


def _click(driver, locator):
    _wait(driver).until(EC.element_to_be_clickable(locator)).click()


def _visible(driver, locator):
    return _wait(driver).until(EC.visibility_of_element_located(locator))


def _login(driver):
    driver.get("https://www.saucedemo.com")
    _visible(driver, (By.ID, "user-name")).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    _wait(driver).until(EC.url_contains("inventory.html"))
    _visible(driver, (By.CLASS_NAME, "inventory_list"))


def _ordenar(driver, valor):
    Select(_visible(driver, (By.CLASS_NAME, "product_sort_container"))).select_by_value(valor)
    _visible(driver, (By.CLASS_NAME, "inventory_list"))


def test_ordenar_produtos_por_preco_crescente(driver):

    # Cenario: Ordenar produtos por preco crescente
    _login(driver)

    _ordenar(driver, "lohi")

    precos_texto = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precos = [float(p.text.replace("$", "")) for p in precos_texto]

    assert len(precos) > 0
    assert precos == sorted(precos)


def test_ordenar_produtos_por_nome(driver):

    # Cenario: Ordenar produtos por nome de A a Z
    _login(driver)

    _ordenar(driver, "za")
    _ordenar(driver, "az")

    nomes_texto = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    nomes = [n.text for n in nomes_texto]

    assert len(nomes) > 0
    assert nomes == sorted(nomes)


def test_continuar_comprando_apos_adicionar_item(driver):

    # Cenario: Continuar comprando apos adicionar item
    _login(driver)

    _click(driver, (By.ID, "add-to-cart-sauce-labs-backpack"))
    _visible(driver, (By.CLASS_NAME, "shopping_cart_badge"))

    _click(driver, (By.CLASS_NAME, "shopping_cart_link"))
    _wait(driver).until(EC.url_contains("cart.html"))

    _click(driver, (By.ID, "continue-shopping"))
    _wait(driver).until(EC.url_contains("inventory.html"))
    _visible(driver, (By.CLASS_NAME, "inventory_list"))

    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert "inventory.html" in driver.current_url
    assert len(produtos) > 0