from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import Optional

class RegistrationForm(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=32)
    last_name: str = Field(..., min_length=1, max_length=32)
    email: str
    password: str = Field(..., min_length=4, max_length=20)
    confirm_password: str
    agree_privacy_policy: bool = Field(..., alias="agree")

    @field_validator('confirm_password')
    def passwords_match(cls, v: str, values) -> str:
        if 'password' in values.data and v != values.data['password']:
            raise ValueError("Passwords do not match!")
        return v


class LoginForm(BaseModel):
    username: str
    password: str

    @field_validator('username')
    def validate_username(cls, v):
        if v != "user":
            raise ValueError('No match for Username and/or Password.')
        return v

    @field_validator('password')
    def validate_password(cls, v):
        if v != "111":
            raise ValueError('No match for Username and/or Password.')
        return v
