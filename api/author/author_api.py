import json

from flask import Blueprint, Response

from domain.author import Author

author = Blueprint("author", __name__, url_prefix="/authors")


@author.get("/")
def authors():
    authors: list[Author] = []

    for i in range(10):
        author: Author = Author(str(i), "Author " + str(i))
        authors.append(author)

    authors_dicts = [author.__dict__ for author in authors]
    return Response(json.dumps(authors_dicts), mimetype="application/json")
