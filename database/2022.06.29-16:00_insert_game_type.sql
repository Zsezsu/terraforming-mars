---------------------------------------------Drop foreign keys-----------------------------------------------------

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    DROP CONSTRAINT IF EXISTS fk_game_type_id CASCADE;

ALTER TABLE IF EXISTS ONLY public.expansions
    DROP CONSTRAINT IF EXISTS fk_game_type_id CASCADE;

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    DROP CONSTRAINT IF EXISTS fk_expansion_id CASCADE;

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    DROP CONSTRAINT IF EXISTS fk_corporation_id CASCADE;


---------------------------------------------Drop primary keys-----------------------------------------------------

ALTER TABLE IF EXISTS ONLY public.game_types
    DROP CONSTRAINT IF EXISTS pk_game_types_id CASCADE;


--------------------------------------------------Create Tables--------------------------------------------------

DROP TABLE IF EXISTS game_types;
CREATE TABLE game_types
(
    id   SERIAL,
    name VARCHAR
);
--CREATE primary key to game_type.id
ALTER TABLE IF EXISTS ONLY public.game_types
    ADD CONSTRAINT pk_game_types_id PRIMARY KEY (id);

INSERT INTO game_types(name)
VALUES ('Terraforming Mars'),
       ('Ares Expedition');


-----------------------------------------------------------------------------------------------------------------
-- ADD new column to expansions table.

ALTER TABLE IF EXISTS expansions
    ADD COLUMN IF NOT EXISTS game_type_id INTEGER;

-- UPDATE some Mars's expansions game_type_id to NULL
UPDATE expansions
SET game_type_id = NULL

WHERE expansion_name = 'Prelude'
   OR expansion_name = 'Venus Next'
   OR expansion_name = 'Colonies';

--CREATE expansion foreign key(game types id)
ALTER TABLE IF EXISTS ONLY public.expansions
    ADD CONSTRAINT
        fk_game_type_id FOREIGN KEY (game_type_id) REFERENCES game_types (id) ON DELETE CASCADE;

DELETE
FROM expansions
WHERE expansion_name = 'Turmoil'
   OR expansion_name = 'Promo';

INSERT INTO expansions(expansion_name)
VALUES ('Turmoil'),
       ('Promo');

UPDATE expansions
SET game_type_id = (SELECT id FROM game_types WHERE name = 'Terraforming Mars')

WHERE expansion_name = 'Prelude'
   OR expansion_name = 'Venus Next'
   OR expansion_name = 'Colonies'
   OR expansion_name = 'Turmoil'
   OR expansion_name = 'Promo';

---------------------------------------------------------------------------------------------------------------

DROP TABLE IF EXISTS game_types_corporations_expansions;
CREATE TABLE game_types_corporations_expansions
(
    id             SERIAL,
    game_type_id   INTEGER,
    expansion_id   INTEGER,
    corporation_id INTEGER
);
--CREATE foreign keys to game_types_corporations_expansions
ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    ADD CONSTRAINT
        fk_game_type_id FOREIGN KEY (game_type_id) REFERENCES game_types (id) ON DELETE CASCADE;

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    ADD CONSTRAINT
        fk_expansion_id FOREIGN KEY (expansion_id) REFERENCES expansions (id) ON DELETE CASCADE;

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    ADD CONSTRAINT
        fk_corporation_id FOREIGN KEY (corporation_id) REFERENCES corporations (id) ON DELETE CASCADE;



-----------------------------------------------------------------------------------------------------------------
-- DROP unused column from corporations table.

ALTER TABLE IF EXISTS corporations
    DROP COLUMN IF EXISTS expansion_id;


-----------------------------------------------------------------------------------------------------------------
-- ADD new column to leagues table.

-- DROP already existing foreign key if exist
ALTER TABLE IF EXISTS ONLY public.leagues
    DROP CONSTRAINT IF EXISTS fk_game_type_id CASCADE;

-- ADD new game_type_id column to leagues if not exist
ALTER TABLE IF EXISTS leagues
    ADD COLUMN IF NOT EXISTS game_type_id INTEGER;

-- ADD new foreign key to leagues(game_type_id)
ALTER TABLE IF EXISTS ONLY public.leagues
    ADD CONSTRAINT
        fk_game_type_id FOREIGN KEY (game_type_id) REFERENCES game_types (id) ON DELETE CASCADE;

-- UPDATE already added leagues game type to terraforming mars's game type id
UPDATE public.leagues
SET game_type_id = (SELECT id FROM game_types WHERE name = 'Terraforming Mars')
WHERE leagues.game_type_id IS NULL;

-----------------------------------------------------------------------------------------------------------------
-- ADD new column to boards table.

-- DROP already existing foreign key if exist
ALTER TABLE IF EXISTS ONLY public.boards
    DROP CONSTRAINT IF EXISTS fk_game_type_id CASCADE;

--ADD new game_type_id column to boards if not exist
ALTER TABLE IF EXISTS boards
    ADD COLUMN IF NOT EXISTS game_type_id INTEGER;

-- ADD new foreign key to boards(game_type_id)
ALTER TABLE IF EXISTS ONLY public.boards
    ADD CONSTRAINT
        fk_game_type_id FOREIGN KEY (game_type_id) REFERENCES game_types (id) ON DELETE CASCADE;

-- UPDATE already added tearraforming mars's boards with terraforming mars's id
DELETE
FROM boards
WHERE board_name = 'Basic' AND boards.game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition');

-- INSERT new basic board to Ares
UPDATE public.boards
SET game_type_id = (SELECT id FROM game_types WHERE name = 'Terraforming Mars')
WHERE boards.board_name = 'Basic'
   OR boards.board_name = 'Elysium'
   OR boards.board_name = 'Hellas';

INSERT INTO boards(board_name, game_type_id)
VALUES ('Basic', (SELECT id FROM game_types WHERE name = 'Ares Expedition'));

--------------------------------------------Insert corporation relations------------------------------------------
DELETE
FROM corporations
WHERE name = 'Pharmacy Union'
   OR name = 'Astrodrill Enterprise'
   OR name = 'Factorum'
   OR name = 'Mons Insurance'
   OR name = 'Philares'
   OR name = 'Arcadian Communities'
   OR name = 'Recyclon'
   OR name = 'Splice Tactical Genomics'
   OR name = 'Lakefront Resorts'
   OR name = 'Pristar'
   OR name = 'Septem Tribus'
   OR name = 'Terralabs Research'
   OR name = 'Utopia Invest';

INSERT INTO corporations(name)
VALUES ('Pharmacy Union'),
       ('Astrodrill Enterprise'),
       ('Factorum'),
       ('Mons Insurance'),
       ('Philares'),
       ('Arcadian Communities'),
       ('Recyclon'),
       ('Splice Tactical Genomics'),
       ('Lakefront Resorts'),
       ('Pristar'),
       ('Septem Tribus'),
       ('Terralabs Research'),
       ('Utopia Invest');

--------------------------------------------Insert corporation's relations------------------------------------------

--BASE GAME CORPORATION'S RELATIONS--

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Credicor'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Ecoline'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Helion'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Mining Guild'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Interplanetary Cinematics'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Inventrix'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Phobolog'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Tharsis Rebuplic'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Teractor'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Thorgate'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'United Nations Mars Initiative'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'), NULL,
        (SELECT id FROM corporations WHERE name = 'Saturn Systems'));

--VENUS NEXT CORPORATION'S RELATIONS--

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Venus Next'),
        (SELECT id FROM corporations WHERE name = 'Aphrodite'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Venus Next'),
        (SELECT id FROM corporations WHERE name = 'Celestic'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Venus Next'),
        (SELECT id FROM corporations WHERE name = 'Manutech'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Venus Next'),
        (SELECT id FROM corporations WHERE name = 'Morning Star Inc'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Venus Next'),
        (SELECT id FROM corporations WHERE name = 'Viron'));

--PRELUDE CORPORATION'S RELATIONS--

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Prelude'),
        (SELECT id FROM corporations WHERE name = 'Cheung Shing Mars'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Prelude'),
        (SELECT id FROM corporations WHERE name = 'Point Luna'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Prelude'),
        (SELECT id FROM corporations WHERE name = 'Robinson Industries'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Prelude'),
        (SELECT id FROM corporations WHERE name = 'Valley Trust'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Prelude'),
        (SELECT id FROM corporations WHERE name = 'Vitor'));

--COLONIES CORPORATION'S RELATIONS--

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Colonies'),
        (SELECT id FROM corporations WHERE name = 'Aridor'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Colonies'),
        (SELECT id FROM corporations WHERE name = 'Arklight'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Colonies'),
        (SELECT id FROM corporations WHERE name = 'Polyphemos'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Colonies'),
        (SELECT id FROM corporations WHERE name = 'Poseidon'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Colonies'),
        (SELECT id FROM corporations WHERE name = 'Storm Craft Incorporated'));

--TURMOIL CORPORATION'S RELATIONS--

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Turmoil'),
        (SELECT id FROM corporations WHERE name = 'Lakefront Resorts'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Turmoil'),
        (SELECT id FROM corporations WHERE name = 'Pristar'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Turmoil'),
        (SELECT id FROM corporations WHERE name = 'Septem Tribus'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Turmoil'),
        (SELECT id FROM corporations WHERE name = 'Terralabs Research'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Turmoil'),
        (SELECT id FROM corporations WHERE name = 'Utopia Invest'));

--TURMOIL CORPORATION'S RELATIONS--

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Promo'),
        (SELECT id FROM corporations WHERE name = 'Pharmacy Union'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Promo'),
        (SELECT id FROM corporations WHERE name = 'Astrodrill Enterprise'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Promo'),
        (SELECT id FROM corporations WHERE name = 'Factorum'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Promo'),
        (SELECT id FROM corporations WHERE name = 'Mons Insurance'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Promo'),
        (SELECT id FROM corporations WHERE name = 'Philares'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Promo'),
        (SELECT id FROM corporations WHERE name = 'Arcadian Communities'));

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Promo'),
        (SELECT id FROM corporations WHERE name = 'Recyclon'));


INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Terraforming Mars'),
        (SELECT id FROM expansions WHERE expansion_name = 'Promo'),
        (SELECT id FROM corporations WHERE name = 'Splice Tactical Genomics'));
