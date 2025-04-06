import requests, re, time, pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_name_cart(browser):
    cart = 'ipod-classic'
    catalog_path = f"{browser.base_url}/en-gb/product/mp3-players/{cart}"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    product = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1, .product-name, .title")))
    assert cart.replace('-', ' ') in product.text.strip().lower()


def test_add_cart(browser):
    cart = 'ipod-classic'
    catalog_path = f"{browser.base_url}/en-gb/product/mp3-players/{cart}"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    add_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#button-cart, .btn-cart, .add-to-cart, .btn-primary"))
    )
    time.sleep(1)
    add_button.click()
    success_message = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )
    product = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1, .product-name, .title")))
    assert f"Success: You have added {product.text.strip()} to your shopping cart!" in success_message.text


def test_reviewst(browser):
    cart = 'ipod-classic'
    catalog_path = f"{browser.base_url}/en-gb/product/mp3-players/{cart}"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    reviews_tab = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[href='#tab-review'], .nav-tabs li:last-child a, .review-tab")
        )
    )
    browser.execute_script("arguments[0].scrollIntoView();", reviews_tab)
    time.sleep(0.5)
    reviews_tab.click()
    no_reviews_message = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#tab-review p:first-child, .no-reviews")
        )
    )
    assert "There are no reviews for this product." in no_reviews_message.text


def test_compare(browser):
    cart = 'ipod-classic'
    catalog_path = f"{browser.base_url}/en-gb/product/mp3-players/{cart}"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    compare_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "[title='Compare this Product'], [data-original-title='Compare this Product'], .compare-button")
        )
    )
    action = ActionChains(browser)
    action.move_to_element(compare_button).perform()
    time.sleep(1)  # Даем время для появления подсказки
    browser.execute_script("arguments[0].scrollIntoView();", compare_button)
    time.sleep(0.5)
    compare_button.click()
    success_message = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".alert-success, .success:not([style*='display: none'])")
        )
    )
    product = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "h1, .product-name, .title")))
    assert f"Success: You have added {product.text.strip()} to your product comparison!" in success_message.text


def test_apply_button_redirect(browser):
    cart = 'ipod-classic'
    catalog_path = f"{browser.base_url}/en-gb/product/mp3-players/{cart}"
    expected_url = f"{browser.base_url}en-gb/apple?route=product/manufacturer.info"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    apply_button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "a[href*='manufacturer.info'], "
             ".apply-btn, "
             "button[onclick*='apply'], "
             "input[value='Apply']")
        )
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", apply_button)
    time.sleep(0.5)
    current_url = browser.current_url
    try:
        apply_button.click()
    except:
        browser.execute_script("arguments[0].click();", apply_button)
    WebDriverWait(browser, 15).until(
        lambda d: d.current_url != current_url
    )
    assert expected_url in browser.current_url



