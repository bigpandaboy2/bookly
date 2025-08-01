import uuid
from pydantic import BaseModel
from datetime import datetime
from typing import List
from src.reviews.schemas import ReviewModel

class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str
    created_at: datetime
    updated_at: datetime

class BookDetailModel(Book):
    reviews: List[ReviewModel]

class BookCreateModel(BaseModel):
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str

class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str