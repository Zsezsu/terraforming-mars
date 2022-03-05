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
ALTER TABLE IF EXISTS ONLY public.players           DROP CONSTRAINT IF EXISTS players_pkey          CASCADE;

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
ALTER TABLE IF EXISTS ONLY public.points            DROP CONSTRAINT IF EXISTS fk_round_id           CASCADE;


--------------------------------------------------Game Properties--------------------------------------------------

DROP TABLE IF EXISTS images;
CREATE TABLE images
(
    id          SERIAL UNIQUE NOT NULL,
    source       TEXT,
    league_card BOOLEAN DEFAULT FALSE,
    round_card  BOOLEAN DEFAULT FALSE,
    user_image  BOOLEAN DEFAULT FALSE,
    corporation BOOLEAN DEFAULT FALSE
);

DROP TABLE IF EXISTS corporations;
CREATE TABLE corporations
(
    id              SERIAL UNIQUE NOT NULL,
    name            TEXT,
    expansion_id    INTEGER,
    image_id        INTEGER,
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



DROP TABLE IF EXISTS players;
CREATE TABLE players
(
    id          SERIAL UNIQUE  NOT NULL,
    username    TEXT UNIQUE    NOT NULL,
    first_name  TEXT           NOT NULL,
    last_name   TEXT           NOT NULL,
    email       VARCHAR UNIQUE NOT NULL,
    password    VARCHAR        NOT NULL,
    image_id    INTEGER,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS leagues;
CREATE TABLE leagues
(
    id              SERIAL UNIQUE NOT NULL,
    league_name     TEXT,
    league_admin    INTEGER       NULL,
    round_number    INTEGER,
    image_id        INTEGER,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS league_players;
CREATE TABLE league_players
(
    id        SERIAL UNIQUE,
    league_id INTEGER,
    player_id INTEGER,
    CONSTRAINT fk_league_id
        FOREIGN KEY (league_id)
            REFERENCES leagues (id) ON DELETE CASCADE
);

DROP TABLE IF EXISTS rounds;
CREATE TABLE rounds
(
    id          SERIAL UNIQUE NOT NULL,
    league_id   INTEGER,
    sequence    INTEGER,
    started     BOOLEAN DEFAULT FALSE,
    finished    BOOLEAN DEFAULT FALSE,
    image_id    INTEGER,
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

DROP TABLE IF EXISTS points;
CREATE TABLE points
(
    id                       SERIAL UNIQUE NOT NULL,
    round_id                 INTEGER,
    player_id                INTEGER,
    tr_number                INTEGER       NOT NULL,
    milestones_points        INTEGER,
    award_points             INTEGER,
    number_of_own_greeneries INTEGER,
    number_of_cities         INTEGER,
    greeneries_around_cities INTEGER,
    vp_on_cards              INTEGER,
    sum_points               INTEGER,
    CONSTRAINT fk_round_id
        FOREIGN KEY (round_id)
            REFERENCES rounds (id) ON DELETE CASCADE
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
    ('Terraformer',     1,      NULL),
    ('Mayor',           1,      NULL),
    ('Gardener',        1,      NULL),
    ('Builder',         1,      NULL),
    ('Planner',         1,      NULL),
    ('Generalist',      2,      NULL),
    ('Specialist',      2,      NULL),
    ('Ecologist',       2,      NULL),
    ('Tycoon',          2,      NULL),
    ('Legend',          2,      NULL),
    ('Diversifier',     3,      NULL),
    ('Tactician',       3,      NULL),
    ('Polar Explorer',  3,      NULL),
    ('Energizer',       3,      NULL),
    ('Rim Settler',     3,      NULL),
    ('Hoverlord',       NULL,   2);

INSERT INTO
    awards(awards_name, board_id, expansion_id)
VALUES
    ('Landlord',        1,      NULL),
    ('Banker',          1,      NULL),
    ('Scientist',       1,      NULL),
    ('Hermalist',       1,      NULL),
    ('Miner',           1,      NULL),
    ('Celebrity',       2,      NULL),
    ('Industrialist',   2,      NULL),
    ('Desert Settler',  2,      NULL),
    ('Estate Dealer',   2,      NULL),
    ('Benefactor',      2,      NULL),
    ('Cultivator',      3,      NULL),
    ('Magnate',         3,      NULL),
    ('Space Baron',     3,      NULL),
    ('Excentric',       3,      NULL),
    ('Contractor',      3,      NULL),
    ('Venuphille',      NULL,   2);

INSERT INTO
    corporations(name, expansion_id, image_id)
VALUES
    ('Credicor',                        NULL, NULL),
    ('Ecoline',                         NULL, NULL),
    ('Helion',                          NULL, NULL),
    ('Mining Guild',                    NULL, NULL),
    ('Interplanetary Cinematics',       NULL, NULL),
    ('Inventrix',                       NULL, NULL),
    ('Phobolog',                        NULL, NULL),
    ('Tharsis Rebuplic',                NULL, NULL),
    ('Thorgate',                        NULL, NULL),
    ('United Nations Mars Initiative',  NULL, NULL),
    ('Teractor',                        NULL, NULL),
    ('Saturn Systems',                  NULL, NULL),
    ('Aphrodite',                       NULL, 2),
    ('Celestic',                        NULL, 2),
    ('Manutech',                        NULL, 2),
    ('Morning Star Inc',                NULL, 2),
    ('Viron',                           NULL, 2),
    ('Cheung Shing Mars',               NULL, 1),
    ('Point Luna',                      NULL, 1),
    ('Robinson Industries',             NULL, 1),
    ('Valley Trust',                    NULL, 1),
    ('Vitor',                           NULL, 1),
    ('Aridor',                          NULL, 3),
    ('Arklight',                        NULL, 3),
    ('Polyphemos',                      NULL, 3),
    ('Poseidon',                        NULL, 3),
    ('Storm Craft Incorporated',        NULL, 3);


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