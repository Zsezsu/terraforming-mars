from psycopg2.sql import SQL, Literal, Identifier

from data_manager import execute_delete


def delete_league(league_id):
    query = """
    DELETE FROM leagues WHERE id = {league_id};
    """
    return execute_delete(SQL(query).format(league_id=Literal(league_id)))

