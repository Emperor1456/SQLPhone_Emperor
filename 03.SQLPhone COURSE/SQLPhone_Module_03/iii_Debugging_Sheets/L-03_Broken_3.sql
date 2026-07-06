-- 🐛 BROKEN QUERY 3 – Multiple Issues
-- This script is meant to create two tables with a foreign key,
-- insert data, and then perform a JOIN. It fails due to:
--   1. Missing PRIMARY KEY in the referenced table.
--   2. A typo in the JOIN condition.
--   3. A missing semicolon after the INSERT.

-- Broken script:
CREATE TABLE departments (
    id INTEGER,
    name TEXT
);

CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(id)
);

INSERT INTO employees VALUES (1, 'Alice', 1)

SELECT e.name, d.name
FROM employees e
JOIN departments d ON e.dept_id = d.id;   -- ❌ typo: d.id instead of d.id?
-- Fix all three issues to make the script run.
