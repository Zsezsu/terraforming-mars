from flask import Blueprint, Flask, request, jsonify

import queries.insert_queries as insert_queries
import queries.select_queries as select_queries
import queries.update_queries as update_queries
import queries.delete_queries as delete_queries

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/api/players')
def send_players():
    players = select_queries.get_players()
    return jsonify(players)


@api.route('/api/images/leagues')
def send_league_images():
    league_images = select_queries.get_images('leagues')
    return jsonify(league_images)