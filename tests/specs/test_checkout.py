from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver  # noqa: F401


def _wait(driver, timeout=10):
    return WebDriverWait(driver, timeout)


def _click(driver, locator):
    _wait(driver).until(EC.element_to_be_clickable(locator)).click()


def _visible(driver, locator):
    return _wait(driver).until(EC.visibility_of_element_located(locator))


def test_compra_produto_com_sucesso(driver):

    # =========================
    # 1. LOGIN
    # =========================
    driver.get("https://www.saucedemo.com")

    _visible(driver, (By.ID, "user-name")).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    _click(driver, (By.ID, "login-button"))

    _wait(driver).until(EC.url_contains("inventory.html"))
    _visible(driver, (By.CLASS_NAME, "inventory_list"))
    assert "inventory.html" in driver.current_url

    # =========================
    # 2. ADICIONAR PRODUTO
    # =========================
    _click(driver, (By.ID, "add-to-cart-sauce-labs-backpack"))
    _visible(driver, (By.CLASS_NAME, "shopping_cart_badge"))

    # =========================
    # 3. IR PARA CARRINHO
    # =========================
    _click(driver, (By.CLASS_NAME, "shopping_cart_link"))

    _wait(driver).until(EC.url_contains("cart.html"))
    assert "cart.html" in driver.current_url

    # =========================
    # 4. INICIAR CHECKOUT
    # =========================
    _click(driver, (By.ID, "checkout"))

    _wait(driver).until(EC.url_contains("checkout-step-one.html"))
    assert "checkout-step-one.html" in driver.current_url

    # =========================
    # 5. PREENCHER DADOS
    # =========================
    _visible(driver, (By.ID, "first-name")).send_keys("Douglas")
    driver.find_element(By.ID, "last-name").send_keys("Teste")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    _click(driver, (By.ID, "continue"))

    _wait(driver).until(EC.url_contains("checkout-step-two.html"))
    assert "checkout-step-two.html" in driver.current_url

    # =========================
    # 6. FINALIZAR COMPRA
    # =========================
    _click(driver, (By.ID, "finish"))

    # =========================
    # 7. VALIDAÇÃO FINAL
    # =========================
    mensagem = _visible(driver, (By.CLASS_NAME, "complete-header"))

    assert mensagem.is_displayed()
    assert "Thank you" in mensagem.text