import os

from flask import Flask, session, render_template, jsonify, url_for
from flask_socketio import SocketIO, emit
import requests, json

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":  
    app.run(debug=True)