from psycopg2.sql import SQL, Literal, Identifier

from data_manager import execute_update


def update_profile_picture(player_id, image_id):
    query = """
    UPDATE players
    SET image_id = {image_id}
    WHERE id = {player_id}
    """
    execute_update(SQL(query).format(
        player_id=Literal(player_id),
        image_id=Literal(image_id)
    ))


def update_password(player_id, new_password):
    query = """
    UPDATE players
    SET password = {new_password}
    WHERE id = {player_id}
    """
    execute_update(SQL(query).format(
        player_id=Literal(player_id),
        new_password=Literal(new_password)
    ))


def update_round_players_ranks(player_id_list):
    for player_id in player_id_list:
        query = """
        UPDATE players
        SET ranks_id = (SELECT id
                        FROM ranks
                        WHERE minimum_points <= (
                            WITH total_ares_points AS (
                                                        SELECT coalesce(SUM(coalesce(round_points, 0)),0) AS total 
                                                        FROM ares_points 
                                                        WHERE player_id = {player_id}
                                                        ),
                                 total_mars_points AS (
                                                        SELECT coalesce(SUM(coalesce(round_points, 0)), 0) AS total 
                                                        FROM mars_points 
                                                        WHERE player_id = {player_id}
                                                        )
                            SELECT total_mars_points.total + total_ares_points.total AS total
                            FROM total_mars_points,
                                 total_ares_points
                            GROUP BY    total_ares_points.total, 
                                        total_mars_points.total
                        )
                        ORDER BY minimum_points DESC
                        LIMIT 1)
        WHERE players.id = {player_id}
        """
        execute_update(SQL(query).format(
            player_id=Literal(player_id)
        ))
