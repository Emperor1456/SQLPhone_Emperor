-- 🐛 BROKEN – Module 03, Lesson 24 (GROUP BY)
-- Missing GROUP BY for non‑aggregate column.

SELECT department, AVG(salary) FROM employees;  -- ❌ needs GROUP BY department
