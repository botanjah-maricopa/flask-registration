# Bryson Otanjah
# CIS256 Fall 2026
# Programming Assignment 5

import re

import bcrypt
from flask import Flask, render_template, request

app = Flask(__name__)


# GET request, display the empty registration form
@app.route("/register", methods=["GET"])
def show_form():
    return render_template("register.html")


# POST request, capture, validate, hash, and confirm
@app.route("/register", methods=["POST"])
def handle_registration():
    # Capture values
    full_name = request.form.get("full_name", "").strip()
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "")
    confirm_password = request.form.get("confirm_password", "")

    # Validate input
    errors = []

    if not full_name:
        errors.append("Full name required.")

    if not re.fullmatch(r"[A-Za-z0-9_]+", username):
        errors.append("Username: only letters, numbers, and underscores.")

    if (
        len(password) < 8
        or not re.search(r"[A-Za-z]", password)
        or not re.search(r"[0-9]", password)
    ):
        errors.append("Password: At least 8 characters long, include both letters and numbers.")

    if password != confirm_password:
        errors.append("Password and confirm password must match.")

    if errors:
        return render_template(
            "register.html",
            errors=errors,
            full_name=full_name,
            username=username,
        )

    # Hash the password
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    # Display confirmation
    return render_template(
        "register.html",
        success=True,
        full_name=full_name,
        username=username,
        hashed=hashed,
    )


# Run the application
if __name__ == "__main__":
    app.run(debug=True, port=5002)
