
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



----------------------------------------------------Add Keys---------------------------------------------------------


--------------------------------------------Primary Keys-------------------------------------------------

ALTER TABLE IF EXISTS ONLY public.game_types
    ADD CONSTRAINT pk_game_types_id PRIMARY KEY (id);
