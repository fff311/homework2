import pytest
import requests

from pydantic import ValidationError

from models import RegistrationForm


def test_without_a_name(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    with pytest.raises(ValidationError) as exc_info:
        RegistrationForm(
            last_name="Шевченко",
            email="shevchenko.asu@yandex.ru",
            password="TestPass123",
            agree=True
        )
    errors = exc_info.value.errors()
    assert any(
        error['loc'] == ('first_name',) and
        error['type'] in ('missing', 'string_too_short')
        for error in errors
    )


def test_without_a_lastname(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    with pytest.raises(ValidationError) as exc_info:
        RegistrationForm(
            first_name="Юлия",
            email="shevchenko.asu@yandex.ru",
            password="TestPass123",
            agree=True
        )
    errors = exc_info.value.errors()
    assert any(
        error['loc'] == ('last_name',) and
        error['type'] in ('missing', 'string_too_short')
        for error in errors
    )


def test_without_email(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    with pytest.raises(ValidationError) as exc_info:
        RegistrationForm(
            first_name="Юлия",
            last_name="Шевченко",
            password="TestPass123",
            agree=True
        )
    errors = exc_info.value.errors()
    assert any(
        error['loc'] == ('email',) and
        error['type'] in ('missing', 'string_too_short')
        for error in errors
    )


def test_without_password(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    with pytest.raises(ValidationError) as exc_info:
        RegistrationForm(
            first_name="Юлия",
            last_name="Шевченко",
            email="shevchenko.asu@yandex.ru",
            agree=True
        )
    errors = exc_info.value.errors()
    assert any(
        error['loc'] == ('password',) and
        error['type'] in ('missing', 'string_too_short')
        for error in errors
    )


def test_min_password_name(browser):
    catalog_path = f"{browser.base_url}/index.php?route=account/register"
    browser.get(catalog_path)
    response = requests.get(catalog_path, timeout=5)
    assert response.status_code == 200
    with pytest.raises(ValidationError) as exc_info:
        RegistrationForm(
            last_name="Шевченко",
            email="shevchenko.asu@yandex.ru",
            password="111",
            agree=True
        )
    errors = exc_info.value.errors()
    assert any(
        error['loc'] == ('password',) and
        error['type'] == 'string_too_short'
        for error in errors
    )
    assert any(
        error['loc'] == ('first_name',) and
        error['type'] == 'missing'
        for error in errors
    )
