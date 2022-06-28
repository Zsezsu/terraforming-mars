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


def get_user_id(token):
    query = """
    SELECT id
    FROM players
    WHERE username LIKE {token} OR email LIKE {token};
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
    LEFT JOIN images ON players.image_id = images.id;
    """
    return execute_select(SQL(query))


def get_round_by_id(round_id):
    query = """
    SELECT 
        rounds.league_id,
        leagues.league_name AS league_name,
        rounds.started,
        rounds.finished,
        rounds.sequence
    FROM 
        rounds
        LEFT JOIN leagues ON rounds.league_id = leagues.id
    WHERE rounds.id = {round_id};
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


def get_round_points(round_id):
    query = """
    SELECT 
        players.username                    AS  username,
        corporations.name                   AS  corporation_name,
        points.tr_number                    AS  tr_number,
        points.milestones_points            AS  milestones_points,
        points.award_points                 AS  award_points,
        points.number_of_own_greeneries     AS  number_of_own_greeneries,
        points.number_of_cities             AS  number_of_cities,
        points.greeneries_around_cities     AS  greeneries_around_cities,
        points.vp_on_cards                  AS  vp_on_cards,
        points.mega_credits                 AS  mega_credits,
        points.sum_points                   AS  sum_points
        
    FROM
        points
    LEFT JOIN players           ON  points.player_id = players.id
    LEFT JOIN round_players     ON  players.id = round_players.player_id
    LEFT JOIN corporations      ON  round_players.corporation_id = corporations.id
    WHERE
        points.round_id = {round_id}
        AND round_players.round_id = {round_id}
    ORDER BY
        points.round_points DESC,
        points.sum_points DESC,
        points.mega_credits DESC,
        points.vp_on_cards DESC,
        players.id DESC;
    """
    return execute_select(SQL(query).format(round_id=Literal(round_id)))


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
        corporations.name           AS  corporation_name
    FROM
        round_players
    LEFT JOIN corporations  ON  round_players.corporation_id =  corporations.id
    LEFT JOIN players       ON  round_players.player_id      =  players.id
    WHERE
        round_players.round_id = {round_id};
    """
    return execute_select(SQL(query).format(round_id=Literal(round_id)))


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
    WHERE 
        images.{image_type} IS TRUE;
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
    WHERE 
        players.id = {user_id};
    """
    return execute_select(SQL(query).format(user_id=Literal(user_id)), fetchall=False)


def get_logged_in_user_leagues(user_id):
    query = """
    SELECT
        leagues.id                                                          AS  id,
        leagues.league_name                                                 AS  league_name,
        leagues.league_admin                                                AS  league_admin,
        leagues.round_number                                                AS  round_number,
        array_length(league_players.players, 1)                             AS  player_number,
        COUNT(DISTINCT rounds.id) FILTER ( WHERE rounds.finished IS TRUE )  AS  finished_rounds,
        images.source                                                       AS  league_image_source

    FROM
        leagues
    LEFT JOIN images ON leagues.image_id = images.id
    LEFT JOIN rounds ON leagues.id = rounds.league_id
    LEFT JOIN (SELECT league_id, array_agg(player_id) as players FROM league_players

GROUP BY league_id) as league_players on league_players.league_id = leagues.id
    WHERE
        leagues.league_admin = {user_id}
    OR
       {user_id} = ANY(league_players.players)
    GROUP BY
        leagues.id, images.source, league_players.players
    ORDER BY
        leagues.id DESC;
    """
    return execute_select(SQL(query).format(user_id=Literal(user_id)))


def get_rounds_for_league(league_id, logged_in_user_id):
    query = """
    SELECT
        rounds.id                                       AS id,
        rounds.league_id                                AS league_id,
        leagues.league_name                             AS league_name,
        rounds.sequence                                 AS sequence,
        rounds.started                                  AS started,
        rounds.finished                                 AS finished,
        boards.board_name                               AS board,
        string_agg(expansions.expansion_name, ', ')     AS expansions,
        leagues.league_admin                            AS league_admin
    FROM 
        rounds
    LEFT JOIN leagues ON rounds.league_id = leagues.id
    LEFT JOIN game_setup ON rounds.id = game_setup.round_id
    LEFT JOIN boards ON game_setup.board_id = boards.id
    LEFT JOIN expansions ON game_setup.expansion_id = expansions.id
    WHERE 
        rounds.league_id = {league_id}
    GROUP BY
             rounds.id,
             leagues.id,
             boards.id
    ORDER BY 
        rounds.sequence;
     """
    return execute_select(SQL(query).format(
        league_id=Literal(league_id)
    ))


def get_password(token):
    query = """
    SELECT 
        id, password
    FROM 
        players
    WHERE 
        username LIKE {token} OR email LIKE {token};
    """
    return execute_select(SQL(query).format(
        token=Literal(token)
    ), fetchall=False)


def get_user_email(user_id):
    query = """
    SELECT 
        email
    FROM 
        players
    WHERE 
        id = {user_id};
    """
    return execute_select(SQL(query).format(
        user_id=Literal(user_id)
    ), fetchall=False)


def get_pictures():
    query = """
    SELECT 
        id, 
        source AS image_source
    FROM 
        images
    WHERE 
        user_image IS TRUE;
    """
    return execute_select(SQL(query))


def get_user_data(uid):
    query = """
    SELECT 
        username, first_name, last_name, email, source 
    FROM 
        players
    JOIN 
        images
        ON players.image_id = images.id
    WHERE players.id = {uid};
    """
    return dict(execute_select(SQL(query).format(
        uid=Literal(uid)
    ), fetchall=False))


def get_game_types():
    query = """
    SELECT
        id, name
    FROM
        game_types
    """
    return execute_select(SQL(query))


def get_player_scores(league_id):
    query = """
    SELECT
            players.username                        AS username,
            SUM(points.round_points)                AS total_round_points,
            SUM(points.sum_points)                  AS total_points,
            SUM(points.mega_credits)                AS total_mega_credits,
            SUM(points.tr_number)                   AS total_tr_numbers,
            SUM(points.milestones_points)           AS total_milestones_points,
            SUM(points.award_points)                AS total_award_points,
            SUM(points.number_of_own_greeneries)    AS total_number_of_own_greeneries,
            SUM(points.number_of_cities)            AS total_number_of_cities,
            SUM(points.greeneries_around_cities)    AS total_greeneries_around_cities,
            SUM(points.vp_on_cards)                 AS total_vp_on_cards,
            COUNT(rounds.finished)                  AS finished_rounds,
            (SELECT
                MAX(rounds.sequence)
            FROM
                rounds
            WHERE
            rounds.league_id = {league_id})         AS number_of_rounds,
            leagues.league_name                     AS league_name
    FROM leagues
    LEFT JOIN rounds ON leagues.id = rounds.league_id
    LEFT JOIN round_players ON rounds.id = round_players.round_id
    LEFT JOIN players ON round_players.player_id = players.id
    LEFT JOIN points ON players.id = points.player_id
    WHERE 
        leagues.id = {league_id}
        AND
            rounds.finished IS TRUE
        AND
            rounds.id = points.round_id
    GROUP BY players.id, leagues.id
    ORDER BY 
        total_round_points DESC, 
        total_points DESC, 
        total_mega_credits DESC, 
        total_vp_on_cards DESC, 
        players.id DESC;
    """
    return execute_select(SQL(query).format(league_id=Literal(league_id)))
