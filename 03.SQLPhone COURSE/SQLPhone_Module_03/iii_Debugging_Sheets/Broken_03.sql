-- 🐛 BROKEN – Module 03, Lesson 21 (COUNT)
-- COUNT(column) ignores NULLs; this query may miscount.
-- If phone is NULL, COUNT(phone) < COUNT(*).

SELECT COUNT(phone) FROM contacts;  -- ❌ maybe not what you want
