def create_table_header(game_type_name):
    if game_type_name == 'Terraforming Mars':
        return [
            'TR number',
            'Milestone points',
            'Award points',
            'Greeneries',
            'Cities',
            'Greeneries around cities',
            'Victory points',
            'M€'
        ]
    elif game_type_name == 'Ares Expedition':
        return [
            'TR number',
            'Greeneries',
            'Victory points',
            'M€'
        ]
    else:
        raise AttributeError('No such game type in database: ' + game_type_name)


def create_scoreboard_table_header(game_type_name):
    if game_type_name == 'Terraforming Mars':
        return [
            'Place',
            'Player',
            'Round points',
            'Total points',
            'Total M€',
            'Total TR points',
            'Total milestones points',
            'Total award points',
            'Total greeneries',
            'Total cities',
            'Total greeneries around cities',
            'Total victory points'
        ]
    elif game_type_name == 'Ares Expedition':
        return [
            'Place',
            'Player',
            'Round points',
            'Total points',
            'Total M€',
            'Total award points',
            'Total greeneries',
            'Total victory points'
        ]
    else:
        raise AttributeError('No such game type in database: ' + game_type_name)


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
    if len(expansions) > 0:
        for index in range(len(expansions)):
            separator = ',' if index < len(expansions) - 1 else ''
            values += f'({round_id}, {board_id}, {expansions[index]}){separator}'
    else:
        values += f'({round_id}, {board_id}, NULL)'
    return values


def init_round_players_values(round_id, players):
    values = ""
    for index in range(len(players)):
        separator = ',' if index < len(players) - 1 else ''
        player = players[index]
        player_id, corporation_id = player[0], player[1]
        values += f'({round_id}, {player_id}, {corporation_id}){separator}'
    return values


def insert_point_values(round_id, round_data):
    round_points = count_round_points(round_data)
    values = ''
    for index in range(len(round_data)):
        player = round_data[index]
        separator = ', ' if index < len(round_data) - 1 else ''
        points = add_points(player['points'])
        player_id = player["playerId"]
        player_round_point = round_points[player_id]
        values += f'({round_id}, {player_id}, {points}{player["total"]}, {player_round_point}){separator}'
    return values


def count_round_points(round_data):
    first = 3
    second = 2
    third = 1
    player_id = 0
    player_points = []
    for player in round_data:
        player_points.append((player['playerId'],
                              int(player['total']),
                              int(player['points']['mega_credits']),
                              int(player['points']['tr_number']),
                              int(player['points']['vp_on_cards'])))
    player_points.sort(
        key=lambda player_point: (player_point[1], player_point[2], player_point[3], player_point[4], player_point[0]),
        reverse=True)
    points = {}
    number_of_players = len(player_points)
    for index in range(number_of_players):
        player = player_points[index]
        if index == 0:
            points[player[player_id]] = first
        elif index == 1:
            points[player[player_id]] = second
        elif index == 2:
            points[player[player_id]] = third
        else:
            points[player[player_id]] = 0
    return points


def add_points(points):
    point_types = [
        'tr_number',
        'milestones_points',
        'award_points',
        'number_of_own_greeneries',
        'number_of_cities',
        'greeneries_around_cities',
        'vp_on_cards',
        'mega_credits'
    ]
    point_query_values = ''
    for index in range(len(points)):
        value = points[point_types[index]]
        value = value if value else 'NULL'
        point_query_values += f'{value}, '
    return point_query_values
