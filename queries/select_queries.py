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
        players.username as name,
        players.id 
    FROM 
        players
    """
    return execute_select(SQL(query))


def get_images(type):
    image_type = ''
    if type == 'leagues':
        image_type = 'league_card'
    query = """
    SELECT 
        images.id as id,
        images.source as source 
    FROM 
        images
    WHERE images.{image_type} IS TRUE;
    """
    return execute_select(SQL(query).format(image_type=Identifier(image_type)))
