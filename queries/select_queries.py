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


def get_boards(game_type_id):
    query = """
    SELECT
        *
    FROM 
        boards
    WHERE
        game_type_id = {game_type_id}
    ORDER BY 
        boards.board_name;
    """
    return execute_select(SQL(query).format(
        game_type_id=Literal(game_type_id)
    ))


def get_expansions(game_type_id):
    query = """
    SELECT
        *
    FROM 
        expansions
    WHERE
        game_type_id = {game_type_id}
    ORDER BY 
        expansions.expansion_name;
    """
    return execute_select(SQL(query).format(
        game_type_id=Literal(game_type_id)
    ))


def get_corporations(game_type_id):
    query = """
    SELECT 
        game_types_corporations_expansions.expansion_id AS expansion_id,
       corporations.id                                  AS corporation_id,
       corporations.name                                AS corporation_name
    FROM 
        game_types_corporations_expansions
    LEFT JOIN corporations ON game_types_corporations_expansions.corporation_id = corporations.id
    WHERE 
        game_types_corporations_expansions.game_type_id = {game_type_id}
    ORDER BY
        corporation_name;
    """
    return execute_select(SQL(query).format(
        game_type_id=Literal(game_type_id)
    ))


def get_round_points(round_id, game_type_name):
    if game_type_name == 'Terraforming Mars':
        query = """
        SELECT 
            players.username                    AS  username,
            corporations.name                   AS  corporation_name,
            mars_points.tr_number                    AS  tr_number,
            mars_points.milestones_points            AS  milestones_points,
            mars_points.award_points                 AS  award_points,
            mars_points.number_of_own_greeneries     AS  number_of_own_greeneries,
            mars_points.number_of_cities             AS  number_of_cities,
            mars_points.greeneries_around_cities     AS  greeneries_around_cities,
            mars_points.vp_on_cards                  AS  vp_on_cards,
            mars_points.mega_credits                 AS  mega_credits,
            mars_points.sum_points                   AS  sum_points
            
        FROM
            mars_points
        LEFT JOIN players           ON  mars_points.player_id = players.id
        LEFT JOIN round_players     ON  players.id = round_players.player_id
        LEFT JOIN corporations      ON  round_players.corporation_id = corporations.id
        WHERE
            mars_points.round_id = {round_id}
            AND round_players.round_id = {round_id}
        ORDER BY
            mars_points.round_points DESC,
            mars_points.sum_points DESC,
            mars_points.mega_credits DESC,
            mars_points.vp_on_cards DESC,
            players.id DESC;
        """
    elif game_type_name == 'Ares Expedition':
        query = """
        SELECT 
           players.username                     AS username,
           corporations.name                    AS corporation_name,
           ares_points.tr_number                AS tr_number,
           ares_points.number_of_own_greeneries AS number_of_own_greeneries,
           ares_points.vp_on_cards              AS vp_on_cards,
           ares_points.mega_credits             AS mega_credits,
           ares_points.sum_points               AS sum_points

        FROM ares_points
             LEFT JOIN players ON ares_points.player_id = players.id
             LEFT JOIN round_players ON players.id = round_players.player_id
             LEFT JOIN corporations ON round_players.corporation_id = corporations.id
        WHERE 
            ares_points.round_id = {round_id}
            AND round_players.round_id = {round_id}
        ORDER BY ares_points.round_points DESC,
            ares_points.sum_points DESC,
            ares_points.mega_credits DESC,
            ares_points.vp_on_cards DESC,
            players.id DESC;
        """
    else:
        raise AttributeError('No such game type in database: ' + game_type_name)
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
        game_types.name                                                     AS  game_type_name,
        game_types.id                                                       AS  game_type_id,
        array_length(league_players.players, 1)                             AS  player_number,
        COUNT(DISTINCT rounds.id) FILTER ( WHERE rounds.finished IS TRUE )  AS  finished_rounds,
        images.source                                                       AS  league_image_source

    FROM
        leagues
    LEFT JOIN images ON leagues.image_id = images.id
    LEFT JOIN rounds ON leagues.id = rounds.league_id
    LEFT JOIN game_types ON leagues.game_type_id = game_types.id
    LEFT JOIN (SELECT league_id, array_agg(player_id) as players FROM league_players

GROUP BY league_id) as league_players on league_players.league_id = leagues.id
    WHERE
        leagues.league_admin = {user_id}
    OR
       {user_id} = ANY(league_players.players)
    GROUP BY
        leagues.id, images.source, league_players.players, game_types.name, game_types.id
    ORDER BY
        leagues.id DESC;
    """
    return execute_select(SQL(query).format(user_id=Literal(user_id)))


def get_rounds_for_league(league_id):
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


def get_password_by_id(player_id):
    query = """
    SELECT
        id, password
    FROM
        players
    WHERE
        id = {player_id};
    """
    return execute_select(SQL(query).format(
        player_id=Literal(player_id)
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
        players.username,
        players.first_name,
        players.last_name,
        players.email,
        ranks.name AS rank,
        images.source AS source,
        images.id AS image_id
    FROM 
        players
    LEFT JOIN images ON players.image_id = images.id
    LEFT JOIN ranks ON players.ranks_id = ranks.id
    
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


def get_game_type_by_league_id(league_id):
    query = """
    SELECT 
        game_types.id           AS id,
        game_types.name         AS name
    FROM 
        game_types
    LEFT JOIN leagues ON leagues.game_type_id = game_types.id
    WHERE 
        leagues.id = {league_id};
    """
    return execute_select(SQL(query).format(
        league_id=Literal(league_id)
    ), fetchall=False)


def get_player_scores(league_id, game_type_name):
    if game_type_name == 'Terraforming Mars':
        query = """
        WITH round AS (SELECT MAX(rounds.sequence) AS max,
                      rounds.league_id
               FROM rounds
               GROUP BY rounds.league_id)
        SELECT
                players.username                             AS username,
                SUM(mars_points.round_points)                AS total_round_points,
                SUM(mars_points.sum_points)                  AS total_points,
                SUM(mars_points.mega_credits)                AS total_mega_credits,
                SUM(mars_points.tr_number)                   AS total_tr_numbers,
                SUM(mars_points.milestones_points)           AS total_milestones_points,
                SUM(mars_points.award_points)                AS total_award_points,
                SUM(mars_points.number_of_own_greeneries)    AS total_number_of_own_greeneries,
                SUM(mars_points.number_of_cities)            AS total_number_of_cities,
                SUM(mars_points.greeneries_around_cities)    AS total_greeneries_around_cities,
                SUM(mars_points.vp_on_cards)                 AS total_vp_on_cards,
                COUNT(rounds.finished)                       AS finished_rounds,
                round.max                                    AS number_of_rounds,
                leagues.league_name                          AS league_name
        FROM leagues
                LEFT JOIN rounds ON leagues.id = rounds.league_id
                LEFT JOIN round_players ON rounds.id = round_players.round_id
                LEFT JOIN players ON round_players.player_id = players.id
                LEFT JOIN mars_points ON players.id = mars_points.player_id,
            round
        WHERE 
            leagues.id = {league_id} 
            AND
                round.league_id = {league_id}
            AND
                rounds.finished IS TRUE
            AND
                rounds.id = mars_points.round_id
        GROUP BY players.id, leagues.id, number_of_rounds
        ORDER BY 
            total_round_points DESC, 
            total_points DESC, 
            total_mega_credits DESC, 
            total_vp_on_cards DESC, 
            players.id DESC;
        """
    elif game_type_name == 'Ares Expedition':
        query = """
        WITH round AS (SELECT MAX(rounds.sequence) AS max,
                              rounds.league_id
                       FROM rounds
                       GROUP BY rounds.league_id)
        SELECT players.username                          AS username,
               SUM(ares_points.round_points)             AS total_round_points,
               SUM(ares_points.sum_points)               AS total_points,
               SUM(ares_points.mega_credits)             AS total_mega_credits,
               SUM(ares_points.tr_number)                AS total_tr_numbers,
               SUM(ares_points.number_of_own_greeneries) AS total_number_of_own_greeneries,
               SUM(ares_points.vp_on_cards)              AS total_vp_on_cards,
               COUNT(rounds.finished)                    AS finished_rounds,
               round.max                                 AS number_of_rounds,
               leagues.league_name                       AS league_name
        FROM leagues
                 LEFT JOIN rounds ON leagues.id = rounds.league_id
                 LEFT JOIN round_players ON rounds.id = round_players.round_id
                 LEFT JOIN players ON round_players.player_id = players.id
                 LEFT JOIN ares_points ON players.id = ares_points.player_id,
             round
        WHERE 
                leagues.id = {league_id} 
          AND 
                round.league_id = {league_id}
          AND
                rounds.finished IS TRUE
          AND
                rounds.id = ares_points.round_id
        GROUP BY players.id, leagues.id, number_of_rounds
        ORDER BY total_round_points DESC,
                 total_points DESC,
                 total_mega_credits DESC,
                 total_vp_on_cards DESC,
                 players.id DESC;
        """
    else:
        raise AttributeError('No such game type in database: ' + game_type_name)
    return execute_select(SQL(query).format(league_id=Literal(league_id)))


def get_league_player_ids(league_id):
    query = """
    SELECT league_players.player_id 
    FROM league_players
    WHERE league_id = {league_id}
    """
    return execute_select(SQL(query).format(
        league_id=Literal(league_id)
    ))
