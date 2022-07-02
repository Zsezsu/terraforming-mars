--------------------------------------------------CREATE ranks table--------------------------------------------------
--DROP ranks id primary key
ALTER TABLE IF EXISTS ONLY public.ranks
    DROP CONSTRAINT IF EXISTS pk_ranks_id;

--CREATE ranks table
DROP TABLE IF EXISTS ranks;
CREATE TABLE public.ranks
(
    id         SERIAL,
    name       TEXT,
    rank_level INTEGER UNIQUE NOT NULL

);

--ADD ranks id primary key
ALTER TABLE IF EXISTS ONLY public.ranks
    ADD CONSTRAINT pk_ranks_id PRIMARY KEY (id);

-------------------------------------------------UPDATE players table-------------------------------------------------
--DROP ranks id foreign key
ALTER TABLE IF EXISTS ONLY public.players
    DROP CONSTRAINT IF EXISTS fk_ranks_id;

--ADD new ranks id column to players table
ALTER TABLE IF EXISTS players
    ADD COLUMN IF NOT EXISTS ranks_id INTEGER;

--ADD ranks id foreign key to players table
ALTER TABLE IF EXISTS public.players
    ADD CONSTRAINT fk_ranks_id FOREIGN KEY (ranks_id) REFERENCES ranks (id);

-----------------------------------------------------INSERT ranks-----------------------------------------------------

INSERT INTO public.ranks(name, rank_level)
VALUES ('Space Traveller', 1),
       ('Dock Worker', 2),
       ('Settler', 3),
       ('trader', 4),
       ('Astronaut', 5),
       ('Builder', 6),
       ('Terraformer', 7),
       ('President', 8),
       ('League Master', 9),
       ('League Grand Master', 10);