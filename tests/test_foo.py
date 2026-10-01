from selenium import webdriver
import time


def test_navegacao():
    # Inicializa o ChromeDriver automaticamente
    driver = webdriver.Edge()

    try:
        # 1. Abre a URL inicial
        driver.get("https://example.com")
        time.sleep(2)  # Pausa apenas para você visualizar a ação

    finally:
        # Fecha o navegador e encerra o processo
        driver.quit()
