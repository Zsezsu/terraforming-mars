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


def get_round_players(league_id):
    query = """
    SELECT
        players.id                                      AS  id,
        players.username                                AS  username
    FROM players
    LEFT JOIN league_players ON players.id = league_players.player_id
    WHERE
        league_players.league_id = {league_id}
    ORDER BY 
        players.username;
    """
    return execute_select(SQL(query).format(league_id=Literal(league_id)))


def get_players_in_round(round_id):
    query = """
    SELECT 
        round_players.player_id     AS  player_id,
        players.username            AS  username,
        corporations.name           AS  corporation_name,
        images.source               AS  corporation_image_source
    FROM
        round_players
    LEFT JOIN corporations  ON  round_players.corporation_id =  corporations.id
    LEFT JOIN players       ON  round_players.player_id      =  players.id
    LEFT JOIN images        ON  corporations.image_id        =  images.id
    WHERE
        round_players.round_id = {round_id};
    """
    return execute_select(SQL(query).format(round_id=Literal(round_id)))
