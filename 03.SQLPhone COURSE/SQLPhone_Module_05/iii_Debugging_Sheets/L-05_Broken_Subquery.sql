-- 🐛 BROKEN QUERY – Module 05
-- This subquery should find employees earning above the average,
-- but it returns no rows due to a correlation mistake.

CREATE TABLE emp5 (id INTEGER, name TEXT, salary REAL);
INSERT INTO emp5 VALUES (1,'X',50000),(2,'Y',80000),(3,'Z',60000);

-- Broken query
SELECT name FROM emp5
WHERE salary > (SELECT AVG(salary) FROM emp5 WHERE name = name);  -- ❌ ambiguous column name

-- Fix: alias the outer table and reference it in the subquery.
-- Expected: Y and Z (above average 63333).
