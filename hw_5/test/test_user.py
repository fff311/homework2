from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_login(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    continue_button = browser.find_element(By.XPATH, "//button[@type='submit' and text()='Continue']")
    assert continue_button.is_enabled()


def test_without_a_name(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    checkbox = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.NAME, "agree"))
    )
    checkbox.click()
    assert checkbox.is_selected()


def test_policy(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    privacy_policy_link = browser.find_element(By.LINK_TEXT, "Privacy Policy")
    assert privacy_policy_link.is_enabled()


def test_login_page(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    privacy_policy_link = browser.find_element(By.LINK_TEXT, "login page")
    assert privacy_policy_link.is_enabled()


def test_subscribe(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    newsletter_toggle = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.form-check-input[name='newsletter']"))
    )
    newsletter_toggle.click()
    assert newsletter_toggle.is_selected()
