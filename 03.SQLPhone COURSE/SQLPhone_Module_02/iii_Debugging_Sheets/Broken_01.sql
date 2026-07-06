-- 🐛 BROKEN – Module 02, Lesson 18 (LIKE)
-- This query uses '=' with a wildcard. It should use LIKE.

SELECT * FROM users WHERE email = '%@gmail.com';  -- ❌
