import json

from flask import Blueprint, Response

from domain.book import Book

book = Blueprint("book", __name__, url_prefix="/books")


@book.get("/")
def books():
    books: list[Book] = []

    for i in range(10):
        book: Book = Book(str(i), "Book " + str(i))
        books.append(book)

    books_dicts = [book.__dict__ for book in books]
    return Response(json.dumps(books_dicts), mimetype="application/json")
