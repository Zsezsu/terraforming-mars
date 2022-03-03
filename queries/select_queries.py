from psycopg2.sql import SQL, Literal, Identifier

from data_manager import execute_select


def get_milestones():
    query = """
    SELECT milestone_name FROM milestones;
    """
    return execute_select(SQL(query))


def get_players():
    query = """
    SELECT players.username as name, players.id FROM players
    """
    return execute_select(SQL(query))
