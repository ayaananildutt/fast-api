from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field
from typing import Annotated

api = FastAPI()

class Book(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    author: str = Field(min_length=1, max_length=100)
    year: int = Field(ge=1000, le=2025)
    genre: str = Field(min_length=1, max_length=50)

class BookFilter(BaseModel):
    genre: str = "all"
    limit: int = 10
    year: int | None = None

class Review(BaseModel):
    reviewer: str = Field(min_length=1, max_length=100)
    comment: str = Field(min_length=1, max_length=500)
    rating: int = Field(ge=1, le=5)

@api.get('/')
def root():
    return {"message" : "Welcome to the Book Club API"}

@api.get('/status')
def status():
    return {
        "status" : "running",
        "api" : "Book Club"
    }

@api.get('/books/{book_id}')
def get_book(book_id: int = Path(ge=1)):
    return {
        "book_id": book_id,
        "title": f"Book #{book_id}"
    }

@api.get('/books/{book_id}/chapter/{chapter_num}')
def get_chapter(book_id: int = Path(ge=1), chapter_num: int = Path(ge=1, le=100)):
    return {
        "book_id" : book_id,
        "chapter" : chapter_num,
        "content" : f"Chapter {chapter_num} of Book #{book_id}"
    }

@api.get('/books')
def list_books(filters: Annotated[BookFilter, Query()]):
    return {
        "genre": filters.genre,
        "limit": filters.limit,
        "year": filters.year,
        "books": []
    }

@api.get('/search')
def search_books(query: str = Query(min_length=2, max_length=50), limit: int = Query(default=5)):
    return {
        "query": query,
        "limit": limit,
        "results": []
    }

@api.post('/books')
def create_book(book: Book):
    return {
        "message": "Book added",
        "book": book
    }

@api.put('/books/{book_id}')
def update_book(book: Book, book_id: int = Path(ge=1)):
    return {"message" : f"Book #{book_id}",
        "book" : book
    }


@api.post('/books/{book_id}/review')
def add_review(review: Review, book_id: int = Path(ge=1)):
    return {"book_id" : book_id,
        "review" : review
    }


print("branch 1")
