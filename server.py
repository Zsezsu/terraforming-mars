import os, secrets
import logging, traceback
from werkzeug.exceptions import HTTPException
from flask import Flask, render_template, request, url_for, redirect, session
from dotenv import load_dotenv
from api import api

import profile_manager as pm
from mail_system import send_registration_email as send_mail
from queries import insert_queries
from queries import select_queries
import helper


load_dotenv()
app = Flask(__name__)
app.register_blueprint(api)
app.secret_key = os.getenv("FLASK_SECRET_KEY") or secrets.token_hex(32)
logging.basicConfig(level=logging.INFO)


def _render_safe_error(message: str = "Something went wrong. Please try again later.", code: int = 500):
    """
    Safely render a user-friendly error response.

    Tries to render a shared error template with the provided message and HTTP
    status code. If template rendering itself fails (e.g., missing template),
    it falls back to returning a plain-text response to guarantee a reply.

    Args:
        message (str): Human-friendly message to display to the user.
        code (int): HTTP status code to return (e.g., 404, 500).

    Returns:
        tuple[flask.wrappers.Response, int]:
            A Flask response (HTML or plain text) and the HTTP status code.

    Notes:
        - Requires `render_template` to be imported.
        - This helper never raises; it always returns a response.
    """
    try:
        return render_template("error.html", message=message), code
    except Exception:
        return message, code


@app.errorhandler(HTTPException)
def handle_http_error(e: HTTPException):
    """
    Global handler for Werkzeug/Flask HTTPExceptions (e.g., 404, 403).

    Logs the HTTP error with path context and returns a friendly page using the
    exception's status code. Avoids exposing internal details to the end user.

    Args:
        e (HTTPException): The raised HTTP-related exception.

    Returns:
        tuple[flask.wrappers.Response, int]:
            A user-friendly error page and the original HTTP status code.

    Side Effects:
        - Writes a warning entry to the Flask app logger.

    Examples:
        - Missing route -> 404 Not Found
        - Forbidden access -> 403 Forbidden
    """
    app.logger.warning(f"HTTP error {e.code} at {request.path}: {e.description}")
    return _render_safe_error(message="Oops! That page isn’t available.", code=e.code)


@app.errorhandler(Exception)
def handle_exception(e: Exception):
    """
    Catch-all handler for any uncaught non-HTTP exceptions.

    Captures the full traceback and logs it as an error, then returns a generic
    500 response without leaking internal details to the client. This prevents
    the app from crashing and provides a consistent failure experience.

    Args:
        e (Exception): The unexpected exception that was not handled elsewhere.

    Returns:
        tuple[flask.wrappers.Response, int]:
            A generic error page and HTTP 500 status code.

    Side Effects:
        - Writes a detailed error (including traceback) to the Flask app logger.

    Notes:
        - Ensure `import traceback` is available at module scope.
        - In production, set `debug=False` so Flask does not override this with
          its own debugger/traceback page.
    """
    app.logger.error(
        "Unhandled exception at %s\n%s",
        request.path,
        "".join(traceback.format_exception(type(e), e, e.__traceback__)),
    )
    return _render_safe_error()


@app.route('/')
def index():
    if session.get('UID'):
        return redirect(url_for('dashboard'))
    else:
        return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    if session.get('UID'):
        username = session['USERNAME']
        return render_template('dashboard.html', username=username)
    else:
        return redirect(url_for('login'))


@app.route('/design')
def design():
    return render_template('design/design.html')


@app.route('/profile')
def profile():
    if session['UID']:
        user_data = select_queries.get_user_data(session['UID'])
        username = session['USERNAME']
        return render_template('profile.html', data=user_data, username=username, user_id=session['UID'])
    else:
        return redirect(url_for('login'))


@app.route('/league/<league_id>')
def league(league_id):
    if session.get('UID'):
        logged_in_user_id = session.get('UID')
        rounds = select_queries.get_rounds_for_league(league_id)
        user_is_admin = logged_in_user_id == rounds[0]['league_admin']
        return render_template('league.html', rounds=rounds, user_is_admin=user_is_admin)
    else:
        return redirect(url_for('index'))


@app.route('/my-leagues')
def leagues():
    if session.get('UID'):
        uid = session.get('UID')
        game_types = select_queries.get_game_types()
        logged_in_user = select_queries.get_logged_in_user(uid)
        logged_in_user_leagues = select_queries.get_logged_in_user_leagues(uid)
        username = session['USERNAME']
        return render_template(
            'my_leagues.html',
            game_types=game_types,
            logged_in_user=logged_in_user,
            leagues=logged_in_user_leagues,
            username=username
        )
    else:
        return redirect(url_for('login'))


@app.route('/account/signup')
def registration():
    if session.get('UID'):
        return redirect(url_for('dashboard'))
    else:
        d_error = request.args.get('d_error')
        pictures = select_queries.get_pictures()
        return render_template('profile-register.html', error=d_error, pictures=pictures)


@app.route('/registration-onsubmit', methods=['POST'])
def registration_onsubmit():
    error_message = pm.validate_registration(request.form)
    if error_message == '':
        user_id = pm.submit_registration(request.form)
        user_email = select_queries.get_user_email(user_id)['email']
        username = select_queries.get_user_data(user_id)['username']
        session['UID'] = user_id
        session['USERNAME'] = username
        
        try:
            send_mail(user_email, username)
        except Exception as e:
            app.logger.warning(f"Registration email failed for {user_email}: {e}")
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('registration', d_error=error_message))


@app.route('/account/login')
def login():
    if session.get('UID'):
        return redirect(url_for('dashboard'))
    else:
        error = request.args.get('error')
        return render_template('profile-login.html', error=error)


@app.route('/login-onsubmit', methods=['POST'])
def login_onsubmit():
    if pm.validate_login(request.form):
        user_id = select_queries.get_user_id(request.form['login_token'])['id']
        username = select_queries.get_user_data(user_id)['username']
        session['UID'] = user_id
        session['USERNAME'] = username
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login', error=True))


@app.route('/logout')
def logout():
    session.pop('UID')
    session.pop('USERNAME')
    return redirect(url_for('index'))


@app.route('/league/<league_id>/round/<round_id>', methods=['GET'])
def results(league_id=1, round_id=2):
    if session.get('UID'):
        game_type = select_queries.get_game_type_by_league_id(league_id)
        round_data = select_queries.get_round_by_id(round_id)
        round_status = helper.get_round_status(round_data)
        table_headers = helper.create_table_header(game_type['name'])
        game_data, players_data, players_in_game, round_points = (None, None, None, None)
        username = session['USERNAME']

        if round_status == 'init_round':
            players_data = select_queries.get_round_players(league_id)
            game_data = {
                "boards": select_queries.get_boards(game_type['id']),
                "expansions": select_queries.get_expansions(game_type['id']),
                "corporations": select_queries.get_corporations(game_type['id'])
            }

        elif round_status == 'started':
            players_in_game = select_queries.get_players_in_round(round_id)

        elif round_status == 'finished':
            round_points = select_queries.get_round_points(round_id, game_type['name'])

        else:
            return redirect('/')
        return render_template('round_details.html',
                               game_type=game_type,
                               round_status=round_status,
                               round_points=round_points,
                               table_headers=table_headers,
                               round=round_data,
                               round_id=round_id,
                               league_id=league_id,
                               game=game_data,
                               players=players_data,
                               players_in_game=players_in_game,
                               username=username)
    else:
        return redirect(url_for('login'))


@app.route('/league/<league_id>/round/<round_id>', methods=['POST'])
def init_round(league_id, round_id):
    if session.get('UID'):
        round_details = request.form
        insert_queries.init_round(round_details, round_id)
        return redirect(f'/league/{league_id}/round/{round_id}')
    else:
        return redirect(url_for('login'))


@app.route('/score/<league_id>')
def score_board(league_id):
    if session.get('UID'):
        game_type = select_queries.get_game_type_by_league_id(league_id)
        player_scores = select_queries.get_player_scores(league_id, game_type['name'])
        header = helper.create_scoreboard_table_header(game_type['name'])
        username = session['USERNAME']
        return render_template('scores.html', player_scores=player_scores, header=header, league_id=league_id,
                               username=username)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True,
            port=8000,
            host="0.0.0.0")
