import os

from flask import Flask, session, request, render_template, jsonify, url_for
from flask_session import Session
from flask_socketio import SocketIO, emit
import requests, json

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


curUser = []

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET","POST"])
def login():

    session.logged_in = True

    curUser = request.form.get("username") 
    session["curUser"] = curUser

    return render_template("index.html", curUser=curUser)


@app.route("/logout")
def logout():

    session.logged_in = False

    curUser = []
    session["curUser"] = []

    return render_template("index.html", curUser=curUser)

if __name__ == "__main__":  
    app.run(debug=True)