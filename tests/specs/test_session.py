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


def _login(driver):
    driver.get("https://www.saucedemo.com")
    _visible(driver, (By.ID, "user-name")).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    _wait(driver).until(EC.url_contains("inventory.html"))
    _visible(driver, (By.CLASS_NAME, "inventory_list"))


def _abrir_menu(driver):
    _click(driver, (By.ID, "react-burger-menu-btn"))
    _visible(driver, (By.ID, "logout_sidebar_link"))


def test_logout_com_sucesso(driver):

    # Cenario: Logout com sucesso
    _login(driver)

    _abrir_menu(driver)
    _click(driver, (By.ID, "logout_sidebar_link"))

    _visible(driver, (By.ID, "login-button"))
    _wait(driver).until(EC.url_to_be("https://www.saucedemo.com/"))

    assert driver.current_url == "https://www.saucedemo.com/"


def test_resetar_carrinho(driver):

    # Cenario: Resetar carrinho
    _login(driver)

    _click(driver, (By.ID, "add-to-cart-sauce-labs-backpack"))
    _visible(driver, (By.CLASS_NAME, "shopping_cart_badge"))

    _abrir_menu(driver)
    _click(driver, (By.ID, "reset_sidebar_link"))

    _click(driver, (By.ID, "react-burger-cross-btn"))

    carrinho_vazio = _wait(driver).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert carrinho_vazio