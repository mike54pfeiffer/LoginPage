from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import make_response
from flask import flash 
from flask import url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/hacker")
def hacker():
    return render_template("hacker.html")

@app.route("/login", methods = ['POST'])
def login():
            fName = request.form['firstName']
            lName = request.form['lastName']
            mail = request.form['email']
            pNumber = request.form['phoneNumber']
            pw = request.form['password']
if __name__ == "__main__":
    app.run(debug=True)