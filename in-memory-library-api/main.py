from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="In-Memory Library API")

# In-memory storage
books_db = []

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


@app.post("/books")
def add_book(book: Book):
    for b in books_db:
        if b["id"] == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")

    books_db.append(book.dict())
    return {"message": "Book added successfully"}


@app.get("/books/{id}")
def get_book(id: int):
    for book in books_db:
        if book["id"] == id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.get("/books")
def get_books(year: int = None):
    if year:
        return [book for book in books_db if book["year"] == year]
    return books_db


@app.delete("/books/{id}")
def delete_book(id: int):
    for book in books_db:
        if book["id"] == id:
            books_db.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
