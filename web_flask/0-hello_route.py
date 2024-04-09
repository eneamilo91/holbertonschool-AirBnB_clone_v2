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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
=======
@app.route('/',strict_slashes=False)
def home():
    """func to be executed"""
    return "Hello HBNB!"

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000)
>>>>>>> f8fc929b8545ce466a6173b756146a580a15b191
