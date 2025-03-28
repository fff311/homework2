import pytest
import requests
from pydantic import BaseModel, ValidationError, field_validator
from typing import Dict, List, Optional

BASE_URL = 'https://dog.ceo/api'


class BaseResponse(BaseModel):
    status: str
    message: Optional[str] = None


class BreedListResponse(BaseResponse):
    message: Dict[str, List[str]]


class ImageResponse(BaseResponse):
    message: str


class ImageListResponse(BaseResponse):
    message: List[str]


class ErrorResponse(BaseModel):
    status: str
    message: str
    code: Optional[int] = None

    @field_validator('code')
    def check_code_match_status(cls, v, info):
        if v is not None and info.data.get('status') == 'error':
            assert v >= 400, "Error code should be >= 400"
        return v


def test_api_base_status():
    response = requests.get(f'{BASE_URL}/breeds/list/all')
    response_data = response.json()

    assert response.status_code == 200

    try:
        BreedListResponse.model_validate(response_data)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert response_data['status'] == 'success'


def test_random_dog_image():
    response = requests.get(f'{BASE_URL}/breeds/image/random')
    response_data = response.json()

    assert response.status_code == 200

    try:
        ImageResponse.model_validate(response_data)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert response_data['status'] == 'success'
    assert response_data['message'].endswith(('.jpg', '.png', '.jpeg'))


def test_non_existent_breed_returns_error():
    response = requests.get(f'{BASE_URL}/breed/mcnab/images/random')
    response_data = response.json()

    assert response.status_code == 404

    try:
        ErrorResponse.model_validate(response_data)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert response_data['status'] == 'error'


@pytest.mark.parametrize('breed', [
    'labradoodle',
    'bulldog',
    'poodle',
    'chow',
    'danish'
])
def test_breed_images_endpoint_returns_non_empty_list(breed):
    response = requests.get(f'{BASE_URL}/breed/{breed}/images')
    response_data = response.json()

    assert response.status_code == 200

    try:
        ImageListResponse.model_validate(response_data)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert isinstance(response_data['message'], list)
    assert len(response_data['message']) > 0


@pytest.mark.parametrize('breed', [
    'akita',
    'germanshepherd',
    'husky',
    'leonberg',
    'spaniel'
])
def test_breed_exists_in_master_list(breed):
    response = requests.get(f'{BASE_URL}/breeds/list/all')
    response_data = response.json()

    assert response.status_code == 200

    try:
        BreedListResponse.model_validate(response_data)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")

    assert breed in response_data['message'].keys()
