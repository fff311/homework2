import pytest
import requests

from pydantic import ValidationError

from models import LoginForm


def test_invalid_username(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    with pytest.raises(ValidationError) as exc_info:
        LoginForm(username="user1", password="111")
    errors = exc_info.value.errors()
    assert any(e['loc'] == ('username',) for e in errors)


def test_invalid_password(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    with pytest.raises(ValidationError) as exc_info:
        LoginForm(username="user", password="1112")
    errors = exc_info.value.errors()
    assert any(e['loc'] == ('password',) for e in errors)


def test_invalid_password_username(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    with pytest.raises(ValidationError) as exc_info:
        LoginForm(username="user2", password="1112")
    errors = exc_info.value.errors()
    assert any(e['loc'] == ('password',) for e in errors)
    assert any(e['loc'] == ('username',) for e in errors)


def test_no_username_password(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    with pytest.raises(ValidationError) as exc_info:
        LoginForm(username="", password="")
    errors = exc_info.value.errors()
    assert any(e['loc'] == ('password',) for e in errors)
    assert any(e['loc'] == ('username',) for e in errors)


def test_correct_authorization(browser):
    catalog_path = f"{browser.base_url}administration/"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200

    login_data = LoginForm(username="user", password="111")
    assert login_data.username == "user"
    assert login_data.password == "111"
