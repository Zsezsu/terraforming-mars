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
        
        UPDATE 
            rounds
        SET 
            started = TRUE
        WHERE
            rounds.id = {round_id};
    COMMIT;
    """
    execute_insert(SQL(query).format(
        game_setup_values=SQL(game_setup_values),
        round_players_values=SQL(round_players_values),
        round_id=Literal(round_id)
    ))


def insert_round_points_results(round_id, round_data):
    result_values = helper.insert_round_result_values(round_id, round_data)
    query = """
    INSERT INTO 
        results(round_id, player_id, sum_points)
    VALUES 
        {result_values}
    RETURNING id;
    """
    result_id = execute_insert(SQL(query).format(result_values=SQL(result_values)), fetchone=True)
    insert_round_points(result_id, round_data)


def insert_round_points(result_id, round_data):
    round_points_values = helper.insert_round_point_values(result_id[0], round_data)
    query = """
    INSERT INTO 
        points(
            result_id,
            tr_number,
            milestones_points,
            award_points,
            number_of_own_greeneries,
            number_of_cities,
            greeneries_around_cities,
            vp_on_cards
        )
    VALUES 
        {round_points_values};
    """
    execute_insert(SQL(query).format(round_points_values=SQL(round_points_values)))
