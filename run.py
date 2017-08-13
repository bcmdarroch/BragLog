#!../flask/bin/python

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Brag Log: log your brags! you did it!"

if __name__ == "__main__":
    app.run(debug=True)
