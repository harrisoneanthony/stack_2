-- INSERT INTO dojos (name)
-- VALUES ("Boston"), ("Denver"), ("Online");

-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM dojos;

-- INSERT INTO ninjas (first_name, last_name, age, dojo_id)
-- VALUES ("Jaylen", "Brown", 26, 7), ("Jayson", "Tatum", 24, 7), ("Marcus", "Smart", 28, 7),
-- 		("Jamal", "Murray", 25, 8), ("Nikola", "Jokic", 27, 8), ("Aaron", "Gordon", 27, 8),
--         ("Harrison", "Anthony", 32, 9), ("Hayley", "Finik", 26, 9), ("Bella", "Alzendez", 3, 9);

-- SELECT * FROM dojos
-- LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
-- WHERE dojos.id = 7;

-- SELECT * FROM dojos
-- LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
-- WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);

SELECT * FROM dojos
WHERE dojos.id = (SELECT  dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1)



