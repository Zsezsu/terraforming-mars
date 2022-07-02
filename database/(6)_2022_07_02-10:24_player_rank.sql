--DROP ranks id foreign key
ALTER TABLE IF EXISTS ONLY public.players
    DROP CONSTRAINT IF EXISTS fk_ranks_id;

--------------------------------------------------CREATE ranks table--------------------------------------------------
--DROP ranks id primary key
ALTER TABLE IF EXISTS ONLY public.ranks
    DROP CONSTRAINT IF EXISTS pk_ranks_id;

--CREATE ranks table
DROP TABLE IF EXISTS ranks;
CREATE TABLE public.ranks
(
    id             SERIAL,
    name           TEXT,
    rank_level     INTEGER UNIQUE NOT NULL,
    minimum_points INTEGER        NOT NULL

);

--ADD ranks id primary key
ALTER TABLE IF EXISTS ONLY public.ranks
    ADD CONSTRAINT pk_ranks_id PRIMARY KEY (id);

-------------------------------------------------UPDATE players table-------------------------------------------------
--DROP ranks_id column if exist from players table
ALTER TABLE IF EXISTS players
    DROP COLUMN IF EXISTS ranks_id;
--CREATE a function to get the default rank level from the table ranks with default rank level as an argument.
CREATE OR REPLACE FUNCTION default_rank_level_id(default_rank_level INTEGER) RETURNS INT
    LANGUAGE SQL AS
$$
SELECT id
FROM ranks
WHERE rank_level = default_rank_level;
$$;
--ADD new ranks id column to players table with default rank level
ALTER TABLE IF EXISTS players
    ADD COLUMN IF NOT EXISTS ranks_id INTEGER DEFAULT default_rank_level_id(1);


--ADD ranks id foreign key to players table
ALTER TABLE IF EXISTS public.players
    ADD CONSTRAINT fk_ranks_id FOREIGN KEY (ranks_id) REFERENCES ranks (id);



-----------------------------------------------------INSERT ranks-----------------------------------------------------

INSERT INTO public.ranks(name, rank_level, minimum_points)
VALUES ('Space Traveller', 1, 0),
       ('Dock Worker', 2, 3),
       ('Settler', 3, 10),
       ('trader', 4, 20),
       ('Astronaut', 5, 30),
       ('Builder', 6, 50),
       ('Terraformer', 7, 80),
       ('President', 8, 100),
       ('League Master', 9, 120),
       ('League Grand Master', 10, 150);
