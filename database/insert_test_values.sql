INSERT INTO
    players(username, email, password)
VALUES
    ('Zsu', 'zsu@mars.hu', '1234'),
    ('Bende', 'bende@mars.hu', '1234'),
    ('Benedek', 'benedek@mars.hu', '1234'),
    ('Viktor', 'viktor@mars.hu', '1234'),
    ('Akárki', 'akarki@mars.hu', '1234');

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