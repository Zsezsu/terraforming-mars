from psycopg2.sql import SQL, Literal, Identifier

from data_manager import execute_select


def get_milestones():
    query = """
    SELECT milestone_name FROM milestones;
    """
    return execute_select(SQL(query))
