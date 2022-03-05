from psycopg2.sql import SQL, Literal, Identifier

from data_manager import execute_select


def get_milestones():
    query = """
    SELECT 
        milestone_name 
    FROM 
        milestones
    ORDER BY
        milestones.milestone_name;
    """
    return execute_select(SQL(query))


def get_round_by_id(round_id):
    query = """
    SELECT 
        league_id, started, finished, sequence
    FROM 
        rounds
    WHERE id = {round_id};
    """
    return execute_select(SQL(query).format(round_id=Literal(round_id)), fetchall=False)


def get_boards():
    query = """
    SELECT
        *
    FROM 
        boards
    ORDER BY 
        boards.board_name;
    """
    return execute_select(SQL(query))


def get_expansions():
    query = """
    SELECT
        *
    FROM 
        expansions
    ORDER BY 
        expansions.expansion_name;
    """
    return execute_select(SQL(query))


def get_corporations():
    query = """
    SELECT
        *
    FROM 
        corporations
    ORDER BY 
        corporations.name;
    """
    return execute_select(SQL(query))

