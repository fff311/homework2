from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_name_cart(browser, desktop_card_url):
    browser.get(desktop_card_url)
    reviews_tab = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='#tab-description']")
        )
    )
    assert reviews_tab.is_enabled()


def test_add_cart(browser, desktop_card_url):

    browser.get(desktop_card_url)
    add_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-cart")))
    assert add_button.is_enabled()


def test_reviewst(browser, desktop_card_url):
    browser.get(desktop_card_url)
    reviews_tab = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='#tab-review']")
        )
    )
    assert reviews_tab.is_enabled()


def test_compare(browser, desktop_card_url):
    browser.get(desktop_card_url)
    compare_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "[title='Compare this Product']")
        )
    )
    assert compare_button.is_enabled()


def test_apply_button_redirect(browser, desktop_card_url):
    browser.get(desktop_card_url)
    apply_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "a[href*='manufacturer.info']")
        )
    )
    assert apply_button.is_enabled()
