# Bryson Otanjah
# CIS256 Fall 2026
# Programming Assignment 5

from flask import Flask

app = Flask(__name__) #creates the application

@app.route('/register', methods=['GET']) # sends browser visits to the following function
def show_form():
    return "Registration page - under construction" # !!placeholder!!

if __name__ == "__main__":
    app.run(debug=True, port=5001) # starts server on port 5001