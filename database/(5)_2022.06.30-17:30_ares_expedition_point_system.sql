--RENAME points table to mars_points
ALTER TABLE IF EXISTS public.points
    RENAME TO mars_points;
--RENAME points primary key
ALTER INDEX IF EXISTS pk_points_id RENAME TO pk_mars_points_id;


--DROP foreign keys to ares_points
ALTER TABLE IF EXISTS ONLY public.ares_points
    DROP CONSTRAINT IF EXISTS fk_round_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.ares_points
    DROP CONSTRAINT IF EXISTS fk_player_id CASCADE;
--DROP primary key to ares_points
ALTER TABLE IF EXISTS ONLY public.ares_points
    DROP CONSTRAINT IF EXISTS pk_ares_points_id;

--CREATE ares_points table
DROP TABLE IF EXISTS ares_points;
CREATE TABLE ares_points
(
    id                       SERIAL,
    round_id                 INTEGER NOT NULL,
    player_id                INTEGER NOT NULL,
    tr_number                INTEGER NOT NULL,
    number_of_own_greeneries INTEGER,
    vp_on_cards              INTEGER,
    mega_credits             INTEGER,
    sum_points               INTEGER,
    round_points             INTEGER
);

--CREATE primary key to ares_points
ALTER TABLE IF EXISTS ONLY public.ares_points
    ADD CONSTRAINT pk_ares_points_id PRIMARY KEY (id);
--CREATE foreign key to ares_points
ALTER TABLE IF EXISTS ONLY public.ares_points
    ADD CONSTRAINT
        fk_round_id FOREIGN KEY (round_id) REFERENCES rounds (id) ON DELETE CASCADE;
ALTER TABLE IF EXISTS ONLY public.ares_points
    ADD CONSTRAINT
        fk_player_id FOREIGN KEY (player_id) REFERENCES players (id) ON DELETE CASCADE;
