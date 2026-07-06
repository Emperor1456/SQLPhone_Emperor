-- 🐛 BROKEN – Module 05, Lesson 45 (CTE)
-- CTE defined but never referenced.

WITH dept_avg AS (
    SELECT department, AVG(salary) AS avg_sal FROM employees GROUP BY department
)
SELECT * FROM employees;  -- ❌ dept_avg not used
