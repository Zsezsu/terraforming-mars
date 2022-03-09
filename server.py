from flask import Flask, render_template, request, url_for, redirect, jsonify, session
from dotenv import load_dotenv
from api import api
from mail_system import mail

import profile_manager as pm
from mail_system import send_registration_email as send_mail
import queries.insert_queries as insert_queries
import queries.select_queries as select_queries
import queries.update_queries as update_queries
import queries.delete_queries as delete_queries
import helper


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
    if session['UID']:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('registration'))


@app.route('/profile')
def profile():
    if session['UID']:
        user_data = select_queries.get_user_data(session['UID'])
        return render_template('profile.html', data=user_data)
    else:
        return redirect(url_for('registration'))


@app.route('/league/<league_id>')
def league(league_id):
    # For testing purposes
    logged_in_user_id = session['UID']
    rounds = select_queries.get_rounds_for_league(league_id, logged_in_user_id)
    return render_template('league.html', rounds=rounds, logged_in_user_id=logged_in_user_id)


@app.route('/my-leagues')
def leagues():
    if session['UID']:
        uid = session['UID']
        logged_in_user = select_queries.get_logged_in_user(uid)
        logged_in_user_leagues = select_queries.get_logged_in_user_leagues(uid)
        return render_template('my_leagues.html', logged_in_user=logged_in_user, leagues=logged_in_user_leagues)
    else:
        return redirect(url_for('registration'))


@app.route('/account/signup')
def registration():
    d_error = request.args.get('d_error')
    pictures = select_queries.get_pictures()
    return render_template('profile-register.html', error=d_error, pictures=pictures)


@app.route('/registration-onsubmit', methods=['POST'])
def registration_onsubmit():
    error_message = pm.validate_registration(request.form)
    if error_message == '':
        user_id = pm.submit_registration(request.form)
        user_email = select_queries.get_user_email(user_id)
        send_mail(user_email['email'])
        session['UID'] = user_id
        return redirect(url_for('index'))
    else:
        return redirect(url_for('registration', d_error=error_message))


@app.route('/account/login')
def login():
    error = request.args.get('error')
    return render_template('profile-login.html', error=error)


@app.route('/login-onsubmit', methods=['POST'])
def login_onsubmit():
    if pm.validate_login(request.form):
        session['UID'] = select_queries.get_user_id(request.form['login_token'])['id']
        return render_template('index.html')
    else:
        return redirect(url_for('login', error=True))


@app.route('/logout')
def logout():
    session['UID'] = ''
    return redirect(url_for('index'))


@app.route('/league/<league_id>/round/<round_id>', methods=['GET'])
def results(league_id=1, round_id=2):
    if session['UID']:
        round_data = select_queries.get_round_by_id(round_id)
        round_status = helper.get_round_status(round_data)
        table_headers = helper.create_table_header()
        game_data, players_data, players_in_game, round_points = (None, None, None, None)

        if round_status == 'init_round':
            players_data = select_queries.get_round_players(league_id)
            game_data = {
                "boards": select_queries.get_boards(),
                "expansions": select_queries.get_expansions(),
                "corporations": select_queries.get_corporations()
            }

        elif round_status == 'started':
            players_in_game = select_queries.get_players_in_round(round_id)

        elif round_status == 'finished':
            round_points = select_queries.get_round_points(round_id)

        else:
            return redirect('/')
        return render_template('round_details.html',
                               round_status=round_status,
                               round_points=round_points,
                               table_headers=table_headers,
                               round=round_data,
                               round_id=round_id,
                               league_id=league_id,
                               game=game_data,
                               players=players_data,
                               players_in_game=players_in_game)
    else:
        return redirect(url_for('registration'))


@app.route('/league/<league_id>/round/<round_id>', methods=['POST'])
def init_round(league_id, round_id):
    if session['UID']:
        round_details = request.form
        insert_queries.init_round(round_details, round_id)
        return redirect(f'/league/{league_id}/round/{round_id}')
    else:
        return redirect(url_for('registration'))


if __name__ == '__main__':
    app.run(debug=True,
            port=8000,
            host="0.0.0.0")
