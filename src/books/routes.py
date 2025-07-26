from fastapi import APIRouter, status, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from src.books.schemas import Book, BookCreateModel, BookUpdateModel
from src.db.main import get_session
from src.books.service import BookService
from src.auth.dependencies import AccessTokenBearer

book_router = APIRouter()
book_service = BookService()
access_token_bearer = AccessTokenBearer()

@book_router.get('/', response_model=List[Book])
async def get_all_books(
    session: AsyncSession = Depends(get_session), 
    user_details=Depends(access_token_bearer)
):
    print(user_details)
    books = await book_service.get_all_books(session)
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_a_book(
    book_data: BookCreateModel, session: AsyncSession = Depends(get_session),
    user_details=Depends(access_token_bearer)
):
    return await book_service.create_book(book_data, session)

@book_router.get("/{book_uid}", response_model=Book)
async def get_book(
    book_uid: str, 
    session: AsyncSession = Depends(get_session),
    user_details=Depends(access_token_bearer)
):
    book = await book_service.get_book(book_uid, session)
    if book:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.patch("/{book_uid}", response_model=Book)
async def update_book(
    book_uid: str,
    book_update_data: BookUpdateModel,
    session: AsyncSession = Depends(get_session),
    user_details=Depends(access_token_bearer)
):
    updated_book = await book_service.update_book(book_uid, book_update_data, session)
    if updated_book:
        return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@book_router.delete("/{book_uid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_uid: str, 
    session: AsyncSession = Depends(get_session),
    user_details=Depends(access_token_bearer)
):
    deleted = await book_service.delete_book(book_uid, session)
    if deleted:
        return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")