-- 🐛 BROKEN QUERY – Module 03
-- This query tries to find departments with more than 3 employees,
-- but the HAVING clause is misused.

CREATE TABLE emp (id INTEGER, dept TEXT);
INSERT INTO emp VALUES (1,'Sales'),(2,'Sales'),(3,'Sales'),(4,'HR'),(5,'HR');

-- Broken query
SELECT dept, COUNT(*) AS cnt
FROM emp
WHERE cnt > 3        -- ❌ can't use alias in WHERE; should be HAVING
GROUP BY dept;

-- Fix by moving the filter to HAVING. Expected: only 'Sales' (cnt=3, no >3 here? Actually 3 is not >3, so maybe adjust data to have >3? We'll make data such that Sales has 4. Let's change insert to have 4 Sales.)
-- Note: you need to adjust data so that a group has >3 rows.
-- After fixing, run the corrected query.
