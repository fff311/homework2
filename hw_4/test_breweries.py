import pytest
import requests
from pydantic import BaseModel, ValidationError, RootModel
from typing import Optional, List

BASE_URL = 'https://api.openbrewerydb.org/v1'


class BreweryModel(BaseModel):
    id: str
    name: str
    brewery_type: str
    city: str
    state: str
    country: Optional[str] = None
    postal_code: Optional[str] = None
    website_url: Optional[str] = None


class BreweryListModel(RootModel):
    root: List[BreweryModel]


@pytest.mark.parametrize('brewery_id', [
    '5128df48-79fc-4f0f-8b52-d06be54d0cec',
    '9c5a66c8-cc13-416f-a5d9-0a769c87d318',
    '232e8f62-9afc-45f5-b4bc-582c26b5c43b'
])
def test_single_brewery(brewery_id):
    response = requests.get(f'{BASE_URL}/breweries/{brewery_id}')
    data = response.json()

    assert response.status_code == 200
    assert data['id'] == brewery_id

    try:
        BreweryModel.model_validate(data)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")


@pytest.mark.parametrize('city', [
    'San Diego',
    'Mount Pleasant',
    'Austintown',
    'Norman'
])
def test_breweries_by_city(city):
    response = requests.get(f'{BASE_URL}/breweries?by_city={city}')
    breweries = response.json()

    assert response.status_code == 200
    assert all(brewery['city'] == city for brewery in breweries)

    try:
        BreweryListModel.model_validate(breweries)
    except ValidationError as e:
        pytest.fail(f"List validation failed: {e}")


def test_no_breweries_for_non_existing_country():
    response = requests.get(f'{BASE_URL}/breweries?by_country=greece')
    breweries = response.json()

    assert response.status_code == 200
    assert len(breweries) == 0

    try:
        BreweryListModel.model_validate(breweries)
    except ValidationError as e:
        pytest.fail(f"Empty list validation failed: {e}")


def test_specific_brewery_name():
    brewery_id = 'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0'
    response = requests.get(f'{BASE_URL}/breweries/{brewery_id}')
    brewery_data = response.json()

    assert response.status_code == 200
    assert isinstance(brewery_data['name'], str)

    try:
        BreweryModel.model_validate(brewery_data)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")


@pytest.mark.parametrize('brewery_type', [
    'micro',
    'nano',
    'regional'
])
def test_breweries_by_type(brewery_type):
    response = requests.get(f'{BASE_URL}/breweries?by_type={brewery_type}')
    breweries = response.json()

    assert response.status_code == 200
    assert len(breweries) > 0
    assert all(brewery['brewery_type'] == brewery_type for brewery in breweries)

    try:
        BreweryListModel.model_validate(breweries)
    except ValidationError as e:
        pytest.fail(f"List validation failed: {e}")


def test_non_existent_brewery():
    response = requests.get(f'{BASE_URL}/breweries/b5444444b16e1-ac3b-4bff-a11f-f7ae9ddc27e0')
    assert response.status_code == 404


def test_pagination():
    per_page = 3
    response = requests.get(f'{BASE_URL}/breweries?per_page={per_page}')
    breweries = response.json()

    assert response.status_code == 200
    assert len(breweries) == per_page

    try:
        BreweryListModel.model_validate(breweries)
    except ValidationError as e:
        pytest.fail(f"List validation failed: {e}")
