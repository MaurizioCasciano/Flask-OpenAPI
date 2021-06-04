from flask import Flask

app = Flask(__name__)


@app.get('/')
def hello_world():
    return 'Flask - OpenAPI'


if __name__ == '__main__':
    app.run()
