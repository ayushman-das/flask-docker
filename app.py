import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome! (This is the latest update for pipeline test!!)"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":

    app.run()

