-- 🐛 BROKEN – Module 02, Lesson 16 (BETWEEN)
-- BETWEEN is inclusive; this logic misses the upper bound.

SELECT * FROM orders WHERE amount > 10 AND amount < 50;  -- excludes 50
-- Should use BETWEEN 10 AND 50.
