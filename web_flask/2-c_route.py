<<<<<<< HEAD
=======
#!/usr/bin/python3
"""Module of a python script"""

>>>>>>> f8fc929b8545ce466a6173b756146a580a15b191
from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/', strict_slashes=False)
def index():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace("_", " ")
    return f"C {text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
=======
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

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000)
>>>>>>> f8fc929b8545ce466a6173b756146a580a15b191
