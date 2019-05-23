from flask import Flask, render_template, request, redirect, make_response, flash, url_for, Response

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
            fName = request.form['firstName']
            lName = request.form['lastName']
            mail = request.form['email']
            pNumber = request.form['phoneNumber']
            pw = request.form['password']
            print("User logged in with: " + fName + " " + lName + " | " + mail)
            print("Phone number: " + pNumber)
            print("Password: " + pw)
            return render_template("loginSuccess.html", firstName = fName, lastName = lName, 
            email = mail, phoneNumber = pNumber, password = pw)
if __name__ == "__main__":
    app.run(debug=True)