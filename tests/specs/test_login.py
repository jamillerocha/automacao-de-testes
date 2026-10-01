from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver  # noqa: F401


def _wait(driver, timeout=10):
    return WebDriverWait(driver, timeout)


def _visible(driver, locator):
    return _wait(driver).until(EC.visibility_of_element_located(locator))


def _fazer_login(driver, usuario, senha):
    driver.get("https://www.saucedemo.com")
    _visible(driver, (By.ID, "user-name")).send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(senha)
    _wait(driver).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()


def test_login_com_sucesso(driver):

    # Cenario: Login com sucesso
    _fazer_login(driver, "standard_user", "secret_sauce")

    _wait(driver).until(EC.url_contains("inventory.html"))
    _visible(driver, (By.CLASS_NAME, "inventory_list"))

    assert "inventory.html" in driver.current_url


def test_login_com_credenciais_invalidas(driver):

    # Cenario: Login com credenciais invalidas
    _fazer_login(driver, "usuario_invalido", "senha_invalida")

    mensagem_erro = _visible(driver, (By.CSS_SELECTOR, "[data-test='error']"))

    assert mensagem_erro.is_displayed()
    assert "Username and password do not match any user in this service" in mensagem_erro.text


def test_login_usuario_bloqueado(driver):

    # Cenario: Usuario bloqueado
    _fazer_login(driver, "locked_out_user", "secret_sauce")

    mensagem_erro = _visible(driver, (By.CSS_SELECTOR, "[data-test='error']"))

    assert mensagem_erro.is_displayed()
    assert "Sorry, this user has been locked out" in mensagem_erro.text