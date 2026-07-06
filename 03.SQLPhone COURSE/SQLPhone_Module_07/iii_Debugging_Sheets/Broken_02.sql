-- 🐛 BROKEN – Module 07, Lesson 63 (COALESCE)
-- COALESCE with all NULL arguments still returns NULL, not the fallback.

SELECT COALESCE(NULL, NULL, 'fallback');  -- returns 'fallback'?
-- Actually this is correct, but the mistake is expecting it to return 0 when all are NULL.
-- The real bug: using COALESCE on a column that is always NULL, and the fallback is also NULL.
SELECT COALESCE(middle_name, NULL) FROM contacts;  -- ❌ always NULL
