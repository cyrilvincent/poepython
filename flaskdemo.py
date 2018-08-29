import flask # pip install Flask

app = flask.Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/html")
def html():
    return """
        <html>
            <body>
                <h1>Hello World<font color="red">!</font></h1>
            </body>
        </html>
    """

import media
import jsonpickle # pip install jsonpickle
@app.route("/mock/<id>", methods=["GET"])
def mock(id):
    book = media.Book(id,"Python",9.99)
    return jsonpickle.encode(book)


app.run()