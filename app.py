# Bryson Otanjah
# CIS256 Fall 2026
# Programming Assignment 5

from flask import Flask, render_template

app = Flask(__name__)


# GET request displays the empty registration form
@app.route("/register", methods=["GET"])
def show_form():
    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)