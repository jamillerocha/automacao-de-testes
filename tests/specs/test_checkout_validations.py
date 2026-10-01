from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver  # noqa: F401


def _wait(driver, timeout=10):
    return WebDriverWait(driver, timeout)


def _click(driver, locator):
    _wait(driver).until(EC.element_to_be_clickable(locator)).click()


def _login_e_iniciar_checkout(driver):
    driver.get("https://www.saucedemo.com")
    _wait(driver).until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    _wait(driver).until(EC.url_contains("inventory.html"))

    _click(driver, (By.ID, "add-to-cart-sauce-labs-backpack"))
    _wait(driver).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

    _click(driver, (By.CLASS_NAME, "shopping_cart_link"))
    _wait(driver).until(EC.url_contains("cart.html"))

    _click(driver, (By.ID, "checkout"))
    _wait(driver).until(EC.url_contains("checkout-step-one.html"))
    _wait(driver).until(EC.visibility_of_element_located((By.ID, "first-name")))


def test_checkout_sem_preencher_dados(driver):

    # Cenario: Checkout sem preencher dados
    _login_e_iniciar_checkout(driver)

    _click(driver, (By.ID, "continue"))

    erro = _wait(driver).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    assert erro.is_displayed()
    assert "First Name is required" in erro.text


def test_checkout_parcial(driver):

    # Cenario: Checkout parcial (preenche apenas parte dos dados)
    _login_e_iniciar_checkout(driver)

    driver.find_element(By.ID, "first-name").send_keys("Douglas")

    _click(driver, (By.ID, "continue"))

    erro = _wait(driver).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    assert erro.is_displayed()
    assert "Last Name is required" in erro.text