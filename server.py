from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from dotenv import load_dotenv
from api import api
from mail_system import mail

import profile_manager as pm
import queries.insert_queries as insert_queries
import queries.select_queries as select_queries
import queries.update_queries as update_queries
import queries.delete_queries as delete_queries


load_dotenv()
app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(mail)

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


@app.route('/league/<league_id>')
def league(league_id):
    # For testing purposes
    return f'League {league_id}'


@app.route('/my-leagues')
def leagues():
    uid = session['UID']
    logged_in_user = select_queries.get_logged_in_user(uid)
    logged_in_user = session['logged_in_user'] # DUMMY DATA----------------------------------------------
    logged_in_user_leagues = select_queries.get_logged_in_user_leagues(uid)
    return render_template('my_leagues.html', logged_in_user=logged_in_user, leagues=logged_in_user_leagues)


@app.route('/account/signup')
def registration():
    d_error = request.args.get('d_error')
    return render_template('profile-register.html', error=d_error)


@app.route('/registration-onsubmit', methods=['POST'])
def registration_onsubmit():
    print(request.form)
    error_message = pm.validate_registration(request.form)
    if error_message == '':
        user_id = pm.submit_registration(request.form)
        session['UID'] = user_id
        return render_template('index.html')
    else:
        return redirect(url_for('registration', d_error=error_message))


@app.route('/account/login')
def login():
    pass


@app.route('/logout')
def logout():
    pass


if __name__ == '__main__':
    app.run(debug=True,
            port=8000,
            host="0.0.0.0")
