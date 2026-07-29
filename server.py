from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import requests

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get("nickname")
        password = request.form.get("password")
        return redirect(url_for('index'))
    return render_template('login.html', title='Аварийный доступ')


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass


if __name__ == "__main__":
    app.run(port=5000)