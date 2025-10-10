

------------------------------------Insert dummy data Players--------------------------------------

--FOR ALL DUMMY USER, THE PASSWORD IS: Testing1234!
INSERT INTO public.players (id, username, first_name, last_name, email, password, image_id) VALUES (1, 'GrandeCruz', 'Bendegúz', 'Dudaskó', 'dudaskobende@gmail.com', '$2b$12$pKlpXOvw1OpKzOUElhtbzeMIUZt9jnK2xHnHdjstGaQg97gJXi1vG', 19);
INSERT INTO public.players (id, username, first_name, last_name, email, password, image_id) VALUES (2, 'Zsezsu', 'Zsuzsanna', 'Juhász', 'zsezsu@terraformingmars.com', '$2b$12$pKlpXOvw1OpKzOUElhtbzeMIUZt9jnK2xHnHdjstGaQg97gJXi1vG', 22);
INSERT INTO public.players (id, username, first_name, last_name, email, password, image_id) VALUES (3, 'BigDoor', 'Viktor', 'Sági', 'bigdoor@terraformingmars.com', '$2b$12$pKlpXOvw1OpKzOUElhtbzeMIUZt9jnK2xHnHdjstGaQg97gJXi1vG', 13);
INSERT INTO public.players (id, username, first_name, last_name, email, password, image_id) VALUES (4, 'Frienedek', 'Benedek', 'Halaj', 'frienedek@terraformingmars.com', '$2b$12$pKlpXOvw1OpKzOUElhtbzeMIUZt9jnK2xHnHdjstGaQg97gJXi1vG', 20);
INSERT INTO public.players (id, username, first_name, last_name, email, password, image_id) VALUES (5, 'Buborekfujocska', 'Vivien', 'Turcsányi', 'Buborekfujocska@terraformingmars.com', '$2b$12$pKlpXOvw1OpKzOUElhtbzeMIUZt9jnK2xHnHdjstGaQg97gJXi1vG', 10);
INSERT INTO public.players (id, username, first_name, last_name, email, password, image_id) VALUES (6, 'CodeCooler', 'Code', 'Cooler', 'codecooler@terraformingmars.com', '$2b$12$pKlpXOvw1OpKzOUElhtbzeMIUZt9jnK2xHnHdjstGaQg97gJXi1vG', 22);

SELECT setval(
  pg_get_serial_sequence('players', 'id'),
  (SELECT COALESCE(MAX(id), 0) FROM public.players)
);

