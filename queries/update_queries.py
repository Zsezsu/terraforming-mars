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
