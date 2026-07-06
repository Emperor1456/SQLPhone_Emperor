# 04.SQLPhone NOTES/Module_03_Aggregation_Grouping.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 03 – Aggregation & Grouping

## Aggregate Functions
- `COUNT(*)` – total rows; `COUNT(col)` ignores NULLs.
- `SUM(col)` – total sum of numeric column.
- `AVG(col)` – average value.
- `MIN(col)`, `MAX(col)` – extremes (numeric, text, date).

## Grouping
- `GROUP BY col` collapses rows with same value.
- Multiple columns create nested groups.
- Every non‑aggregate column in `SELECT` must be in `GROUP BY`.

## Filtering Groups
- `WHERE` filters rows **before** grouping.
- `HAVING` filters groups **after** aggregation.

## Execution Order
`FROM` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY`

## Examples
```sql
-- Count per department
SELECT department, COUNT(*) FROM employees GROUP BY department;

-- Total sales per category, only high performers
SELECT category, SUM(amount) AS total
FROM sales
WHERE year = 2026
GROUP BY category
HAVING total > 5000
ORDER BY total DESC;
```
