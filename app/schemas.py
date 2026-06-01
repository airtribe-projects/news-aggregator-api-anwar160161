from pydantic import BaseModel, EmailStr
from typing import List


class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class PreferenceRequest(BaseModel):
    categories: List[str]