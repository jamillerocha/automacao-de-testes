from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver


def test_compra_produto_com_sucesso(driver):

    # =========================
    # 1. LOGIN
    # =========================
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url

    # =========================
    # 2. ADICIONAR PRODUTO
    # =========================
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # =========================
    # 3. IR PARA CARRINHO
    # =========================
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(EC.url_contains("cart.html"))
    assert "cart.html" in driver.current_url

    # =========================
    # 4. INICIAR CHECKOUT
    # =========================
    driver.find_element(By.ID, "checkout").click()

    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-one.html"))
    assert "checkout-step-one.html" in driver.current_url

    # =========================
    # 5. PREENCHER DADOS
    # =========================
    driver.find_element(By.ID, "first-name").send_keys("Douglas")
    driver.find_element(By.ID, "last-name").send_keys("Teste")
    driver.find_element(By.ID, "postal-code").send_keys("12345")

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10).until(EC.url_contains("checkout-step-two.html"))
    assert "checkout-step-two.html" in driver.current_url

    # =========================
    # 6. FINALIZAR COMPRA
    # =========================
    driver.find_element(By.ID, "finish").click()

    # =========================
    # 7. VALIDAÇÃO FINAL
    # =========================
    mensagem = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    assert mensagem.is_displayed()
    assert "Thank you" in mensagem.text
