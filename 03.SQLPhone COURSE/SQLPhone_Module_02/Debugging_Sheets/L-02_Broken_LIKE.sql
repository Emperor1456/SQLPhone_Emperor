-- 🐛 BROKEN QUERY – Module 02
-- This query is supposed to find all users with a Gmail address,
-- but it returns nothing. Find the mistake.

-- Table setup
CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT);
INSERT INTO users (email) VALUES ('emperor@gmail.com'), ('test@yahoo.com'), ('admin@gmail.com');

-- Broken query (doesn't work)
SELECT * FROM users WHERE email = '%@gmail.com';   -- ❌ using '=' with wildcard

-- Fix it to use LIKE instead. Expected: 2 rows.
