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
