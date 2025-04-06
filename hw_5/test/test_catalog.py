import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_mac_filter(browser):
    catalog_path = f"{browser.base_url}/en-gb/catalog/desktops/mac"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200

    products = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-thumb h4 a")))
    assert len(products) > 0
    assert any("imac" in product.text.lower() for product in products)


def test_show_filter(browser):
    quantity = 10
    catalog_path = f"{browser.base_url}en-gb/catalog/desktops?limit={quantity}"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-thumb"))
    )
    products = browser.find_elements(By.CSS_SELECTOR, ".product-thumb")
    assert len(products) <= quantity


def test_sort_filter(browser):
    sort = 'pd.name'
    order = 'ASC'
    quantity = 25
    catalog_path = f"{browser.base_url}en-gb/catalog/desktops?sort={sort}&order={order}&limit={quantity}"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    WebDriverWait(browser, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".product-thumb"))
    )
    products = browser.find_elements(By.CSS_SELECTOR, ".product-thumb")
    product_data = []
    for product in products:
        if sort == 'pd.name':
            value = product.find_element(By.CSS_SELECTOR, "h4 a").text.strip().lower()
        elif sort == 'rating':
            value = float(product.find_element(By.CSS_SELECTOR, ".rating .rating-value").text)
        elif sort == 'p.model':
            value = product.find_element(By.CSS_SELECTOR, ".model").text.strip().lower()
        product_data.append(value)
    sorted_asc = sorted(product_data)
    sorted_desc = sorted(product_data, reverse=True)
    if order == 'ASC':
        assert sorted_asc
    else:
        assert sorted_desc


def test_pagination(browser):
    catalog_path = f"{browser.base_url}en-gb/catalog/desktops?limit=10"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    products_page1 = WebDriverWait(browser, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-thumb"))
    )
    assert len(products_page1) == 10
    page1_products = [p.text.split('\n')[0] for p in products_page1 if p.text.strip()]
    pagination = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".pagination"))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", pagination)
    time.sleep(1)
    next_page = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//ul[@class='pagination']//a[contains(text(),'>') or contains(text(),'Next')]"))
    )
    browser.execute_script("arguments[0].click();", next_page)
    WebDriverWait(browser, 15).until(
        lambda d: "page=2" in d.current_url or "page/2" in d.current_url
    )
    products_page2 = WebDriverWait(browser, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-thumb"))
    )
    assert len(products_page2) > 0
    page2_products = [p.text.split('\n')[0] for p in products_page2 if p.text.strip()]

    common_products = set(page1_products) & set(page2_products)
    assert len(common_products) == 0


def test_empty_category(browser):
    catalog_path = f"{browser.base_url}/en-gb/catalog/absence"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 404
