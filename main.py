from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=5000)