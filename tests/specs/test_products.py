from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver


def _login(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))


def test_ordenar_produtos_por_preco_crescente(driver):

    # Cenario: Ordenar produtos por preco crescente
    _login(driver)

    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")

    precos_texto = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precos = [float(p.text.replace("$", "")) for p in precos_texto]

    assert precos == sorted(precos)


def test_ordenar_produtos_por_nome(driver):

    # Cenario: Ordenar produtos por nome de A a Z
    _login(driver)

    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("za")
    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("az")

    nomes_texto = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    nomes = [n.text for n in nomes_texto]

    assert nomes == sorted(nomes)


def test_continuar_comprando_apos_adicionar_item(driver):

    # Cenario: Continuar comprando apos adicionar item
    _login(driver)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(EC.url_contains("cart.html"))

    driver.find_element(By.ID, "continue-shopping").click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

    produtos = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert "inventory.html" in driver.current_url
    assert len(produtos) > 0