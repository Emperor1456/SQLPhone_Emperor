-- 🐛 BROKEN – Module 03, Lesson 26 (HAVING)
-- HAVING used without GROUP BY, and aggregate in WHERE.

SELECT department, COUNT(*) FROM employees
WHERE COUNT(*) > 5;  -- ❌ can't use aggregate in WHERE
