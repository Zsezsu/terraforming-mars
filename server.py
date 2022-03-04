from flask import Flask, render_template, request, url_for, redirect, jsonify
from dotenv import load_dotenv
from api import api

import queries.insert_queries as insert_queries
import queries.select_queries as select_queries
import queries.update_queries as update_queries
import queries.delete_queries as delete_queries
import helper

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


@app.route('/games')
def games():
    return render_template('games.html')


@app.route('/test')
def test():
    milestones = select_queries.get_milestones()
    return render_template('test.html', milestones=milestones)


@app.route('/round/<round_id>')
def results(round_id=1):
    round_data = select_queries.get_round_by_id(round_id)
    round_status = helper.get_round_status(round_data)
    game_data = {
        "boards": select_queries.get_boards(),
        "expansions": select_queries.get_expansions(),
        "corporations": select_queries.get_corporations()
    }
    players_data = [
        {'username': 'dudaskobende', 'player_id': 1},
        {'username': 'Zsezsu', 'player_id': 2},
        {'username': 'Sagi-Viktor', 'player_id': 3},
        {'username': 'benedekhalaj', 'player_id': 4}
    ]
    return render_template('round_details.html',
                           round_status=round_status,
                           round=round_data,
                           round_id=round_id,
                           game=game_data,
                           players=players_data)


if __name__ == '__main__':
    app.run(debug=True,
            port=8000,
            host="0.0.0.0")
