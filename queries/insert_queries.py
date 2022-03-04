from psycopg2.sql import SQL, Literal, Identifier

from data_manager import execute_insert


def add_new_league(data):

    # create league(returning league id)
    insert_league_query = """
        INSERT INTO
            leagues(league_name, league_admin, round_number, image_id)
        VALUES 
            ({league_name}, {league_admin}, {round_number}, {image_id})
        RETURNING leagues.id;
    """
    league_id = execute_insert(SQL(insert_league_query).format(
        league_name=Literal(data['leagueName']),
        league_admin=Literal(data['leagueAdminId']),
        round_number=Literal(data['leagueRounds']),
        image_id=Literal(data['leagueImageId'])
    ), fetchone=True)

    # insert league players
    users = data['userIds']
    user_id_values = ''
    for index in range(len(users)):
        separator = ','
        if index == len(users) -1:
            separator = ''
        user_id_values += f"({league_id[0]}, {users[index]['id']}){separator}"
    insert_league_players_query = """
    INSERT INTO
        league_players(league_id, player_id)
    VALUES {users}
    """
    execute_insert(SQL(insert_league_players_query).format(users=SQL(user_id_values)))

    # create league rounds



