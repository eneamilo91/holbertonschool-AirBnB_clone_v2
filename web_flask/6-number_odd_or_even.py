#!/usr/bin/python3
"""Module of a python script"""

from flask import *

app = Flask(__name__)

@app.route('/',strict_slashes=False)
def home():
    """func to be executed"""
    return "Hello HBNB!"

@app.route('/hbnb',strict_slashes=False)
def hbnb():
    """func to be executed"""
    return "HBNB"

@app.route('/c/<text>',strict_slashes=False)
def cisvariable(text):
    """func to be executed"""
    text=text.replace("_", " ")
    return f"C {text}"

@app.route('/python/<text>',strict_slashes=False)
def pythonisvariable(text = "is cool"):
    """func to be executed"""
    if text:
        text=text.replace("_", " ")
        return f"Python {text}"
    return f"Python {text}"


@app.route('/number/<int:n>',strict_slashes=False)
def number(n):
    """func to be executed"""

    return f"{n} is a number"


@app.route('/number_template/<int:n>',strict_slashes=False)
def number(n):
    """func to be executed"""

    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>',strict_slashes=False)
def number(n):
    """func to be executed"""

    return render_template("6-number_odd_or_even.html", n=n)

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000)