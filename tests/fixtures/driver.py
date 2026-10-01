# tests/fixtures/driver.py
import os
import tempfile
import pytest
from selenium import webdriver


def create_driver():
    options = webdriver.ChromeOptions()

    # Perfil limpo a cada execução
    options.add_argument(f"--user-data-dir={tempfile.mkdtemp()}")

    # Desativa gerenciador de senhas, detecção de senha vazada e safe browsing
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False,
        "profile.default_content_setting_values.notifications": 2,
    })
    options.add_argument("--disable-features=PasswordLeakDetection")

    # Sem notificações, infobars e extensões
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # No GitHub Actions (CI=true), roda sem interface gráfica
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    return webdriver.Chrome(options=options)


@pytest.fixture
def driver():
    d = create_driver()
    yield d
    d.quit()