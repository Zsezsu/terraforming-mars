INSERT INTO
    corporations(name)
VALUES
    ('Celestior'),
    ('DevTechs'),
    ('Launch Star Incorporated'),
    ('Mai-Ni Productions'),
    ('Zetasel');

INSERT INTO
    game_types_corporations_expansions(game_type_id, expansion_id, corporation_id)
VALUES
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Credicor')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Ecoline')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Helion')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Mining Guild')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Interplanetary Cinematics')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Inventrix')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Phobolog')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Tharsis Rebuplic')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Thorgate')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'United Nations Mars Initiative')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Teractor')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Saturn Systems')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Arklight')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Celestior')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'DevTechs')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Launch Star Incorporated')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Mai-Ni Productions')),
    ((SELECT id FROM game_types WHERE name = 'Ares Expedition'), NULL, (SELECT id FROM corporations WHERE name = 'Zetasel'));
