from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver  # noqa: F401


def _wait(driver, timeout=10):
    return WebDriverWait(driver, timeout)


def _login(driver):
    driver.get("https://www.saucedemo.com")
    _wait(driver).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    _wait(driver).until(EC.url_contains("inventory.html"))
    _wait(driver).until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list")))


def test_adicionar_item_ao_carrinho(driver):

    # Cenario: Adicionar item ao carrinho
    _login(driver)

    _wait(driver).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    badge = _wait(driver).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert badge.text == "1"


def test_remover_item_do_carrinho(driver):

    # Cenario: Remover item do carrinho
    _login(driver)

    _wait(driver).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    ).click()

    _wait(driver).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    _wait(driver).until(
        EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))
    ).click()

    carrinho_vazio = _wait(driver).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert carrinho_vazio


def test_acessar_carrinho_sem_itens(driver):

    # Cenario: Acessar carrinho sem itens
    _login(driver)

    _wait(driver).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
    ).click()

    _wait(driver).until(EC.url_contains("cart.html"))
    _wait(driver).until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_list")))

    itens = driver.find_elements(By.CLASS_NAME, "cart_item")

    assert len(itens) == 0