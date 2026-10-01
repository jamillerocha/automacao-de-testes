from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.fixtures.driver import driver


def _login(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))


def test_logout_com_sucesso(driver):

    # Cenario: Logout com sucesso
    _login(driver)

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    logout_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
    )
    logout_link.click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )

    assert driver.current_url == "https://www.saucedemo.com/"


def test_resetar_carrinho(driver):

    # Cenario: Resetar carrinho
    _login(driver)

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    driver.find_element(By.ID, "react-burger-menu-btn").click()

    reset_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "reset_sidebar_link"))
    )
    reset_link.click()

    driver.find_element(By.ID, "react-burger-cross-btn").click()

    carrinho_vazio = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert carrinho_vazio