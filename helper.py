
def dummy_data():
    players_data = [
        {'username': 'dudaskobende', 'player_id': 1},
        {'username': 'Zsezsu', 'player_id': 2},
        {'username': 'Sagi-Viktor', 'player_id': 3},
        {'username': 'benedekhalaj', 'player_id': 4}
    ]
    players_in_game = [
        {'username': 'dudaskobende', 'player_id': 1, 'company': 'company 1'},
        {'username': 'Zsezsu', 'player_id': 2, 'company': 'company 2'},
        {'username': 'Sagi-Viktor', 'player_id': 3, 'company': 'company 3'},
        {'username': 'benedekhalaj', 'player_id': 4, 'company': 'company 4'}
    ]
    return players_data, players_in_game



def get_round_status(round):
    round_status = ''
    for key, value in round.items():
        if key == 'started' or key == 'finished':
            if value:
                round_status = key
    round_status = 'init_round' if round_status == '' else round_status
    return round_status


def get_round_details(round_details):
    board = round_details['board']
    expansions = []
    players = []
    for type, detail in round_details.items():
        if 'expansion' in type:
            expansions.append(detail)
        elif 'player' in type:
            id = type.split('-')[1]
            players.append((id, detail))
    return board, expansions, players


def init_game_setup_values(round_id, board_id, expansions):
    values = ""
    for index in range(len(expansions)):
        separator = ',' if index < len(expansions) - 1 else ''
        values += f'({round_id}, {board_id}, {expansions[index]}){separator}'
    return values


def init_round_players_values(round_id, players):
    values = ""
    for index in range(len(players)):
        separator = ',' if index < len(players) - 1 else ''
        player = players[index]
        player_id, corporation_id = player[0], player[1]
        values += f'({round_id}, {player_id}, {corporation_id}){separator}'
    return values


def insert_round_values(round_id, round_data):
    values = ''
    for index in range(len(round_data)):
        player = round_data[index]
        separator = ', ' if index < len(round_data) - 1 else ''
        points = add_points(player['points'])
        values += f'({round_id}, {player["playerId"]}, {points}{player["total"]}){separator}'
    return values


def add_points(points):
    point_types = [
        'tr_number',
        'milestones_points',
        'award_points',
        'number_of_own_greeneries',
        'number_of_cities',
        'greeneries_around_cities',
        'vp_on_cards',
    ]
    point_query_values = ''
    for index in range(len(points)):
        point_query_values += f'{points[point_types[index]]}, '
    return point_query_values
