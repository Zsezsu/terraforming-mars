ALTER TABLE IF EXISTS mars_points
    DROP CONSTRAINT IF EXISTS fk_player_id;

ALTER TABLE IF EXISTS mars_points
    ADD CONSTRAINT fk_player_id
        FOREIGN KEY (player_id) REFERENCES players (id) ON DELETE CASCADE;
