from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



def test_invalid_username(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    browser.find_element(By.NAME, "username").send_keys("user1")
    browser.find_element(By.NAME, "password").send_keys("111")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "administration" in browser.current_url


def test_invalid_password(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("1112")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    assert "administration" in browser.current_url


def test_no_username_password(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    login_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    assert login_button.is_enabled()


def test_correct_authorization(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("111")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_blocks = browser.find_elements(By.CSS_SELECTOR, ".alert-danger, .text-danger")
    assert len(error_blocks) == 0


def test_invalid_password_username(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    browser.find_element(By.NAME, "username").send_keys("user2")
    browser.find_element(By.NAME, "password").send_keys("1112")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    error_msg = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
    ).text
    assert "No match for Username and/or Password" in error_msg
