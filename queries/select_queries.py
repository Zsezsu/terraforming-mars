from psycopg2.sql import SQL, Literal, Identifier

from data_manager import execute_select


def get_milestones():
    query = """
    SELECT milestone_name FROM milestones;
    """
    return execute_select(SQL(query))


def get_leagues():
    query = """
    SELECT 
        *
    FROM
        leagues
    ORDER BY
        id DESC
    """
    return execute_select(SQL(query))


def get_rounds(league_id):
    query = """
    SELECT
        *
    FROM
        rounds
    WHERE 
        league_id = {league_id}
    """
    return execute_select(SQL(query).format(
        league_id=Literal(int(league_id))
    ))
