<<<<<<< HEAD
=======
#!/usr/bin/python3
"""Module of a python script"""

>>>>>>> f8fc929b8545ce466a6173b756146a580a15b191
from flask import Flask

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/')
def hello():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>')
def number(n):
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
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

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000)
>>>>>>> f8fc929b8545ce466a6173b756146a580a15b191
