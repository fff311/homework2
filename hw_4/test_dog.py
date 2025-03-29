import pytest
import requests
from .pydantik import BreedListResponse, ImageResponse, ErrorResponse, ImageListResponse
from pydantic import ValidationError

BASE_URL = 'https://dog.ceo/api'


def test_api_base_status():
    response = requests.get(f'{BASE_URL}/breeds/list/all')
    assert response.status_code == 200

    try:
        response_data = BreedListResponse.model_validate(response.json())
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert response_data.status == 'success'


def test_random_dog_image():
    response = requests.get(f'{BASE_URL}/breeds/image/random')
    assert response.status_code == 200

    try:
        response_data = ImageResponse.model_validate(response.json())
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert response_data.status == 'success'
    assert response_data.message.endswith(('.jpg', '.png', '.jpeg'))


def test_non_existent_breed_returns_error():
    response = requests.get(f'{BASE_URL}/breed/mcnab/images/random')
    assert response.status_code == 404

    try:
        response_data = ErrorResponse.model_validate(response.json())
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert response_data.status == 'error'


@pytest.mark.parametrize('breed', [
    'labradoodle',
    'bulldog',
    'poodle',
    'chow',
    'danish'
])
def test_breed_images_endpoint_returns_non_empty_list(breed):
    response = requests.get(f'{BASE_URL}/breed/{breed}/images')
    assert response.status_code == 200

    try:
        response_data = ImageListResponse.model_validate(response.json())
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert isinstance(response_data.message, list)
    assert len(response_data.message) > 0


@pytest.mark.parametrize('breed', [
    'akita',
    'germanshepherd',
    'husky',
    'leonberg',
    'spaniel'
])
def test_breed_exists_in_master_list(breed):
    response = requests.get(f'{BASE_URL}/breeds/list/all')
    assert response.status_code == 200

    try:
        response_data = BreedListResponse.model_validate(response.json())
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert breed in response_data.message.keys()
