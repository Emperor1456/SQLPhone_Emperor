# 04.SQLPhone NOTES/Module_02_Reading_Filtering.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 02 – Reading & Filtering Data

## Core Concepts
- `SELECT DISTINCT` eliminates duplicate rows.
- `WHERE` filters rows before grouping/sorting.
- Logical operators `AND`, `OR`, `NOT` combine conditions.
- `ORDER BY` sorts results; `ASC` (default) or `DESC`.
- `LIMIT` caps rows; `OFFSET` skips rows for pagination.
- `BETWEEN` checks inclusive ranges.
- `IN` matches against a list; `NOT IN` excludes.
- `LIKE` performs pattern matching (`%` any sequence, `_` single char).
- `IS NULL` / `IS NOT NULL` test for missing values.
- Column/table aliases (`AS`) rename output for clarity.

## Key Patterns
```sql
-- Distinct values
SELECT DISTINCT city FROM customers;

-- Filter with multiple conditions
SELECT * FROM orders WHERE amount > 100 AND status = 'paid';

-- Sort and paginate
SELECT name, score FROM players ORDER BY score DESC LIMIT 10 OFFSET 20;

-- Range filter
SELECT * FROM events WHERE event_date BETWEEN '2026-01-01' AND '2026-06-30';

-- List matching
SELECT * FROM products WHERE category IN ('Electronics', 'Books');

-- Pattern search
SELECT * FROM users WHERE email LIKE '%@gmail.com';

-- NULL handling
SELECT * FROM tasks WHERE completed_date IS NULL;

-- Aliases
SELECT first_name || ' ' || last_name AS full_name FROM employees;
```
