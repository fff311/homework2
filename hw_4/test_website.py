import pytest
import requests

def test_url_status_code(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code

@pytest.mark.parametrize("url, status_code", [
    ("https://ya.ru/sfhfhfhfhfhfhfhfh", 404),
    ("https://google.com", 200)
])
def test_multiple_urls(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code
