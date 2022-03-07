import json

from flask import Blueprint, Flask, request, jsonify, session

import queries.insert_queries as insert_queries
import queries.select_queries as select_queries
import queries.update_queries as update_queries
import queries.delete_queries as delete_queries

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/api/players')
def send_players():
    players = select_queries.get_players()
    players = [
        {'id': 1, 'username': 'egyetlenkiralyano', 'name': 'Zsuzsanna Juhász', 'image_source': 'img/favicon.ico'},
        {'id': 2, 'username': 'grandecruz', 'name': 'Bendegúz Dudaskó', 'image_source': 'img/favicon.ico'},
        {'id': 3, 'username': 'viktorurunkkiralyunk', 'name': 'Viktor Sági', 'image_source': 'img/favicon.ico'},
        {'id': 4, 'username': 'benedekhalaj', 'name': 'Benedek Halaj', 'image_source': 'img/favicon.ico'}
    ] # DUMMY DATA----------------------------------------------
    return jsonify(players)


@api.route('/api/users/logged-in')
def send_logged_in_user():
    uid = session['UID']
    logged_in_user = select_queries.get_logged_in_user(uid)
    logged_in_user = session['logged_in_user'] # DUMMY DATA----------------------------------------------
    return jsonify(logged_in_user)


@api.route('/api/images/league-cards')
def send_league_images():
    league_images = select_queries.get_images('leagues')
    return jsonify(league_images)


@api.route('/api/leagues', methods=['POST'])
def create_league():
    data = json.loads(request.data)
    league_id = insert_queries.add_new_league(data)
    new_league_id = {'league_id': league_id}
    return jsonify(new_league_id)
