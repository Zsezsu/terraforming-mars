DELETE
FROM corporations
WHERE name = 'Celestior'
   OR name = 'DevTechs'
   OR name = 'Launch Star Incorporated'
   OR name = 'Mai-Ni Productions'
   OR name = 'Zetasel';

INSERT INTO corporations(name)
VALUES ('Celestior'),
       ('DevTechs'),
       ('Launch Star Incorporated'),
       ('Mai-Ni Productions'),
       ('Zetasel');


DELETE
FROM game_types_corporations_expansions
WHERE game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Credicor')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Ecoline')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Helion')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Mining Guild')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Interplanetary Cinematics')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Inventrix')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Phobolog')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Tharsis Rebuplic')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Thorgate')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'United Nations Mars Initiative')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Teractor')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Saturn Systems')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Arklight')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Celestior')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'DevTechs')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Launch Star Incorporated')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Mai-Ni Productions')

   OR game_type_id = (SELECT id FROM game_types WHERE name = 'Ares Expedition')
    AND expansion_id IS NULL
    AND corporation_id = (SELECT id FROM corporations WHERE name = 'Zetasel');

INSERT INTO game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Credicor')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Ecoline')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Helion')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Mining Guild')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Interplanetary Cinematics')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Inventrix')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Phobolog')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Tharsis Rebuplic')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Thorgate')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'United Nations Mars Initiative')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Teractor')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Saturn Systems')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Arklight')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Celestior')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'DevTechs')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Launch Star Incorporated')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Mai-Ni Productions')),

       ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL,
        (SELECT id FROM corporations WHERE name = 'Zetasel'));
