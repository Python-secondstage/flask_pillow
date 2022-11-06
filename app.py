from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def show_form():
    return render_template("index.html")


@app.route("/upload", method=["POST"])
def upload():
    return "Hello Upload"


if __name__ == "__main__":
    app.run(debug=True)
