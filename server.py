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


@app.route('/league/<league_id>/round/<round_id>', methods=['GET'])
def results(league_id=1, round_id=2):
    round_data = select_queries.get_round_by_id(round_id)
    round_status = helper.get_round_status(round_data)
    game_data, players_data, players_in_game, round_points = (None, None, None, None)
    players_data, players_in_game = helper.dummy_data()  # CREATES DUMMY DATA
    # init_game, started, finished

    if round_status == 'init_round':
        # players_data = select_queries.get_round_players(league_id)
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
                           round=round_data,
                           round_id=round_id,
                           league_id=league_id,
                           game=game_data,
                           players=players_data,
                           players_in_game=players_in_game)


@app.route('/league/<league_id>/round/<round_id>', methods=['POST'])
def init_round(league_id, round_id):
    round_details = request.form
    insert_queries.init_round(round_details, round_id)
    return redirect(f'/league/{league_id}/round/{round_id}')


if __name__ == '__main__':
    app.run(debug=True,
            port=8000,
            host="0.0.0.0")
