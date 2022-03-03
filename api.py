from flask import Blueprint, Flask, request, jsonify, session

import queries.insert_queries as insert_queries
import queries.select_queries as select_queries
import queries.update_queries as update_queries
import queries.delete_queries as delete_queries

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/api/players')
def send_players():
    players = select_queries.get_players()

    players = [{'id': 1, 'username': 'Zsu', 'name': 'Zsuzsanna Juhász'},
               {'id': 2, 'username': 'Bende', 'name': 'Bendegúz Dudaskó'},
               {'id': 3, 'username': 'Viktor', 'name': 'Sági Viktor'},
               {'id': 4, 'username': 'Benedek', 'name': 'Halaj Benedek'}
               ]
    return jsonify(players)


@api.route('/api/users/logged-in')
def send_logged_in_user():
    uid = session['UID']
    logged_in_user = select_queries.get_logged_in_user(uid)
    return jsonify(logged_in_user)


@api.route('/api/images/leagues')
def send_league_images():
    league_images = select_queries.get_images('leagues')
    league_images = [{'id': 1, 'image_source': 'img/mars-1.webp'},
                    {'id': 2, 'image_source': 'img/mars-2.webp'},
                    {'id': 3, 'image_source': 'img/mars-3.webp'},
                    {'id': 4, 'image_source': 'img/mars-4.webp'}
                    ]
    return jsonify(league_images)
