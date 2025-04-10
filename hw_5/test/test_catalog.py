from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_mac_filter(browser):
    catalog_path = f"{browser.base_url}/en-gb/catalog/desktops/mac"
    browser.get(catalog_path)
    products = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-thumb h4 a")))
    assert any("imac" in product.text.lower() for product in products)


def test_empty_category(browser):
    catalog_path = f"{browser.base_url}/en-gb/catalog/absence"
    browser.get(catalog_path)
    products = browser.find_elements(By.CSS_SELECTOR, ".product-thumb")
    assert len(products) == 0


def test_show_filter(browser):
    quantity = 10
    catalog_path = f"{browser.base_url}en-gb/catalog/desktops?limit={quantity}"
    browser.get(catalog_path)
    products = browser.find_elements(By.CSS_SELECTOR, ".product-thumb")
    assert len(products) <= quantity


def test_desktops(browser, desktop_catalog_url):
    browser.get(desktop_catalog_url)
    compare_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "[title='Desktops']")
        )
    )
    assert compare_button.is_enabled()


def test_grid(browser, desktop_catalog_url):
    browser.maximize_window()
    browser.get(desktop_catalog_url)
    login_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "[title='Grid']")
        )
    )
    assert login_button.is_enabled()


def test_list(browser, desktop_catalog_url):
    browser.maximize_window()
    browser.get(desktop_catalog_url)
    login_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "[title='List']")
        )
    )
    assert login_button.is_enabled()
