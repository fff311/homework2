from pydantic import BaseModel, ValidationError, field_validator, RootModel
from typing import Dict, List, Optional


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


class PostModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class PostsResponseModel(RootModel):
    root: List[PostModel]


class CommentModel(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class CommentsResponseModel(RootModel):
    root: List[CommentModel]


class UserModel(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: dict
    phone: str
    website: str
    company: dict
