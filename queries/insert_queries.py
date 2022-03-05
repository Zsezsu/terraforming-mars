from psycopg2.sql import SQL, Identifier, Literal

from data_manager import execute_insert
import helper


def init_round(round_details, round_id):
    board_id, expansions, players = helper.get_round_details(round_details)
    game_setup_values = helper.init_game_setup_values(round_id, board_id, expansions)
    round_players_values = helper.init_round_players_values(round_id, players)
    query = """
    BEGIN;
        INSERT INTO 
            game_setup(round_id, board_id, expansion_id)
        VALUES 
            {game_setup_values};
        
        INSERT INTO 
        round_players(round_id, player_id, corporation_id)
    VALUES
        {round_players_values};
    COMMIT;
    """
    execute_insert(SQL(query).format(
        game_setup_values=SQL(game_setup_values),
        round_players_values=SQL(round_players_values)
    ))


def add_new_league(data):
    # create league(returning league id)
    league_id = add_league(data)[0]
    # insert league players
    add_league_players(league_id, data)
    # create league rounds
    add_league_rounds(league_id, data)
    return league_id


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


def insert_new_user(data):
    query = """
    INSERT INTO
        players(username, first_name, last_name, email, password, image_id)
    VALUES
        ({username}, {first_name}, {last_name}, {email}, {password}, {image_id})
    RETURNING id
    """
    return execute_insert(SQL(query).format(
        username=Literal(data['nickname']),
        first_name=Literal(data['first_name']),
        last_name=Literal(data['last_name']),
        email=Literal(data['email']),
        password=Literal(data['password']),
        image_id=Literal(data['pp_id'])
    ), fetchone=True)
