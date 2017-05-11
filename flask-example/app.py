"""A simple flask application for test."""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    """Main function to run when accessed."""
    return "Hello World"

if __name__ == "__main__":
    app.run("0.0.0.0")
