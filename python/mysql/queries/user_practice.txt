INSERT INTO users (first_name, last_name, email)
VALUE ("Harrison", "Anthony", "harrisoneanthony@gmail.com"),("Hayley", "Finik", "hfinik@nobull.com"),("Bella", "Alzened", "bella@dog.com");

SELECT * from users; --

SELECT * from users
WHERE email = "harrisoneanthony@gmail.com";

SELECT * from users
WHERE id = 3;

UPDATE users SET last_name = "Pancakes"
WHERE users.id = 3;

DELETE FROM users
WHERE users.id = 2;

SELECT * FROM users
ORDER BY first_name;

SELECT * FROM users
ORDER BY first_name DESC;