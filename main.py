from fastapi import FastAPI
from pydantic import BaseModel

api = FastAPI()

class Book(BaseModel):
    title: str
    author: str
    year: int
    genre: str

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
def get_book(book_id: int):
    return {
        "book_id": book_id,
        "title": f"Book #{book_id}"
    }

@api.get('/books/{book_id}/chapter/{chapter_num}')
def get_chapter(book_id: int, chapter_num: int):
    return {
        "book_id" : book_id,
        "chapter" : chapter_num,
        "content" : f"Chapter {chapter_num} of Book #{book_id}"
    }

@api.get('/books')
def list_books(genre: str | None = "all", limit: int | None = 10):
    return {
        "genre": genre,
        "limit": limit,
        "books": []
    }

@api.get('/search')
def search_books(query: str, limit: int | None = 5):
    return {
        "query": query,
        "limit": limit,
        "results": []
    }

@api.post('/books')
def create_book(book: Book):
    return {
        "message": "Book added",
        "book": {
            "title" : book.title,
            "author" : book.author,
            "year" : book.year,
            "genre" : book.genre
        }
    }
