# 04.SQLPhone NOTES/Module_04_Joins_Unions.md
# SQLPhone Emperor — The Best Phone‑First SQL Curriculum

# 📝 Module 04 – Joins & Unions

## Join Types
| Join | Result |
|------|--------|
| `INNER JOIN` | Only rows with matches in both tables |
| `LEFT JOIN` | All rows from left table; NULLs where no match |
| `RIGHT JOIN` (simulate) | Swap tables and use LEFT JOIN |
| `FULL OUTER JOIN` (simulate) | UNION of two LEFT JOINs |
| Self‑join | Join a table to itself (use aliases) |

## UNION
- `UNION` combines result sets, removes duplicates.
- `UNION ALL` keeps all rows, faster.

## Foreign Keys
- Enable with `PRAGMA foreign_keys = ON;`
- Referential actions: `ON DELETE CASCADE`, `SET NULL`, `RESTRICT`

## Examples
```sql
-- Inner join
SELECT c.name, o.product
FROM customers c
JOIN orders o ON c.id = o.customer_id;

-- Left join with NULL check
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.id IS NULL;

-- Full outer join simulation
SELECT ... FROM A LEFT JOIN B ON ... UNION
SELECT ... FROM B LEFT JOIN A ON ... WHERE A.key IS NULL;
```
