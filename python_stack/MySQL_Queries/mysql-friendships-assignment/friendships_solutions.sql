-- ---------------------------------------------------------
-- Assignment: Friendships (Self-Join Practice)
-- Author: Mahmoud Miqdad
-- ---------------------------------------------------------
CREATE DATABASE IF NOT EXISTS friendships_schema;
USE friendships_schema;

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(45) NULL,
    last_name VARCHAR(45) NULL,
    created_at DATETIME NULL DEFAULT NOW(),
    updated_at DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
    PRIMARY KEY (id)
) ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS friendships (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    friend_id INT NOT NULL,
    created_at DATETIME NULL DEFAULT NOW(),
    updated_at DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
    PRIMARY KEY (id),
    INDEX fk_friendships_users1_idx (user_id ASC),
    INDEX fk_friendships_users2_idx (friend_id ASC),
    CONSTRAINT fk_friendships_users1
        FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fk_friendships_users2
        FOREIGN KEY (friend_id)
        REFERENCES users (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE = InnoDB;

-- 1. Query: Create 6 new users
INSERT INTO users (first_name, last_name, created_at, updated_at)
VALUES 
('Amy', 'Giver', NOW(), NOW()),
('Eli', 'Byers', NOW(), NOW()),
('Marky', 'Mark', NOW(), NOW()),
('Big', 'Bird', NOW(), NOW()),
('Kermit', 'The Frog', NOW(), NOW()),
('Mahmoud', 'Miqdad', NOW(), NOW());

-- 2. Query: Create Relationships (Friendships)
-- User 1 (Amy) is friends with 2, 4, and 6
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES 
(1, 2, NOW(), NOW()),
(1, 4, NOW(), NOW()),
(1, 6, NOW(), NOW());

-- User 2 (Eli) is friends with 1, 3, and 5
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES 
(2, 1, NOW(), NOW()), 
(2, 3, NOW(), NOW()), 
(2, 5, NOW(), NOW());

-- User 3 (Marky) is friends with 2 and 5
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES 
(3, 2, NOW(), NOW()), 
(3, 5, NOW(), NOW());

-- User 4 (Big Bird) is friends with 3
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES (4, 3, NOW(), NOW());

-- User 5 (Kermit) is friends with 1 and 6
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES 
(5, 1, NOW(), NOW()), 
(5, 6, NOW(), NOW());

-- User 6 (Mahmoud) is friends with 2 and 3
INSERT INTO friendships (user_id, friend_id, created_at, updated_at)
VALUES 
(6, 2, NOW(), NOW()), 
(6, 3, NOW(), NOW());


-- 3. Query: Display the relationships created as shown in the image
SELECT users.first_name, users.last_name, 
       user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON friendships.friend_id = user2.id;


-- ---------------------------------------------------------
-- NINJA QUERIES
-- ---------------------------------------------------------

-- 1. NINJA Query: Return all users who are friends with the first user (Amy)
SELECT user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON friendships.friend_id = user2.id
WHERE users.id = 1;

-- 2. NINJA Query: Return the count of all friendships
SELECT COUNT(*) AS total_friendships_count
FROM friendships;

-- 3. NINJA Query: Find out who has the most friends and return the count
SELECT users.first_name, users.last_name, COUNT(friendships.id) AS friends_count
FROM users
JOIN friendships ON users.id = friendships.user_id
GROUP BY users.id
HAVING friends_count = (
    SELECT COUNT(id) 
    FROM friendships 
    GROUP BY user_id 
    ORDER BY COUNT(id) DESC 
    LIMIT 1
);

-- 4. NINJA Query: Return the friends of the third user (Marky) in alphabetical order
SELECT user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users AS user2 ON friendships.friend_id = user2.id
WHERE users.id = 3
ORDER BY friend_first_name ASC;