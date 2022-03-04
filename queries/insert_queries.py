from psycopg2.sql import SQL, Literal, Identifier

from data_manager import execute_insert


def add_new_league(data):
    # create league(returning league id)
    league_id = add_league(data)[0]
    # insert league players
    add_league_players(league_id, data)
    # create league rounds
    add_league_rounds(league_id, data)


def add_league(data):
    query = """
        INSERT INTO
            leagues(league_name, league_admin, round_number, image_id)
        VALUES 
            ({league_name}, {league_admin}, {round_number}, {image_id})
        RETURNING leagues.id;
    """
    return execute_insert(SQL(query).format(
        league_name=Literal(data['leagueName']),
        league_admin=Literal(data['leagueAdminId']),
        round_number=Literal(data['leagueRounds']),
        image_id=Literal(data['leagueImageId'])
    ), fetchone=True)


def add_league_players(league_id, data):
    users = data['userIds']
    user_id_values = ''

    for index in range(len(users)):
        separator = ','
        if index == len(users) - 1:
            separator = ''
        user_id_values += f"({league_id}, {users[index]['id']}){separator}"

    query = """
        INSERT INTO
            league_players(league_id, player_id)
        VALUES {users}
        """
    execute_insert(SQL(query).format(users=SQL(user_id_values)))


def add_league_rounds(league_id, data):
    rounds_number = int(data['leagueRounds'])
    image_id = 6
    rounds = ''

    for game_round in range(1, rounds_number + 1):
        separator = ','
        if game_round == rounds_number:
            separator = ''
        rounds += f"({league_id}, {game_round}, {image_id}){separator}"

    query = """
        INSERT INTO 
            rounds(league_id, sequence, image_id)
        VALUES {rounds}
    """
    execute_insert(SQL(query).format(rounds=SQL(rounds)))
