import uuid
from src.books.schemas import Book
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from src.reviews.schemas import ReviewModel

class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=30)
    last_name: str = Field(max_length=30)
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)

class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    uid: uuid.UUID
    username: str
    email: str
    first_name: str
    last_name: str
    is_verified: bool 
    password_hash: str = Field(exclude=True)
    created_at: datetime 
    updated_at: datetime

class CreateUserResponse(BaseModel):
    message: str
    user: UserModel

class UserBooksModel(UserModel):
    books: List[Book]
    reviews: List[ReviewModel]

class UserLoginModel(BaseModel):
    email: str = Field(max_length=40)
    password: str = Field(min_length=6)

class EmailModel(BaseModel):
    addresses: List[str]