-- 🐛 BROKEN – Module 07, Lesson 62 (CAST)
-- Casting 'abc' to INTEGER yields 0, not an error, causing silent data corruption.
INSERT INTO scores VALUES (CAST('abc' AS INTEGER));  -- ❌ inserts 0
