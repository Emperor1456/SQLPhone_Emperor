-- 🐛 BROKEN – Module 05, Lesson 44 (Correlated Subquery)
-- Forgot to correlate the inner query; returns same value for all rows.

SELECT e.name, e.salary FROM employees e
WHERE e.salary > (SELECT AVG(salary) FROM employees);  -- ❌ missing e.department
