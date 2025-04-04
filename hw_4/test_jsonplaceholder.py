import requests
import pytest
from .pydantik import PostsResponseModel, PostModel, CommentsResponseModel, UserModel
from pydantic import ValidationError

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_all_posts():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200

    try:
        posts = PostsResponseModel.model_validate(response.json())
        assert len(posts.root) > 0
    except ValidationError as e:
        pytest.fail(f"Posts validation failed: {e}")


@pytest.mark.parametrize("post_id", [1, 5, 10, 50, 100])
def test_get_single_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200

    try:
        post = PostModel.model_validate(response.json())
        assert post.id == post_id
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")


def test_get_post_comments():
    response = requests.get(f"{BASE_URL}/posts/1/comments")
    assert response.status_code == 200

    try:
        comments = CommentsResponseModel.model_validate(response.json())
        assert len(comments.root) > 0
    except ValidationError as e:
        pytest.fail(f"Comments validation failed: {e}")


@pytest.mark.parametrize("user_id", [1, 3, 5, 7, 10])
def test_get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200

    try:
        user = UserModel.model_validate(response.json())
        assert user.id == user_id
    except ValidationError as e:
        pytest.fail(f"User validation failed: {e}")


def test_create_post():
    new_post = {
        "title": "Test Post",
        "body": "This is a test post body",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201

    try:
        created_post = PostModel.model_validate(response.json())
        assert created_post.title == new_post["title"]
        assert created_post.userId == new_post["userId"]
    except ValidationError as e:
        pytest.fail(f"Created post validation failed: {e}")
