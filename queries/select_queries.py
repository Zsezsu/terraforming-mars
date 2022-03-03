from psycopg2.sql import SQL, Literal, Identifier

from data_manager import execute_select


def get_milestones():
    query = """
    SELECT 
        milestone_name 
    FROM 
        milestones;
    """
    return execute_select(SQL(query))


def get_user_id(token):
    query = """
    SELECT id
    FROM players
    WHERE username LIKE {token} OR email LIKE {token}
    """
    return execute_select(SQL(query).format(
        token=Literal(token)
    ), fetchall=False)


def get_players():
    query = """
    SELECT 
        players.id AS id,
        players.username AS username,
        players.first_name || ' ' || players.last_name AS name,
        images.source AS image_source
    FROM 
        players
    LEFT JOIN images ON players.image_id = images.id
    """
    return execute_select(SQL(query))


def get_round_by_id(round_id):
    query = """
    SELECT 
        started, finished
    FROM 
        rounds
    WHERE id = {round_id}
    """
    return execute_select(SQL(query).format(round_id=Literal(round_id)), fetchall=False)



def get_images(type):
    image_type = ''
    if type == 'leagues':
        image_type = 'league_card'
    query = """
    SELECT 
        images.id as id,
        images.source as image_source 
    FROM 
        images
    WHERE images.{image_type} IS TRUE;
    """
    return execute_select(SQL(query).format(image_type=Identifier(image_type)))


def get_logged_in_user(user_id):
    query = """
    SELECT 
        players.id AS id,
        players.username AS username,
        players.first_name || ' ' || players.last_name AS name,
        images.source AS image_source
    FROM 
        players
    LEFT JOIN images ON players.image_id = images.id
    WHERE players.id = {user_id} 
    """
    return execute_select(SQL(query).format(user_id=Literal(user_id)), fetchall=False)


def get_logged_in_user_leagues(user_id):
    query = """
    SELECT
            leagues.id                                                          AS  id,
            leagues.league_name                                                 AS  league_name,
            leagues.league_admin                                                AS  league_admin,
            leagues.round_number                                                AS  round_number,
            COUNT(DISTINCT league_players.player_id)                            AS  player_number,
            COUNT(DISTINCT rounds.id) FILTER ( WHERE rounds.finished IS TRUE )  AS  finished_rounds,
            images.source                                                       AS  league_image_source
    
        FROM
            leagues
        LEFT JOIN league_players ON leagues.id = league_players.league_id
        LEFT JOIN images ON leagues.image_id = images.id
        LEFT JOIN rounds ON leagues.id = rounds.league_id
        WHERE
            leagues.league_admin = {user_id}
        OR
            league_players.player_id = {user_id}
        GROUP BY
            leagues.id, images.source
        ORDER BY
            leagues.id DESC;
    """
    return execute_select(SQL(query).format(user_id=Literal(user_id)))


def get_password(token):
    query = """
    SELECT id, password
    FROM players
    WHERE username LIKE {token} OR email LIKE {token}
    """
    return execute_select(SQL(query).format(
        token=Literal(token)
    ), fetchall=False)


def get_user_email(user_id):
    query = """
    SELECT email
    FROM players
    WHERE id = {user_id}
    """
    return execute_select(SQL(query).format(
        user_id=Literal(user_id)
    ), fetchall=False)


def get_pictures():
    query = """
    SELECT id, source
    FROM images
    WHERE user_image IS TRUE
    """
    return execute_select(SQL(query))


def get_user_data(uid):
    query = """
    SELECT username, first_name, last_name, email, source 
    FROM players
    JOIN images
        ON players.image_id = images.id::varchar
    WHERE players.id = {uid}
    """
    return dict(execute_select(SQL(query).format(
        uid=Literal(uid)
    ), fetchall=False))
