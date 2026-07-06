-- 🐛 BROKEN QUERY – Module 06
-- This UPDATE is meant to increase the salary of all Sales employees by 10%,
-- but it accidentally gives everyone a raise.

CREATE TABLE staff (id INTEGER, name TEXT, dept TEXT, salary REAL);
INSERT INTO staff VALUES (1,'A','Sales',50000),(2,'B','HR',60000),(3,'C','Sales',70000);

-- Broken query
UPDATE staff
SET salary = salary * 1.10;   -- ❌ missing WHERE clause

-- Fix: add WHERE dept = 'Sales'.
-- After fix, verify that only Sales employees' salaries changed.
