import requests
from selenium.webdriver.common.by import By


def test_search_field(browser):
    browser.get(browser.base_url)
    response = requests.get(browser.base_url, timeout=5)
    assert response.status_code == 200
    search = browser.find_element(By.NAME, "search")
    assert search.is_displayed()
    assert search.get_attribute("placeholder") == "Search"


def test_link(browser):
    browser.get(browser.base_url)
    response = requests.get(browser.base_url, timeout=5)
    assert response.status_code == 200
    links = browser.find_elements(By.TAG_NAME, 'a')
    assert len(links) > 0


def test_img(browser):
    browser.get(browser.base_url)
    response = requests.get(browser.base_url, timeout=5)
    assert response.status_code == 200
    links = browser.find_elements(By.TAG_NAME, 'img')
    assert len(links) > 0


def test_image_carousel(browser):
    browser.get(browser.base_url)
    response = requests.get(browser.base_url, timeout=5)
    assert response.status_code == 200
    carousel = browser.find_elements(By.CSS_SELECTOR, ".carousel, .slider, [data-ride='carousel']")
    assert len(carousel) > 0


def test_navigation_menu(browser):
    browser.get(browser.base_url)
    response = requests.get(browser.base_url, timeout=5)
    assert response.status_code == 200
    menu_items = browser.find_elements(By.CSS_SELECTOR, "nav ul li a")
    assert len(menu_items) > 0
