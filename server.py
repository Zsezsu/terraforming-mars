from flask import Flask, render_template, request, url_for, redirect, jsonify
from api import api

from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.register_blueprint(api)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/design')
def design():
    return render_template('design/design.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/my-leagues')
def leagues():
    return render_template('my_leagues.html')


if __name__ == '__main__':
    app.run(debug=True,
            port=8000,
            host="0.0.0.0")
