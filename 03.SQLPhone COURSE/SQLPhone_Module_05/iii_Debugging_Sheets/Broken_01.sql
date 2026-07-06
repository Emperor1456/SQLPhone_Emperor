-- 🐛 BROKEN – Module 05, Lesson 39 (Scalar Subquery)
-- Subquery returns more than one row, causing error.

SELECT name FROM products
WHERE price > (SELECT price FROM products WHERE category='Electronics');
-- ❌ if multiple Electronics, scalar subquery fails.
