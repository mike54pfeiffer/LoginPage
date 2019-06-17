from flask import Flask, render_template, request, redirect, make_response, flash, url_for, Response
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginSuccess", methods = ['POST'])
def loginSuccess():
            mail = request.form['email']
            pword = request.form['password']
            print("User logged in with: " + mail + " | " + pword)
            return render_template("loginSuccess.html", email = mail, password = pword)
if __name__ == "__main__":
    app.run(debug=True)