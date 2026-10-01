from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver


def test_login_com_sucesso(driver):

    # Cenario: Login com sucesso
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url


def test_login_com_credenciais_invalidas(driver):

    # Cenario: Login com credenciais invalidas
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("senha_invalida")
    driver.find_element(By.ID, "login-button").click()

    mensagem_erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    assert mensagem_erro.is_displayed()
    assert "Username and password do not match any user in this service" in mensagem_erro.text


def test_login_usuario_bloqueado(driver):

    # Cenario: Usuario bloqueado
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    mensagem_erro = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )

    assert mensagem_erro.is_displayed()
    assert "Sorry, this user has been locked out" in mensagem_erro.text
