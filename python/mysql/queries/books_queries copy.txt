INSERT INTO users (first_name, last_name)
VALUE ("Jane", "Amsden"), ("Emily", "Dixon"), ("Theodore", "Dostoevsky"), ("William", "Shapiro"), ("Lao", "Xiu");

INSERT INTO books (title, num_of_pages)
VALUE ("C Sharp", 0), ("Java", 0), ("Python", 0), ("PHP", 0), ("Ruby", 0);

SELECT * FROM books;

UPDATE books SET title = "C#"
WHERE title = "C Sharp";

UPDATE users SET first_name = "Bill"
WHERE id = 4;

INSERT INTO favorites (user_id, book_id)
VALUE (1,1),(1,2);

INSERT INTO favorites (user_id, book_id)
VALUE (2,1),(2,2),(2,3), (3,1),(3,2),(3,3),(3,4), (4,1),(4,2),(4,3),(4,4),(4,5);

SELECT * FROM users
JOIN favorites on users.id = favorites.user_id
WHERE favorites.book_id = 3;

DELETE FROM favorites WHERE user_id = 2 and book_id = 3;

INSERT INTO favorites (user_id, book_id)
VALUE (5,2);

SELECT * FROM books
JOIN favorites on books.id = favorites.book_id
WHERE favorites.user_id = 3;

SELECT * FROM users
JOIN favorites on users.id = favorites.user_id
WHERE favorites.book_id = 5;

