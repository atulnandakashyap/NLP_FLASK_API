from flask import Flask, render_template, request, redirect, session
from db import Database
import api

app = Flask(__name__)
dbo = Database()
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

@app.route("/")
def index():
    session["logged_in"] = 0
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route("/perform_registration", methods=['post'])
def perform_registration():
    name = request.form.get("user_name")
    email = request.form.get("user_email")
    password = request.form.get("user_password")
    response = dbo.insert(name, email, password)
    if response:
        return render_template("login.html", message="Registration successful. Kindly login to proceed.")
    else:
        return render_template("register.html", message="Email already exists")

@app.route("/perform_login", methods=["post"])
def perform_login():
    email = request.form.get("user_email")
    password = request.form.get("user_password")

    response = dbo.search(email, password)

    if response:
        session["logged_in"] = 1
        return redirect("/profile")
    else:
        return render_template("login.html",message = "Incorrect email/password")

@app.route("/profile")
def profile():
    if session["logged_in"] == 1:
        return render_template("profile.html")
    else:
        return redirect("/")

@app.route("/ner")
def ner():
    if session["logged_in"] == 1:
        return render_template("ner.html")
    else:
        return redirect("/")

@app.route("/perform_ner", methods=["post"])
def perform_ner():
    if session["logged_in"] == 1:
        text = request.form.get("ner_text")
        response = api.ner(text)
        return render_template("ner.html",response=response)
    else:
        return redirect("/")

@app.route("/sentiment")
def sentiment():
    if session["logged_in"] == 1:
        return render_template("sentiment.html")
    else:
        return redirect("/")

@app.route("/perform_sentiment_analysis", methods=["post"])
def perform_sentiment_analysis():
    if session["logged_in"] == 1:
        text = request.form.get("text")
        response = api.sentiment_analysis(text)
        return render_template("sentiment.html", response=response)
    else:
        return redirect("/")

@app.route("/abuse")
def abuse():
    if session["logged_in"] == 1:
        return render_template("abuse.html")
    else:
        return redirect("/")

@app.route("/perform_abuse_detection", methods=["post"])
def perform_abuse_detection():
    if session["logged_in"] == 1:
        text = request.form.get("text")
        response = api.abuse_detection(text)
        return render_template("abuse.html", response=response)
    else:
        return redirect("/")

@app.route("/emotion")
def emotion():
    if session["logged_in"] == 1:
        return render_template("emotion.html")
    else:
        return redirect("/")

@app.route("/perform_emotion_detection", methods=["post"])
def perform_emotion_detection():
    if session["logged_in"] == 1:
        text = request.form.get("text")
        response = api.emotion_detection(text)
        return render_template("emotion.html", response=response)
    else:
        return redirect("/")

@app.route("/logout", methods=["post"])
def logout():
    session["logged_in"] = 0
    return redirect("/")

app.run(debug=True)
