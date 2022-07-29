import flask
from flask import Blueprint, Flask, request, redirect, session, jsonify, json, make_response
import profile_manager as pm

import queries.insert_queries as insert_queries
import queries.select_queries as select_queries
import queries.update_queries as update_queries
import queries.delete_queries as delete_queries

api = Blueprint('api', __name__, template_folder='templates')


@api.route('/api/leagues/<league_id>/rounds/<round_id>', methods=['POST'])
def save_round_points(league_id, round_id):
    round_data = json.loads(request.data)
    game_type = select_queries.get_game_type_by_league_id(league_id)
    insert_queries.insert_round_points(round_id, round_data, game_type['name'])
    return jsonify('')


@api.route('/api/players')
def send_players():
    players = select_queries.get_players()
    return jsonify(players)


@api.route('/api/users/logged-in')
def send_logged_in_user():
    uid = session['UID']
    logged_in_user = select_queries.get_logged_in_user(uid)
    return jsonify(logged_in_user)


@api.route('/api/images/league-cards')
def send_league_images():
    league_images = select_queries.get_images('leagues')
    return jsonify(league_images)


@api.route('/api/images/profile-pictures')
def get_profile_pictures():
    profile_pictures = select_queries.get_pictures()
    return jsonify(profile_pictures)


@api.route('/api/leagues', methods=['POST'])
def create_league():
    data = json.loads(request.data)
    league_id = insert_queries.add_new_league(data)
    new_league_id = {'league_id': league_id}
    return jsonify(new_league_id)


@api.route('/api/user/name/<token>')
def is_unique_token_exist(token):
    return jsonify(bool(select_queries.get_user_id(token)))


@api.route('/api/leagues/<league_id>', methods=['DELETE'])
def delete_league(league_id):
    delete_queries.delete_league(league_id)
    return 'OK'


@api.route('/api/players/<player_id>/profile-picture', methods=['PUT'])
def update_profile_picture(player_id):
    data = json.loads(request.data)
    image_id = data['imageId']
    update_queries.update_profile_picture(player_id, image_id)
    return flask.make_response('OK', 200)


@api.route('/api/players/<player_id>/password', methods=['PUT'])
def update_password(player_id):
    data = json.loads(request.data)
    old_password = data['oldPassword']
    hashed_old_password = select_queries.get_password_by_id(player_id)['password']
    if not pm.verify_password(old_password, hashed_old_password):
        return flask.make_response('Invalid old password!', 401)

    new_password = data['newPassword']
    hashed_new_password = pm.hash_password(new_password)
    update_queries.update_password(player_id, hashed_new_password)
    return flask.make_response('OK', 200)


@api.route('/api/leagues', methods=['GET'])
def get_all_leagues():
    leagues = select_queries.get_leagues()
    return jsonify(leagues)
