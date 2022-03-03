from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from api import api

from dotenv import load_dotenv
import queries.insert_queries as insert_queries
import queries.select_queries as select_queries
import queries.update_queries as update_queries
import queries.delete_queries as delete_queries

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
    session['UID'] = 1
    uid = session['UID']
    logged_in_user = select_queries.get_logged_in_user(uid)
    logged_in_user = {'id': 1,
                      'username': 'Zsu',
                      'name': 'Zsuzsanna Juhász',
                      'image_source': 'img/favicon.ico'
                      }
    return render_template('my_leagues.html', logged_in_user=logged_in_user)


if __name__ == '__main__':
    app.run(debug=True,
            port=8000,
            host="0.0.0.0")
