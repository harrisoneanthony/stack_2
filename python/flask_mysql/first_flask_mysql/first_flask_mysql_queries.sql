INSERT into friends (first_name, last_name, occupation, created_at, updated_at)
VALUES ('HARRISON', 'ANTHONY', 'Developer', NOW(), NOW());

UPDATE FRIENDS set first_name = "Harrison", friends.last_name = "Anthony", updated_at = NOW()
where id = 1;

SELECT * FROM friends;