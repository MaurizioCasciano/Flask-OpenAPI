from flask import Flask
from api.author.author_api import author
from api.book.book_api import book

app = Flask(__name__)
app.register_blueprint(author, url_prefix="/authors")
app.register_blueprint(book, url_prefix="/books")


@app.get('/')
def hello_world():
    return 'Flask - OpenAPI'


if __name__ == '__main__':
    app.run()
