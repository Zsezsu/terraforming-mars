------------------------------------------------------------
-- 7_prelude2_and_corporations.sql
-- Targets current schema after 3_insert_game_types.sql
--  - expansions: (id, expansion_name, game_type_id)
--  - corporations: (id, name)
--  - game_types: ('Terraforming Mars', 'Ares Expedition')
--  - game_types_corporations_expansions: (id, game_type_id, expansion_id, corporation_id)
------------------------------------------------------------

-- 1) Ensure expansion "Prelude 2" exists and is tied to Terraforming Mars
INSERT INTO expansions (expansion_name, game_type_id)
SELECT 'Prelude 2', (SELECT id FROM game_types WHERE name = 'Terraforming Mars')
WHERE NOT EXISTS (
  SELECT 1 FROM expansions WHERE expansion_name = 'Prelude 2'
);

-- If it already existed without game_type_id, backfill it
UPDATE expansions
SET game_type_id = (SELECT id FROM game_types WHERE name = 'Terraforming Mars')
WHERE expansion_name = 'Prelude 2' AND game_type_id IS NULL;

-- 2) Insert Prelude 2 corporations (only if missing)
INSERT INTO corporations (name)
SELECT v.name
FROM (VALUES
  ('Ecotec'),
  ('Nirgal Enterprises'),
  ('Palladin Shipping'),
  ('Sagitta Frontier Services'),
  ('Spire')
) AS v(name)
WHERE NOT EXISTS (SELECT 1 FROM corporations c WHERE c.name = v.name);

-- Link Prelude 2 corps to TMars + Prelude 2 (CTEs + CROSS JOIN form)
WITH
  gt AS (SELECT id AS game_type_id FROM game_types WHERE name = 'Terraforming Mars' LIMIT 1),
  ex AS (SELECT id AS expansion_id FROM expansions WHERE expansion_name = 'Prelude 2' LIMIT 1),
  corps AS (
    SELECT id AS corporation_id
    FROM corporations
    WHERE name IN ('Ecotec','Nirgal Enterprises','Palladin Shipping','Sagitta Frontier Services','Spire')
  )
INSERT INTO game_types_corporations_expansions (game_type_id, expansion_id, corporation_id)
SELECT gt.game_type_id, ex.expansion_id, corps.corporation_id
FROM corps
CROSS JOIN gt
CROSS JOIN ex
LEFT JOIN game_types_corporations_expansions j
  ON j.game_type_id = gt.game_type_id
 AND j.expansion_id = ex.expansion_id
 AND j.corporation_id = corps.corporation_id
WHERE j.id IS NULL;



-- 4) (Nice-to-have) Fix the original typo in base-game corp name if still present.
UPDATE corporations
SET name = 'Tharsis Republic'
WHERE name = 'Tharsis Rebuplic';

-- NOTE: The Ares mapping file (4_ares_corporations.sql) references 'Tharsis Rebuplic' by name
-- for lookups during INSERT. That script has already run earlier in the chain.
-- Renaming AFTER those inserts is safe because the join table stores corporation_id, not name.
-- If you ever re-run 4_ares_corporations.sql from scratch, update the lookup there too.


------------------------------------------------------------
-- 1) Ensure a generic 'Promo' expansion exists and is tied to TM game type
------------------------------------------------------------
INSERT INTO expansions (expansion_name, game_type_id)
SELECT 'Promo', (SELECT id FROM game_types WHERE name = 'Terraforming Mars')
WHERE NOT EXISTS (
  SELECT 1 FROM expansions e WHERE e.expansion_name = 'Promo'
);

------------------------------------------------------------
-- 2) Standardize Big Box corp name: 'Astrodrill'
--    (rename any legacy 'Astrodrill Enterprise' → 'Astrodrill')
------------------------------------------------------------
UPDATE corporations
SET name = 'Astrodrill'
WHERE LOWER(name) IN ('astrodrill enterprise', 'astrodrill')
  AND name <> 'Astrodrill';

------------------------------------------------------------
-- 3) Ensure all 8 official Promo corporations exist
--    (Promo buckets: Original/Promo Pack, Turmoil Promo, Big Box Promo)
------------------------------------------------------------
WITH need(name) AS (
  VALUES
    ('Arcadian Communities'),
    ('Recyclon'),
    ('Splice Tactical Genomics'),
    ('Factorum'),
    ('Mons Insurance'),
    ('Philares'),
    ('Astrodrill'),
    ('Pharmacy Union')
)
INSERT INTO corporations (name)
SELECT n.name
FROM need n
LEFT JOIN corporations c ON c.name = n.name
WHERE c.id IS NULL;

------------------------------------------------------------
-- 4) Link each promo corp to TM + Promo in the junction table
------------------------------------------------------------
WITH tm AS (
  SELECT id AS game_type_id FROM game_types WHERE name = 'Terraforming Mars'
),
px AS (
  SELECT id AS expansion_id FROM expansions WHERE expansion_name = 'Promo'
),
corp AS (
  SELECT id, name FROM corporations
  WHERE name IN (
    'Arcadian Communities','Recyclon','Splice Tactical Genomics',
    'Factorum','Mons Insurance','Philares','Astrodrill','Pharmacy Union'
  )
)
INSERT INTO game_types_corporations_expansions (game_type_id, expansion_id, corporation_id)
SELECT tm.game_type_id, px.expansion_id, c.id
FROM corp c
CROSS JOIN tm
CROSS JOIN px
LEFT JOIN game_types_corporations_expansions j
  ON j.game_type_id = tm.game_type_id
 AND j.expansion_id = px.expansion_id
 AND j.corporation_id = c.id
WHERE j.id IS NULL;

