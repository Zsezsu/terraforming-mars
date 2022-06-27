---------------------------------------------Drop foreign keys-----------------------------------------------------

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    DROP CONSTRAINT IF EXISTS fk_game_type_id CASCADE;

ALTER TABLE IF EXISTS ONLY public.expansions
    DROP CONSTRAINT IF EXISTS fk_game_type_id CASCADE;

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    DROP CONSTRAINT IF EXISTS fk_expansion_id CASCADE;

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    DROP CONSTRAINT IF EXISTS fk_corporation_id CASCADE;

ALTER TABLE IF EXISTS ONLY public.expansions
    DROP CONSTRAINT IF EXISTS fk_game_type_id CASCADE;


---------------------------------------------Drop primary keys-----------------------------------------------------

ALTER TABLE IF EXISTS ONLY public.game_types
    DROP CONSTRAINT IF EXISTS pk_game_types_id;


--------------------------------------------------Create Tables--------------------------------------------------

DROP TABLE IF EXISTS game_types;
CREATE TABLE game_types
(
    id   SERIAL,
    name VARCHAR
);

DROP TABLE IF EXISTS game_types_corporations_expansions;
CREATE TABLE game_types_corporations_expansions
(
    id             SERIAL,
    game_type_id   INTEGER,
    expansion_id   INTEGER,
    corporation_id INTEGER
);


-----------------------------------------------------------------------------------------------------------------
-- DROP unused column from corporations table.

ALTER TABLE IF EXISTS corporations DROP COLUMN IF EXISTS expansion_id;


-----------------------------------------------------------------------------------------------------------------
-- ADD new column to expansions table.

ALTER TABLE IF EXISTS expansions ADD COLUMN IF NOT EXISTS game_type_id INTEGER;
----------------------------------------------------Add Keys---------------------------------------------------------


--------------------------------------------Primary Keys-------------------------------------------------

ALTER TABLE IF EXISTS ONLY public.game_types
    ADD CONSTRAINT pk_game_types_id PRIMARY KEY (id);


--------------------------------------------Foreign Keys-------------------------------------------------

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    ADD CONSTRAINT
        fk_game_type_id FOREIGN KEY (game_type_id) REFERENCES game_types (id) ON DELETE CASCADE;

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    ADD CONSTRAINT
        fk_expansion_id FOREIGN KEY (expansion_id) REFERENCES expansions (id) ON DELETE CASCADE;

ALTER TABLE IF EXISTS ONLY public.game_types_corporations_expansions
    ADD CONSTRAINT
        fk_corporation_id FOREIGN KEY (corporation_id) REFERENCES corporations (id) ON DELETE CASCADE;

ALTER TABLE IF EXISTS ONLY public.expansions
    ADD CONSTRAINT
        fk_game_type_id FOREIGN KEY (game_type_id) REFERENCES game_types (id) ON DELETE CASCADE;
