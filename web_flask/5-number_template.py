from flask import Flask, render_template

app = Flask(__name__)

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
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        return 'Invalid input'

@app.route('/number_template/<int:n>')
def number_template(n):
    if isinstance(n, int):
        return render_template('5-number.html', number=n)
    else:
        return 'Invalid input'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)