from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from pydantic import BaseModel

from database import Book, SessionLocal, create_tables

app = FastAPI()

create_tables()  # Create tables on app startup

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic schema for data validation
class BookSchema(BaseModel):
    title: str
    author: str
    category: str

    class Config:
        orm_mode = True

@app.get("/books")
def read_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

@app.get("/books/{title}")
def read_book(title: str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.title.ilike(title)).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books/create_book")
def create_book(book: BookSchema, db: Session = Depends(get_db)):
    existing_book = db.query(Book).filter(Book.title.ilike(book.title)).first()
    if existing_book:
        raise HTTPException(status_code=400, detail="Book already exists")
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.put("/books/update_book")
def update_book(book: BookSchema, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.title.ilike(book.title)).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db_book.author = book.author
    db_book.category = book.category
    db.commit()
    db.refresh(db_book)
    return db_book

@app.delete("/books/delete_book/{title}")
def delete_book(title: str, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.title.ilike(title)).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(db_book)
    db.commit()
    return {"message": f"Book '{title}' deleted successfully"}
