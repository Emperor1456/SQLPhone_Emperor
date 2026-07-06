-- 🐛 BROKEN – Module 04, Lesson 35 (UNION)
-- UNION columns mismatch: first SELECT has 2 cols, second has 3.

SELECT id, name FROM current_employees
UNION
SELECT id, name, email FROM former_employees;  -- ❌ column count mismatch
