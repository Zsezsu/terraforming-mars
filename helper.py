def get_round_status(round):
    round_status = ''
    for key, value in round.items():
        if key == 'started' or key == 'finished':
            if value:
                round_status = key
    round_status = 'init_round' if round_status == '' else round_status
    return round_status
