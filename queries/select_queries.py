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
