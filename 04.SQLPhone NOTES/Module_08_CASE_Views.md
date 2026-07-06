# 04.SQLPhone NOTES/Module_08_CASE_Views.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 08 – Conditional Logic & Views

## CASE Expression
- Simple: `CASE col WHEN val THEN ... END`
- Searched: `CASE WHEN condition THEN ... END`
- Can be used in `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`.

## Views
- `CREATE VIEW vname AS SELECT ...;`
- Acts as a virtual table; queries run the underlying SQL.
- `DROP VIEW IF EXISTS vname;`
- Updatable views must be simple (single table, no joins/aggregation).

## CSV Export
- CLI: `.mode csv`, `.output file.csv`, run query, `.output stdout`
- Python: use `csv.writer` with cursor description.

## Examples
```sql
SELECT name,
  CASE WHEN score >= 90 THEN 'A' WHEN score >= 80 THEN 'B' ELSE 'F' END AS grade
FROM students;

CREATE VIEW active_customers AS SELECT * FROM customers WHERE status = 'active';
```
