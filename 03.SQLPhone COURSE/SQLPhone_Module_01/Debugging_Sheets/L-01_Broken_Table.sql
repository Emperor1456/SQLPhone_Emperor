-- 🐛 BROKEN QUERY – Module 01
-- This query tries to create a table and insert a row but fails.
-- Find the two mistakes and fix them.

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);

INSERT INTO users (id, name, email)
VALUES (1, 'Emperor', 'emperor@sqlphone.dev');

INSERT INTO users (name, email)
VALUES (NULL, 'test@example.com');   -- ❌ name cannot be NULL

-- After fixing, run: SELECT * FROM users;
-- Expected: two rows, no errors.
