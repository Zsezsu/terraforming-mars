--
-- PostrgeSQL database dump
--

-- Database version = 13.6

---------------------------------------------Drop primary keys-----------------------------------------------------

ALTER TABLE IF EXISTS ONLY public.corporations      DROP CONSTRAINT IF EXISTS corporations_pkey     CASCADE;
ALTER TABLE IF EXISTS ONLY public.corporations      DROP CONSTRAINT IF EXISTS corporations_id_key   CASCADE;
ALTER TABLE IF EXISTS ONLY public.boards            DROP CONSTRAINT IF EXISTS boards_pkey           CASCADE;
ALTER TABLE IF EXISTS ONLY public.expansions        DROP CONSTRAINT IF EXISTS expansions_pkey       CASCADE;
ALTER TABLE IF EXISTS ONLY public.legues            DROP CONSTRAINT IF EXISTS leagues_pkey          CASCADE;
ALTER TABLE IF EXISTS ONLY public.results           DROP CONSTRAINT IF EXISTS results_pkey          CASCADE;

---------------------------------------------Drop foreign keys-----------------------------------------------------

ALTER TABLE IF EXISTS ONLY public.milestones        DROP CONSTRAINT IF EXISTS fk_board_id           CASCADE;
ALTER TABLE IF EXISTS ONLY public.milestones        DROP CONSTRAINT IF EXISTS fk_expansion_id       CASCADE;
ALTER TABLE IF EXISTS ONLY public.milestones        DROP CONSTRAINT IF EXISTS fk_expansion_id       CASCADE;
ALTER TABLE IF EXISTS ONLY public.awards            DROP CONSTRAINT IF EXISTS fk_board_id           CASCADE;
ALTER TABLE IF EXISTS ONLY public.legues            DROP CONSTRAINT IF EXISTS fk_league_id          CASCADE;
ALTER TABLE IF EXISTS ONLY public.league_players    DROP CONSTRAINT IF EXISTS fk_league_id          CASCADE;
ALTER TABLE IF EXISTS ONLY public.rounds            DROP CONSTRAINT IF EXISTS fk_league_id          CASCADE;
ALTER TABLE IF EXISTS ONLY public.round_players     DROP CONSTRAINT IF EXISTS fk_round_id           CASCADE;
ALTER TABLE IF EXISTS ONLY public.round_players     DROP CONSTRAINT IF EXISTS fk_corporation_id     CASCADE;
ALTER TABLE IF EXISTS ONLY public.game_setup        DROP CONSTRAINT IF EXISTS fk_round_id           CASCADE;
ALTER TABLE IF EXISTS ONLY public.game_setup        DROP CONSTRAINT IF EXISTS fk_board_id           CASCADE;
ALTER TABLE IF EXISTS ONLY public.game_setup        DROP CONSTRAINT IF EXISTS fk_expansion_id       CASCADE;
ALTER TABLE IF EXISTS ONLY public.results           DROP CONSTRAINT IF EXISTS fk_round_id           CASCADE;

--------------------------------------------------Game Properties--------------------------------------------------


DROP TABLE IF EXISTS corporations;
CREATE TABLE corporations
(
    id    SERIAL UNIQUE NOT NULL,
    name  TEXT,
    image VARCHAR,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS boards;
CREATE TABLE boards
(
    id         SERIAL UNIQUE NOT NULL,
    board_name TEXT,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS expansions;
CREATE TABLE expansions
(
    id             SERIAL UNIQUE NOT NULL,
    expansion_name TEXT          NOT NULL,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS milestones;
CREATE TABLE milestones
(
    id             SERIAL UNIQUE NOT NULL,
    milestone_name TEXT          NOT NULL,
    board_id       INTEGER,
    expansion_id   INTEGER,
    CONSTRAINT fk_board_id
        FOREIGN KEY (board_id)
            REFERENCES boards (id) ON DELETE CASCADE,
    CONSTRAINT fk_expansion_id
        FOREIGN KEY (expansion_id)
            REFERENCES expansions (id)
);

DROP TABLE IF EXISTS awards;
CREATE TABLE awards
(
    id           SERIAL UNIQUE NOT NULL,
    awards_name  TEXT          NOT NULL,
    board_id     INTEGER,
    expansion_id INTEGER,
    CONSTRAINT fk_board_id
        FOREIGN KEY (board_id)
            REFERENCES boards (id) ON DELETE CASCADE,
    CONSTRAINT fk_expansion_id
        FOREIGN KEY (expansion_id)
            REFERENCES expansions (id)
);

--------------------------------------------------Create Tables--------------------------------------------------


ALTER TABLE IF EXISTS ONLY public.players
    DROP CONSTRAINT IF EXISTS players_pkey CASCADE;
DROP TABLE IF EXISTS players;
CREATE TABLE players
(
    id       SERIAL UNIQUE  NOT NULL,
    username TEXT UNIQUE    NOT NULL,
    email    VARCHAR UNIQUE NOT NULL,
    password VARCHAR        NOT NULL,
    image    VARCHAR,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS leagues;
CREATE TABLE leagues
(
    id           SERIAL UNIQUE NOT NULL,
    league_admin INTEGER       NULL,
    round_number INTEGER,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS league_players;
CREATE TABLE league_players
(
    id        SERIAL UNIQUE,
    league_id INTEGER,
    CONSTRAINT fk_league_id
        FOREIGN KEY (league_id)
            REFERENCES leagues (id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS rounds;
CREATE TABLE rounds
(
    id        SERIAL UNIQUE NOT NULL,
    league_id INTEGER,
    CONSTRAINT fk_league_id
        FOREIGN KEY (league_id)
            REFERENCES leagues (id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS round_players;
CREATE TABLE round_players
(
    id             SERIAL UNIQUE NOT NULL,
    round_id       INTEGER,
    player_id      INTEGER,
    corporation_id INTEGER,
    CONSTRAINT fk_round_id
        FOREIGN KEY (round_id)
            REFERENCES rounds (id) ON DELETE CASCADE,
    CONSTRAINT fk_corporation_id
        FOREIGN KEY (corporation_id)
            REFERENCES corporations (id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS game_setup;
CREATE TABLE game_setup
(
    id           SERIAL UNIQUE NOT NULL,
    round_id     INTEGER,
    board_id     INTEGER,
    expansion_id INTEGER,
    CONSTRAINT fk_round_id
        FOREIGN KEY (round_id)
            REFERENCES rounds (id) ON DELETE CASCADE,
    CONSTRAINT fk_board_id
        FOREIGN KEY (board_id)
            REFERENCES boards (id) ON DELETE CASCADE,
    CONSTRAINT fk_expansion_id
        FOREIGN KEY (expansion_id)
            REFERENCES expansions (id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS results;
CREATE TABLE results
(
    id         SERIAL UNIQUE NOT NULL,
    round_id   INTEGER,
    player_id  INTEGER,
    sum_points INTEGER,
    PRIMARY KEY (id),
    CONSTRAINT fk_round_id
        FOREIGN KEY (round_id)
            REFERENCES rounds (id) ON DELETE CASCADE
);

ALTER TABLE IF EXISTS ONLY public.points
    DROP CONSTRAINT IF EXISTS fk_result_id CASCADE;
DROP TABLE IF EXISTS points;
CREATE TABLE points
(
    id                       SERIAL UNIQUE NOT NULL,
    result_id                INTEGER,
    tr_number                INTEGER       NOT NULL,
    milestones_points        INTEGER,
    award_points             INTEGER,
    number_of_own_greeneries INTEGER,
    number_of_cities         INTEGER,
    greeneries_around_cities INTEGER,
    vp_on_cards              INTEGER,
    CONSTRAINT fk_result_id
        FOREIGN KEY (result_id)
            REFERENCES results (id) ON DELETE CASCADE
);

----------------------------------------------------Insert---------------------------------------------------------
INSERT INTO
    boards(board_name)
VALUES
    ('Basic'),
    ('Elysium'),
    ('Hellas');

INSERT INTO
    expansions(expansion_name)
VALUES
    ('Prelude'),
    ('Venus Next'),
    ('Colonies');

INSERT INTO
    milestones(milestone_name, board_id, expansion_id)
VALUES
    ('Terraformer',1, null),
    ('Mayor', 1, null),
    ('Gardener', 1, null),
    ('Builder', 1, null),
    ('Planner', 1, null),
    ('Generalist',2 , null),
    ('Specialist',2 , null),
    ('Ecologist',2 , null),
    ('Tycoon',2 , null),
    ('Legend',2 , null),
    ('Hoverlord', null, 2);

INSERT INTO
    awards(awards_name, board_id, expansion_id)
VALUES
    ('Landlord', 1, null),
    ('Banker', 1, null),
    ('Scientist', 1, null),
    ('hermalist', 1, null),
    ('Miner', 1, null),
    ('Celebrity', 2, null),
    ('Industrialist', 2, null),
    ('Desert Settler', 2, null),
    ('Estate Dealer', 2, null),
    ('Benefactor', 2, null),
    ('Venuphille', null, 2)


/*Terraforming Mars database

Tables:

Players

Leagues
League_players #connect table

Rounds
Round_player 	#connect table

Game setup 	#connect table
Boards
Expansions

Results
Points
Milestones
Awards

Nem tudom hogy kell-e:
Corporations - felsorolni a cégeket



Columns on tables:

Players table columns:
id (unique, primary key) / username (unique) / email (uniqe) / password / image

Leagues table columns:
id (unique, primary key) / league_admin (who created the league, player_id) / round_number (not null, max 10 ?)

League_players columns:
id (unique, primary key) / league_id / player_id


Rounds columns:
id (unique, primary key) / league_id (not null, foreign key)

Round_players columns:
id (unique, primary key) / round_id (foreign key) / player_id


Game_setup columns:
id (unique, primary key) / round_id / board_id / expansion_id



Boards columns:
id (unique, primary key) / board_name
			1 Basic
			2 Elysium
			3 Hellas

Expansions table columns:
id (unique, primary key) / expansion_name
			1 Prelude
			2 Venus Next
			3 Colonies



Milestones columns:
id (unique, primary key) / milestone_name / board_id / expansion_id
		1 	/ Terraformer 	/ 1		/ null
		2 	/ Mayor	/ 1		/ null
		3	/ Gardener	/ 1		/ null
		4	/ Builder	/ 1		/ null
		5	/ Planner	/ 1		/ null
		6	/ Generalist	/ 2		/ null
		7	/ Specialist	/ 2		/ null
		8	/ Ecologist	/ 2		/ null
		9 	/ Tycoon	/ 2		/ null
		10	/ Legend	/ 2 		/ null
		11	/ Hoverlord	/ null		/ 2


Awards columns:
id (unique, primary key) / award_name / board_id / expansion_id
		1	/ Landlord	/1		/ null
		2	/ Banker	/1		/ null
		3	/ Scientist	/1		/ null
		4	/ Thermalist	/1		/ null
		5	/ Miner	/1		/ null
		6 	/ Celebrity	/2		/ null
		7	/ Industrialist/2		/ null
		8	/ Desert Settler/2		/ null
		9 	/ Estate Dealer/2		/ null
		10	/ Benefactor	/2		/ null
		11	/ Venuphille	/null		/ 2


Results columns:
id (unique, primary key) / round_id (not null, foreign key) / player_id / sum_points

!!! nem biztos hogy külön kell szedni a results és a points táblákat, de egyben túl nagynak éreztem !!!

Points columns:
id (unique, primary key) / result_id / tr_number (not null) / milestone_points / award_points / number_of_own_greeneries / number_of_cities / greeneries_around_cities / vp_on_cards
*/