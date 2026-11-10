# Bryson Otanjah
# CIS256 Fall 2026
# Programming Assignment 5

from flask import Flask, render_template, request

app = Flask(__name__)


# GET request display the empty registration form
@app.route("/register", methods=["GET"])
def show_form():
    return render_template("register.html")


# POST request capture the submitted values
@app.route("/register", methods=["POST"])
def handle_registration():
    full_name = request.form.get("full_name", "").strip()
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")

    # Temporary, no validation or hashing yet
    return render_template(
        "register.html",
        success=True,
        full_name=full_name,
        username=username,
        hashed="(not hashed yet)",
    )


if __name__ == "__main__":
    app.run(debug=True, port=5002)
