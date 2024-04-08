#!/usr/bin/python3
"""Module of a python script"""

from flask import Flask

app = Flask(__name__)

@app.route('/',strict_slashes=False)
def home():
    """func to be executed"""
    return "Hello HBNB!"

@app.route('/hbnb',strict_slashes=False)
def hbnb():
    """func to be executed"""
    return "HBNB"

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000)