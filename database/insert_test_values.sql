INSERT INTO
    players(username, first_name, last_name, email, password)
VALUES
    ('Zsu', 'Zsu', 'Juhász', 'zsu@mars.hu', '1234'),
    ('Bende', 'Bendegúz', 'Dudaskó', 'bende@mars.hu', '1234'),
    ('Benedek', 'Benedek', 'Halaj', 'benedek@mars.hu', '1234'),
    ('Viktor', 'Viktor', 'Sági', 'viktor@mars.hu', '1234'),
    ('Akárki', 'Akar', 'ki', 'akarki@mars.hu', '1234');

INSERT INTO
    leagues(round_number)
VALUES
    (5);

INSERT INTO
    rounds(league_id, sequence)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5);

INSERT INTO
    game_setup(round_id, board_id, expansion_id)
VALUES
    (1, 1, 1),
    (2, 1, 2),
    (3, 1, 2),
    (4, 2, 2),
    (5, 3, 1);

INSERT INTO
    points(round_id, player_id, tr_number, milestones_points,
           award_points, number_of_own_greeneries, number_of_cities, greeneries_around_cities, vp_on_cards, sum_points)
VALUES
    (1, 1,1, 44, 5, 5, 5, 2, 8, 12),
    (1, 2,2, 48, 5, 5, 4, 3, 11, 3),
    (1, 3,3, 51, 5, 5, 6, 4, 6, 6),
    (1, 4,4, 40, 5, 5, 7, 2, 4, 8),
    (1, 5,5, 60, 5, 5, 13, 2, 9, 10);